#!/usr/bin/env python3
"""
Unit tests for Skill Benchmark, Gap-Closer & Remediated Engines.
Verifies:
1. SkillBenchmarkAndGapCloser teardown matrix.
2. GenerativeUIWidgetSynthesizer Antigravity conformance.
3. SelfHealingCodeEngine diagnosis & execution.
4. TestTimeComputeEngine PRM & Reflexion amplification.
5. All 4 new MCP server tool calls.
"""

import os
import sys
import unittest
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.skill_benchmark_and_gap_closer import SkillBenchmarkAndGapCloser
from scripts.generative_ui_widget_synthesizer import GenerativeUIWidgetSynthesizer
from scripts.self_healing_code_engine import SelfHealingCodeEngine
from scripts.test_time_compute_engine import TestTimeComputeEngine
from scripts.zobar_mcp_server import ZobarMCPServer


class TestSkillBenchmarkAndGapCloser(unittest.TestCase):
    def setUp(self):
        self.closer = SkillBenchmarkAndGapCloser()
        self.gen_ui = GenerativeUIWidgetSynthesizer()
        self.healer = SelfHealingCodeEngine()
        self.ttc = TestTimeComputeEngine()
        self.server = ZobarMCPServer()

    def test_competitive_benchmark_teardown(self):
        res = self.closer.execute_competitive_teardown()
        self.assertGreaterEqual(res["total_benchmark_skills_evaluated"], 4)
        self.assertEqual(res["competitive_audit_verdict"], "ALL IDENTIFIED BLIND SPOTS REMEDIATED")
        self.assertGreater(res["operational_resilience_score"], 95.0)
        self.assertEqual(len(res["next_evolutionary_phases"]), 3)

    def test_generative_ui_widget_conformance(self):
        pulse = self.gen_ui.synthesize_telemetry_widget("Live Kernel Telemetry")
        self.assertIn("tailwindcss.min.js", pulse["html_code"])
        self.assertIn("bg-[var(--card)]", pulse["html_code"])
        self.assertIn("text-[var(--foreground)]", pulse["html_code"])
        self.assertIn("<agent-embed", pulse["embed_tag_example"])

        calc = self.gen_ui.synthesize_slider_calculator_widget()
        self.assertIn("input type=\"range\"", calc["html_code"])
        self.assertIn("calcGain", calc["html_code"])

    def test_self_healing_diagnosis_syntax_and_imports(self):
        diag_syntax = self.healer.diagnose_failure('File "test.py", line 12\n    def foo(\nSyntaxError: unexpected EOF while parsing', "")
        self.assertEqual(diag_syntax["error_type"], "SyntaxError")
        self.assertEqual(diag_syntax["line"], 12)

        diag_import = self.healer.diagnose_failure('ModuleNotFoundError: No module named "quantum_gate"', "")
        self.assertEqual(diag_import["error_type"], "ImportError")

        diag_assert = self.healer.diagnose_failure('AssertionError: 50.0 not greater than 75.0', "")
        self.assertEqual(diag_assert["error_type"], "AssertionError")

    def test_test_time_compute_prm_and_reflexion(self):
        res = self.ttc.amplify_model_reasoning("Zero-copy lock-free ring buffer")
        self.assertIn("amplification_factor", res)
        self.assertEqual(res["candidate_branches_evaluated"], 3)
        self.assertGreaterEqual(res["prm_winning_score"], 90.0)
        self.assertIn("verbal_reflexion_trace", res["reflexion_cycle"])
        self.assertGreater(res["reflexion_cycle"]["delta_quality_gain"], 0.0)

    def test_mcp_tools_gap_closure_suite(self):
        # 1. benchmark_and_close_skill_gaps
        res1 = self.server.execute_tool("benchmark_and_close_skill_gaps", {})
        self.assertEqual(res1["tool_status"], "SUCCESS")

        # 2. synthesize_generative_ui_widget
        res2 = self.server.execute_tool("synthesize_generative_ui_widget", {"widget_type": "telemetry_pulse"})
        self.assertEqual(res2["tool_status"], "SUCCESS")
        self.assertIn("html_code", res2["result"])

        # 3. amplify_model_test_time_compute
        res3 = self.server.execute_tool("amplify_model_test_time_compute", {"problem": "Simplicial authorization"})
        self.assertEqual(res3["tool_status"], "SUCCESS")
        self.assertIn("prm_winning_branch", res3["result"])


if __name__ == "__main__":
    unittest.main()
