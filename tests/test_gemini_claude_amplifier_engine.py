#!/usr/bin/env python3
"""
Unit and Integration Tests for Gemini vs Claude Transcendence Engine & MCP Tooling.
Verifies comparative benchmark dimensions, diagnostic accuracy, surgical guardrail generation,
and MCP server tool execution.
"""

import unittest
import os
import sys

# Ensure scripts dir in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from gemini_claude_amplifier_engine import (
    GeminiClaudeAmplifierEngine,
    MODEL_COMPARISON_MATRIX
)
from zobar_mcp_server import ZobarMCPServer


class TestGeminiClaudeAmplifierEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GeminiClaudeAmplifierEngine()

    def test_model_comparison_matrix_structure(self):
        """Must cover core technical dimensions comparing Claude and Gemini."""
        required = [
            "CODE_REASONING_AND_LOGIC",
            "LARGE_REPO_CONTEXT_INGESTION",
            "LATENCY_AND_FINOPS",
            "TOOL_USE_AND_SELF_HEALING"
        ]
        for key in required:
            self.assertIn(key, MODEL_COMPARISON_MATRIX)
            entry = MODEL_COMPARISON_MATRIX[key]
            self.assertIn("claude_baseline", entry)
            self.assertIn("gemini_baseline", entry)
            self.assertIn("transcendence_scaffold", entry)

    def test_get_comparative_benchmark(self):
        """Must return diagnostic identifying Gemini's verbose bias and Claude's conciseness."""
        res = self.engine.get_comparative_benchmark()
        self.assertEqual(res["status"], "SUCCESS")
        self.assertIn("Claude", res["core_diagnostic"])
        self.assertIn("Gemini", res["core_diagnostic"])
        self.assertIn("fluff", res["core_diagnostic"].lower())

    def test_synthesize_claude_beating_guardrails(self):
        """Must synthesize strict zero-fluff prompt and tactical advantages."""
        res = self.engine.synthesize_claude_beating_guardrails("Fix race condition in Tokio ring buffer")
        self.assertEqual(res["target_task"], "Fix race condition in Tokio ring buffer")
        
        prompt = res["guardrail_system_prompt"]
        self.assertIn("SURGICAL EXECUTION PROTOCOL", prompt)
        self.assertIn("ZERO CONVERSATIONAL FLUFF", prompt)
        self.assertIn("TEST-TIME VERIFICATION GATE", prompt)
        self.assertIn("2026 ACADEMIC GROUND TRUTH", prompt)
        self.assertIn("SELF-HEALING FALLBACK", prompt)

        advantages = res["tactical_advantages_over_claude"]
        self.assertTrue(len(advantages) >= 3)

    def test_mcp_server_claude_transcendence_tools(self):
        """Must execute both Gemini/Claude tools cleanly via MCP JSON-RPC router."""
        server = ZobarMCPServer()

        # Tool 1: benchmark_gemini_vs_claude
        res1 = server.execute_tool("benchmark_gemini_vs_claude", {})
        self.assertEqual(res1["tool_status"], "SUCCESS")
        self.assertEqual(res1["result"]["status"], "SUCCESS")
        self.assertIn("benchmark_dimensions", res1["result"])

        # Tool 2: synthesize_claude_beating_guardrails
        res2 = server.execute_tool("synthesize_claude_beating_guardrails", {
            "target_task": "Port PostgreSQL extension to Rust"
        })
        self.assertEqual(res2["tool_status"], "SUCCESS")
        self.assertIn("guardrail_system_prompt", res2["result"])
        self.assertIn("SURGICAL EXECUTION", res2["result"]["guardrail_system_prompt"])


if __name__ == "__main__":
    unittest.main()
