"""
Stage 6 MCP & Business School Case Engine Tests
Unit tests for MCPSkillIntegrator and BusinessSchoolCaseEngine.
"""

import unittest
from scripts.mcp_skill_integrator import MCPSkillIntegrator
from scripts.business_school_case_engine import BusinessSchoolCaseEngine


class TestStage6MCPAndBusiness(unittest.TestCase):
    def test_mcp_server_template_generation(self):
        sample_tools = [
            {
                "name": "calculate_tax",
                "description": "Calculates sales tax",
                "inputSchema": {"type": "object", "properties": {"amount": {"type": "number"}}}
            }
        ]
        server_code = MCPSkillIntegrator.generate_mcp_server_template("tax-server", sample_tools)

        self.assertIn("tools/list", server_code)
        self.assertIn("tools/call", server_code)
        self.assertIn("calculate_tax", server_code)
        self.assertIn("jsonrpc", server_code)

    def test_skill_markdown_generation(self):
        skill_md = MCPSkillIntegrator.generate_skill_markdown(
            name="patent-researcher",
            description="Autonomous patent prior art searcher",
            steps=["Query Google Patents", "Analyze Claims", "Verify TRL"]
        )

        self.assertIn("name: patent-researcher", skill_md)
        self.assertIn("1. **Query Google Patents**", skill_md)
        self.assertIn("2. **Analyze Claims**", skill_md)

    def test_claude_desktop_config_generation(self):
        config = MCPSkillIntegrator.generate_claude_desktop_mcp_config("my-db", "scripts/test.py")
        self.assertIn("mcpServers", config)
        self.assertIn("my-db", config["mcpServers"])
        self.assertEqual(config["mcpServers"]["my-db"]["command"], "python")

    def test_business_school_porter_forces_dynamic_archetypes(self):
        # 1. Biotech
        bio = BusinessSchoolCaseEngine.analyze_porter_five_forces("Biotech Oncology Clinical Drugs")
        self.assertEqual(bio["detected_archetype"], "Regulated Life Sciences & Biotech")
        self.assertEqual(bio["forces"]["threat_of_new_entrants"]["score"], 1)
        self.assertGreater(bio["industry_attractiveness_index"], 60)

        # 2. Consumer E-Commerce
        comm = BusinessSchoolCaseEngine.analyze_porter_five_forces("Consumer Fashion E-Commerce Retail")
        self.assertEqual(comm["detected_archetype"], "High-Churn Consumer & E-Commerce")
        self.assertEqual(comm["forces"]["bargaining_power_of_buyers"]["score"], 10)
        self.assertLess(comm["industry_attractiveness_index"], 45)

        # 3. B2B SaaS
        saas = BusinessSchoolCaseEngine.analyze_porter_five_forces("B2B Cloud Developer Tools")
        self.assertEqual(saas["detected_archetype"], "B2B Software, Cloud & AI Engineering")
        self.assertIn("threat_of_new_entrants", saas["forces"])

    def test_lean_ai_workforce_calculation(self):
        calc = BusinessSchoolCaseEngine.calculate_lean_ai_workforce_multiplier(
            current_human_headcount=10,
            avg_annual_salary_usd=70000.0,
            ai_agent_tier1_budget_monthly_usd=250.0,
            human_specialists_retained=2,
        )

        self.assertEqual(calc["traditional_workforce"]["annual_cost_usd"], 700000.0)
        self.assertEqual(calc["lean_ai_enterprise"]["human_specialists"], 2)
        self.assertGreater(calc["annual_savings_usd"], 500000.0)
        self.assertGreater(calc["cost_reduction_percent"], 70.0)

    def test_historical_wealth_models(self):
        models = BusinessSchoolCaseEngine.HISTORICAL_MODELS
        self.assertIn("venetian_arbitrage", models)
        self.assertIn("rockefeller_monopoly", models)
        self.assertIn("buffett_float", models)
        self.assertIn("constellation_rollup", models)
        self.assertIn("naval_permissionless_leverage", models)


if __name__ == "__main__":
    unittest.main()
