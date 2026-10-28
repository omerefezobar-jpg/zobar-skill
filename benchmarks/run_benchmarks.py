#!/usr/bin/env python3
"""
Automated Ground-Truth Benchmark & Evaluation Suite for Zobar Skill.
Measures output accuracy, statutory compliance precision, architectural fit,
and evidence grounding ratio across diverse real-world domain testbeds.
"""

import sys
import os
import json
import time
import datetime

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.scan_regulations import evaluate_compliance
from scripts.synthesize_architecture import synthesize_tech_stack
from scripts.validate_inventions import generate_validated_inventions
from scripts.benchmark_competitors import search_commercial_incumbents

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BENCHMARK_TESTBEDS = [
    {
        "id": "CASE-01",
        "name": "Kritik Tıbbi Teşhis ve Otonom Karar Sistemi (Medical Diagnostics)",
        "query": "medical diagnostic patient telemetry autonomous AI system",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_article": "Madde 6 & Ek III",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": True
    },
    {
        "id": "CASE-02",
        "name": "Yüksek Başarımlı AST Derleyici & Kod Analiz Motoru (Code Analysis)",
        "query": "AST parser compiler code analysis static linter",
        "expected_ai_act_tier": "Minimal / Low Risk (Genel Yazılım Kapsamı)",
        "expected_statutory_article": "Madde 69",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": False
    },
    {
        "id": "CASE-03",
        "name": "Üretken Kod Asistanı & Otonom LLM Ajanı (Generative Coding Agent)",
        "query": "LLM generative code assistant autonomous software agent",
        "expected_ai_act_tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
        "expected_statutory_article": "Madde 50",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": False
    }
]

def run_benchmarks():
    print("========================================================================")
    print(" 🎯 ZOBAR SKILL — OTOMATİK KALİTE, DOĞRULUK & BENCHMARK TEST SUITE 🎯")
    print("========================================================================\n")

    start_time = time.time()
    results = []
    total_score = 0
    max_score = len(BENCHMARK_TESTBEDS) * 100

    for test in BENCHMARK_TESTBEDS:
        print(f"[*] Test Ediliyor [{test['id']}]: {test['name']}...")
        test_score = 0
        notes = []

        # 1. Mevzuat Doğruluk Testi
        compliance = evaluate_compliance(test["query"])
        eu_res = compliance["eu_ai_act"]

        if eu_res["tier"] == test["expected_ai_act_tier"]:
            test_score += 30
            notes.append("✅ EU AI Act risk sınıflandırması tam isabet.")
        else:
            notes.append(f"❌ EU AI Act sınıflandırma sapması: {eu_res['tier']}")

        if test["expected_statutory_article"] in eu_res["statutory_basis"]:
            test_score += 20
            notes.append(f"✅ Kanun maddesi referansı doğru ({test['expected_statutory_article']}).")
        else:
            notes.append("❌ Kanun maddesi referansı eşleşmedi.")

        if eu_res["requires_expert_counsel"] == test["expected_expert_counsel_flag"]:
            test_score += 10
            notes.append("✅ Hukuki uzman incelemesi bayrağı doğru.")

        # 2. Mimari Uyum Testi
        arch = synthesize_tech_stack(test["query"])
        if arch["core_language"] == test["expected_core_lang"]:
            test_score += 20
            notes.append(f"✅ Çekirdek dil seçimi amaca tam uygun ({arch['core_language']}).")
        else:
            test_score += 10
            notes.append(f"⚠️ Çekirdek dil kabul edilebilir ama hedef dışı: {arch['core_language']}")

        # 3. İcat ve Kanıt Ayrımı Disiplini Testi
        inventions_data = generate_validated_inventions(test["query"])
        inventions = inventions_data["inventions"]
        evidence_tagged = all("[Model Hipotezi" in inv["trl_evidence_type"] or "[Literatür İspatı" in inv["trl_evidence_type"] for inv in inventions)
        has_failure_modes = all(len(inv["failure_modes"]) == 3 for inv in inventions)

        if evidence_tagged and has_failure_modes:
            test_score += 20
            notes.append("✅ Tüm icatlar TRL kanıt türü ve 3 hata modu ile zırhlı.")
        else:
            notes.append("❌ İcat kanıt taksonomisinde eksik var.")

        total_score += test_score
        results.append({
            "id": test["id"],
            "name": test["name"],
            "score": test_score,
            "max": 100,
            "notes": notes
        })
        print(f"    -> Başarı Skoru: {test_score}/100\n")

    duration = time.time() - start_time
    final_percentage = (total_score / max_score) * 100

    print("========================================================================")
    print(f" 🏆 GENEL BENCHMARK SONUCU: %{final_percentage:.1f} DOĞRULUK SKORU ({total_score}/{max_score})")
    print(f" ⏱️ Toplam Test Süresi: {duration:.3f} saniye")
    print("========================================================================\n")

    # Markdown Raporu Üret
    report_lines = [
        "# ZOBAR SKILL DOĞRULUK & BENCHMARK SKORKARTI",
        f"**Tarih (UTC):** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | **Test Süresi:** {duration:.3f}s\n",
        f"### 🎯 Genel Doğruluk Oranı: %{final_percentage:.1f} ({total_score}/{max_score})\n",
        "---",
        "## 📋 Vaka Bazlı Sonuç Dağılımı\n",
        "| Test Kodu | Vaka Adı | Puan | Durum |",
        "| :--- | :--- | :--- | :--- |"
    ]

    for r in results:
        status_tag = "🌟 Kusursuz (Production Grade)" if r["score"] >= 90 else "⚠️ Geliştirilebilir"
        report_lines.append(f"| {r['id']} | {r['name']} | **{r['score']}/100** | {status_tag} |")

    report_lines.append("\n---")
    report_lines.append("## 🔍 Detaylı Denetim Maddeleri\n")

    for r in results:
        report_lines.append(f"### {r['id']}: {r['name']}")
        for n in r["notes"]:
            report_lines.append(f"- {n}")
        report_lines.append("")

    with open("benchmarks/BENCHMARK_REPORT.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    with open("benchmarks/benchmark_results.json", "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "final_percentage": final_percentage,
            "total_score": total_score,
            "max_score": max_score,
            "cases": results
        }, f, indent=2, ensure_ascii=False)

    print("[+] Benchmark raporu kaydedildi: benchmarks/BENCHMARK_REPORT.md")
    print("[+] Makine tarafından okunabilir JSON kaydedildi: benchmarks/benchmark_results.json")

    return final_percentage >= 90

if __name__ == "__main__":
    success = run_benchmarks()
    sys.exit(0 if success else 1)
