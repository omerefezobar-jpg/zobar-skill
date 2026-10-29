#!/usr/bin/env python3
"""
Unit tests for Academic Foundations & University Literature Grounding Engine.
Verifies theorem mapping, textbook recommendations, university course integration,
and MCP tool execution under sub-millisecond conditions.
"""

import os
import sys
import unittest
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.academic_foundations_engine import (
    AcademicFoundationsEngine,
    FOUNDATIONAL_THEOREMS_CATALOG,
    SEMINAL_TEXTBOOKS_CATALOG
)
from scripts.zobar_mcp_server import ZobarMCPServer


class TestAcademicFoundationsEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AcademicFoundationsEngine()

    def test_catalog_integrity(self):
        self.assertGreaterEqual(len(FOUNDATIONAL_THEOREMS_CATALOG), 6)
        self.assertGreaterEqual(len(SEMINAL_TEXTBOOKS_CATALOG), 6)
        for thm in FOUNDATIONAL_THEOREMS_CATALOG:
            self.assertIn("id", thm)
            self.assertIn("formula", thm)
            self.assertIn("implication", thm)

    def test_ground_domain_database_and_distributed(self):
        res = self.engine.ground_domain("distributed database replication and postgres latency", "MVCC isolation")
        self.assertIn("matched_theorems", res)
        self.assertIn("matched_textbooks", res)
        self.assertIn("university_courses", res)
        self.assertIn("executive_architecture", res)

        thm_names = [t["name"] for t in res["matched_theorems"]]
        self.assertTrue(any("PACELC" in name or "Little" in name for name in thm_names))

        book_titles = [b["title"] for b in res["matched_textbooks"]]
        self.assertTrue(any("Data-Intensive" in title or "TAOCP" in title for title in book_titles))

    def test_ground_domain_ui_ux_cognitive(self):
        res = self.engine.ground_domain("frontend ux conversion navigation and layout", "high-friction command palette")
        thm_names = [t["name"] for t in res["matched_theorems"]]
        self.assertTrue(any("Hick" in name or "Fitts" in name or "Entropy" in name for name in thm_names))

    def test_invisible_depth_mandate(self):
        res = self.engine.ground_domain("compiler ast parser")
        self.assertEqual(res["invisible_depth_compliance"], "Verified (Depth powers internal logic; deliverables remain pristine enterprise code)")
        self.assertIn("production_guidelines", res["executive_architecture"])
        self.assertGreaterEqual(len(res["executive_architecture"]["production_guidelines"]), 3)

    def test_sub_millisecond_grounding_performance(self):
        t_start = time.perf_counter()
        for _ in range(50):
            self.engine.ground_domain("realtime edge analytics", "sub-millisecond streaming")
        elapsed = (time.perf_counter() - t_start) / 50.0
        self.assertLess(elapsed * 1000.0, 5.0, f"Academic grounding too slow: {elapsed * 1000.0:.2f}ms > 5ms")

    def test_mcp_tool_ground_academic_foundations(self):
        server = ZobarMCPServer()
        res = server.execute_tool("ground_academic_foundations", {
            "domain": "distributed microservices and cloud cache",
            "problem_statement": "Queueing backpressure and Little's Law limits"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertLess(res["execution_latency_ms"], 50.0)

        payload = res["result"]
        self.assertIn("executive_architecture", payload)
        self.assertIn("matched_theorems", payload)


if __name__ == "__main__":
    unittest.main()
