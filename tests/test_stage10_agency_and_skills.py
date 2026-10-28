#!/usr/bin/env python3
"""
Unit Test Suite for Zobar Skill Stage 10 Frontier Expansion:
1. Human Delight, Dopamine Loops & Viral K-Factor Psychology.
2. Freelance, Agency & Client Acquisition Pitch Engine (MRR Retainers & Cold Audits).
3. Skill Discovery, Auto-Loader & MCP Terminal Command Runner.
4. Free Modern UI Component Snippets Vault (React & Tailwind v4).
5. Live MCP Server 19-Tool Manifest & Dispatch Integrity.
"""

import unittest
import os
import json

from scripts.human_delight_psychology_engine import (
    analyze_user_psychology_and_delight, calculate_viral_k_factor, DELIGHT_PATTERNS
)
from scripts.freelance_agency_growth_engine import (
    generate_cold_audit_proposal, calculate_agency_retainer_growth, NICHE_OPPORTUNITIES
)
from scripts.skill_registry_and_installer_engine import (
    search_ecosystem_skills, synthesize_new_skill_scaffold, execute_terminal_mcp_command
)
from scripts.modern_component_snippets import ModernComponentsEngine
from scripts.zobar_mcp_server import ZobarMCPServer

class TestHumanDelightAndViralPsychology(unittest.TestCase):
    def test_delight_patterns_and_friction_score(self):
        res = analyze_user_psychology_and_delight("One-Click Glassy Booking Funnel")
        self.assertGreaterEqual(res["delight_score"], 60)
        self.assertLessEqual(res["cognitive_friction_index"], 40)
        self.assertTrue(len(res["top_delight_patterns"]) >= 3)
        self.assertTrue(any("Optimistic UI" in p["principle"] for p in res["top_delight_patterns"]))

    def test_viral_k_factor_calculation(self):
        super_viral = calculate_viral_k_factor(invites_per_user=3.5, invitee_conversion_rate=0.40)
        self.assertEqual(super_viral["k_factor"], 1.4)
        self.assertIn("Super-Viral", super_viral["status"])

        sub_critical = calculate_viral_k_factor(invites_per_user=1.2, invitee_conversion_rate=0.20)
        self.assertEqual(sub_critical["k_factor"], 0.24)
        self.assertIn("Düşük Viralite", sub_critical["status"])

class TestFreelanceAgencyGrowthEngine(unittest.TestCase):
    def test_cold_audit_proposal_generation(self):
        proposal = generate_cold_audit_proposal("Apex Aesthetics Clinic", niche_key="clinic", client_website="apexaesthetics.com")
        self.assertIn("Apex Aesthetics Clinic", proposal["outreach_strategy"]["email_subject"])
        self.assertIn("apexaesthetics.com", proposal["outreach_strategy"]["cold_email_body"])
        self.assertIn("$1800", proposal["retainer_monetization_plan"]["initial_project_fee"])
        self.assertIn("$300/ay", proposal["retainer_monetization_plan"]["monthly_maintenance_retainer"])

    def test_agency_mrr_calculation(self):
        growth = calculate_agency_retainer_growth(client_count=10, avg_monthly_fee=300.0)
        self.assertEqual(growth["monthly_recurring_revenue_mrr"], "$3,000.00")
        self.assertEqual(growth["annual_run_rate_arr"], "$36,000.00")
        self.assertIn("feast-and-famine", growth["financial_stability_assessment"])

class TestSkillRegistryAndInstallerEngine(unittest.TestCase):
    def test_search_ecosystem_skills(self):
        matches = search_ecosystem_skills("postgres")
        self.assertGreaterEqual(len(matches), 1)
        self.assertIn("postgres", matches[0]["name"])

    def test_synthesize_skill_scaffold(self):
        scaffold = synthesize_new_skill_scaffold("Test Analytics Skill", "Measures web traffic without cookies")
        self.assertTrue(scaffold["yaml_frontmatter_valid"])
        self.assertIn("name: test-analytics-skill", scaffold["scaffold_content"])

    def test_mcp_terminal_command_execution(self):
        res = execute_terminal_mcp_command("python -c \"print('MCP_TERMINAL_ONLINE')\"")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["exit_code"], 0)
        self.assertIn("MCP_TERMINAL_ONLINE", res["stdout"])
        self.assertGreater(res["latency_ms"], 0.0)

class TestModernComponentsEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ModernComponentsEngine()

    def test_search_and_get_by_id(self):
        results = self.engine.search_components("skeleton")
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "COMP-01")
        self.assertIn("ShimmerSkeletonCard", results[0]["react_jsx"])

        by_id = self.engine.get_component_by_id("COMP-03")
        self.assertIsNotNone(by_id)
        self.assertIn("WhatsApp", by_id["name"])

class TestMCPStage10ToolsIntegration(unittest.TestCase):
    def setUp(self):
        self.server = ZobarMCPServer()

    def test_mcp_manifest_contains_19_tools(self):
        tools = self.server.get_tools_manifest()
        self.assertGreaterEqual(len(tools), 19)
        names = [t["name"] for t in tools]
        self.assertIn("analyze_human_delight", names)
        self.assertIn("generate_client_agency_pitch", names)
        self.assertIn("manage_skills_and_mcp", names)
        self.assertIn("get_free_component_snippet", names)
        self.assertIn("run_unified_orchestration", names)
        self.assertIn("audit_security_sandbox", names)
        self.assertIn("query_evidence_provenance", names)
        self.assertIn("query_learning_registry", names)

    def test_mcp_execute_human_delight(self):
        res = self.server.execute_tool("analyze_human_delight", {
            "feature_or_page": "Instant WhatsApp Booking",
            "invites_per_user": 2.0,
            "invitee_conversion_rate": 0.50
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertEqual(res["result"]["viral_k_factor"]["k_factor"], 1.0)

    def test_mcp_execute_agency_pitch(self):
        res = self.server.execute_tool("generate_client_agency_pitch", {
            "target_business": "SunPower Solar",
            "niche": "contractor"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertIn("client_proposal", res["result"])
        self.assertIn("agency_10_client_growth_model", res["result"])

    def test_mcp_execute_skill_manager(self):
        res = self.server.execute_tool("manage_skills_and_mcp", {
            "action": "search",
            "query": "browser"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertTrue(len(res["result"]["matched_skills"]) >= 1)

    def test_mcp_execute_free_component(self):
        res = self.server.execute_tool("get_free_component_snippet", {
            "component_id": "COMP-04"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertIn("ClientROICalculator", res["result"]["component"]["react_jsx"])

if __name__ == "__main__":
    unittest.main()
