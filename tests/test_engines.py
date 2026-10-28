#!/usr/bin/env python3
"""
Comprehensive Ground-Truth Unit & Benchmark Test Suite for Zobar Skill.
Tests statutory compliance precision with intended-purpose discrimination,
university curriculum ground truth, hybrid competitor benchmarking,
clause-level negation sentiment mining, dynamic TRIZ validation, and CSP security.
"""

import unittest
from unittest.mock import patch, MagicMock
import json

from scripts.export_html_report import (
    parse_markdown_to_html, is_safe_url, export_to_html,
    sanitize_mermaid_diagram, HTML_TEMPLATE
)
from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.fetch_university_research import (
    find_university_curriculum, fetch_openalex_papers
)
from scripts.mine_user_sentiment import (
    clean_html, search_sentiment, calculate_friction_score, split_into_clauses
)
from scripts.benchmark_competitors import (
    benchmark_competitors, search_commercial_incumbents, fetch_package_registry_telemetry
)
from scripts.search_prior_art import search_patents
from scripts.scan_regulations import evaluate_compliance
from scripts.synthesize_architecture import synthesize_tech_stack
from scripts.validate_inventions import (
    generate_validated_inventions, calculate_dynamic_validation_metrics
)

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

    def test_mermaid_sanitization_preserves_arrows_and_kills_scripts(self):
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
        self.assertIn('A --> B', output)
        self.assertNotIn('<script>alert(1)</script>', output)

class TestUniversityCurriculumAndAcademics(unittest.TestCase):
    def test_university_curriculum_mapping(self):
        res = find_university_curriculum("compiler AST static analysis")
        self.assertGreaterEqual(len(res["curriculum"]), 1)
        stanford = next((c for c in res["curriculum"] if c["institution"] == "Stanford University"), None)
        self.assertIsNotNone(stanford)
        self.assertEqual(stanford["course_code"], "CS143")
        self.assertIn("Dragon Book", stanford["seminal_textbook"])

    def test_distributed_systems_mit_mapping(self):
        res = find_university_curriculum("distributed consensus raft")
        mit = next((c for c in res["curriculum"] if "MIT" in c["institution"]), None)
        self.assertIsNotNone(mit)
        self.assertIn("6.824", mit["course_code"])
        self.assertIn("Kleppmann", mit["seminal_textbook"])

    @patch("urllib.request.urlopen")
    def test_openalex_papers_mock(self, mock_urlopen):
        sample_openalex_json = json.dumps({
            "meta": {"count": 1},
            "results": [
                {
                    "title": "In Search of an Understandable Consensus Algorithm",
                    "publication_year": 2014,
                    "cited_by_count": 3400,
                    "authorships": [{"author": {"display_name": "Diego Ongaro"}}, {"author": {"display_name": "John Ousterhout"}}],
                    "primary_location": {"source": {"display_name": "USENIX ATC"}},
                    "doi": "https://doi.org/10.5555/2643634.2643666"
                }
            ]
        }).encode("utf-8")

        mock_resp = MagicMock()
        mock_resp.read.return_value = sample_openalex_json
        mock_resp.__enter__.return_value = mock_resp
        mock_urlopen.return_value = mock_resp

        res = fetch_openalex_papers("consensus raft", max_results=1)
        self.assertEqual(res["status"], "success")
        self.assertEqual(len(res["papers"]), 1)
        self.assertEqual(res["papers"][0]["citation_count"], 3400)
        self.assertIn("Ongaro", res["papers"][0]["authors"])

class TestSentimentAndNegation(unittest.TestCase):
    def test_negation_aware_friction_scoring(self):
        self.assertEqual(calculate_friction_score("The app is not slow at all"), 0)
        self.assertEqual(calculate_friction_score("We had no issues and it never crashed"), 0)
        self.assertEqual(calculate_friction_score("It isn't broken"), 0)
        self.assertEqual(calculate_friction_score("The app is slow"), 1)

    def test_clause_level_conjunction_separation(self):
        compound = "The UI is fast, but the compiler crashes constantly and the documentation is terrible."
        clauses = split_into_clauses(compound)
        self.assertGreaterEqual(len(clauses), 2)
        score = calculate_friction_score(compound)
        self.assertGreaterEqual(score, 4)

