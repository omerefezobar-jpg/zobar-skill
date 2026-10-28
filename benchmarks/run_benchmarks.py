#!/usr/bin/env python3
"""
Strict Zero-Tolerance Ground-Truth Benchmark & Evaluation Suite for Zobar Skill.
Enforces 100% deterministic compliance across statutory EU AI Act precedents,
clinical intended-purpose discrimination, architectural suitability, and evidence taxonomy.
POLICY: A single regulatory, architectural, or evidence failure FAILS the entire suite (Zero Tolerance).
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

# 20 Rigorous Ground-Truth Benchmark Testbeds backed by official EU Statutory Precedents
BENCHMARK_TESTBEDS = [
    {
        "id": "CASE-01",
        "name": "Klinik Tıbbi Teşhis ve Hasta Karar Desteği (Clinical Diagnostic)",
        "query": "medical diagnostic patient telemetry clinical treatment decision AI",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_basis": "MDR (AB) 2017/745 Kural 11",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "EU 2024/1689 Article 6(1) & MDR (EU) 2017/745 Annex VIII Rule 11 (Software as a Medical Device)"
    },
    {
        "id": "CASE-02",
        "name": "Hastane İdari Randevu & Vardiya Planlama (Hospital Administrative Scheduling)",
        "query": "hospital administrative scheduling patient appointment billing shift management",
        "expected_ai_act_tier": "Minimal / Düşük Risk (İdari Sağlık Yazılımı)",
        "expected_statutory_basis": "MDR (AB) 2017/745 Kapsam Dışı",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "MDR (EU) 2017/745 Annex VIII Rule 11 (Administrative hospital software is excluded from high risk)"
    },
    {
        "id": "CASE-03",
        "name": "Geliştirici Aracı, AST Ayrıştırıcı & Statik Analiz (Compiler & Linter)",
        "query": "AST parser compiler code analysis static linter refactoring tool",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Geliştirici Aracı / AI Act Muafiyeti)",
        "expected_statutory_basis": "Madde 2(8)",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 2(8) (Exemption for AI systems developed solely for research & development)"
    },
    {
        "id": "CASE-04",
        "name": "Kullanıcıyla Doğrudan Etkileşen Sohbet Botu (Conversational Chatbot)",
        "query": "conversational bot customer service chatbot interaction natural person",
        "expected_ai_act_tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
        "expected_statutory_basis": "Madde 50(1)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 50(1) (Transparency obligation for AI interacting with humans)"
    },
    {
        "id": "CASE-05",
        "name": "Sosyal Puanlama & İzinsiz Biyometrik Veri Tabanı (Prohibited Practice)",
        "query": "social scoring biometric categorisation untargeted facial recognition database",
        "expected_ai_act_tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
        "expected_statutory_basis": "Madde 5(1)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 5(1)(c)/(e) (Prohibited AI Practices)"
    },
    {
        "id": "CASE-06",
        "name": "Tüketici Kredi Puanlama ve Finansal Risk Değerlendirmesi (Credit Scoring)",
        "query": "credit score creditworthiness financial risk consumer loan evaluation",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_basis": "Ek III Nokta 5(b)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Annex III Point 5(b) & EDPB Guidelines WP251 on Automated Decision-Making"
    },
    {
        "id": "CASE-07",
        "name": "Dağıtık Mikro-Servis Ağı & API Gateway (Distributed Infrastructure)",
        "query": "distributed network microservice gateway orchestrator",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
        "expected_statutory_basis": "Recital 34",
        "expected_core_lang": "Go",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Recital 34 (General software not listed in Annex III is minimal risk)"
    },
    {
        "id": "CASE-08",
        "name": "İnsan Kaynakları & Otomatik Özgeçmiş Filtreleme (HR Resume Screening)",
        "query": "recruitment hiring automated resume screening candidate evaluation",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_basis": "Ek III Nokta 4(a)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Annex III Point 4(a) (Recruitment and selection of natural persons)"
    },
    {
        "id": "CASE-09",
        "name": "Eğitim Sınav Değerlendirme & Puanlama (Exam Grading Assessment)",
        "query": "educational exam grading student assessment admission evaluation",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_basis": "Ek III Nokta 3(a)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Annex III Point 3(a) (Assessment of students in educational institutions)"
    },
    {
        "id": "CASE-10",
        "name": "Kritik Enerji Şebekesi & Su Yönetimi SCADA (Critical Infrastructure)",
        "query": "critical infrastructure safety component power grid water management scada",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_basis": "Ek III Nokta 2",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Annex III Point 2 (Safety components in the management of critical infrastructure)"
    },
    {
        "id": "CASE-11",
        "name": "Otonom Araç Gerçek Zamanlı Frenleme & Telemetri (Automotive Safety Component)",
        "query": "autonomous vehicle braking safety telemetry critical machinery component",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_basis": "Ek I",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Annex I & Machinery Regulation (EU) 2023/1230"
    },
    {
        "id": "CASE-12",
        "name": "Sentetik Video & Deepfake Medya Üretimi (Synthetic Media Watermarking)",
        "query": "deepfake public synthetic media synthetic video generation",
        "expected_ai_act_tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
        "expected_statutory_basis": "Madde 50(2)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 50(2) (Obligation to watermark artificially generated content)"
    },
    {
        "id": "CASE-13",
        "name": "İşyerinde Çalışan Duygu Analizi (Workplace Emotion Recognition)",
        "query": "workplace emotion recognition employee monitoring sentiment",
        "expected_ai_act_tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
        "expected_statutory_basis": "Madde 5(1)(f)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 5(1)(f) (Prohibition of emotion recognition in the workplace)"
    },
    {
        "id": "CASE-14",
        "name": "Bireysel Suç Tekerrür Tahmini (Individual Predictive Policing)",
        "query": "predictive policing recidivism assessment individual crime risk",
        "expected_ai_act_tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
        "expected_statutory_basis": "Madde 5(1)(d)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 5(1)(d) (Prohibition of risk assessment of natural persons for criminal offenses)"
    },
    {
        "id": "CASE-15",
        "name": "Geliştirici Kod İyileştirme & Git Asistanı (Refactoring Tool)",
        "query": "developer code refactoring git workflow assistant linter",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Geliştirici Aracı / AI Act Muafiyeti)",
        "expected_statutory_basis": "Madde 2(8)",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 2(8) (Exemption for developer and engineering tools)"
    },
    {
        "id": "CASE-16",
        "name": "Bilinçaltı Manipülatif Davranış Çarpıtma (Subliminal Behavior Distortion)",
        "query": "subliminal manipulation for harm psychological exploitation",
        "expected_ai_act_tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
        "expected_statutory_basis": "Madde 5(1)(a)",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Article 5(1)(a) (Prohibition of subliminal techniques causing harm)"
    },
    {
        "id": "CASE-17",
        "name": "Radyoloji Görüntüleme Tümör Tespiti (Hospital Radiology Imaging)",
        "query": "hospital radiology imaging tumor detection clinical oncology diagnostic",
        "expected_ai_act_tier": "Yüksek Riskli Sistem (High-Risk AI System)",
        "expected_statutory_basis": "MDR (AB) 2017/745 Kural 11",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": True,
        "official_ground_truth_source": "MDR (EU) 2017/745 Annex VIII Rule 11 & Regulation (EU) 2024/1689 Article 6(1)"
    },
    {
        "id": "CASE-18",
        "name": "E-Ticaret Ürün Tavsiye ve Arama Sıralaması (Product Recommendation)",
        "query": "e-commerce product recommendation search re-ranking filter catalog",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
        "expected_statutory_basis": "Recital 34",
        "expected_core_lang": "TypeScript / Rust (Hibrit Mimari)",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Recital 34 (General consumer search ranking is minimal risk)"
    },
    {
        "id": "CASE-19",
        "name": "Gerçek Zamanlı Yüksek Frekanslı Algoritmik Ticaret (HFT Algorithmic Trading)",
        "query": "realtime algorithmic high frequency trading engine market order",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
        "expected_statutory_basis": "Recital 34",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Recital 34 (Financial trading is minimal risk under AI Act, regulated under MiFID II)"
    },
    {
        "id": "CASE-20",
        "name": "Uç Nokta Akıllı Termostat Firmware'i (Edge IoT Smart Thermostat)",
        "query": "edge embedded iot smart thermostat firmware temperature controller",
        "expected_ai_act_tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
        "expected_statutory_basis": "Recital 34",
        "expected_core_lang": "Rust",
        "expected_expert_counsel_flag": False,
        "official_ground_truth_source": "Regulation (EU) 2024/1689 Recital 34 (Home appliance automation firmware is minimal risk)"
    }
]

def run_benchmarks():
    print("========================================================================")
    print(" 🎯 ZOBAR SKILL — SIFIR TOLERANSLI 20-VAKALIK RESMÎ BENCHMARK SUITE 🎯")
    print("========================================================================\n")

    start_time = time.time()
    results = []
    total_failures = 0

    for test in BENCHMARK_TESTBEDS:
        print(f"[*] Denetleniyor [{test['id']}]: {test['name']}...")
        failures = []

        # 1. Mevzuat Doğruluk Testi (Sıfır Tolerans)
        compliance = evaluate_compliance(test["query"])
        eu_res = compliance["eu_ai_act"]

        if eu_res["tier"] != test["expected_ai_act_tier"]:
            failures.append(f"Mevzuat Sınıflandırma Hatası: Beklenen '{test['expected_ai_act_tier']}', Alınan '{eu_res['tier']}'")

        if test["expected_statutory_basis"] not in eu_res["statutory_basis"]:
            failures.append(f"Statutory Basis Hatası: Beklenen '{test['expected_statutory_basis']}', Alınan '{eu_res['statutory_basis']}'")

        if eu_res["requires_expert_counsel"] != test["expected_expert_counsel_flag"]:
            failures.append(f"Hukuki Mütalaa Bayrağı Uyuşmazlığı: Beklenen {test['expected_expert_counsel_flag']}, Alınan {eu_res['requires_expert_counsel']}")

        # 2. Mimari Uyum Testi (Sıfır Tolerans)
        arch = synthesize_tech_stack(test["query"])
        if arch["core_language"] != test["expected_core_lang"]:
            failures.append(f"Mimari Dil Uyuşmazlığı: Beklenen '{test['expected_core_lang']}', Alınan '{arch['core_language']}'")

        # 3. İcat ve Dinamik Kanıt Ayrımı Disiplini Testi (Sıfır Tolerans)
        inventions_data = generate_validated_inventions(test["query"])
        inventions = inventions_data["inventions"]
        evidence_tagged = all("[Model Hipotezi" in inv["trl_evidence_type"] or "[Literatür İspatı" in inv["trl_evidence_type"] for inv in inventions)
        has_failure_modes = all(len(inv["failure_modes"]) == 3 for inv in inventions)

        if not evidence_tagged or not has_failure_modes:
            failures.append("Kanıt Ayrımı Hatası: TRL kanıt türü etiketi veya 3 hata modu eksik.")

        if failures:
            total_failures += len(failures)
            status = "❌ BAŞARISIZ"
            score = 0
            print(f"    -> {status} ({len(failures)} kritik hata)")
            for f in failures:
                print(f"       - {f}")
        else:
            status = "✅ KUSURSUZ (100/100)"
            score = 100
            print(f"    -> {status} — Emsal: {test['official_ground_truth_source']}")

        results.append({
            "id": test["id"],
            "name": test["name"],
            "status": status,
            "score": score,
            "failures": failures,
            "ground_truth_precedent": test["official_ground_truth_source"]
        })
        print()

    duration = time.time() - start_time
    total_cases = len(BENCHMARK_TESTBEDS)
    successful_cases = sum(1 for r in results if r["score"] == 100)
    pass_rate = (successful_cases / total_cases) * 100

    print("========================================================================")
    print(f" 📊 BENCHMARK ÖZETİ: {successful_cases}/{total_cases} Vaka Geçti (%{pass_rate:.1f})")
    print(f" ⚠️ Toplam Kritik Hata Sayısı: {total_failures}")
    print(f" ⏱️ Toplam Test Süresi       : {duration:.3f} saniye")
    print("========================================================================\n")

    # Dürüst, Sertifikalı Markdown Raporu
    report_lines = [
        "# ZOBAR SKILL 20-VAKALIK SIFIR TOLERANSLI DOĞRULUK & EMSAL SKORKARTI",
        f"**Rapor Tarihi (UTC):** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | **Test Süresi:** {duration:.3f}s\n",
        "> 🏛️ **Resmî Mevzuat Emsalleri:** Bu test kümesindeki tüm referans değerler resmî AB mevzuatlarına (Regulation (EU) 2024/1689 AI Act, MDR (EU) 2017/745 Annex VIII Rule 11, EDPB Guidelines WP251) dayandırılmıştır.\n",
        "> ⚠️ **Sıfır Tolerans Politikası:** Tek bir yasal madde sınıflandırma hatası veya kanıt taksonomisi sapması durumunda test derhal başarısız sayılır ve CI durdurulur.\n",
        f"### 🎯 Başarı Oranı: %{pass_rate:.1f} ({successful_cases}/{total_cases} Vaka Sıfır Hatayla Geçti)\n",
        "---",
        "## 📋 Vaka Bazlı Denetim Tablosu\n",
        "| Kod | Test Edilen Senaryo | Resmî Emsal / Yasal Dayanak | Puan | Statü |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]

    for r in results:
        report_lines.append(f"| {r['id']} | {r['name']} | *{r['ground_truth_precedent']}* | **{r['score']}/100** | {r['status']} |")

    report_lines.append("\n---")
    report_lines.append("## 🔍 Sıfır Tolerans Denetim Günlüğü\n")

    for r in results:
        report_lines.append(f"### {r['id']}: {r['name']}")
        report_lines.append(f"- **Resmî Hukuki Emsal:** {r['ground_truth_precedent']}")
        if r["failures"]:
            for f in r["failures"]:
                report_lines.append(f"- ❌ {f}")
        else:
            report_lines.append("- ✅ Mevzuat sınıflandırması, kullanım amacı ayrımı, mimari seçim ve kanıt taksonomisi tam uyumlu.")
        report_lines.append("")

    with open("benchmarks/BENCHMARK_REPORT.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    with open("benchmarks/benchmark_results.json", "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "policy": "Strict Zero-Tolerance (Any failure fails CI)",
            "pass_rate_percentage": pass_rate,
            "total_cases": total_cases,
            "successful_cases": successful_cases,
            "total_failures": total_failures,
            "cases": results
        }, f, indent=2, ensure_ascii=False)

    print("[+] Skorkart kaydedildi: benchmarks/BENCHMARK_REPORT.md")
    print("[+] JSON kaydedildi: benchmarks/benchmark_results.json")

    # STRICT ZERO TOLERANCE: Any failure returns False -> fails CI!
    return total_failures == 0

if __name__ == "__main__":
    success = run_benchmarks()
    sys.exit(0 if success else 1)
