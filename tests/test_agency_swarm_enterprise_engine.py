#!/usr/bin/env python3
"""
Unit and Integration Tests for Agency Swarm Enterprise Engine & MCP Tooling.
Verifies 10-division / 100-specialist firm simulation, adversarial cross-departmental debate,
cross-functional masterplan synthesis, session prompt generation, and MCP server execution.
"""

import unittest
import os
import sys

# Ensure scripts dir in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from agency_swarm_enterprise_engine import (
    AgencySwarmEnterpriseEngine,
    ENTERPRISE_DIVISIONS
)
from zobar_mcp_server import ZobarMCPServer


class TestAgencySwarmEnterpriseEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AgencySwarmEnterpriseEngine()

    def test_enterprise_divisions_and_specialists_count(self):
        """Must comprise exactly 10 specialized divisions and 100 total virtual specialists."""
        self.assertEqual(len(ENTERPRISE_DIVISIONS), 10)
        total_specialists = sum(d["specialists_count"] for d in ENTERPRISE_DIVISIONS.values())
        self.assertEqual(total_specialists, 100)
        self.assertEqual(self.engine.total_specialists, 100)

    def test_conduct_departmental_deliberation(self):
        """Must run cross-functional deliberation across all 10 departments with debate resolution."""
        res = self.engine.conduct_departmental_deliberation(
            product_brief="Autonomous MedTech diagnostic portal with real-time vitals and HIPAA compliance",
            target_sector="medtech"
        )
        self.assertEqual(res["status"], "CONSENSUS_RATIFIED")
        self.assertEqual(res["total_departments"], 10)
        self.assertEqual(res["total_specialists_represented"], 100)
        self.assertGreaterEqual(res["mean_alignment_score"], 80.0)

        # Verify all 10 departments have spoken
        transcript = res["deliberation_transcript"]
        self.assertIn("EXECUTIVE_SUITE", transcript)
        self.assertIn("SOFTWARE_AND_SYSTEMS", transcript)
        self.assertIn("DESIGN_AND_CREATIVE", transcript)
        self.assertIn("LEGAL_AND_REGULATORY", transcript)
        self.assertIn("GROWTH_AND_SOCIAL", transcript)
        self.assertIn("CYBER_SECURITY_RED_TEAM", transcript)
        self.assertIn("AI_RESEARCH_LAB", transcript)
        self.assertIn("FINANCE_AND_FINOPS", transcript)
        self.assertIn("QUALITY_ASSURANCE", transcript)
        self.assertIn("PRODUCT_OPERATIONS", transcript)

        # Verify cross-departmental debates resolved
        debates = res["cross_departmental_debates"]
        self.assertGreaterEqual(len(debates), 3)
        for debate in debates:
            self.assertIn("debate", debate)
            self.assertIn("resolution", debate)

    def test_synthesize_firm_masterplan(self):
        """Must synthesize a comprehensive enterprise masterplan with core pillars."""
        res = self.engine.conduct_departmental_deliberation(
            product_brief="High-frequency algorithmic trading desk terminal",
            target_sector="fintech_hft"
        )
        masterplan = res["unified_enterprise_masterplan"]
        self.assertIn("Enterprise FINTECH_HFT Solution", masterplan["product_name"])
        self.assertIn("10 Enterprise Divisions", masterplan["executive_summary"])
        self.assertEqual(masterplan["launch_readiness"], "100% PRODUCTION_READY")
        
        pillars = masterplan["pillars"]
        self.assertIn("architecture", pillars)
        self.assertIn("design", pillars)
        self.assertIn("legal_and_security", pillars)
        self.assertIn("growth_and_viral", pillars)
        self.assertIn("finops", pillars)

    def test_synthesize_agency_session_prompt(self):
        """Must synthesize a clean, high-density agency prompt block for active agent sessions."""
        prompt = self.engine.synthesize_agency_session_prompt(
            product_brief="Next-generation spatial 3D studio with real-time canvas collaboration",
            target_sector="saas"
        )
        self.assertIn("Enterprise Agency Directorate Masterplan", prompt)
        self.assertIn("10 Divisions / 100 Virtual Specialists", prompt)
        self.assertIn("Executive Directorate & C-Suite", prompt)
        self.assertIn("Cross-Departmental Debate Resolutions", prompt)
        self.assertIn("Resolution:", prompt)

    def test_mcp_server_agency_tools(self):
        """Must execute agency deliberation and prompt synthesis via MCP JSON-RPC router."""
        server = ZobarMCPServer()

        # Tool 1: execute_agency_deliberation
        res1 = server.execute_tool("execute_agency_deliberation", {
            "product_brief": "Cyber defense telemetry platform with real-time packet entropy inspection",
            "target_sector": "cyber_defense"
        })
        self.assertEqual(res1["tool_status"], "SUCCESS")
        self.assertEqual(res1["result"]["status"], "CONSENSUS_RATIFIED")
        self.assertEqual(res1["result"]["total_departments"], 10)

        # Tool 2: synthesize_agency_executive_prompt
        res2 = server.execute_tool("synthesize_agency_executive_prompt", {
            "product_brief": "Robotics fleet management dashboard with edge telemetry",
            "target_sector": "robotics_iot"
        })
        self.assertEqual(res2["tool_status"], "SUCCESS")
        self.assertIn("agency_prompt", res2["result"])
        self.assertIn("100 Virtual Specialists", res2["result"]["agency_prompt"])


if __name__ == "__main__":
    unittest.main()
