#!/usr/bin/env python3
"""
Comprehensive Unit Test Suite for Frontier Innovator.
Tests all parsing, scraping, and export engines with offline mocks,
ensuring 100% deterministic regression testing without relying on live APIs.
"""

import unittest
from unittest.mock import patch, MagicMock
import io
import json

from scripts.export_html_report import parse_markdown_to_html, is_safe_url, export_to_html
from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.mine_user_sentiment import clean_html, search_hn_sentiment, FRICTION_KEYWORDS
from scripts.search_prior_art import search_patents

class TestExportHtmlSecurity(unittest.TestCase):
    def test_safe_url_validation(self):
        self.assertTrue(is_safe_url("https://example.com"))
        self.assertTrue(is_safe_url("http://arxiv.org/abs/123"))
        self.assertTrue(is_safe_url("#section-1"))
        self.assertTrue(is_safe_url("./scripts/test.py"))
        
        # Malicious protocols MUST be rejected
        self.assertFalse(is_safe_url("javascript:alert(1)"))
        self.assertFalse(is_safe_url("data:text/html;base64,PHNjcmlwdD4="))
        self.assertFalse(is_safe_url("vbscript:msgbox(1)"))
        self.assertFalse(is_safe_url(""))

    def test_xss_injection_escaping(self):
        malicious_input = "# Heading with <script>alert('pwned')</script>\n" \
                          "Normal text with [evil link](javascript:alert(1)) and <b>unescaped</b> html."
        output_html = parse_markdown_to_html(malicious_input)
        
        # Script tags must be escaped
        self.assertNotIn("<script>alert('pwned')</script>", output_html)
        self.assertIn("&lt;script&gt;alert(&#x27;pwned&#x27;)&lt;/script&gt;", output_html)
        
        # javascript: link should NOT be an href
        self.assertNotIn('href="javascript:alert(1)"', output_html)

    def test_mermaid_preservation(self):
        md = "```mermaid\nflowchart TD\nA --> B\n```"
        output = parse_markdown_to_html(md)
        self.assertIn('<div class="mermaid">', output)
        self.assertIn("A --> B", output)

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
        self.assertEqual(papers[0]["evidence_grade"], "Akademik Ön Baskı (arXiv Pre-print)")

class TestSentimentMiner(unittest.TestCase):
    def test_clean_html(self):
        raw = "<p>This is a <b>buggy</b> &amp; terrible tool.</p>"
        cleaned = clean_html(raw)
        self.assertEqual(cleaned, "This is a  buggy  & terrible tool.")

    @patch("urllib.request.urlopen")
    def test_hn_mining_mock(self, mock_urlopen):
        sample_json = json.dumps({
            "hits": [
                {
                    "objectID": "12345",
                    "comment_text": "This framework is so slow and broken, I hate it.",
                    "author": "tester_dev",
                    "story_title": "Modern Frameworks",
                    "created_at": "2026-03-01T12:00:00Z"
                }
            ]
        }).encode("utf-8")

        mock_response = MagicMock()
        mock_response.read.return_value = sample_json
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        results = search_hn_sentiment("Modern Frameworks", max_comments=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["author"], "tester_dev")
        # Should have detected friction keywords: slow, broken, hate
        self.assertGreaterEqual(results[0]["friction_score"], 2)

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

if __name__ == "__main__":
    unittest.main()
