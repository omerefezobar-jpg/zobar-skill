#!/usr/bin/env python3
"""
Unit and Integration Tests for Video Session Intelligence Engine & MCP Tooling.
Verifies YouTube & Instagram video ingestion, WebVTT/SRT transcript parsing,
domain relevance scoring, blueprint/token distillation, session context synthesis,
and MCP server execution.
"""

import unittest
import os
import sys

# Ensure scripts dir is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from video_session_intelligence_engine import (
    VideoSessionIntelligenceEngine,
    DOMAIN_TAXONOMY,
    OFFLINE_BENCHMARK_CORPUS
)
from zobar_mcp_server import ZobarMCPServer


class TestVideoSessionIntelligenceEngine(unittest.TestCase):
    def setUp(self):
        self.engine = VideoSessionIntelligenceEngine()

    def test_parse_video_url_youtube(self):
        """Must correctly parse watch, youtu.be, shorts, and raw IDs."""
        urls = [
            ("https://www.youtube.com/watch?v=kCc8FmEb1nY", "kCc8FmEb1nY"),
            ("https://youtu.be/kCc8FmEb1nY", "kCc8FmEb1nY"),
            ("https://www.youtube.com/shorts/kCc8FmEb1nY", "kCc8FmEb1nY"),
            ("kCc8FmEb1nY", "kCc8FmEb1nY")
        ]
        for url, expected_id in urls:
            parsed = self.engine.parse_video_url(url)
            self.assertEqual(parsed["platform"], "youtube")
            self.assertEqual(parsed["video_id"], expected_id)
            self.assertIn("watch?v=", parsed["canonical_url"])

    def test_parse_video_url_instagram(self):
        """Must correctly parse Instagram reel, reels, and post URLs."""
        urls = [
            ("https://www.instagram.com/reel/C9xK4mLP10a/", "C9xK4mLP10a"),
            ("https://www.instagram.com/reels/C9xK4mLP10a", "C9xK4mLP10a"),
            ("https://www.instagram.com/p/C9xK4mLP10a/", "C9xK4mLP10a")
        ]
        for url, expected_id in urls:
            parsed = self.engine.parse_video_url(url)
            self.assertEqual(parsed["platform"], "instagram")
            self.assertEqual(parsed["video_id"], expected_id)
            self.assertIn("/reel/", parsed["canonical_url"])

    def test_parse_transcript_text_vtt_srt(self):
        """Must correctly parse WebVTT and SRT timestamped captions."""
        vtt_sample = (
            "WEBVTT\n\n"
            "00:00:05.100 --> 00:00:08.500\n"
            "In this video we explore zero-copy ring buffers.\n\n"
            "00:00:09.000 --> 00:00:14.200\n"
            "Lock-free concurrency ensures sub-millisecond throughput under extreme contention."
        )
        segments = self.engine.parse_transcript_text(vtt_sample)
        self.assertEqual(len(segments), 2)
        self.assertAlmostEqual(segments[0]["start"], 5.1)
        self.assertIn("zero-copy ring buffers", segments[0]["text"])
        self.assertAlmostEqual(segments[1]["start"], 9.0)
        self.assertIn("Lock-free concurrency", segments[1]["text"])

    def test_score_transcript_relevance(self):
        """Must identify relevant engineering domains and compute technical density."""
        tech_text = (
            "We are implementing PagedAttention and KV-cache compression to optimize "
            "transformer attention mechanism for our high-throughput reasoning model."
        )
        tech_result = self.engine.score_transcript_relevance(tech_text)
        self.assertTrue(tech_result["is_relevant"])
        self.assertEqual(tech_result["primary_domain"], "FRONTIER_AI_AND_ML")
        self.assertGreater(tech_result["relevance_score"], 0)
        self.assertGreater(tech_result["technical_density"], 0)

        # Irrelevant casual banter
        casual_text = "Hey guys welcome back today I went to the grocery store and bought apples and oranges."
        casual_result = self.engine.score_transcript_relevance(casual_text)
        self.assertEqual(casual_result["technical_density"], 0.0)

    def test_distill_video_intelligence(self):
        """Must extract blueprints, tokens, code snippets, anti-patterns, and knowledge triples."""
        segments = [
            {
                "start": 0.0,
                "duration": 15.0,
                "text": "For fluid S-Tier UI micro-interactions, use spring physics with stiffness 180 and damping 24. Do not blur giant background surfaces."
            }
        ]
        intel = self.engine.distill_video_intelligence(
            title="S-Tier UI Spring Physics",
            creator="DesignPro",
            segments=segments,
            primary_domain="FRONTEND_AND_DESIGN"
        )
        self.assertIn("spring_physics", intel["design_tokens"])
        self.assertEqual(intel["design_tokens"]["spring_physics"]["stiffness"], 180)
        self.assertEqual(intel["design_tokens"]["spring_physics"]["damping"], 24)
        self.assertTrue(len(intel["code_snippets"]) > 0)
        self.assertTrue(len(intel["anti_patterns"]) > 0)
        self.assertTrue(len(intel["knowledge_triples"]) > 0)

    def test_transcribe_and_ingest_benchmark_and_custom(self):
        """Must ingest benchmark videos as well as custom transcripts, persisting records."""
        # 1. Ingest YouTube benchmark
        res_yt = self.engine.transcribe_and_ingest("https://www.youtube.com/watch?v=kCc8FmEb1nY")
        self.assertEqual(res_yt["status"], "success")
        self.assertEqual(res_yt["platform"], "youtube")
        self.assertIn("GPT", res_yt["title"])
        self.assertEqual(res_yt["primary_domain"], "FRONTIER_AI_AND_ML")

        # 2. Ingest Instagram benchmark
        res_ig = self.engine.transcribe_and_ingest("https://www.instagram.com/reel/C9xK4mLP10a/")
        self.assertEqual(res_ig["status"], "success")
        self.assertEqual(res_ig["platform"], "instagram")
        self.assertIn("PostgreSQL", res_ig["title"])
        self.assertEqual(res_ig["primary_domain"], "SYSTEMS_ARCHITECTURE")

        # 3. Ingest Custom Transcript
        custom_txt = "Rule of thumb: always enforce PostgreSQL Row-Level Security for multi-tenant isolation."
        res_custom = self.engine.transcribe_and_ingest(
            url_or_id="custom_video_101",
            custom_transcript=custom_txt,
            title_override="Custom Multi-Tenant Video",
            creator_override="SecurityTeam"
        )
        self.assertEqual(res_custom["status"], "success")
        self.assertEqual(res_custom["title"], "Custom Multi-Tenant Video")

    def test_query_video_insights_and_context_synthesis(self):
        """Must query indexed video intelligence and synthesize clean prompt enrichment context."""
        # Seed engine with benchmark
        self.engine.transcribe_and_ingest("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
        # Query
        matches = self.engine.query_video_insights("CSS spring physics", limit=1)
        self.assertGreaterEqual(len(matches), 1)
        self.assertIn("Fireship", matches[0]["creator"])

        # Synthesize markdown context block
        context_md = self.engine.synthesize_session_enhancement_context("spring physics")
        self.assertIn("### Active Session Video Intelligence Context", context_md)
        self.assertIn("Fireship", context_md)
        self.assertIn("stiffness", context_md.lower())

    def test_mcp_server_video_tools(self):
        """Must execute all 3 video session tools cleanly through MCP JSON-RPC router."""
        server = ZobarMCPServer()

        # Tool 1: transcribe_and_ingest_video
        res1 = server.execute_tool("transcribe_and_ingest_video", {
            "url_or_id": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        })
        self.assertEqual(res1["tool_status"], "SUCCESS")
        self.assertIn("title", res1["result"])

        # Tool 2: query_video_session_insights
        res2 = server.execute_tool("query_video_session_insights", {
            "query": "spring physics",
            "limit": 2
        })
        self.assertEqual(res2["tool_status"], "SUCCESS")
        self.assertIsInstance(res2["result"], list)

        # Tool 3: synthesize_session_video_context
        res3 = server.execute_tool("synthesize_session_video_context", {
            "current_topic": "KV-cache and Transformer Attention"
        })
        self.assertEqual(res3["tool_status"], "SUCCESS")
        self.assertIn("context_markdown", res3["result"])
        self.assertIn("Active Session Video Intelligence", res3["result"]["context_markdown"])


if __name__ == "__main__":
    unittest.main()
