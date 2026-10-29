#!/usr/bin/env python3
"""
Unit and Integration Tests for University Curriculum Evolution Engine & MCP Tooling.
Verifies historical curriculum analysis (1960s to 2026 across MIT, Stanford, UC Berkeley, CMU, ETH),
pedagogical paradigm shift tracking, 2026 modern syllabus retrieval, and MCP tool execution.
"""

import unittest
import os
import sys

# Ensure scripts dir in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from university_curriculum_evolution_engine import (
    UniversityCurriculumEvolutionEngine,
    CURRICULUM_EVOLUTION_DATABASE
)
from zobar_mcp_server import ZobarMCPServer


class TestUniversityCurriculumEvolutionEngine(unittest.TestCase):
    def setUp(self):
        self.engine = UniversityCurriculumEvolutionEngine()

    def test_curriculum_evolution_database_domains(self):
        """Must cover all 5 core engineering domains with 4 historical eras each."""
        required_domains = [
            "SYSTEMS_AND_CONCURRENCY",
            "ARTIFICIAL_INTELLIGENCE_AND_ML",
            "PROGRAMMING_LANGUAGES_AND_COMPILERS",
            "DATABASES_AND_DATA_SYSTEMS",
            "USER_INTERFACE_AND_HUMAN_COMPUTER_INTERACTION"
        ]
        for dom in required_domains:
            self.assertIn(dom, CURRICULUM_EVOLUTION_DATABASE)
            eras = CURRICULUM_EVOLUTION_DATABASE[dom]["historical_eras"]
            self.assertGreaterEqual(len(eras), 4)
            self.assertIn("era_4_2020_2026", eras)
            self.assertTrue(len(CURRICULUM_EVOLUTION_DATABASE[dom]["modern_actionable_principles"]) >= 3)

    def test_analyze_curriculum_evolution_ai(self):
        """Must correctly trace AI evolution from Lisp/Prolog to Transformers and Test-Time Compute."""
        res = self.engine.analyze_curriculum_evolution("Transformers and MCTS Reasoning")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["matched_domain"], "Artificial Intelligence & Cognitive Computing")
        self.assertIn("scaling", res["why_curriculum_changed"].lower())

        modern = res["modern_active_curriculum_2026"]
        self.assertIn("MIT 6.5940", modern["course_code"])
        self.assertIn("Song Han", modern["seminal_textbook"])
        self.assertIn("Test-Time Compute", modern["pedagogy"])

    def test_analyze_curriculum_evolution_databases(self):
        """Must trace database evolution from B-Trees to CMU Andy Pavlo's HNSW vector search and RLS."""
        res = self.engine.analyze_curriculum_evolution("PostgreSQL vector index and RLS")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["matched_domain"], "Databases, Storage Engines & Vector Search")
        
        modern = res["modern_active_curriculum_2026"]
        self.assertIn("CMU 15-445/645", modern["course_code"])
        self.assertIn("HNSW", modern["pedagogy"])

    def test_synthesize_curriculum_grounding_context(self):
        """Must synthesize authoritative markdown context block with historical paradigm shifts."""
        context = self.engine.synthesize_curriculum_grounding_context("systems performance and concurrency")
        self.assertIn("Elite University Curriculum Grounding", context)
        self.assertIn("MIT, Stanford, UC Berkeley, CMU & ETH Zürich", context)
        self.assertIn("Historical Paradigm Shift", context)
        self.assertIn("Actionable Architectural Mandates", context)

    def test_mcp_server_curriculum_tools(self):
        """Must execute both curriculum tools cleanly via MCP JSON-RPC router."""
        server = ZobarMCPServer()

        # Tool 1: analyze_curriculum_evolution
        res1 = server.execute_tool("analyze_curriculum_evolution", {
            "topic": "S-Tier UI spring physics and command palettes"
        })
        self.assertEqual(res1["tool_status"], "SUCCESS")
        self.assertEqual(res1["result"]["status"], "SUCCESS")
        self.assertIn("Human-Computer Interaction", res1["result"]["matched_domain"])

        # Tool 2: synthesize_curriculum_grounding
        res2 = server.execute_tool("synthesize_curriculum_grounding", {
            "topic": "compilers, AST and program synthesis"
        })
        self.assertEqual(res2["tool_status"], "SUCCESS")
        self.assertIn("grounding_markdown", res2["result"])
        self.assertIn("Curriculum Grounding", res2["result"]["grounding_markdown"])


if __name__ == "__main__":
    unittest.main()
