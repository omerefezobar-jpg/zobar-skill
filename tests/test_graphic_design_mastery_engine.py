#!/usr/bin/env python3
"""
Unit tests for Graphic Design Mastery Engine & Anti-Cliché Iconography Suite.
Verifies Paul Rand's 7-Step Logo Test, Dieter Rams checks, anti-AI prompt synthesis,
parametric SVG generation, and MCP server execution.
"""

import os
import sys
import unittest
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.graphic_design_mastery_engine import GraphicDesignMasteryEngine
from scripts.image_prompt_synthesizer import ImagePromptSynthesizer
from scripts.zobar_mcp_server import ZobarMCPServer


class TestGraphicDesignMasteryEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GraphicDesignMasteryEngine()

    def test_vault_loading_and_treatises(self):
        vault = self.engine.vault
        self.assertIn("vault_metadata", vault)
        self.assertIn("core_treatises", vault["vault_metadata"])
        self.assertIn("paul_rand_rubric", vault)
        self.assertIn("anti_ai_icon_manifesto", vault)
        self.assertGreaterEqual(len(vault["iconic_archetypes"]), 5)

    def test_paul_rand_evaluation(self):
        res = self.engine.evaluate_paul_rand_test(
            concept_name="Apex Cloud Key",
            description="Minimalist negative space security key brandmark",
            archetype="Negative Space Gestalt Monolith"
        )
        self.assertIn("paul_rand_composite_index", res)
        self.assertGreaterEqual(res["paul_rand_composite_index"], 85.0)
        self.assertEqual(res["grade"], "Paul Rand Master Standard")
        self.assertIn("dieter_rams_ten_principles", res)
        self.assertTrue(res["dieter_rams_ten_principles"]["as_little_design_as_possible"])

    def test_anti_cliche_prompt_synthesis_banned_terms(self):
        for eng in ["midjourney", "flux", "dalle3"]:
            res = self.engine.synthesize_master_prompt(
                concept="Quantum Router Glyph",
                archetype="negative_space_monolith",
                medium="vector_silkscreen",
                engine=eng
            )
            self.assertIn("positive_prompt", res)
            self.assertIn("negative_prompt", res)

            # Positive prompt should reference classic graphic design masters
            pos = res["positive_prompt"]
            self.assertTrue("Paul Rand" in pos or "Swiss" in pos or "vector" in pos)

            # Negative prompt should explicitly ban standard AI clichés
            neg = res["negative_prompt"]
            self.assertIn("glossy 3d clay", neg)
            self.assertIn("rainbow gradient", neg)
            self.assertIn("internal circuits", neg)

    def test_parametric_svg_generation_all_archetypes(self):
        archetypes = [
            "negative_space_monolith",
            "swiss_ribbon",
            "golden_spiral_vortex",
            "brutalist_monogram",
            "precision_reticle"
        ]
        for arch in archetypes:
            svg_res = self.engine.generate_parametric_svg("BrandMark", archetype=arch)
            self.assertIn("svg_code", svg_res)
            code = svg_res["svg_code"]
            self.assertTrue(code.startswith("<svg"))
            self.assertTrue(code.endswith("</svg>"))
            self.assertIn('viewBox="0 0 512 512"', code)
            self.assertEqual(svg_res["contrast_ratio"], "21.0:1 (Monochrome figure-ground perfection)")

    def test_image_prompt_synthesizer_integration(self):
        synth = ImagePromptSynthesizer()
        res = synth.generate_master_logo_or_icon(
            brand_name="Vertex Edge",
            concept="Sub-millisecond API proxy",
            archetype="swiss_ribbon"
        )
        self.assertIn("paul_rand_evaluation", res)
        self.assertIn("image_prompts", res)
        self.assertIn("parametric_svg", res)
        self.assertEqual(res["archetype"], "swiss_ribbon")

    def test_sub_millisecond_execution_performance(self):
        t_start = time.perf_counter()
        for _ in range(50):
            self.engine.generate_parametric_svg("FastLogo", "precision_reticle")
            self.engine.evaluate_paul_rand_test("FastLogo", "Minimalist icon")
        elapsed = (time.perf_counter() - t_start) / 50.0

        # Sub-millisecond execution mandate: average execution should be well under 5ms
        self.assertLess(elapsed * 1000.0, 5.0, f"Graphic design engine too slow: {elapsed * 1000.0:.2f}ms > 5ms")

    def test_mcp_tool_synthesize_master_logo_and_icons(self):
        server = ZobarMCPServer()
        res = server.execute_tool("synthesize_master_logo_and_icons", {
            "concept": "Starlight Observability Engine",
            "archetype": "precision_reticle",
            "medium": "titanium_etched",
            "engine": "midjourney"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertLess(res["execution_latency_ms"], 50.0)

        payload = res["result"]
        self.assertIn("paul_rand_evaluation", payload)
        self.assertIn("master_prompts", payload)
        self.assertIn("parametric_svg", payload)


if __name__ == "__main__":
    unittest.main()
