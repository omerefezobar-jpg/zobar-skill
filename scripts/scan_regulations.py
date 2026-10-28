#!/usr/bin/env python3
"""
Statutory Regulatory & Compliance Screener for Frontier Innovator.
Maps domain characteristics to specific legal articles in the EU AI Act (2024/1689),
GDPR (2016/679), and OSI Open Source licensing compatibility guidelines.
Provides transparent statutory citations and confidence levels.
"""

import sys
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def evaluate_compliance(domain_keywords: str):
    """
    Evaluates statutory compliance triggers with article-level legal citations.
    Returns risk classifications, statutory references, and indeterminate/counsel flags.
    """
    lowered = domain_keywords.lower()
    
    # 1. EU AI Act (Regulation EU 2024/1689)
    eu_status = {
        "tier": "Minimal / Low Risk (Genel Yazılım Kapsamı)",
        "statutory_basis": "EU AI Act Madde 69 (Genel Amaçlı / Doğrudan Yasaklanmamış Sistemler)",
        "confidence": "Yüksek (Doğrudan Yüksek Risk Listesinde Değil)",
        "requires_expert_counsel": False,
        "articles": ["Regulation (EU) 2024/1689 Recital 34 & Article 69"],
        "obligations": [
            "Gönüllü davranış kuralları (Codes of Conduct) ve telif hakları mevzuatına saygı."
        ]
    }

    # Prohibited AI Systems (Article 5)
    if any(k in lowered for k in ["subliminal", "social score", "biometric categorisation", "facial recognition database", "untargeted scraping"]):
        eu_status["tier"] = "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)"
        eu_status["statutory_basis"] = "EU AI Act Madde 5(1) (Bilinçaltı manipülasyon, sosyal puanlama, izinsiz yüz tanıma veritabanları)"
        eu_status["confidence"] = "Kritik / Hukuki Danışmanlık Şart"
        eu_status["requires_expert_counsel"] = True
        eu_status["articles"] = ["EU AI Act Madde 5(1)(a)-(h)"]
        eu_status["obligations"] = [
            "Bu sistemlerin AB pazarında piyasaya sürülmesi, hizmete sunulması veya kullanılması KESİNLİKLE YASAKTIR."
        ]

    # High-Risk AI Systems (Article 6 & Annex III)
    elif any(k in lowered for k in ["medical", "health", "credit scoring", "recruitment", "hiring", "critical infrastructure", "aviation", "autonomous drive", "law enforcement"]):
        eu_status["tier"] = "Yüksek Riskli Sistem (High-Risk AI System)"
        eu_status["statutory_basis"] = "EU AI Act Madde 6 & Ek III (Kritik altyapı, sağlık, istihdam, finansal erişim sistemleri)"
        eu_status["confidence"] = "Yüksek (Ek III Kapsamına Giriyor)"
        eu_status["requires_expert_counsel"] = True
        eu_status["articles"] = ["EU AI Act Madde 6, Madde 9-15 (Risk Yönetimi, Veri Yönetişimi, İnsan Denetimi) & Ek III"]
        eu_status["obligations"] = [
            "Zorunlu Risk Yönetim Sistemi (Madde 9).",
            "Yüksek kaliteli ve önyargısız eğitim verisi yönetişimi (Madde 10).",
            "Sürekli otomatik kayıt tutma / Audit logging (Madde 12).",
            "İnsan denetimi / Human-in-the-loop mimarisi (Madde 14).",
            "CE İşareti ve AB Uygunluk Beyanı."
        ]

    # Specific Transparency Obligations (Article 50)
    elif any(k in lowered for k in ["llm", "generative", "agent", "deepfake", "synthetic", "bot", "assistant", "code generation"]):
        eu_status["tier"] = "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)"
        eu_status["statutory_basis"] = "EU AI Act Madde 50 (İnsanlarla etkileşime giren ve içerik üreten yapay zeka)"
        eu_status["confidence"] = "Doğrulanmış (Üretken ve Otonom Sistemler)"
        eu_status["requires_expert_counsel"] = False
        eu_status["articles"] = ["EU AI Act Madde 50(1) ve 50(2)"]
        eu_status["obligations"] = [
            "Kullanıcıya yapay zeka sistemiyle etkileşimde olduğunun açıkça bildirilmesi (Madde 50(1)).",
            "Yapay zeka tarafından üretilen kod, metin veya medyanın makine tarafından okunabilir formatta etiketlenmesi (Madde 50(2)).",
            "AB Telif Hakkı Direktifi (2019/790) Madde 4 kapsamındaki Text and Data Mining (TDM) hak sahiplerinin opt-out taleplerine uyum."
        ]

    # 2. GDPR / KVKK Veri Koruma Yükümlülükleri
    gdpr_status = []
    if any(k in lowered for k in ["user data", "personal", "identity", "email", "tracking", "telemetry"]):
        gdpr_status.append({
            "topic": "Kişisel Verilerin İşlenmesi",
            "statutory_basis": "GDPR Madde 5 (İlkeler) & Madde 6 (Hukuki Sebep)",
            "requirement": "Veri minimizasyonu, açık rıza veya meşru menfaat değerlendirmesi zorunludur."
        })
    if any(k in lowered for k in ["code", "repository", "proprietary", "secret", "financial", "confidential"]):
        gdpr_status.append({
            "topic": "Ticari Sır & Üçüncü Taraf Veri Güvenliği",
            "statutory_basis": "GDPR Madde 32 (İşleme Güvenliği) & AB Ticari Sırlar Direktifi (2016/943)",
            "requirement": "Fikri mülkiyet içeren kodların harici LLM API'lerine sızmasını önleyen Zero Data Retention (ZDR) anlaşmaları veya yerel (on-prem) SLM modelleri zorunludur."
        })
    if not gdpr_status:
        gdpr_status.append({
            "topic": "Genel Veri Güvenliği",
            "statutory_basis": "GDPR Madde 25 (Data Protection by Design)",
            "requirement": "Varsayılan olarak veri koruma ve standart şifreleme önlemleri yeterlidir."
        })

    # 3. Açık Kaynak Lisans Uyumluluğu
    licensing_framework = [
        {
            "category": "Permissive (MIT, Apache 2.0, BSD-3)",
            "risk_level": "Düşük Ticari Risk",
            "legal_rule": "Ticari kapalı kod ürünlerde kullanılabilir; telif ve lisans bildirim metninin korunması şarttır (Apache 2.0 patent koruma şartı içerir)."
        },
        {
            "category": "Copyleft Riski (GPLv3, AGPLv3)",
            "risk_level": "Kritik Fikri Mülkiyet Riski",
            "legal_rule": "GPLv3 kodları içeren bileşenler ticari kapalı kaynak projelere statik bağlanırsa, tüm projenin açık kaynak yapılmasını zorunlu kılabilir (Viral etki). AST seviyesinde engellenmelidir."
        }
    ]

    return {
        "domain": domain_keywords,
        "eu_ai_act": eu_status,
        "gdpr_kvkk": gdpr_status,
        "licensing": licensing_framework,
        "statutory_disclaimer": "Bu tarama resmi mevzuat maddeleri üzerinden teknik ön inceleme sunar; Baro üyesi bir patent veya bilişim avukatının resmi mütalaası yerine geçmez."
    }

