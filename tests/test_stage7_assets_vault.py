"""
Stage 7 Asset & 3D Vault Engine Tests
Unit tests for AssetVaultQueryEngine and search_asset_vault MCP integration.
"""

import unittest
from scripts.query_asset_vault import AssetVaultQueryEngine
from scripts.zobar_mcp_server import ZobarMCPServer


class TestStage7AssetsVault(unittest.TestCase):
    def setUp(self):
        self.engine = AssetVaultQueryEngine()
        self.server = ZobarMCPServer()

    def test_asset_vault_total_and_categories(self):
        summary = self.engine.get_summary()
        self.assertGreaterEqual(summary["total_resources"], 20)
        categories = summary["categories"]
        self.assertIn("3d_models_and_meshes", categories)
        self.assertIn("pbr_textures_and_materials", categories)
        self.assertIn("ui_component_and_animation_libraries", categories)
        self.assertIn("icons_and_vector_design_systems", categories)
        self.assertIn("audio_sfx_and_soundtracks", categories)

    def test_search_3d_models_gltf(self):
        matches = self.engine.search(query="gltf", category="3d_models_and_meshes")
        self.assertGreater(len(matches), 0)
        names = [m["name"] for m in matches]
        self.assertTrue(any("Kenney" in n for n in names))
        self.assertTrue(any("Poly Pizza" in n for n in names))

    def test_search_ui_components(self):
        matches = self.engine.search(query="bento", category="ui_component_and_animation_libraries")
        self.assertGreater(len(matches), 0)
        names = [m["name"] for m in matches]
        self.assertTrue(any("Aceternity" in n or "Magic UI" in n for n in names))

    def test_search_pbr_textures(self):
        matches = self.engine.search(query="pbr", category="pbr_textures_and_materials")
        self.assertGreater(len(matches), 0)
        names = [m["name"] for m in matches]
        self.assertTrue(any("Poly Haven" in n for n in names))

    def test_search_audio_sfx(self):
        matches = self.engine.search(query="audio", category="audio_sfx_and_soundtracks")
        self.assertGreater(len(matches), 0)
        names = [m["name"] for m in matches]
        self.assertTrue(any("Kenney" in n or "Freesound" in n or "Soniss" in n for n in names))

    def test_mcp_server_search_asset_vault_tool(self):
        res = self.server.execute_tool("search_asset_vault", {"query": "3d", "preferred_format": "GLTF"})
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertGreater(res["result"]["matches_found"], 0)
        self.assertLess(res["execution_latency_ms"], 20.0)


if __name__ == "__main__":
    unittest.main()
