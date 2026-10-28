#!/usr/bin/env python3
"""
Unit and Integration Tests for Stage 11: Trend & Trick Harvester Engine.
Verifies multi-source trend ingestion (YouTube/Instagram Reels, GitHub Trending, Global News),
continuous active session syncing, continual memory knowledge injection, and MCP tool execution.
"""

import unittest
import os
import sys

# Ensure scripts dir in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from trend_trick_harvester_engine import TrendTrickHarvesterEngine
from zobar_mcp_server import ZobarMCPServer


class TestTrendTrickHarvesterEngine(unittest.TestCase):
    def setUp(self):
        self.engine = TrendTrickHarvesterEngine()

    def test_harvest_youtube_instagram_reels(self):
        """Must return video tricks with creator attribution and actionable snippets."""
        reels = self.engine.harvest_youtube_instagram_reels(topic="react", max_items=2)
        self.assertGreaterEqual(len(reels), 1)
        item = reels[0]
        self.assertIn("title", item)
        self.assertIn("creator", item)
        self.assertIn("trick_snippet", item)
        self.assertTrue(item["viral_score"] >= 50)

    def test_harvest_github_trending_repos(self):
        """Must return trending repositories with star telemetry and architectural imports."""
        repos = self.engine.harvest_github_trending_repos(query="mcp", max_items=2)
        self.assertGreaterEqual(len(repos), 1)
        item = repos[0]
        self.assertIn("title", item)
        self.assertIn("verified_impact", item)
        self.assertIn("source_url", item)

    def test_harvest_global_tech_news(self):
        """Must return tech news wire items with discussion metrics."""
        news = self.engine.harvest_global_tech_news(category="ai", max_items=2)
        self.assertGreaterEqual(len(news), 1)
        item = news[0]
        self.assertIn("title", item)
        self.assertIn("viral_score", item)

    def test_search_tricks_filtering(self):
        """Keyword and platform filtering must work accurately."""
        # By keyword
        css_tricks = self.engine.search_tricks(keyword="css")
        self.assertGreaterEqual(len(css_tricks), 1)
        self.assertTrue(any("css" in t["title"].lower() or "css" in t.get("tags", []) for t in css_tricks))

        # By platform
        ig_tricks = self.engine.search_tricks(platform="Instagram")
        self.assertGreaterEqual(len(ig_tricks), 1)
        for t in ig_tricks:
            self.assertIn("Instagram", t["platform"])

    def test_sync_active_session_assimilates_memory(self):
        """Syncing active session must update heartbeat, update queue, and push to continual memory."""
        res = self.engine.sync_active_session()
        self.assertEqual(res["status"], "ACTIVE_MONITORING")
        self.assertIn("last_heartbeat_utc", res)
        self.assertGreater(res["total_vault_tricks"], 0)
        self.assertTrue(len(res["active_monitoring_channels"]) >= 3)

        # Verify memory engine received knowledge triples
        memory_triples = self.engine.memory_engine.triples
        has_trick_subject = any(t.get("subject") in ["live_trend_harvester", "trick_vault"] for t in memory_triples)
        self.assertTrue(has_trick_subject)

    def test_origin_separation_live_vs_curated(self):
        """Must strictly separate LIVE_NETWORK_SCRAPED from CURATED_OFFLINE_BENCHMARK."""
        curated_matches = self.engine.search_tricks(origin_filter="CURATED_ONLY")
        self.assertGreaterEqual(len(curated_matches), 5)
        for t in curated_matches:
            self.assertEqual(t.get("data_origin"), "CURATED_OFFLINE_BENCHMARK")

        live_matches = self.engine.search_tricks(origin_filter="LIVE_ONLY")
        for t in live_matches:
            self.assertEqual(t.get("data_origin"), "LIVE_NETWORK_SCRAPED")

    def test_mathematical_viral_score_formulas(self):
        """Deterministic logarithmic engagement verification."""
        # Test GitHub formula
        score_gh, formula_gh = self.engine.calculate_github_viral_score(stars=10000, forks=2000)
        self.assertGreaterEqual(score_gh, 85)
        self.assertIn("log10", formula_gh)

        # Test Hacker News formula
        score_hn, formula_hn = self.engine.calculate_news_viral_score(points=500, comments=150)
        self.assertGreaterEqual(score_hn, 80)
        self.assertIn("log10", formula_hn)

    def test_continuous_daemon_loop_and_telemetry_audit(self):
        """Daemon must execute real ticks and write append-only telemetry records."""
        audit_file = self.engine.audit_log_path
        initial_lines = 0
        if os.path.exists(audit_file):
            with open(audit_file, "r", encoding="utf-8") as f:
                initial_lines = len(f.readlines())

        # Run 2 ticks directly
        self.engine.run_continuous_monitoring_daemon(interval_seconds=1, max_ticks=2)
        self.assertFalse(self.engine.session_data.get("is_daemon_running"))

        with open(audit_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertGreaterEqual(len(lines), initial_lines + 2)

    def test_daily_brief_generation(self):
        """Must generate structured executive markdown daily trick brief."""
        brief = self.engine.generate_daily_trick_brief()
        self.assertIn("# ⚡ Zobar Live Daily Trend & Trick Digest", brief)
        self.assertIn("```typescript", brief)
        self.assertIn("Viral Puan", brief)


class TestMCPTrendToolIntegration(unittest.TestCase):
    def setUp(self):
        self.server = ZobarMCPServer()

    def test_mcp_manifest_contains_24_tools(self):
        tools = self.server.get_tools_manifest()
        self.assertGreaterEqual(len(tools), 24)
        names = [t["name"] for t in tools]
        self.assertIn("harvest_trending_tricks", names)

    def test_mcp_execute_harvest_trending_tricks(self):
        # 1. Action: search_tricks
        res = self.server.execute_tool("harvest_trending_tricks", {
            "action": "search_tricks",
            "keyword": "optimistic"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        matches = res["result"]["matches"]
        self.assertGreaterEqual(len(matches), 1)
        self.assertIn("Optimistic", matches[0]["title"])

        # 2. Action: get_daily_brief
        res_brief = self.server.execute_tool("harvest_trending_tricks", {
            "action": "get_daily_brief"
        })
        self.assertEqual(res_brief["tool_status"], "SUCCESS")
        self.assertIn("brief_markdown", res_brief["result"])


if __name__ == "__main__":
    unittest.main()
