#!/usr/bin/env python3
"""
Unit tests for End-to-End Application Architect & Co-Creation Engine.
Verifies complete UI generation across Profile, Settings, Products, Command Palette,
internal self-critique scoring, concise conversational dialogue, and MCP execution.
"""

import unittest
import os
import tempfile
from scripts.end_to_end_app_architect import (
    synthesize_complete_application,
    evaluate_feature_internally,
    generate_concise_co_creation_dialogue,
    export_standalone_app_file
)
from scripts.production_cleaner import inspect_cleanliness
from scripts.zobar_mcp_server import ZobarMCPServer

class TestEndToEndAppArchitect(unittest.TestCase):
    def test_synthesize_complete_application_structure(self):
        spec = synthesize_complete_application(
            app_name="AeroTelemetry Cloud",
            domain_type="Aviation & Autonomous Drone Ops"
        )
        self.assertEqual(spec["app_name"], "AeroTelemetry Cloud")
        self.assertIn("Core Dashboard", spec["views_implemented"])
        self.assertIn("User Profile", spec["views_implemented"])
        self.assertIn("Workspace Settings", spec["views_implemented"])
        self.assertIn("Product Catalog", spec["views_implemented"])
        
        # Check generated HTML
        html = spec["generated_html_code"]
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("Ctrl+K", html)
        self.assertIn("switchView('profile')", html)
        self.assertIn("showToast", html)

        # Audit cleanliness: must be 100% free of internal meta-slogans
        cleanliness = inspect_cleanliness(html)
        self.assertTrue(cleanliness["is_production_clean"])
        self.assertEqual(cleanliness["cleanliness_score"], 100.0)

    def test_internal_feature_evaluation(self):
        res = evaluate_feature_internally(
            feature_name="Instant Keyboard-Driven Inline Split Filter",
            domain_context="FinTech Trading SaaS"
        )
        critique = res["internal_critique"]
        self.assertGreaterEqual(critique["cognitive_load_score"], 70)
        self.assertGreaterEqual(critique["user_delight_score"], 80)
        self.assertEqual(critique["verdict"], "APPROVED_FOR_CO_CREATION")

    def test_concise_co_creation_dialogue(self):
        critiques = [
            evaluate_feature_internally("Optimistic Offline Local Sync Queue", "Enterprise SaaS"),
            evaluate_feature_internally("Live Multi-Cursor Presence", "Collaboration")
        ]
        dialogue = generate_concise_co_creation_dialogue(critiques)
        self.assertEqual(len(dialogue["quick_options"]), 2)
        # Ensure concise output without wall of text
        for opt in dialogue["quick_options"]:
            self.assertTrue(opt["prompt_for_user"].startswith("["))
            self.assertLess(len(opt["one_line_impact"]), 150)

    def test_export_standalone_app_file(self):
        spec = synthesize_complete_application("TestApp", "DevTools")
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = os.path.join(tmp_dir, "test_app.html")
            saved = export_standalone_app_file(out_path, spec)
            self.assertTrue(os.path.exists(saved))
            with open(saved, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn("<title>TestApp", content)

    def test_mcp_synthesize_complete_application(self):
        server = ZobarMCPServer()
        res = server.execute_tool("synthesize_complete_application", {
            "app_name": "SpectraMetrics",
            "domain_type": "High-Throughput Analytics"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        result = res["result"]
        self.assertEqual(result["app_name"], "SpectraMetrics")
        self.assertEqual(len(result["views_implemented"]), 4)

    def test_mcp_evaluate_feature_co_creation(self):
        server = ZobarMCPServer()
        res = server.execute_tool("evaluate_feature_co_creation", {
            "feature_name": "Predictive Omnibar Search",
            "domain_context": "B2B SaaS"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        result = res["result"]
        self.assertIn("internal_evaluation", result)
        self.assertIn("concise_co_creation_dialogue", result)

    def test_multi_sector_synthesis_and_persistence(self):
        from scripts.end_to_end_app_architect import synthesize_domain_application, synthesize_all_domain_apps

        # Test Ecommerce
        ecom = synthesize_domain_application("ecommerce", "Lumina Store")
        self.assertIn("Shopping Bag", ecom["generated_html_code"])
        self.assertIn("lumina_cart", ecom["generated_html_code"])
        self.assertIn("addToCart", ecom["generated_html_code"])

        # Test MedTech
        med = synthesize_domain_application("medtech", "PulseCare Portal")
        self.assertIn("Lead II", med["generated_html_code"])
        self.assertIn("ecgCanvas", med["generated_html_code"])

        # Test Creative Agency
        cre = synthesize_domain_application("creative_agency", "Kroma 3D")
        self.assertIn("render3D", cre["generated_html_code"])
        self.assertIn("viewCanvas", cre["generated_html_code"])

        # Test Batch Synthesis
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_apps = os.path.join(tmp_dir, "apps")
            paths = synthesize_all_domain_apps(out_apps)
            self.assertIn("saas", paths)
            self.assertIn("ecommerce", paths)
            self.assertIn("medtech", paths)
            self.assertIn("creative_agency", paths)
            self.assertIn("master_hub", paths)
            for p in paths.values():
                self.assertTrue(os.path.exists(p))

if __name__ == "__main__":
    unittest.main()