def main():
    parser = argparse.ArgumentParser(description="Statutory Compliance Screener for Frontier Innovator.")
    parser.add_argument("domain", help="Technology or domain description to evaluate")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚖️ MADDE BAZLI MEVZUAT & REGÜLASYON DENETİMİ: '{args.domain}'")
    print(f"=======================================================\n")

    res = evaluate_compliance(args.domain)
    ai = res["eu_ai_act"]
    print(f"🇪🇺 EU AI Act Seviyesi      : {ai['tier']}")
    print(f"   Mevzuat Maddesi         : {ai['statutory_basis']}")
    print(f"   Güven & Uzmanlık Durumu : {ai['confidence']}")
    print("   Zorunlu Yasal Yükümlülükler:")
    for ob in ai["obligations"]:
        print(f"     - {ob}")

    print("\n🔒 GDPR / KVKK Veri Egemenliği:")
    for g in res["gdpr_kvkk"]:
        print(f"   - [{g['topic']}] ({g['statutory_basis']}): {g['requirement']}")

    print("\n📜 Açık Kaynak Lisans Çerçevesi:")
    for lic in res["licensing"]:
        print(f"   - [{lic['category']}] ({lic['risk_level']}): {lic['legal_rule']}")

    print(f"\n⚠️ Yasal Uyarı: {res['statutory_disclaimer']}")

if __name__ == "__main__":
    main()
