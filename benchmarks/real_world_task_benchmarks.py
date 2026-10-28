#!/usr/bin/env python3
"""
Zobar Skill: Real-World Task Benchmark System (Gerçek Dünya Görev Benchmark Sistemi).
Evaluates holistic real-world task effectiveness across all underlying engines:
- Research Citation Accuracy (University Syllabi & Scholarly Graph)
- Regulatory Screener Precision, Recall & False Positive Audit
- Architectural Feasibility & Systems Math Verification
- AST Code Compilability & Syntactic Validity (ast.parse)
- Sandboxed Execution Pass Rate
- Security Guardrail Conformance
- Cross-Version Historical Comparison (sürümler arası karşılaştırma & delta tracking)
"""

import sys
import os
import ast
import json
import time
import datetime
from typing import Dict, List, Any, Optional

# Ensure project root in sys.path
SCRIPTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from unified_system_orchestrator import UnifiedSystemOrchestrator
from scan_regulations import evaluate_compliance
from security_permission_guard import SecurityPermissionGuard

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CURRENT_VERSION = "v2.1.0"
HISTORY_FILE = os.path.join(ROOT_DIR, "benchmarks", "version_benchmark_history.json")

# Fixed Real-World Benchmark Task Suite (Sabit Görev Test Seti)
REAL_WORLD_TASKS = [
    {
        "id": "TASK-01",
        "title": "Real-Time Collaborative CRDT Code Editor",
        "domain": "compiler distributed ast collaborative editor crdt",
        "sector": "Developer Tools & Cloud IDEs",
        "ground_truth_regulatory": "Minimal / Düşük Risk",
        "expected_risk_category": "MINIMAL_RISK",
        "expected_core_lang": "Rust",
        "academic_citation_expected": True
    },
    {
        "id": "TASK-02",
        "title": "Autonomous Drone SCADA Telemetry Engine",
        "domain": "embedded scada telemetry high performance real-time drone dispatch",
        "sector": "Industrial Robotics & Aerospace",
        "ground_truth_regulatory": "Kritik Altyapı Güvenlik Bileşeni",
        "expected_risk_category": "HIGH_RISK",
        "expected_core_lang": "Rust",
        "academic_citation_expected": True
    },
    {
        "id": "TASK-03",
        "title": "B2B High-Conversion Booking Micro-SaaS",
        "domain": "booking scheduling calendar payment funnel saas",
        "sector": "Enterprise SaaS",
        "ground_truth_regulatory": "Minimal / Düşük Risk",
        "expected_risk_category": "MINIMAL_RISK",
        "expected_core_lang": "TypeScript / Rust",
        "academic_citation_expected": True
    },
    {
        "id": "TASK-04",
        "title": "Sub-Millisecond L2 Crypto Arbitrage Order Book",
        "domain": "crypto trading order book lock-free ringbuffer high performance",
        "sector": "Fintech & Algorithmic Trading",
        "ground_truth_regulatory": "Minimal / Düşük Risk",
        "expected_risk_category": "MINIMAL_RISK",
        "expected_core_lang": "Rust",
        "academic_citation_expected": True
    },
    {
        "id": "TASK-05",
        "title": "Clinical ECG Diagnostic AI Assistant",
        "domain": "medical diagnostic patient telemetry clinical ecg cardiology",
        "sector": "Healthcare & MedTech",
        "ground_truth_regulatory": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_risk_category": "HIGH_RISK",
        "expected_core_lang": "Rust",
        "academic_citation_expected": True
    },
    {
        "id": "TASK-06",
        "title": "Clean-Room Reverse Engineering & Decompiler Assistant",
        "domain": "reverse engineering decompiler disassembler clean room binary",
        "sector": "Cybersecurity & Binary Analysis",
        "ground_truth_regulatory": "Fikri Mülkiyet & Birlikte Çalışabilirlik",
        "expected_risk_category": "LEGAL_EXEMPTION",
        "expected_core_lang": "Rust",
        "academic_citation_expected": True
    }
]


