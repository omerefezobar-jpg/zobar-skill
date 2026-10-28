#!/usr/bin/env python3
"""
Comprehensive Unit Test Suite for Frontier Innovator.
Tests parsing, scraping, competitor benchmarking, regulatory screening,
and security sanitization with 100% deterministic offline mocks.
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
from scripts.benchmark_competitors import benchmark_competitors
from scripts.search_prior_art import search_patents
from scripts.scan_regulations import evaluate_compliance

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

    def test_mermaid_complex_syntax_preservation_and_sanitization(self):
        """Verifies that subgraphs, Turkish letters, and node brackets survive, but raw tags are killed."""
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
        self.assertIn('Geliştirici Ortamı', output)
        self.assertIn('A --> B', output)
        # Raw script tag must be purged
        self.assertNotIn('<script>alert(1)</script>', output)

class TestSentimentAndNegation(unittest.TestCase):
    def test_negation_aware_friction_scoring(self):
        # Negated phrases should NOT register friction
        self.assertEqual(calculate_friction_score("The app is not slow at all"), 0)
        self.assertEqual(calculate_friction_score("We had no issues and it never crashed"), 0)
        self.assertEqual(calculate_friction_score("It isn't broken"), 0)
        
        # Positive affirmation of friction MUST register friction
        self.assertEqual(calculate_friction_score("The app is slow"), 1)
        
        # Genuine severe complaints must register high friction
        severe_text = "I hate this broken tool, it caused a terrible crash and disaster"
        self.assertGreaterEqual(calculate_friction_score(severe_text), 6)

class TestCompetitorAndRegulatoryEngines(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_benchmark_competitors_mock(self, mock_urlopen):
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
        self.assertEqual(len(res["competitors"]), 1)
        self.assertEqual(res["competitors"][0]["name"], "acme/compiler")
        self.assertEqual(res["competitors"][0]["license"], "Apache-2.0")

    def test_evaluate_compliance_ai_act(self):
        # High-risk trigger
        health_eval = evaluate_compliance("medical diagnostics autonomous agent")
        self.assertEqual(health_eval["eu_ai_act"]["tier"], "High Risk (Yüksek Risk)")
        
        # Specific transparency trigger
        llm_eval = evaluate_compliance("LLM code generation agent")
        self.assertEqual(llm_eval["eu_ai_act"]["tier"], "Specific Transparency Risk (Şeffaflık Yükümlülüğü)")

class TestAcademicAndPriorArtEngines(unittest.TestCase):
    SAMPLE_ARXIV_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <id>https://arxiv.org/abs/2401.00001v1</id>
        <published>2024-01-01T00:00:00Z</published>
        <title> Breakthrough Quantum Architecture </title>
        <summary> A comprehensive study on fault-tolerant quantum algorithms. </summary>
        <author><name>Dr. Alice Smith</name></author>
      </entry>
    </feed>
    """

    @patch("urllib.request.urlopen")
    def test_fetch_arxiv_mock(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.read.return_value = self.SAMPLE_ARXIV_XML
        mock_resp.__enter__.return_value = mock_resp
        mock_urlopen.return_value = mock_resp

        papers = fetch_arxiv_papers("quantum architecture", max_results=1)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["title"], "Breakthrough Quantum Architecture")
        self.assertIn("Pre-print", papers[0]["evidence_grade"])

if __name__ == "__main__":
    unittest.main()
