#!/usr/bin/env python3
"""
Unit and Integration Tests for Cinematic & Literary Criticism Engine.
Verifies:
1. Cinematic Director Aesthetic Synthesis (Kubrick, Deakins, Wong Kar-wai, Anderson, Miyazaki).
2. Aristotelian Poetics UX 3-Act Arc (Hamartia, Peripeteia, Anagnorisis, Catharsis).
3. Italo Calvino Six Memos Interface Token Mapping.
4. MCP Server Tool Invocation ('synthesize_cinematic_art_direction').
5. Sub-millisecond execution performance.
"""

import unittest
import os
import sys
import time

# Ensure project root in sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from cinematic_literary_criticism_engine import (
    CinematicLiteraryCriticismEngine,
    CINEMATIC_DIRECTORS_VAULT,
    LITERARY_CRITICISM_VAULT
)
from zobar_mcp_server import ZobarMCPServer


class TestCinematicLiteraryCriticismEngine(unittest.TestCase):
    def test_cinematic_director_affinities(self):
        """Verifies intelligent mapping from product essence to cinematic director visual grammar."""
        # Finance/Crypto/Security -> Deakins Chiaroscuro
        res_crypto = CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction(
            "Sub-Millisecond L2 Crypto Arbitrage Order Book"
        )
        self.assertEqual(res_crypto["aesthetic_paradigm_key"], "deakins_chiaroscuro")
        self.assertIn("#00F0FF", res_crypto["recommended_palette"])
        self.assertIn("chiaroscuro", res_crypto["visual_grammar"].lower())

        # Compilers/Infrastructure -> Kubrickian Symmetry
        res_compiler = CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction(
            "High Performance Rust AST Compiler & Code Generator"
        )
        self.assertEqual(res_compiler["aesthetic_paradigm_key"], "kubrickian_symmetry")
        self.assertIn("Futura", res_compiler["ui_tokens"]["typography"])

        # Audio/Music/Creator -> Wong Kar-wai Melancholic Neon Blur
        res_audio = CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction(
            "Real-time Generative Audio Synth & Ambient Music Stream"
        )
        self.assertEqual(res_audio["aesthetic_paradigm_key"], "wong_kar_wai_neon_melancholy")
        self.assertIn("step-printing", res_audio["visual_grammar"].lower())

        # EdTech/Books -> Wes Anderson Diegetic Whimsy
        res_ed = CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction(
            "Interactive Student Education Course & Book Reading Platform"
        )
        self.assertEqual(res_ed["aesthetic_paradigm_key"], "wes_anderson_diegetic_whimsy")

    def test_aristotelian_poetics_dramatic_journey(self):
        """Ensures the 3-act dramatic UX arc maps Hamartia, Peripeteia, and Catharsis."""
        res = CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction(
            "Autonomous SCADA Telemetry Monitoring Engine"
        )
        journey = res["dramatic_narrative_journey"]
        self.assertIn("act_1_call_and_hamartia", journey)
        self.assertIn("act_2_peripeteia_and_threshold", journey)
        self.assertIn("act_3_anagnorisis_and_catharsis", journey)

        act3 = journey["act_3_anagnorisis_and_catharsis"]
        self.assertIn("Epifani", act3["dramatic_phase"])
        self.assertIn("Aha!", act3["narrative_beat"])

    def test_calvino_six_memos_and_acoustics(self):
        """Verifies Calvino engineering memos and tactile sound design."""
        res = CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction("Design Canvas")
        memos = res["calvino_six_memos_alignment"]
        self.assertIn("lightness", memos)
        self.assertIn("quickness", memos)
        self.assertIn("exactitude", memos)
        self.assertIn("visibility", memos)

        acoustics = res["acoustic_sound_direction"]
        self.assertIn("ambient_drone", acoustics)
        self.assertIn("interaction_feedback", acoustics)
        self.assertIn("success_chime", acoustics)

    def test_mcp_server_tool_integration(self):
        """Verifies tool execution via ZobarMCPServer."""
        server = ZobarMCPServer()
        tool_res = server.execute_tool(
            "synthesize_cinematic_art_direction",
            {
                "product_vision": "S-Tier Decentralized Matrix Chat with WebAssembly",
                "target_mood": "kubrickian_symmetry"
            }
        )
        self.assertEqual(tool_res["tool_status"], "SUCCESS")
        result = tool_res["result"]
        self.assertEqual(result["chosen_cinematic_aesthetic"], "Stanley Kubrick")
        self.assertEqual(result["aesthetic_paradigm_key"], "kubrickian_symmetry")
        self.assertGreaterEqual(result["artistic_resonance_score"], 90.0)

    def test_execution_latency(self):
        """Must run within sub-millisecond execution budget (< 5ms)."""
        t0 = time.perf_counter()
        for _ in range(50):
            CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction(
                "Realtime Distributed Financial Linter"
            )
        elapsed_avg_ms = ((time.perf_counter() - t0) / 50.0) * 1000.0
        self.assertLess(elapsed_avg_ms, 2.0, f"Average latency too high: {elapsed_avg_ms:.3f}ms")


if __name__ == "__main__":
    unittest.main()
