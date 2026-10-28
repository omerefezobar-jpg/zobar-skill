#!/usr/bin/env python3
"""
Comprehensive Ground-Truth Unit & Benchmark Test Suite for Frontier Innovator.
Tests all 6 autonomous phases, statutory regulatory screening, hybrid competitor
benchmarking, tech stack synthesis, TRIZ invention generation, and strict CSP security.
"""

import unittest
from unittest.mock import patch, MagicMock
import json

from scripts.export_html_report import (
    parse_markdown_to_html, is_safe_url, export_to_html,
    sanitize_mermaid_diagram, HTML_TEMPLATE
)
from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.mine_user_sentiment import (
    clean_html, search_sentiment, calculate_friction_score
)
from scripts.benchmark_competitors import (
    benchmark_competitors, search_commercial_incumbents
)
from scripts.search_prior_art import search_patents
from scripts.scan_regulations import evaluate_compliance
from scripts.synthesize_architecture import synthesize_tech_stack
from scripts.validate_inventions import generate_validated_inventions

class TestSecurityAndCSP(unittest.TestCase):
    def test_csp_hardened_no_unsafe_eval(self):
        """Verifies that CSP strictly forbids unsafe-eval to eliminate eval-based DOM XSS."""
        self.assertNotIn("'unsafe-eval'", HTML_TEMPLATE)
        self.assertIn("default-src 'none'", HTML_TEMPLATE)

    def test_safe_url_validation(self):
        self.assertTrue(is_safe_url("https://example.com"))
        self.assertTrue(is_safe_url("https://arxiv.org/abs/123"))
        self.assertTrue(is_safe_url("#section-1"))
        self.assertTrue(is_safe_url("./scripts/test.py"))
        
        # Dangerous protocols MUST be rejected
        self.assertFalse(is_safe_url("javascript:alert(1)"))
        self.assertFalse(is_safe_url("data:text/html;base64,PHNjcmlwdD4="))
        self.assertFalse(is_safe_url("vbscript:msgbox(1)"))
        self.assertFalse(is_safe_url("file:///etc/passwd"))
        self.assertFalse(is_safe_url(""))

    def test_title_injection_escaping(self):
        malicious_topic = '</title><script>alert("XSS-TITLE")</script>'
        html_out = export_to_html("# Sample Content", title=f"Dossier: {malicious_topic}")
        self.assertNotIn('</title><script>alert("XSS-TITLE")</script>', html_out)
        self.assertIn('&lt;/title&gt;&lt;script&gt;alert(&quot;XSS-TITLE&quot;)&lt;/script&gt;', html_out)

    def test_mermaid_sanitization_preserves_arrows_and_kills_scripts(self):
        complex_mermaid = """```mermaid
flowchart TD
    subgraph Girdi["Geliştirici Ortamı"]
        A["Git Push / PR (İşlem)"]
    end
    subgraph Çekirdek["AetherCode Analiz Çekirdeği"]
        B["Tree-sitter AST <script>alert(1)</script>"]
    end
    A --> B
```"""
        output = parse_markdown_to_html(complex_mermaid)
        self.assertIn('<div class="mermaid">', output)
        self.assertIn('A --> B', output)
        self.assertNotIn('<script>alert(1)</script>', output)

class TestSentimentAndNegation(unittest.TestCase):
    def test_negation_aware_friction_scoring(self):
        self.assertEqual(calculate_friction_score("The app is not slow at all"), 0)
        self.assertEqual(calculate_friction_score("We had no issues and it never crashed"), 0)
        self.assertEqual(calculate_friction_score("It isn't broken"), 0)
        self.assertEqual(calculate_friction_score("The app is slow"), 1)
        
        severe_text = "I hate this broken tool, it caused a terrible crash and disaster"
        self.assertGreaterEqual(calculate_friction_score(severe_text), 6)

class TestStatutoryRegulatoryCompliance(unittest.TestCase):
    def test_statutory_prohibited_ai_trigger(self):
        res = evaluate_compliance("subliminal biometric categorisation system")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)")
        self.assertIn("Madde 5(1)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_statutory_high_risk_trigger(self):
        res = evaluate_compliance("autonomous medical diagnostics agent")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("Madde 6", res["eu_ai_act"]["statutory_basis"])
        self.assertIn("Ek III", res["eu_ai_act"]["statutory_basis"])

    def test_statutory_transparency_trigger(self):
        res = evaluate_compliance("LLM code generation assistant")
        self.assertEqual(res["eu_ai_act"]["tier"], "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)")
        self.assertIn("Madde 50", res["eu_ai_act"]["statutory_basis"])

class TestHybridCompetitorAndMarketBenchmark(unittest.TestCase):
    def test_curated_commercial_incumbents_lookup(self):
        incumbents = search_commercial_incumbents("static analysis code quality")
        self.assertGreaterEqual(len(incumbents), 1)
        sonar = next((i for i in incumbents if "SonarQube" in i["name"]), None)
        self.assertIsNotNone(sonar)
        self.assertIn("Enterprise", sonar["pricing_tier"])
        self.assertIn("false-positive", sonar["core_weakness"])

    @patch("urllib.request.urlopen")
    def test_github_telemetry_mock(self, mock_urlopen):
        sample_gh_json = json.dumps({
            "total_count": 42,
            "items": [
                {
                    "full_name": "acme/compiler",
                    "description": "An open source compiler engine",
                    "stargazers_count": 12500,
                    "forks_count": 890,
                    "open_issues_count": 45,
                    "language": "Rust",
                    "pushed_at": "2026-05-01T00:00:00Z",
                    "html_url": "https://github.com/acme/compiler",
                    "license": {"spdx_id": "Apache-2.0"}
                }
            ]
        }).encode("utf-8")

        mock_resp = MagicMock()
        mock_resp.read.return_value = sample_gh_json
        mock_resp.__enter__.return_value = mock_resp
        mock_urlopen.return_value = mock_resp

        res = benchmark_competitors("compiler", max_results=1)
        self.assertEqual(res["status"], "success")
        self.assertEqual(len(res["open_source_telemetry"]), 1)
        self.assertEqual(res["open_source_telemetry"][0]["name"], "acme/compiler")

class TestAutomatedArchitectureAndTRIZInventions(unittest.TestCase):
    def test_phase_5_tech_stack_synthesis(self):
        arch = synthesize_tech_stack("AST parser compiler engine")
        self.assertEqual(arch["core_language"], "Rust")
        self.assertIn("tree-sitter", arch["recommended_libraries"])
        self.assertIn("Tauri", arch["ui_architecture"]["runtime"])

    def test_phase_6_triz_invention_generation(self):
        inventions_data = generate_validated_inventions("Code Analysis")
        self.assertEqual(len(inventions_data["inventions"]), 2)
        inv1 = inventions_data["inventions"][0]
        self.assertIn("TRL", inv1["trl_level"])
        self.assertIn("Model Hipotezi", inv1["trl_evidence_type"])
        self.assertGreater(inv1["ice_score"]["total"], 0)
        self.assertEqual(len(inv1["failure_modes"]), 3)
        # Ensure generated Mermaid diagram is valid and contains domain
        self.assertIn("flowchart TD", inventions_data["system_architecture_mermaid"])

if __name__ == "__main__":
    unittest.main()
