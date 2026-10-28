#!/usr/bin/env python3
"""
Rigorous Ground-Truth Benchmark & Evaluation Suite for Zobar Skill.
Measures regression accuracy, statutory compliance precision, architectural fit,
and evidence taxonomy discipline across diverse real-world domain testbeds
with zero-tolerance scoring.
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

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Expanded, diverse ground-truth testbed
BENCHMARK_TESTBEDS = [
    {
        "id": "CASE-01",
        "name": "Kritik Tıbbi Teşhis ve Hasta Telemetrisi (Medical Diagnostics)",
        "query": "medical diagnostic patient telemetry autonomous AI system",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_article": "Madde 6",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": True
    },
    {
        "id": "CASE-02",
        "name": "Yüksek Başarımlı AST Derleyici & Statik Kod Analizi (Compiler Engine)",
        "query": "AST parser compiler code analysis static linter",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
        "expected_statutory_article": "Recital 34",
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
    },
    {
        "id": "CASE-04",
        "name": "Sosyal Puanlama & İzinsiz Biyometrik Veri Kazıma (Prohibited System)",
        "query": "social scoring biometric categorisation untargeted facial recognition database",
        "expected_ai_act_tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
        "expected_statutory_article": "Madde 5(1)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True
    },
    {
        "id": "CASE-05",
        "name": "Banka Kredi Skoru & Finansal Uygunluk Değerlendirmesi (Credit Scoring)",
        "query": "credit scoring creditworthiness financial risk evaluation AI",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_article": "Ek III",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True
    },
    {
        "id": "CASE-06",
        "name": "Dağıtık Mikro-Servis Ağı & API Gateway (Distributed Microservices)",
        "query": "distributed network microservice gateway orchestrator",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
        "expected_statutory_article": "Recital 34",
        "expected_core_lang": "Go",
        "expected_expert_counsel_flag": False
    }
]

def run_benchmarks():
    print("========================================================================")
    print(" 🎯 ZOBAR SKILL — KATI DOĞRULUK & REGRESYON BENCHMARK TEST SUITE 🎯")
    print("========================================================================\n")

    start_time = time.time()
    results = []
    total_score = 0
    max_score = len(BENCHMARK_TESTBEDS) * 100

    statutory_matches = 0
    architecture_matches = 0
    evidence_matches = 0

    for test in BENCHMARK_TESTBEDS:
        print(f"[*] Denetleniyor [{test['id']}]: {test['name']}...")
        test_score = 0
        notes = []

        # 1. Mevzuat Doğruluk Testi (Sıfır Tolerans: Yanlış sınıflandırma = 0 puan)
        compliance = evaluate_compliance(test["query"])
        eu_res = compliance["eu_ai_act"]

        if eu_res["tier"] == test["expected_ai_act_tier"]:
            test_score += 30
            statutory_matches += 1
            notes.append(f"✅ Sınıflandırma: Tam İsabet ({eu_res['tier']})")
        else:
            notes.append(f"❌ Sınıflandırma Hatası: Beklenen '{test['expected_ai_act_tier']}', Alınan '{eu_res['tier']}'")

        if test["expected_statutory_article"] in eu_res["statutory_basis"]:
            test_score += 20
            notes.append(f"✅ Kanun Maddesi: {test['expected_statutory_article']}")
        else:
            notes.append(f"❌ Madde Eşleşmedi: {eu_res['statutory_basis']}")

        if eu_res["requires_expert_counsel"] == test["expected_expert_counsel_flag"]:
            test_score += 10
            notes.append("✅ Hukuki Mütalaa Bayrağı: Doğru")
        else:
            notes.append("❌ Hukuki Mütalaa Bayrağı: Uyuşmazlık")

        # 2. Mimari Uyum Testi (Sıfır Tolerans: Eşleşmezse 0 puan)
        arch = synthesize_tech_stack(test["query"])
        if arch["core_language"] == test["expected_core_lang"]:
            test_score += 20
            architecture_matches += 1
            notes.append(f"✅ Çekirdek Dil: {arch['core_language']}")
        else:
            notes.append(f"❌ Dil Uyuşmazlığı: Beklenen '{test['expected_core_lang']}', Alınan '{arch['core_language']}'")

        # 3. İcat ve Kanıt Ayrımı Disiplini Testi (Sıfır Tolerans)
        inventions_data = generate_validated_inventions(test["query"])
        inventions = inventions_data["inventions"]
        evidence_tagged = all("[Model Hipotezi" in inv["trl_evidence_type"] or "[Literatür İspatı" in inv["trl_evidence_type"] for inv in inventions)
        has_failure_modes = all(len(inv["failure_modes"]) == 3 for inv in inventions)

        if evidence_tagged and has_failure_modes:
            test_score += 20
            evidence_matches += 1
            notes.append("✅ Kanıt Taksonomisi: Model hipotezi ve hata modları eksiksiz")
        else:
            notes.append("❌ Kanıt Taksonomisi: İspat etiketi veya hata modları eksik")

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
    pass_rate = (total_score / max_score) * 100

    print("========================================================================")
    print(f" 📊 BENCHMARK SONUCU: %{pass_rate:.1f} REGRESYON GEÇME ORANI ({total_score}/{max_score})")
    print(f" ⚖️ Mevzuat Madde İsabeti : {statutory_matches}/{len(BENCHMARK_TESTBEDS)}")
    print(f" 🛠️ Mimari Uyum Oranı     : {architecture_matches}/{len(BENCHMARK_TESTBEDS)}")
    print(f" 🔍 Kanıt Ayrımı Disiplini: {evidence_matches}/{len(BENCHMARK_TESTBEDS)}")
    print(f" ⏱️ Toplam Test Süresi   : {duration:.3f} saniye")
    print("========================================================================\n")

    # Dürüst Markdown Raporu
    report_lines = [
        "# ZOBAR SKILL OTOMATİK REGRESYON & UYUMLULUK SKORKARTI",
        f"**Tarih (UTC):** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | **Test Süresi:** {duration:.3f}s\n",
        "> ⚠️ **Metodolojik Beyan:** Bu benchmark, Zobar Skill motorunun kodlanmış yasal maddeler (EU AI Act & GDPR), mimari kurallar ve kanıt taksonomisiyle regresyon uyumunu doğrular. Bağımsız avukatlık mütalaası veya empirik pazar başarısı garantisi teşkil etmez.\n",
        f"### 📊 Regresyon Test Kümesi Başarı Oranı: %{pass_rate:.1f} ({total_score}/{max_score})",
        f"- **Mevzuat Sınıflandırma İsabeti:** {statutory_matches}/{len(BENCHMARK_TESTBEDS)} (%{(statutory_matches/len(BENCHMARK_TESTBEDS))*100:.1f})",
        f"- **Teknik Mimari Seçim Uyumu:** {architecture_matches}/{len(BENCHMARK_TESTBEDS)} (%{(architecture_matches/len(BENCHMARK_TESTBEDS))*100:.1f})",
        f"- **Kanıt ve Hipotez Ayrım Oranı:** {evidence_matches}/{len(BENCHMARK_TESTBEDS)} (%{(evidence_matches/len(BENCHMARK_TESTBEDS))*100:.1f})\n",
        "---",
        "## 📋 Vaka Bazlı Denetim Tablosu\n",
        "| Kod | Test Edilen Senaryo | Puan | Statü |",
        "| :--- | :--- | :--- | :--- |"
    ]

    for r in results:
        status_tag = "✅ Başarılı" if r["score"] == 100 else ("⚠️ Kısmi" if r["score"] >= 60 else "❌ Başarısız")
        report_lines.append(f"| {r['id']} | {r['name']} | **{r['score']}/100** | {status_tag} |")

    report_lines.append("\n---")
    report_lines.append("## 🔍 Madde Bazlı Detay Günlüğü\n")

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
            "pass_rate_percentage": pass_rate,
            "total_score": total_score,
            "max_score": max_score,
            "statutory_matches": f"{statutory_matches}/{len(BENCHMARK_TESTBEDS)}",
            "architecture_matches": f"{architecture_matches}/{len(BENCHMARK_TESTBEDS)}",
            "cases": results
        }, f, indent=2, ensure_ascii=False)

    print("[+] Skorkart kaydedildi: benchmarks/BENCHMARK_REPORT.md")
    print("[+] JSON kaydedildi: benchmarks/benchmark_results.json")

    return pass_rate >= 90

if __name__ == "__main__":
    success = run_benchmarks()
    sys.exit(0 if success else 1)
