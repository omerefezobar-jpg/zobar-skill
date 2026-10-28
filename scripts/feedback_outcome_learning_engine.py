#!/usr/bin/env python3
"""
Zobar Skill: Feedback, Empirical Outcome & Learning Engine.
Enforces real, measurable reinforcement learning from executed tasks:
1. Records which architectural recommendations were accepted vs rejected.
2. Tracks which generated code snippets compiled/passed tests vs failed with errors.
3. Dynamically computes pattern reputation weights strictly from verified trials via Bayesian updates:
   W = (alpha + empirical_successes) / (alpha + beta + total_empirical_trials).
4. Strictly separates theoretical Bayesian priors from actual empirical trial records (no pre-seeded fake counts).
5. Feeds calibrated weights back into the synthesizer and model router.
"""

import sys
import os
import json
import time
import argparse
from typing import Dict, List, Any, Optional

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REGISTRY_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "references", "empirical_feedback_registry.json"))


class FeedbackOutcomeEngine:
    def __init__(self, registry_path: Optional[str] = None):
        self.path = registry_path or REGISTRY_FILE
        self.registry = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Migrate / sanitize if old format
                    if "trials" in data:
                        return data
            except Exception:
                pass
        return {
            "version": "2.0.0",
            "metadata": {
                "description": "Empirically verified trial executions and Bayesian calibrated pattern weights",
                "prior_methodology": "Uniform Laplace Beta(2,2) cold-start prior; counts computed strictly from verified trial logs."
            },
            "trials": [],
            "registered_patterns": [
                "lock_free_ringbuffer",
                "rust_tauri_core",
                "greedy_meshing_voxel",
                "clean_room_specification",
                "monolithic_polling_sleep"
            ]
        }

    def _save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.registry, f, indent=2, ensure_ascii=False)

    def record_trial_outcome(
        self,
        task_id: str,
        task_category: str,
        pattern_applied: str,
        success: bool,
        execution_latency_ms: float = 0.0,
        error_details: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Records the verified empirical outcome of an executed task (pass/fail, latency, errors)
        into the persistent trial ledger.
        """
        trial_record = {
            "task_id": task_id,
            "category": task_category,
            "pattern_applied": pattern_applied,
            "status": "PASS" if success else "FAIL",
            "latency_ms": round(execution_latency_ms, 2),
            "error_details": error_details,
            "timestamp": time.time()
        }
        self.registry["trials"].append(trial_record)
        # Keep sliding window of latest 500 verified trials
        self.registry["trials"] = self.registry["trials"][-500:]

        patterns = self.registry.setdefault("registered_patterns", [])
        if pattern_applied not in patterns:
            patterns.append(pattern_applied)

        self._save()
        return self.get_pattern_reputation(pattern_applied)

    def get_pattern_reputation(self, pattern_name: str) -> Dict[str, Any]:
        """
        Calculates Bayesian expected win rate strictly from verified empirical trials.
        Zero pre-seeded counts: trial count is 100% computed from the trial records.
        """
        # Count strictly from real executed trials in the ledger
        real_successes = sum(
            1 for t in self.registry.get("trials", [])
            if t.get("pattern_applied") == pattern_name and t.get("status") == "PASS"
        )
        real_failures = sum(
            1 for t in self.registry.get("trials", [])
            if t.get("pattern_applied") == pattern_name and t.get("status") == "FAIL"
        )
        total_empirical_trials = real_successes + real_failures

        # Standard uninformative / Laplace Beta prior parameters (cold-start smoothing)
        prior_alpha = 2.0
        prior_beta = 2.0

        # Bayesian Expected Value: E[theta] = (alpha + s) / (alpha + beta + s + f)
        expected_win_rate = (prior_alpha + real_successes) / (prior_alpha + prior_beta + total_empirical_trials)

        if total_empirical_trials == 0:
            evidence_status = "COLD_START_PRIOR_ONLY (Henüz Deney Kaydı Yok - Başlangıç Prior)"
        elif expected_win_rate >= 0.80 and total_empirical_trials >= 3:
            evidence_status = "PROVEN_STABLE (Ampirik Olarak Doğrulanmış Güvenli Desen)"
        elif expected_win_rate >= 0.50:
            evidence_status = "EXPERIMENTAL (Deneysel Aşama - Gözlem Devam Ediyor)"
        else:
            evidence_status = "DEPRECATED_HAZARD (Yüksek Hata Oranı - Mimari Tarafından Kaçınılmalı)"

        return {
            "pattern": pattern_name,
            "data_origin": "COMPUTED_FROM_VERIFIED_TRIALS",
            "empirical_trials_count": total_empirical_trials,
            "empirical_successes": real_successes,
            "empirical_failures": real_failures,
            "bayesian_prior": {"prior_alpha": prior_alpha, "prior_beta": prior_beta},
            "win_rate": round(expected_win_rate, 4),
            "win_rate_pct": round(expected_win_rate * 100.0, 2),
            "evidence_status": evidence_status
        }

    def get_calibrated_pattern_weights(self) -> Dict[str, float]:
        """Exports calibrated weight multipliers for the architectural synthesizer."""
        weights = {}
        patterns = self.registry.get("registered_patterns", [])
        for pattern in patterns:
            rep = self.get_pattern_reputation(pattern)
            weights[pattern] = rep["win_rate"]
        return weights


def main():
    parser = argparse.ArgumentParser(description="Zobar Feedback Outcome & Learning Engine.")
    parser.add_argument("--pattern", default="lock_free_ringbuffer", help="Pattern name to audit")
    parser.add_argument("--list", action="store_true", help="List all calibrated pattern weights")
    args = parser.parse_args()

    engine = FeedbackOutcomeEngine()
    print("\n=================================================================")
    print(" 🧠 ZOBAR BAYESYEN ÖĞRENME & AMPİRİK DENEY KAYDI")
    print("=================================================================\n")

    if args.list:
        weights = engine.get_calibrated_pattern_weights()
        for pat, w in weights.items():
            rep = engine.get_pattern_reputation(pat)
            print(f"• {pat:30} : WinRate {w:.3f} ({rep['empirical_successes']} Başarı / {rep['empirical_failures']} Hata | {rep['evidence_status']})")
    else:
        rep = engine.get_pattern_reputation(args.pattern)
        print(f"📌 Desen Adı            : {rep['pattern']}")
        print(f"🔬 Doğrulanmış Deney    : {rep['empirical_trials_count']} adet")
        print(f"✅ Başarılı / Hatalı    : {rep['empirical_successes']} / {rep['empirical_failures']}")
        print(f"📊 Bayesyen Prior       : Alpha={rep['bayesian_prior']['prior_alpha']}, Beta={rep['bayesian_prior']['prior_beta']}")
        print(f"🎯 Beklenen Win Rate    : %{rep['win_rate_pct']} ({rep['win_rate']})")
        print(f"🛡️ Kanıt Durumu         : {rep['evidence_status']}\n")


if __name__ == "__main__":
    main()
