#!/usr/bin/env python3
"""
Unit tests for FullStackTriadEngine (Analiz + Frontend UI + Backend Systems).
Verifies seamless integration across all three engineering pillars.
"""

import os
import sys
import unittest
import tempfile

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.full_stack_triad_engine import FullStackTriadEngine
from scripts.zobar_mcp_server import ZobarMCPServer


class TestFullStackTriadEngine(unittest.TestCase):
    def setUp(self):
        self.engine = FullStackTriadEngine()
        self.vision = "Real-Time Embedded IoT Telemetry Dispatcher"
        self.sector = "Industrial Automation"

    def test_analysis_pillar_execution(self):
        analysis = self.engine.execute_analysis_pillar(self.vision, self.sector)
        self.assertIn("competitor_moat", analysis)
        self.assertIn("regulatory_compliance", analysis)
        self.assertIn("triz_inventions", analysis)
        self.assertIn("systems_mathematics", analysis)
        self.assertIn("queueing_latency", analysis["systems_mathematics"])
        self.assertIn("roofline_analysis", analysis["systems_mathematics"])
        self.assertIn("academic_foundations", analysis)
        self.assertEqual(analysis["analysis_quality_gate"], "PASSED (TRL >= 5, Compliance Verified, Capacity Modeled, Academically Grounded)")

    def test_frontend_pillar_execution(self):
        frontend = self.engine.execute_frontend_pillar(self.vision, self.sector, brand_name="Apex IoT Core")
        self.assertIn("quantum_aesthetic", frontend)
        self.assertIn("ground_state_energy", frontend["quantum_aesthetic"])
        self.assertIn("generated_html_code", frontend)
        html = frontend["generated_html_code"]
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("Apex IoT Core", html)
        self.assertIn("triggerClientMutation()", html)
        self.assertIn("queryBackendTelemetry()", html)

    def test_backend_pillar_execution(self):
        backend = self.engine.execute_backend_pillar(self.vision, self.sector)
        self.assertIn("edge_service_python", backend)
        self.assertIn("database_sql_schema", backend)
        py_code = backend["edge_service_python"]
        sql_code = backend["database_sql_schema"]

        # Backend Python validation
        self.assertIn("class EdgeServiceHandler", py_code)
        self.assertIn("/api/health", py_code)
        self.assertIn("/api/mutate", py_code)

        # Database SQL validation
        self.assertIn("ENABLE ROW LEVEL SECURITY", sql_code)
        self.assertIn("vector_cosine_ops", sql_code)
        self.assertIn("CREATE POLICY", sql_code)

    def test_full_stack_triad_synthesis(self):
        result = self.engine.synthesize_full_stack_triad(self.vision, self.sector, brand_name="Titan Industrial Core")
        self.assertEqual(result["status"], "SUCCESS")
        self.assertIn("pillars", result)
        self.assertIn("pillar_1_deep_analysis", result["pillars"])
        self.assertIn("pillar_2_frontend_design", result["pillars"])
        self.assertIn("pillar_3_backend_systems", result["pillars"])
        self.assertLess(result["synthesis_latency_ms"], 5000.0)

    def test_mcp_tool_synthesize_full_stack_triad(self):
        server = ZobarMCPServer()
        with tempfile.TemporaryDirectory() as tmp_dir:
            res = server.execute_tool("synthesize_full_stack_triad", {
                "vision": "High-Throughput Financial Order Gateway",
                "sector": "FinTech",
                "output_dir": tmp_dir
            })
            self.assertEqual(res["tool_status"], "SUCCESS")
            payload = res["result"]
            self.assertEqual(payload["status"], "SUCCESS")
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, "index.html")))
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, "server.py")))
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, "schema.sql")))


if __name__ == "__main__":
    unittest.main()
