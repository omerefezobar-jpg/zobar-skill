"""
Stage 1 FinOps & Zero-Cost AI Acceleration Tests
Unit tests for SemanticCache, SmartModelRouter, and SupabaseDBOptimizer.
"""

import os
import unittest
import tempfile
import json
from scripts.semantic_cache import SemanticCache
from scripts.smart_model_router import SmartModelRouter
from scripts.supabase_db_optimizer import SupabaseDBOptimizer


class TestStage1FinOps(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.cache_file = os.path.join(self.temp_dir.name, "test_cache.json")
        self.cache = SemanticCache(cache_file=self.cache_file, similarity_threshold=0.72)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_semantic_cache_exact_and_fuzzy_hit(self):
        # 1. Put query into cache
        query = "Python ile asenkron fonksiyon nasıl tanımlanır?"
        response = "async def my_func(): await asyncio.sleep(1)"
        self.cache.put(query, response, remote_latency_ms=1500.0, cost_usd=0.02)

        # 2. Exact match hit
        res_exact = self.cache.get("Python ile asenkron fonksiyon nasıl tanımlanır?")
        self.assertIsNotNone(res_exact)
        self.assertEqual(res_exact["response"], response)
        self.assertGreaterEqual(res_exact["similarity"], 0.99)
        self.assertLess(res_exact["cache_latency_ms"], 20.0)

        # 3. Fuzzy / paraphrased query hit
        fuzzy_query = "Python asenkron fonksiyon nasıl yazılır?"
        res_fuzzy = self.cache.get(fuzzy_query)
        self.assertIsNotNone(res_fuzzy)
        self.assertEqual(res_fuzzy["response"], response)
        self.assertGreaterEqual(res_fuzzy["similarity"], 0.72)

        # 4. Completely unrelated query miss
        res_miss = self.cache.get("İstanbul'da hava durumu bugün nasıl?")
        self.assertIsNone(res_miss)

        # 5. Check metrics
        metrics = self.cache.get_metrics()
        self.assertEqual(metrics["total_queries"], 3)
        self.assertEqual(metrics["cache_hits"], 2)
        self.assertEqual(metrics["cache_misses"], 1)
        self.assertGreater(metrics["total_saved_usd"], 0.03)

    def test_smart_model_router_tier_allocation(self):
        router = SmartModelRouter(semantic_cache=self.cache, enable_cache=True)

        # Routine task should route to Tier 1
        routine_prompt = "Lütfen şu müşteri şikayetini 2 cümlede özetle ve JSON formatına dönüştür."
        routine_res = router.route(routine_prompt)
        self.assertEqual(routine_res["tier"], 1)
        self.assertIn(routine_res["model"], ["gpt-4o-mini", "gemini-1.5-flash", "claude-3-5-haiku"])
        self.assertGreater(routine_res["cost_reduction_percent"], 50.0)

        # Deep architecture & concurrency task should route to Tier 2
        frontier_prompt = "Dağıtık sistemlerde lock-free concurrency, Paxos mutabakatı ve B+ Tree disk mimarisi nasıl kurgulanır?"
        frontier_res = router.route(frontier_prompt)
        self.assertEqual(frontier_res["tier"], 2)
        self.assertEqual(frontier_res["model"], "claude-3-5-sonnet")

        # Caching Tier 0 test
        self.cache.put(routine_prompt, "Özet: Müşteri teslimat gecikmesinden şikayetçi.")
        cached_res = router.route(routine_prompt)
        self.assertEqual(cached_res["tier"], 0)
        self.assertEqual(cached_res["estimated_cost_usd"], 0.0)
        self.assertEqual(cached_res["model"], "semantic-cache-hit")

    def test_supabase_db_optimizer_audit(self):
        schema_path = os.path.join(os.path.dirname(__file__), "..", "references", "supabase_production_schema.sql")
        self.assertTrue(os.path.exists(schema_path))

        optimizer = SupabaseDBOptimizer(schema_path)
        report = optimizer.audit()

        self.assertEqual(report["health_score"], 100)
        self.assertEqual(report["status"], "PRODUCTION_READY")
        self.assertEqual(len(report["missing_rls_tables"]), 0)
        self.assertTrue(report["vector_search"]["extension_enabled"])
        self.assertTrue(report["vector_search"]["hnsw_optimized"])
        self.assertTrue(report["realtime_architecture"]["selective_publication"])

    def test_supabase_optimizer_detects_insecure_schema(self):
        # Create a temporary insecure schema
        insecure_sql = """
        CREATE TABLE public.insecure_table (id UUID PRIMARY KEY, secret TEXT);
        CREATE TABLE public.another_table (id UUID PRIMARY KEY);
        ALTER TABLE public.another_table ENABLE ROW LEVEL SECURITY;
        """
        temp_sql_file = os.path.join(self.temp_dir.name, "insecure.sql")
        with open(temp_sql_file, "w", encoding="utf-8") as f:
            f.write(insecure_sql)

        optimizer = SupabaseDBOptimizer(temp_sql_file)
        report = optimizer.audit()
        self.assertLess(report["health_score"], 90)
        self.assertIn("insecure_table", report["missing_rls_tables"])


if __name__ == "__main__":
    unittest.main()