class TestStatutoryRegulatoryCompliance(unittest.TestCase):
    def test_statutory_prohibited_ai_trigger(self):
        res = evaluate_compliance("subliminal manipulation for harm psychological exploitation")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)")
        self.assertIn("Madde 5(1)(a)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_clinical_decision_support_high_risk_mdr_rule_11(self):
        res = evaluate_compliance("medical diagnostic patient telemetry clinical treatment decision AI")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("MDR (AB) 2017/745 Kural 11", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_hospital_administrative_scheduling_minimal_risk(self):
        res = evaluate_compliance("hospital administrative scheduling patient appointment billing shift management")
        self.assertEqual(res["eu_ai_act"]["tier"], "Minimal / Düşük Risk (İdari Sağlık Yazılımı)")
        self.assertIn("MDR (AB) 2017/745 Kapsam Dışı", res["eu_ai_act"]["statutory_basis"])
        self.assertFalse(res["eu_ai_act"]["requires_expert_counsel"])

    def test_recruitment_high_risk_annex_iii_4a(self):
        res = evaluate_compliance("recruitment hiring automated resume screening candidate evaluation")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("Ek III Nokta 4(a)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_critical_infrastructure_high_risk_annex_iii_2(self):
        res = evaluate_compliance("critical infrastructure safety component power grid water management scada")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("Ek III Nokta 2", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_compiler_developer_tool_article_2_8_exemption(self):
        res = evaluate_compliance("AST parser compiler code analysis static linter refactoring tool")
        self.assertEqual(res["eu_ai_act"]["tier"], "Minimal / Düşük Risk (Geliştirici Aracı / AI Act Muafiyeti)")
        self.assertIn("Madde 2(8)", res["eu_ai_act"]["statutory_basis"])
        self.assertFalse(res["eu_ai_act"]["requires_expert_counsel"])

    def test_statutory_transparency_conversational_bot(self):
        res = evaluate_compliance("conversational bot customer service chatbot interaction natural person")
        self.assertEqual(res["eu_ai_act"]["tier"], "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)")
        self.assertIn("Madde 50(1)", res["eu_ai_act"]["statutory_basis"])

    def test_sensitive_biometrics_prohibited_article_5_1_g(self):
        res = evaluate_compliance("biometric categorization sensitive political sexual orientation religious belief discrimination")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)")
        self.assertIn("Madde 5(1)(g)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_systemic_gpai_article_51_52(self):
        res = evaluate_compliance("frontier general purpose gpai model systemic risk high compute training 10^25 flops evaluation")
        self.assertEqual(res["eu_ai_act"]["tier"], "Sistemik Riskli GPAI Modeli (Systemic Risk GPAI Model)")
        self.assertIn("Madde 51", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_workplace_dismissal_high_risk_annex_iii_4b(self):
        res = evaluate_compliance("workplace algorithmic termination worker task allocation employee performance dismissal decision")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("Ek III Nokta 4(b)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_insurance_underwriting_high_risk_annex_iii_5a(self):
        res = evaluate_compliance("life health insurance underwriting risk assessment pricing policy eligibility determination")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("Ek III Nokta 5(a)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_emergency_112_dispatch_high_risk_annex_iii_5d(self):
        res = evaluate_compliance("emergency 112 service dispatch call triage ambulance emergency response prioritization")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("Ek III Nokta 5(d)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_judicial_sentencing_high_risk_annex_iii_8a(self):
        res = evaluate_compliance("judicial authority sentencing evidence interpretation court legal fact finding dispute resolution")
        self.assertEqual(res["eu_ai_act"]["tier"], "Yüksek Riskli Sistem (High-Risk AI System)")
        self.assertIn("Ek III Nokta 8(a)", res["eu_ai_act"]["statutory_basis"])
        self.assertTrue(res["eu_ai_act"]["requires_expert_counsel"])

    def test_satirical_deepfake_transparency_article_50_4(self):
        res = evaluate_compliance("investigative journalism parody artistic satire synthetic media deepfake artistic freedom")
        self.assertEqual(res["eu_ai_act"]["tier"], "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)")
        self.assertIn("Madde 50(4)", res["eu_ai_act"]["statutory_basis"])
        self.assertFalse(res["eu_ai_act"]["requires_expert_counsel"])

class TestHybridCompetitorAndMarketBenchmark(unittest.TestCase):
    def test_curated_commercial_incumbents_lookup(self):
        incumbents = search_commercial_incumbents("static analysis code quality")
        self.assertGreaterEqual(len(incumbents), 1)
        sonar = next((i for i in incumbents if "SonarQube" in i["name"]), None)
        self.assertIsNotNone(sonar)
        self.assertIn("Enterprise", sonar["pricing_tier"])
        self.assertIn("false-positive", sonar["core_weakness"])

    @patch("urllib.request.urlopen")
    def test_github_telemetry_mock(self, mock_urlopen):
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
        self.assertEqual(len(res["open_source_telemetry"]), 1)
        self.assertEqual(res["open_source_telemetry"][0]["name"], "acme/compiler")

class TestAutomatedArchitectureAndTRIZInventions(unittest.TestCase):
    def test_phase_5_tech_stack_synthesis(self):
        arch = synthesize_tech_stack("AST parser compiler engine")
        self.assertEqual(arch["core_language"], "Rust")
        self.assertIn("tree-sitter", arch["recommended_libraries"])
        self.assertIn("Tauri", arch["ui_architecture"]["runtime"])

    def test_phase_6_dynamic_triz_metrics(self):
        metrics_clinical = calculate_dynamic_validation_metrics("clinical medical diagnostic")
        self.assertEqual(metrics_clinical["trl_number"], 3)
        self.assertEqual(metrics_clinical["ice"]["ease"], 4) # Heavy regulatory hurdle

        metrics_dev = calculate_dynamic_validation_metrics("compiler AST parser")
        self.assertEqual(metrics_dev["trl_number"], 4)
        self.assertEqual(metrics_dev["ice"]["ease"], 7)

    def test_s_tier_design_vault_matching(self):
        from scripts.recommend_ui_patterns import match_s_tier_patterns
        res_stream = match_s_tier_patterns("video streaming cinema", max_results=2)
        self.assertGreaterEqual(res_stream["total_vault_size"], 200)
        self.assertTrue(any("Netflix" in s["name"] or "Spotify" in s["name"] for s in res_stream["matched_sites"]))

        res_fintech = match_s_tier_patterns("fintech payments banking", max_results=2)
        self.assertTrue(any("Stripe" in s["name"] or "Ramp" in s["name"] for s in res_fintech["matched_sites"]))

    def test_heavy_app_architecture_blueprints(self):
        from scripts.analyze_heavy_app_architecture import match_heavy_app_blueprint
        res_steam = match_heavy_app_blueprint("steam game launcher")
        self.assertGreaterEqual(len(res_steam["matched_blueprints"]), 1)
        steam = res_steam["matched_blueprints"][0]
        self.assertEqual(steam["app_name"], "Steam")
        self.assertIn("CEF", steam["how_it_was_built"]["architecture"])
        self.assertIn("Tauri", steam["how_we_build_it_10x_better"]["core_technology"])

        res_excel = match_heavy_app_blueprint("excel spreadsheet formula grid")
        self.assertGreaterEqual(len(res_excel["matched_blueprints"]), 1)
        excel = res_excel["matched_blueprints"][0]
        self.assertEqual(excel["app_name"], "Microsoft Excel")
        self.assertIn("WebGPU", excel["how_we_build_it_10x_better"]["core_technology"])

    def test_phase_6_triz_invention_generation(self):
        inventions_data = generate_validated_inventions("Code Analysis")
        self.assertEqual(len(inventions_data["inventions"]), 2)
        inv1 = inventions_data["inventions"][0]
        self.assertIn("TRL", inv1["trl_level"])
        self.assertGreater(inv1["ice_score"]["total"], 0)
        self.assertEqual(len(inv1["failure_modes"]), 3)
        self.assertIn("flowchart TD", inventions_data["system_architecture_mermaid"])

if __name__ == "__main__":
    unittest.main()
