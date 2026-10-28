"""
End-to-End (E2E) Subprocess Pipe & Cross-Tool Integration Tests
Tests live JSON-RPC 2.0 communication with scripts.zobar_mcp_server over stdio.
"""

import os
import sys
import json
import subprocess
import unittest
import time
from typing import Dict, Any


class TestE2EMCPAndCrossTools(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_script = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "scripts", "zobar_mcp_server.py")
        )
        # Spawn the MCP server as a real live subprocess
        cls.process = subprocess.Popen(
            [sys.executable, cls.server_script],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            bufsize=1,
        )

    @classmethod
    def tearDownClass(cls):
        try:
            cls.process.stdin.close()
            cls.process.terminate()
            cls.process.wait(timeout=2.0)
        except Exception:
            pass

    def send_rpc(self, request_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sends a single-line JSON string into the subprocess stdin, reads stdout.
        """
        req_line = json.dumps(request_dict, ensure_ascii=False) + "\n"
        self.process.stdin.write(req_line)
        self.process.stdin.flush()

        resp_line = self.process.stdout.readline()
        self.assertTrue(len(resp_line.strip()) > 0, "MCP server must return a response")
        return json.loads(resp_line)

    def test_01_initialize_handshake(self):
        req = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {}
        }
        resp = self.send_rpc(req)

        self.assertEqual(resp.get("jsonrpc"), "2.0")
        self.assertEqual(resp.get("id"), 1)
        result = resp.get("result", {})
        self.assertEqual(result.get("protocolVersion"), "2024-11-05")
        self.assertIn("tools", result.get("capabilities", {}))
        self.assertEqual(result.get("serverInfo", {}).get("name"), "zobar-mcp-engine")

    def test_02_tools_list_manifest(self):
        req = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {}
        }
        resp = self.send_rpc(req)

        self.assertEqual(resp.get("id"), 2)
        tools = resp.get("result", {}).get("tools", [])
        self.assertGreaterEqual(len(tools), 8)

        tool_names = [t["name"] for t in tools]
        self.assertIn("semantic_cache_query", tool_names)
        self.assertIn("smart_route", tool_names)
        self.assertIn("audit_supabase_sql", tool_names)
        self.assertIn("compress_context", tool_names)
        self.assertIn("recall_user_memory", tool_names)
        self.assertIn("simulate_unit_economics", tool_names)
        self.assertIn("generate_image_prompt", tool_names)
        self.assertIn("step_ecs_simulation", tool_names)

    def test_03_tool_call_smart_route_execution(self):
        req = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "smart_route",
                "arguments": {
                    "prompt": "Müşterinin basit bir sipariş durumunu sorgulamasını sağlayan API."
                }
            }
        }
        resp = self.send_rpc(req)

        self.assertEqual(resp.get("id"), 3)
        result = resp.get("result", {})
        self.assertFalse(result.get("isError"))
        content = json.loads(result["content"][0]["text"])

        self.assertEqual(content["tool_status"], "SUCCESS")
        self.assertLess(content["execution_latency_ms"], 50.0)
        self.assertEqual(content["result"]["tier"], 1)

    def test_04_tool_call_audit_supabase_sql(self):
        sql_sample = """
        CREATE TABLE public.orders (id UUID PRIMARY KEY, total NUMERIC);
        ALTER TABLE public.orders ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Tenant orders" ON public.orders FOR SELECT USING (true);
        """
        req = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "audit_supabase_sql",
                "arguments": {"sql_content": sql_sample}
            }
        }
        resp = self.send_rpc(req)
        content = json.loads(resp["result"]["content"][0]["text"])

        self.assertEqual(content["tool_status"], "SUCCESS")
        self.assertEqual(content["result"]["total_policies_count"], 1)
        self.assertIn("orders", content["result"]["rls_enabled_tables"])

    def test_05_tool_call_step_ecs_simulation(self):
        req = {
            "jsonrpc": "2.0",
            "id": 5,
            "method": "tools/call",
            "params": {
                "name": "step_ecs_simulation",
                "arguments": {"ticks": 60, "entity_count": 30}
            }
        }
        resp = self.send_rpc(req)
        content = json.loads(resp["result"]["content"][0]["text"])

        self.assertEqual(content["tool_status"], "SUCCESS")
        self.assertEqual(content["result"]["ticks_simulated"], 60)
        self.assertGreater(content["result"]["effective_fps_capacity"], 100.0)

    def test_06_e2e_chained_workflow(self):
        """
        Chained E2E pipeline:
        1. Compress conversation
        2. Recall memory
        3. Route model
        """
        # Step 1: Compress
        comp_req = {
            "jsonrpc": "2.0",
            "id": 10,
            "method": "tools/call",
            "params": {
                "name": "compress_context",
                "arguments": {
                    "messages": [
                        {"role": "user", "content": "Rust ve Tauri ile yüksek hızlı bir masaüstü uygulaması tasarlıyorum."},
                        {"role": "assistant", "content": "Harika, SQLite ile sıfır gecikme elde edebiliriz."},
                        {"role": "user", "content": "Ayrıca pgvector ve HNSW indeksi kullanacağız."},
                    ]
                }
            }
        }
        comp_res = json.loads(self.send_rpc(comp_req)["result"]["content"][0]["text"])
        self.assertEqual(comp_res["tool_status"], "SUCCESS")

        # Step 2: Route model based on extracted facts
        route_req = {
            "jsonrpc": "2.0",
            "id": 11,
            "method": "tools/call",
            "params": {
                "name": "smart_route",
                "arguments": {
                    "prompt": "Tauri v2 ve Rust ile lock-free concurrency mimarisini ve B+ Tree disk organizasyonunu açıkla."
                }
            }
        }
        route_res = json.loads(self.send_rpc(route_req)["result"]["content"][0]["text"])
        self.assertEqual(route_res["tool_status"], "SUCCESS")
        self.assertEqual(route_res["result"]["tier"], 2)

    def test_07_error_handling(self):
        # Malformed request
        self.process.stdin.write("{not valid json}\n")
        self.process.stdin.flush()
        resp = json.loads(self.process.stdout.readline())
        self.assertEqual(resp["error"]["code"], -32700)

        # Unknown method
        unknown_method = {"jsonrpc": "2.0", "id": 99, "method": "non_existent_method"}
        resp2 = self.send_rpc(unknown_method)
        self.assertEqual(resp2["error"]["code"], -32601)


if __name__ == "__main__":
    unittest.main()
