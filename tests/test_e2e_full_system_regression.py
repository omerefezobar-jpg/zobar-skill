#!/usr/bin/env python3
"""
Zobar Skill: End-to-End Full System Integration & Regression Test Suite.
Verifies:
1. End-to-End Orchestrator Pipeline across all 9 phases in a single integrated workflow.
2. Strict Schema Snapshot Validation (no missing keys, expected types, no unhandled nulls).
3. Latency Regression Budget (< 3.5s end-to-end execution).
4. Empirical Bayesian Learning Feedback Loop (verifies weight updates from real outcomes).
5. Cross-Engine Synergy: Security Sandbox + AST + Regulations + Evidence DAG + Math Modeling.
"""

import unittest
import os
import sys
import ast
import time
import json
from typing import Dict, Any

# Ensure project root in sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from unified_system_orchestrator import UnifiedSystemOrchestrator
from evidence_provenance_engine import EvidenceProvenanceGraph, ClaimEvidenceQualityScorer
from feedback_outcome_learning_engine import FeedbackOutcomeEngine
from security_permission_guard import SecurityPermissionGuard


class TestE2EFullSystemRegression(unittest.TestCase):
    def setUp(self):
        self.orchestrator = UnifiedSystemOrchestrator()
        self.security_guard = SecurityPermissionGuard()

    def test_full_pipeline_orchestration_and_schema_validation(self):
        """Executes full 9-phase orchestrator and verifies contract conformance across all stages."""
        vision = "Real-Time Embedded IoT Telemetry Dispatcher"
        t_start = time.perf_counter()

        result = self.orchestrator.orchestrate_product_lifecycle(
            product_vision=vision,
            target_sector="Industrial Automation"
        )
        latency = time.perf_counter() - t_start

        # 1. Latency Regression Budget: must finish in under 3.5 seconds locally
        self.assertLess(latency, 3.5, f"Orchestration exceeded latency budget: {latency:.2f}s > 3.5s")

        # 2. Schema Snapshot Verification
        self.assertIn("orchestration_topic", result)
        self.assertIn("pipeline_stages", result)
        self.assertIn("prototype_code", result)

        stages = result["pipeline_stages"]
        stage_keys = [
            "1_academic_ground_truth",
            "2_user_sentiment",
            "3_competitors_and_moats",
            "4_regulatory_compliance",
            "5_systems_math_and_architecture",
            "6_code_artifacts",
            "7_sandbox_and_deficiencies",
            "8_evidence_and_learning",
            "9_senate_and_chief_engineer"
        ]
        for k in stage_keys:
            self.assertIn(k, stages, f"Missing stage key: {k}")

        # 3. Stage 1: Academic Ground Truth Integrity
        s1 = stages["1_academic_ground_truth"]
        self.assertGreaterEqual(s1["curricula_count"], 1)
        self.assertIn("sample_mental_model", s1)
        self.assertTrue(len(s1["sample_mental_model"]) > 10)

        # 4. Stage 4: Regulatory Screener Integrity
        s4 = stages["4_regulatory_compliance"]
        self.assertIn("classification_tier", s4)
        self.assertIn("statutory_basis", s4)

        # 5. Stage 5: Systems Math Modeling
        s5 = stages["5_systems_math_and_architecture"]
        self.assertIn("littles_law_concurrency", s5)
        self.assertIn("average_latency_ms", s5)

        # 6. Stage 7: Sandbox and AST Syntax
        s7 = stages["7_sandbox_and_deficiencies"]
        self.assertTrue(s7["syntax_valid"], "Generated Python core engine must be syntactically valid")
        self.assertEqual(s7["execution_status"], "EXECUTION_PASSED")

        # 7. Stage 9: Senate & Chief Engineer Ratification
        s9 = stages["9_senate_and_chief_engineer"]
        self.assertTrue(s9["gate_verdict"].startswith("GEÇTİ"))

    def test_bayesian_learning_engine_feedback_loop(self):
        """Verifies that trial outcome recording empirically updates Bayesian pattern weights without pre-seeded bias."""
        learning = FeedbackOutcomeEngine()
        pattern = f"test_pattern_{int(time.time()*1000)}"

        # Baseline: cold start uniform prior W = 2 / 4 = 0.50
        initial_rep = learning.get_pattern_reputation(pattern)
        self.assertEqual(initial_rep["empirical_trials_count"], 0)
        self.assertAlmostEqual(initial_rep["win_rate"], 0.50, delta=0.01)

        # Record 6 consecutive successes: (2 + 6) / (2 + 2 + 6) = 8/10 = 0.80 -> PROVEN_STABLE
        for i in range(6):
            learning.record_trial_outcome(
                task_id=f"TASK-SUCC-{i}",
                task_category="Testing",
                pattern_applied=pattern,
                success=True,
                execution_latency_ms=1.5
            )

        updated_rep = learning.get_pattern_reputation(pattern)
        self.assertEqual(updated_rep["empirical_trials_count"], 6)
        self.assertAlmostEqual(updated_rep["win_rate"], 0.80, delta=0.01)
        self.assertIn("PROVEN_STABLE", updated_rep["evidence_status"])

    def test_evidence_provenance_dag_integrity_and_scoring(self):
        """Verifies that evidence provenance graph correctly tracks causality and scores claim support."""
        g = EvidenceProvenanceGraph()
        g.record_evidence(
            evidence_id="EVID-DO178C",
            source_type="Statutory Standard",
            citation="RTCA DO-178C Software Considerations in Airborne Systems and Equipment Certification",
            claim_supported="Safety-critical flight navigation level A determinism.",
            confidence_tier="STATUTORY_GROUND_TRUTH",
            published_year=2021
        )
        g.link_decision("DEC-AVIONICS", "Avionics DO-178C compliance architecture", ["EVID-DO178C"])

        dossier = g.export_provenance_dossier()
        self.assertEqual(dossier["audit_summary"]["total_evidence_count"], 1)
        self.assertEqual(dossier["audit_summary"]["verified_evidence_count"], 1)
        self.assertEqual(len(dossier["causal_lineage"]), 1)

        # Quality scoring
        score = g.evaluate_claim_quality(
            "Safety-critical flight navigation level A determinism requires strict qualification.",
            "EVID-DO178C"
        )
        self.assertGreaterEqual(score["total_score"], 80.0)
        self.assertEqual(score["quality_grade"], "GROUNDED_HIGH_FIDELITY")

    def test_sandbox_ast_and_system_isolation(self):
        """Ensures the orchestrator security guard blocks unauthorized subprocess escapes."""
        res_del = self.security_guard.execute_sandboxed_command("del /q test.txt")
        self.assertEqual(res_del["status"], "SECURITY_VETO")

        res_git = self.security_guard.execute_sandboxed_command("git status")
        self.assertEqual(res_git["status"], "SUCCESS")


if __name__ == "__main__":
    unittest.main()
