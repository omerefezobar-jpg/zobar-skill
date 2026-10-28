#!/usr/bin/env python3
"""
Comprehensive, Hardened Unit Test Suite for Frontier Innovator.
Includes security tests against XSS, Mermaid tag injection, title injection,
academic pre-print terminology integrity, and multi-source sentiment mocks.
"""

import unittest
from unittest.mock import patch, MagicMock
import json

from scripts.export_html_report import (
    parse_markdown_to_html, is_safe_url, export_to_html, sanitize_mermaid_diagram
)
from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.mine_user_sentiment import (
    clean_html, search_hn_sentiment, search_sentiment, calculate_friction_score
)
from scripts.search_prior_art import search_patents

class TestExportHtmlSecurityAndInjection(unittest.TestCase):
    def test_safe_url_validation(self):
        self.assertTrue(is_safe_url("https://example.com"))
        self.assertTrue(is_safe_url("http://arxiv.org/abs/123"))
        self.assertTrue(is_safe_url("#section-1"))
        self.assertTrue(is_safe_url("./scripts/test.py"))
        
        # Malicious and dangerous URI protocols MUST be rejected
        self.assertFalse(is_safe_url("javascript:alert(1)"))
        self.assertFalse(is_safe_url("data:text/html;base64,PHNjcmlwdD4="))
        self.assertFalse(is_safe_url("vbscript:msgbox(1)"))
        self.assertFalse(is_safe_url("file:///etc/passwd"))
        self.assertFalse(is_safe_url(None))
        self.assertFalse(is_safe_url(""))

    def test_title_injection_escaping(self):
        malicious_topic = '</title><script>alert("XSS-TITLE")</script>'
        html_out = export_to_html("# Sample Content", title=f"Dossier: {malicious_topic}")
        
        # Raw closing tag or script must never exist unescaped in title
        self.assertNotIn('</title><script>alert("XSS-TITLE")</script>', html_out)
        self.assertIn('&lt;/title&gt;&lt;script&gt;alert(&quot;XSS-TITLE&quot;)&lt;/script&gt;', html_out)

    def test_xss_injection_escaping_body(self):
        malicious_input = "# Heading with <script>alert('pwned')</script>\n" \
                          "Normal text with [evil link](javascript:alert(1)) and <img src=x onerror=alert(2)>."
        output_html = parse_markdown_to_html(malicious_input)
        
        # Raw tags must be escaped
        self.assertNotIn("<script>alert('pwned')</script>", output_html)
        self.assertNotIn("<img src=x onerror=alert(2)>", output_html)
        self.assertIn("&lt;script&gt;alert(&#x27;pwned&#x27;)&lt;/script&gt;", output_html)
        
        # javascript: link should NOT be an href
        self.assertNotIn('href="javascript:alert(1)"', output_html)

    def test_mermaid_sanitization_and_isolation(self):
        # Attack payload attempting to break out of .mermaid div
        malicious_mermaid = '```mermaid\n' \
                            'graph TD\n' \
                            'A["Node A"] --> B["Node B</div><script>alert(1)</script>"]\n' \
                            '```'
        output = parse_markdown_to_html(malicious_mermaid)
        self.assertIn('<div class="mermaid">', output)
        # Injected script and div tags must be stripped by sanitize_mermaid_diagram
        self.assertNotIn('<script>alert(1)</script>', output)
        self.assertNotIn('</div><script>', output)

class TestAcademicFetcher(unittest.TestCase):
    SAMPLE_ARXIV_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <entry>
        <id>http://arxiv.org/abs/2401.00001v1</id>
        <published>2024-01-01T00:00:00Z</published>
        <title> Breakthrough Quantum Architecture </title>
        <summary> A comprehensive study on fault-tolerant quantum algorithms. </summary>
        <author><name>Dr. Alice Smith</name></author>
        <author><name>Dr. Bob Jones</name></author>
      </entry>
    </feed>
    """

    @patch("urllib.request.urlopen")
    def test_fetch_arxiv_mock(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = self.SAMPLE_ARXIV_XML
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        papers = fetch_arxiv_papers("quantum architecture", max_results=1)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["title"], "Breakthrough Quantum Architecture")
        self.assertIn("Dr. Alice Smith", papers[0]["authors"])
        self.assertEqual(papers[0]["published"], "2024-01-01")
        # Ensure evidence grade specifically reflects pre-print status
        self.assertIn("Pre-print", papers[0]["evidence_grade"])

class TestSentimentMiner(unittest.TestCase):
    def test_clean_html(self):
        raw = "<p>This is a <b>buggy</b> &amp; terrible tool.</p>"
        cleaned = clean_html(raw)
        self.assertEqual(cleaned, "This is a  buggy  & terrible tool.")

    def test_weighted_friction_score(self):
        # Mild feedback
        self.assertEqual(calculate_friction_score("The tool is a bit slow and clunky"), 2)
        # Heavy critical complaint (hate=2, broken=2, terrible=2, crash=2)
        score = calculate_friction_score("I hate this broken app, it is a terrible disaster and causes crashes")
        self.assertGreaterEqual(score, 6)

    @patch("scripts.mine_user_sentiment.search_hn_sentiment")
    @patch("scripts.mine_user_sentiment.search_reddit_sentiment")
    def test_multi_source_aggregation_and_reporting(self, mock_reddit, mock_hn):
        mock_hn.return_value = {
            "status": "success",
            "comments": [{
                "source": "Hacker News",
                "author": "hn_dev",
                "date": "2026-01-01",
                "title": "Discussion",
                "url": "https://news.ycombinator.com/item?id=1",
                "friction_score": 5,
                "text": "Completely broken framework"
            }]
        }
        mock_reddit.return_value = {
            "status": "rate-limited/error",
            "error": "HTTP 429",
            "comments": []
        }

        res = search_sentiment("test query", max_comments=2)
        self.assertEqual(len(res["comments"]), 1)
        self.assertEqual(res["hn_status"], "success")
        self.assertEqual(res["reddit_status"], "rate-limited/error")
        self.assertIn("Hacker News (1 veri)", res["summary"])
        self.assertIn("Reddit", res["summary"])

class TestPriorArtScreener(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_patent_search_mock(self, mock_urlopen):
        sample_json = json.dumps({
            "results": {
                "cluster": [
                    {
                        "result": [
                            {
                                "patent": {
                                    "publication_number": "US1234567A",
                                    "title": "Autonomous Neural Synthesis",
                                    "assignee": "Tech Corp",
                                    "filing_date": "2023-05-10",
                                    "snippet": "A method for neural code synthesis."
                                }
                            }
                        ]
                    }
                ]
            }
        }).encode("utf-8")

        mock_response = MagicMock()
        mock_response.read.return_value = sample_json
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        patents = search_patents("Neural Synthesis", max_results=1)
        self.assertEqual(len(patents), 1)
        self.assertEqual(patents[0]["id"], "US1234567A")
        self.assertEqual(patents[0]["assignee"], "Tech Corp")
        self.assertIn("Prior Art", patents[0]["legal_nature"])

if __name__ == "__main__":
    unittest.main()
