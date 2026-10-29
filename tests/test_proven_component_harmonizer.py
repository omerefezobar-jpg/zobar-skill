#!/usr/bin/env python3
"""
Unit tests for Proven Component Harmonizer & S-Tier Design Synthesizer.
Verifies the mandate: Never reinvent the wheel with inferior generic UI.
"""

import os
import sys
import tempfile
import unittest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.proven_component_harmonizer import ProvenComponentHarmonizer
from scripts.zobar_mcp_server import ZobarMCPServer


class TestProvenComponentHarmonizer(unittest.TestCase):
    def setUp(self):
        self.harmonizer = ProvenComponentHarmonizer()

    def test_load_vaults_successfully(self):
        comps = self.harmonizer.load_components_vault()
        self.assertGreaterEqual(len(comps), 20, "Components vault should contain at least 20 components and award patterns")

        sites = self.harmonizer.load_s_tier_vault()
        self.assertGreaterEqual(len(sites), 500, "S-Tier vault must contain at least 500 award-winning sites")

    def test_load_award_winning_patterns(self):
        comps = self.harmonizer.load_components_vault()
        comp_ids = [c["id"] for c in comps]
        self.assertIn("AWARD-01", comp_ids)
        self.assertIn("AWARD-02", comp_ids)
        self.assertIn("AWARD-03", comp_ids)

    def test_match_benchmark_sites_linear_and_stripe(self):
        saas_sites = self.harmonizer.match_benchmark_sites("linear issue tracker and stripe", limit=3)
        self.assertEqual(len(saas_sites), 3)
        site_names = [s["name"].lower() for s in saas_sites]
        self.assertTrue(any("linear" in n or "stripe" in n for n in site_names))

    def test_match_proven_components_for_saas(self):
        matches = self.harmonizer.match_proven_components("saas telemetry metrics", limit=3)
        self.assertGreaterEqual(len(matches), 1)
        matched_ids = [m["id"].upper() for m in matches]
        # Should match metric stat card or telemetry badge
        self.assertTrue(any(cid in matched_ids for cid in ["COMP-02", "COMP-08", "COMP-06", "COMP-11"]))

    def test_convert_component_to_vanilla_html(self):
        bento_comp = {"id": "COMP-02", "name": "Bento Metric Stat Card", "category": "Analytics & Bento Grid"}
        html = self.harmonizer.convert_component_to_vanilla_html(bento_comp)
        self.assertIn("provenBentoStat", html)
        self.assertIn("0.03 ms", html)

        telemetry_comp = {"id": "COMP-08", "name": "Real-Time Telemetry Badge", "category": "Status"}
        html_tele = self.harmonizer.convert_component_to_vanilla_html(telemetry_comp)
        self.assertIn("provenTelemetryPill", html_tele)
        self.assertIn("EDGE CLUSTER HEALTHY", html_tele)

    def test_harmonize_ui_components_full_package(self):
        result = self.harmonizer.harmonize_ui_components("luxury ecommerce fine watches")
        self.assertIn("primary_benchmark_site", result)
        self.assertIn("design_tokens", result)
        self.assertIn("key_interactions", result)
        self.assertIn("blended_components", result)
        self.assertIn("combined_html_payload", result)
        self.assertGreaterEqual(len(result["blended_components"]), 1)

    def test_inject_harmonized_components_into_file(self):
        sample_html = """<!DOCTYPE html><html><head><title>Test App</title></head><body><main><p>Original Content</p></main></body></html>"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".html") as f:
            f.write(sample_html)
            tmp_path = f.name

        try:
            res = self.harmonizer.inject_harmonized_components_into_file(tmp_path, "saas dashboard", ["COMP-02", "COMP-08"])
            self.assertEqual(res["status"], "SUCCESS")

            with open(tmp_path, "r", encoding="utf-8") as f:
                updated = f.read()

            self.assertIn("provenBentoStat", updated)
            self.assertIn("provenTelemetryPill", updated)
            self.assertIn("Original Content", updated)

            # Test idempotent re-injection
            re_res = self.harmonizer.inject_harmonized_components_into_file(tmp_path, "saas dashboard", ["COMP-02"])
            self.assertEqual(re_res["status"], "ALREADY_PRESENT")
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_mcp_tool_blend_proven_ui_components(self):
        server = ZobarMCPServer()
        res = server.execute_tool("blend_proven_ui_components", {"query": "clinical medtech icu telemetry"})
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertLess(res["execution_latency_ms"], 50.0, "MCP tool should run in under 50ms")
        payload = res["result"]
        self.assertIn("primary_benchmark_site", payload)
        self.assertIn("blended_components", payload)


if __name__ == "__main__":
    unittest.main()
