"""
Stage 5 Vibe Coding Bridge & Image Synthesizer Tests
Unit tests for VibeCodingBridge and ImagePromptSynthesizer.
"""

import os
import unittest
import tempfile
from scripts.vibe_coding_bridge import VibeCodingBridge
from scripts.image_prompt_synthesizer import ImagePromptSynthesizer


class TestStage5VibeAndImage(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.bridge = VibeCodingBridge(target_dir=self.temp_dir.name)
        self.synth = ImagePromptSynthesizer()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_vibe_coding_bridge_exports_all_ide_configs(self):
        exported = self.bridge.export_all_ide_configs()

        expected_keys = [
            ".cursorrules",
            ".cursor/rules/zobar.mdc",
            "CLAUDE.md",
            ".windsurfrules",
            ".github/copilot-instructions.md",
            "GEMINI.md",
        ]

        for key in expected_keys:
            self.assertIn(key, exported)
            path = exported[key]
            self.assertTrue(os.path.exists(path), f"File {path} must exist on disk")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertGreater(len(content), 100)
                self.assertIn("ZOBAR SKILL", content)
                self.assertIn("SUB-MILLISECOND", content)

    def test_image_prompt_synthesizer_midjourney(self):
        res = self.synth.synthesize(
            subject="A sleek cybernetic wolf standing on a glass skyscraper in futuristic Tokyo",
            style="cyberpunk_scifi",
            aspect_ratio="16:9",
            engine="midjourney",
        )

        self.assertEqual(res["engine"], "midjourney")
        self.assertIn("--ar 16:9", res["positive_prompt"])
        self.assertIn("--v 6.1", res["positive_prompt"])
        self.assertIn("35mm anamorphic", res["positive_prompt"])
        self.assertIsNone(res["negative_prompt"])

    def test_image_prompt_synthesizer_flux_with_negative_prompt(self):
        res = self.synth.synthesize(
            subject="Studio portrait of a senior artisan clockmaker assembling a tourbillon watch",
            style="photorealistic_cinematic",
            aspect_ratio="1:1",
            engine="flux",
        )

        self.assertEqual(res["engine"], "flux")
        self.assertIn("Hasselblad", res["positive_prompt"])
        self.assertIsNotNone(res["negative_prompt"])
        self.assertIn("deformed", res["negative_prompt"])
        self.assertIn("bad anatomy", res["negative_prompt"])

    def test_image_prompt_synthesizer_ui_mockup(self):
        res = self.synth.generate_ui_app_mockup(
            app_name="NexusQuant",
            app_concept="High-frequency algorithmic trading terminal with live tick charts"
        )

        self.assertEqual(res["style"], "modern_ui_product_mockup")
        self.assertIn("NexusQuant", res["positive_prompt"])
        self.assertIn("Bento Grid", res["positive_prompt"])
        self.assertIn("isometric", res["positive_prompt"])


if __name__ == "__main__":
    unittest.main()
