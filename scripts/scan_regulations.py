#!/usr/bin/env python3
"""
Regulatory & Compliance Screener for Frontier Innovator.
Evaluates regulatory risk tiers (EU AI Act, GDPR/KVKK, Open Source Licensing)
based on domain characteristics, providing grounded legal guardrails.
"""

import sys
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def evaluate_compliance(domain_keywords: str):
    """
    Evaluates key regulatory frameworks based on technology domain keywords.
    Returns categorized risk levels, triggers, and mandatory mitigation steps.
    """
    lowered = domain_keywords.lower()
    
    # 1. EU AI Act Risk Tiering
    ai_tier = "Minimal / General Risk"
    ai_reasons = []
    
    if any(k in lowered for k in ["biometric", "facial", "social scor", "emotion"]):
        ai_tier = "Prohibited / Unacceptable Risk"
        ai_reasons.append("Biyometrik tanıma veya sosyal puanlama içeriyor; AB pazarında yasaklanabilir.")
    elif any(k in lowered for k in ["medical", "health", "credit", "recruitment", "critical infra", "surveillance", "autonomous driv"]):
        ai_tier = "High Risk (Yüksek Risk)"
        ai_reasons.append("Kritik altyapı, sağlık veya finansal karar mekanizması içeriyor; zorunlu uygunluk denetimi, CE işareti ve insan denetimi (human-in-the-loop) şarttır.")
    elif any(k in lowered for k in ["llm", "generative", "agent", "deepfake", "synthetic", "bot"]):
        ai_tier = "Specific Transparency Risk (Şeffaflık Yükümlülüğü)"
        ai_reasons.append("Yapay zeka üretimi içerik ve otonom ajanlar kullanıcılara açıkça beyan edilmeli ve suistimal filtreleri bulunmalıdır.")
        
    # 2. GDPR / KVKK Veri Egemenliği
    gdpr_risks = []
    if any(k in lowered for k in ["user data", "personal", "identity", "email", "tracking", "telemetry"]):
        gdpr_risks.append("Kişisel veri (PII) işleniyor: Açık rıza, veri minimizasyonu ve veri anonimleştirme zorunlu.")
    if any(k in lowered for k in ["code", "repository", "proprietary", "secret", "financial"]):
        gdpr_risks.append("Fikri mülkiyet ve ticari sır: Harici LLM'lere kod/veri gönderilmemeli, Zero Data Retention (ZDR) garantili veya yerel (on-prem) modeller tercih edilmeli.")
    if not gdpr_risks:
        gdpr_risks.append("Standart şifreleme ve anonim loglama yeterli.")

    # 3. Açık Kaynak Lisans Uyumluluğu (SPDX)
    license_rules = [
        {"type": "Permissive (MIT, Apache 2.0, BSD-3)", "risk": "Düşük", "rule": "Ticari ürünlerde serbestçe kullanılabilir; telif ve lisans metni korunmalıdır."},
        {"type": "Weak Copyleft (LGPL, MPL 2.0)", "risk": "Orta", "rule": "Kütüphane olarak dinamik bağlanabilir; kütüphanede yapılan değişiklikler açık kaynak sunulmalıdır."},
        {"type": "Strong Copyleft (GPLv3, AGPLv3)", "risk": "Kritik", "rule": "Statik bağlantı veya ağ üzerinden kullanım tüm uygulamanın açık kaynak yapılmasını zorunlu kılabilir; ticari kapalı kod ürünlerde AST seviyesinde engellenmelidir."}
    ]

    return {
        "domain": domain_keywords,
        "eu_ai_act": {
            "tier": ai_tier,
            "justification": " | ".join(ai_reasons) if ai_reasons else "Standart yazılım araçları; genel şeffaflık kuralları geçerli."
        },
        "data_privacy": gdpr_risks,
        "licensing": license_rules
    }

def main():
    parser = argparse.ArgumentParser(description="Regulatory & Compliance Risk Screener.")
    parser.add_argument("domain", help="Technology or domain description")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚖️ REGÜLASYON, KVKK/GDPR & LİSANS DENETİMİ: '{args.domain}'")
    print(f"=======================================================\n")

    res = evaluate_compliance(args.domain)
    print(f"🇪🇺 EU AI Act Seviyesi : {res['eu_ai_act']['tier']}")
    print(f"   Gerekçe            : {res['eu_ai_act']['justification']}\n")
    print("🔒 Veri Gizliliği (KVKK / GDPR):")
    for r in res["data_privacy"]:
        print(f"   - {r}")
    print("\n📜 Açık Kaynak Lisans Stratejisi:")
    for lic in res["licensing"]:
        print(f"   - [{lic['type']}] Risk: {lic['risk']} -> {lic['rule']}")

if __name__ == "__main__":
    main()
