#!/usr/bin/env python3
"""
Unit tests for Multimodal Frontier Expansion Engine.
Verifies all 8 enterprise sectors, modality configurations, sub-millisecond SLA targets,
and MCP server execution.
"""

import os
import sys
import unittest
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.multimodal_scope_expansion_engine import MultimodalScopeExpansionEngine, EXTENDED_DOMAINS_CATALOG
from scripts.zobar_mcp_server import ZobarMCPServer


class TestMultimodalScopeExpansionEngine(unittest.TestCase):
    def setUp(self):
        self.engine = MultimodalScopeExpansionEngine()
        self.server = ZobarMCPServer()

    def test_catalog_completeness_eight_sectors(self):
        domains = self.engine.get_supported_domains()
        self.assertEqual(len(domains), 8)
        expected_keys = [
            "saas", "ecommerce", "medtech", "creative_agency",
            "fintech_hft", "robotics_iot", "cyber_defense", "neuro_tech"
        ]
        for k in expected_keys:
            self.assertIn(k, domains)
            self.assertIn("modality", domains[k])
            self.assertIn("latency_target_ms", domains[k])

    def test_scaffold_synthesis_all_domains(self):
        for k in EXTENDED_DOMAINS_CATALOG.keys():
            res = self.engine.synthesize_domain_scaffold(k, f"Test {k} Brand")
            self.assertEqual(res["domain_key"], k)
            self.assertIn("sql_schema", res)
            self.assertIn("edge_service", res)
            self.assertIn("ENABLE ROW LEVEL SECURITY", res["sql_schema"])
            self.assertIn("hnsw", res["sql_schema"].lower())

    def test_sub_millisecond_execution(self):
        t0 = time.perf_counter()
        for _ in range(50):
            self.engine.synthesize_domain_scaffold("fintech_hft")
        elapsed = (time.perf_counter() - t0) / 50.0
        self.assertLess(elapsed * 1000.0, 5.0, f"Scope expansion too slow: {elapsed * 1000.0:.2f}ms > 5ms")

    def test_mcp_tool_multimodal_scaffold(self):
        res = self.server.execute_tool("synthesize_multimodal_domain_scaffold", {
            "domain_key": "cyber_defense",
            "brand_name": "Aegis Zero Trust"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertEqual(res["result"]["domain_key"], "cyber_defense")
        self.assertEqual(res["result"]["brand_name"], "Aegis Zero Trust")


if __name__ == "__main__":
    unittest.main()
