#!/usr/bin/env python3
"""
Unit tests for Master AI Model Amplifier & Frontier Meta-Cognitive Engine.
Verifies Feynman deconstruction, Monte Carlo Tree Search (MCTS), Process Reward Model (PRM)
test-time compute scaling, DSPy prompt compilation, and MCP server tool execution.
"""

import os
import sys
import unittest
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.master_ai_model_amplifier import MasterAIModelAmplifier
from scripts.zobar_mcp_server import ZobarMCPServer


class TestMasterAIModelAmplifier(unittest.TestCase):
    def setUp(self):
        self.engine = MasterAIModelAmplifier()
        self.server = ZobarMCPServer()

    def test_feynman_deconstruction(self):
        res = self.engine.feynman_deconstruction("High-throughput microsecond orderbook trading system with lock-free concurrency")
        self.assertIn("feynman_simplification", res)
        self.assertIn("atomic_mathematical_invariants", res)
        self.assertGreaterEqual(len(res["atomic_mathematical_invariants"]), 3)
        self.assertEqual(res["cognitive_clarity_score"], 98.0)

    def test_mcts_tree_search(self):
        res = self.engine.mcts_tree_search("Zero-latency inter-process communication", simulation_iterations=10)
        self.assertIn("evaluated_tree_nodes", res)
        self.assertIn("winning_mcts_branch", res)
        self.assertGreaterEqual(res["winning_q_value"], 80.0)
        self.assertEqual(res["search_confidence"], "Converged onto Frontier Optimal Node")

    def test_scale_test_time_compute(self):
        res = self.engine.scale_test_time_compute("Ultra-low-latency distributed consensus")
        self.assertEqual(res["test_time_compute_branches"], 4)
        self.assertIn("optimal_strategy", res)
        self.assertGreaterEqual(res["prm_confidence_rating"], 90.0)
        self.assertIn("100x", res["reasoning_multiplier"])

    def test_dspy_prompt_compilation(self):
        res = self.engine.compile_optimized_meta_prompt("HFT Order Router", "FinTech")
        self.assertIn("compiled_signature", res)
        self.assertIn("FORMAL COMPILER SIGNATURE", res["compiled_signature"])
        self.assertIn("Feynman Deconstruction", res["compiled_signature"])

    def test_complete_amplification_pipeline(self):
        res = self.engine.execute_complete_amplification("Global multi-region real-time permission graph")
        self.assertEqual(res["amplification_status"], "SUPER_REASONING_STATE_ACHIEVED")
        self.assertEqual(res["model_amplification_multiplier"], "100x Reasoning Multiplication")
        self.assertIn("feynman_phase", res)
        self.assertIn("mcts_phase", res)
        self.assertIn("test_time_compute_phase", res)
        self.assertIn("compiled_meta_prompt", res)
        self.assertLess(res["execution_latency_ms"], 10.0)

    def test_mcp_tool_amplify_meta_cognition(self):
        res = self.server.execute_tool("amplify_ai_model_meta_cognition", {
            "problem": "Real-time BCI neural signal processing with zero phase distortion",
            "domain": "NeuroTech"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertEqual(res["result"]["amplification_status"], "SUPER_REASONING_STATE_ACHIEVED")
        self.assertIn("feynman_phase", res["result"])


if __name__ == "__main__":
    unittest.main()