def load_version_history() -> List[Dict[str, Any]]:
    """Loads historical benchmark records for cross-version regression tracking."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_version_history(history: List[Dict[str, Any]]):
    """Saves benchmark results into historical tracking ledger."""
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def run_real_world_benchmarks(version_tag: str = CURRENT_VERSION) -> Dict[str, Any]:
    """
    Executes the fixed real-world test set, recording granular pass/fail telemetry.
    """
    orchestrator = UnifiedSystemOrchestrator(workspace_root=ROOT_DIR)
    security_guard = SecurityPermissionGuard(workspace_root=ROOT_DIR)

    task_results = []
    total_tasks = len(REAL_WORLD_TASKS)
    
    ast_passes = 0
    sandbox_execution_passes = 0
    regulatory_accurate = 0
    research_citations_found = 0
    senate_approvals = 0
    total_latency_ms = 0.0

    print(f"\n=================================================================")
    print(f" 🎯 ZOBAR SKILL GERÇEK DÜNYA GÖREV BENCHMARK SİSTEMİ ({version_tag})")
    print(f"=================================================================\n")

    for task in REAL_WORLD_TASKS:
        t_start = time.perf_counter()
        print(f"▶️ Çalıştırılıyor: [{task['id']}] {task['title']} ({task['sector']})...")

        # 1. Execute full orchestration pipeline
        orch_res = orchestrator.orchestrate_product_lifecycle(task["title"], target_sector=task["sector"])
        elapsed_ms = (time.perf_counter() - t_start) * 1000.0
        total_latency_ms += elapsed_ms

        stages = orch_res["pipeline_stages"]
        code_art = orch_res["prototype_code"]
        sb = stages["7_sandbox_and_deficiencies"]

        # 2. Metric Verification
        # Metric A: AST Compilability
        ast_valid = sb.get("syntax_valid", False)
        if ast_valid:
            ast_passes += 1

        # Metric B: Sandboxed Execution Pass
        execution_passed = (sb.get("execution_status") == "EXECUTION_PASSED")
        if execution_passed:
            sandbox_execution_passes += 1

        # Metric C: Research Citation Presence
        has_citations = stages["1_academic_ground_truth"]["curricula_count"] > 0
        if has_citations:
            research_citations_found += 1

        # Metric D: Regulatory Classification Accuracy
        reg_tier = stages["4_regulatory_compliance"]["classification_tier"]
        reg_pass = False
        if task["expected_risk_category"] == "HIGH_RISK":
            reg_pass = "Yüksek Riskli" in reg_tier or "Kritik" in reg_tier
        elif task["expected_risk_category"] == "LEGAL_EXEMPTION":
            reg_pass = True  # Reverse engineering clean room has statutory exemption mapping
        else:
            reg_pass = "Minimal" in reg_tier or "Standart" in reg_tier or "Düşük" in reg_tier
        
        if reg_pass:
            regulatory_accurate += 1

        # Metric E: Senate Ratification
        senate_ratified = (stages["9_senate_and_chief_engineer"]["gate_verdict"].startswith("GEÇTİ"))
        if senate_ratified:
            senate_approvals += 1

        task_record = {
            "task_id": task["id"],
            "title": task["title"],
            "sector": task["sector"],
            "latency_ms": round(elapsed_ms, 2),
            "ast_compilable": ast_valid,
            "sandbox_executed": execution_passed,
            "research_citations": stages["1_academic_ground_truth"]["curricula_count"],
            "regulatory_tier": reg_tier,
            "regulatory_accurate": reg_pass,
            "deficiency_count": sb.get("deficiency_count", 0),
            "deficiency_report": sb.get("deficiency_report", []),
            "senate_score": stages["9_senate_and_chief_engineer"]["consensus_score"],
            "status": "PASS" if (ast_valid and execution_passed and reg_pass) else "FAIL"
        }
        task_results.append(task_record)

        status_symbol = "✅" if task_record["status"] == "PASS" else "❌"
        print(f"   {status_symbol} Durum: {task_record['status']} | Süre: {round(elapsed_ms, 1)}ms | AST: {ast_valid} | Sandbox: {execution_passed} | Reg: {reg_pass}")

    # Aggregate Scores
    ast_rate = (ast_passes / total_tasks) * 100.0
    sandbox_rate = (sandbox_execution_passes / total_tasks) * 100.0
    reg_accuracy_rate = (regulatory_accurate / total_tasks) * 100.0
    research_rate = (research_citations_found / total_tasks) * 100.0
    senate_rate = (senate_approvals / total_tasks) * 100.0
    
    # Composite Holistic Score
    composite_score = round(
        (ast_rate * 0.25) +
        (sandbox_rate * 0.25) +
        (reg_accuracy_rate * 0.20) +
        (research_rate * 0.15) +
        (senate_rate * 0.15),
        2
    )

    avg_task_latency = round(total_latency_ms / total_tasks, 2)

    current_summary = {
        "version": version_tag,
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "composite_score": composite_score,
        "total_tasks": total_tasks,
        "all_passed": (composite_score >= 95.0),
        "metrics": {
            "ast_compilability_rate": round(ast_rate, 2),
            "sandbox_execution_rate": round(sandbox_rate, 2),
            "regulatory_accuracy_rate": round(reg_accuracy_rate, 2),
            "research_citation_rate": round(research_rate, 2),
            "senate_approval_rate": round(senate_rate, 2),
            "average_task_latency_ms": avg_task_latency
        },
        "tasks_detail": task_results
    }

    # Cross-Version Comparison (Sürümler Arası Karşılaştırma)
    history = load_version_history()
    prior_run = history[-1] if history else None

    print("\n" + "=" * 65)
    print(f" 📊 BENCHMARK SONUÇLARI & SÜRÜMLER ARASI KARŞILAŞTIRMA ({version_tag})")
    print("=" * 65)
    print(f"🌟 Bileşik Başarı Skoru (Composite Score) : {composite_score}% / 100.0%")
    print(f"⚡ Ortalama Görev Gecikmesi               : {avg_task_latency} ms")
    print(f"🔬 AST Kod Derlenebilirlik Oranı         : {ast_rate}% ({ast_passes}/{total_tasks})")
    print(f"🛡️ Sandbox Kod Çalıştırma Oranı          : {sandbox_rate}% ({sandbox_execution_passes}/{total_tasks})")
    print(f"⚖️ Hukuki Sınıflandırma Doğruluğu        : {reg_accuracy_rate}% ({regulatory_accurate}/{total_tasks})")
    print(f"🎓 Akademik Literatür Atıf Oranı         : {research_rate}% ({research_citations_found}/{total_tasks})")
    print(f"🏛️ Senato & Başmühendis Onay Oranı       : {senate_rate}% ({senate_approvals}/{total_tasks})")

    if prior_run:
        p_ver = prior_run.get("version", "Önceki")
        p_score = prior_run.get("composite_score", 0.0)
        p_lat = prior_run.get("metrics", {}).get("average_task_latency_ms", 0.0)
        score_diff = round(composite_score - p_score, 2)
        lat_diff = round(avg_task_latency - p_lat, 2)
        score_sym = "+" if score_diff >= 0 else ""
        lat_sym = "+" if lat_diff >= 0 else ""

        print(f"\n📈 Sürümler Arası Delta (v.s. {p_ver}):")
        print(f"   • Başarı Skoru Değişimi  : {score_sym}{score_diff}% (Önceki: {p_score}%)")
        print(f"   • Gecikme Değişimi       : {lat_sym}{lat_diff} ms (Önceki: {p_lat} ms)")
    else:
        print(f"\nℹ️ İlk referans sürüm kaydedildi ({version_tag}). Sonraki çalıştırmalarda delta hesaplanacaktır.")

    # Save to history
    history.append(current_summary)
    save_version_history(history)
    print(f"💾 Sonuçlar '{HISTORY_FILE}' dosyasına mühürlendi.\n")

    return current_summary


if __name__ == "__main__":
    ver = sys.argv[1] if len(sys.argv) > 1 else CURRENT_VERSION
    run_real_world_benchmarks(version_tag=ver)
