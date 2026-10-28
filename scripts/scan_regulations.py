#!/usr/bin/env python3
"""
Statutory Regulatory & Compliance Screener for Zobar Skill.
Provides preliminary screening against the official text of Regulation (EU) 2024/1689
(EU AI Act) and Regulation (EU) 2016/679 (GDPR).

DISCLAIMER:
This tool provides preliminary automated issue-spotting based on codified statutory criteria.
It DOES NOT provide legal counsel. Regulatory risk depends on intended purpose, deployment
context, and technical implementation.
"""

import sys
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def evaluate_compliance(domain_keywords: str):
    """
    Evaluates statutory compliance triggers against specific EU AI Act articles.
    Categorizes systems with explicit statutory basis, confidence rating, and counsel requirements.
    """
    lowered = domain_keywords.lower()

    # 1. Prohibited AI Practices (Article 5)
    # Strictly defined practices: subliminal manipulation, exploitation of vulnerabilities,
    # social scoring, untargeted scraping of facial images, emotion recognition at workplace/school.
    if any(k in lowered for k in ["subliminal", "social scor", "untargeted facial", "facial recognition database", "predictive policing on individuals"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1) (Bilinçaltı teknikler, sosyal puanlama veya izinsiz biyometrik veri kazıma)",
                "confidence": "Yüksek (Madde 5 Kapsamındaki Yasaklı Alan)",
                "requires_expert_counsel": True,
                "articles": ["Regulation (EU) 2024/1689 Article 5(1)"],
                "obligations": [
                    "Sistemin AB pazarında piyasaya sürülmesi, hizmete sunulması veya kullanımı kesin olarak yasaktır.",
                    "Yasal ceza riski: Küresel cironun %7'sine veya 35 milyon Avro'ya kadar idari para cezası (Madde 99)."
                ]
            },
            "data_privacy": ["Kritik Gizlilik Riski: Özel nitelikli biyometrik verilerin işlenmesi (GDPR Madde 9)."],
            "statutory_disclaimer": "Bu sistem AB mevzuatı gereği yasaklı kategoride değerlendirilmiştir. Hukuki mütalaa alınması zorunludur."
        }

    # 2. High-Risk AI Systems (Article 6 & Annex III)
    # Critical infrastructure, educational assessment, employment/hiring, access to essential services (credit),
    # law enforcement, migration, justice, and safety components of regulated products (medical devices, aviation).
    elif any(k in lowered for k in ["medical device", "medical diagnostic", "patient telemetry", "credit score", "creditworthiness", "recruitment", "hiring evaluation", "critical infrastructure safety", "border surveillance"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III (Sağlık, istihdam, finansal erişim ve kritik altyapı)",
                "confidence": "Yüksek (Ek III Kapsamında Belirtilen Alan)",
                "requires_expert_counsel": True,
                "articles": ["Regulation (EU) 2024/1689 Article 6, Annex III, Articles 9-15"],
                "obligations": [
                    "Sürekli risk yönetim sisteminin kurulması (Madde 9).",
                    "Eğitim, geçerleme ve test veri setlerinin yönetişimi ve önyargı denetimi (Madde 10).",
                    "Teknik dokümantasyon ve AB uygunluk beyanı (Madde 11 & 18).",
                    "Otomatik kayıt tutma (logging) mimarisi (Madde 12).",
                    "Kullanıcıya şeffaflık ve kullanım talimatları sağlanması (Madde 13).",
                    "İnsan denetimi (Human-in-the-loop) arayüzlerinin inşası (Madde 14).",
                    "Siber güvenlik ve sağlamlık (Madde 15)."
                ]
            },
            "data_privacy": [
                "GDPR Madde 9: Sağlık ve genetik verilerin işlenmesinde açık rıza veya kamu sağlığı hukuki dayanağı şarttır.",
                "GDPR Madde 35: Veri Koruma Etki Değerlendirmesi (DPIA) zorunludur."
            ],
            "statutory_disclaimer": "Sistem Ek III kapsamında yüksek risklidir; bağımsız bir uygunluk değerlendirme kuruluşu veya CE işaretleme denetimi gerektirir."
        }

    # 3. Transparency Obligations for Generative & Interactive AI (Article 50)
    # AI systems intended to interact directly with humans, generative text/code/media, deepfakes.
    elif any(k in lowered for k in ["llm", "generative", "conversational bot", "chatbot", "synthetic code", "code generation assistant", "deepfake"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
                "statutory_basis": "EU AI Act Madde 50 (İnsanlarla etkileşime giren ve yapay içerik üreten sistemler)",
                "confidence": "Doğrulanmış (Etkileşimli / Üretken Model)",
                "requires_expert_counsel": False,
                "articles": ["Regulation (EU) 2024/1689 Article 50(1) & 50(2)"],
                "obligations": [
                    "İnsan kullanıcıya bir yapay zeka sistemiyle etkileşime girdiğinin açıkça bildirilmesi (Madde 50(1)).",
                    "Üretilen sentetik çıktıların makine tarafından okunabilir formatta 'yapay zeka üretimi' olarak etiketlenmesi (Madde 50(2)).",
                    "Telif Hakkı Direktifi (2019/790) Madde 4 kapsamındaki Text & Data Mining (TDM) hak sahiplerinin opt-out haklarına riayet."
                ]
            },
            "data_privacy": [
                "Kod ve veri tabanı girdilerinde ticari sırların üçüncü taraf LLM sağlayıcılarına sızmasını önleyen ZDR (Zero Data Retention) mimarisi."
            ],
            "statutory_disclaimer": "Sistem genel şeffaflık yükümlülüklerine tabidir; yüksek riskli Ek III alanlarına entegre edilmediği sürece CE uygunluk denetimi gerektirmez."
        }

    # 4. Minimal / General Risk Systems
    # Standard development tools, compilers, static analyzers, games, internal utilities.
    else:
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
                "statutory_basis": "EU AI Act Resmî Gerekçesi (Recital 34: Ek III ve Madde 5 kapsamı dışındaki genel sistemler)",
                "confidence": "Yüksek (Özel bir AI Act yükümlülüğü tetiklenmedi)",
                "requires_expert_counsel": False,
                "articles": ["Regulation (EU) 2024/1689 Recital 34"],
                "obligations": [
                    "AI Act kapsamında özel bir zorunluluk bulunmamaktadır; genel AB tüketici ve ürün güvenliği mevzuatına tabidir.",
                    "İsteğe bağlı olarak güvenilir yapay zeka davranış kurallarına (Codes of Conduct) uyum teşvik edilir."
                ]
            },
            "data_privacy": [
                "GDPR Madde 25: Varsayılan olarak veri koruma (Data Protection by Design) ve standart şifreleme önlemleri."
            ],
            "statutory_disclaimer": "Sistem doğrudan AI Act risk sınıflarına girmemektedir; genel veri güvenliği kuralları geçerlidir."
        }

def main():
    parser = argparse.ArgumentParser(description="Statutory Compliance Screener for Zobar Skill.")
    parser.add_argument("domain", help="Technology or domain description to evaluate")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚖️ MADDE BAZLI MEVZUAT & REGÜLASYON DENETİMİ: '{args.domain}'")
    print(f"=======================================================\n")

    res = evaluate_compliance(args.domain)
    ai = res["eu_ai_act"]
    print(f"🇪🇺 EU AI Act Seviyesi      : {ai['tier']}")
    print(f"   Mevzuat Maddesi         : {ai['statutory_basis']}")
    print(f"   Güven Derecesi          : {ai['confidence']}")
    print(f"   Hukuki Mütalaa Gerekli  : {'Evet (Kritik)' if ai['requires_expert_counsel'] else 'Hayır'}")
    print("   Zorunlu Yasal Yükümlülükler:")
    for ob in ai["obligations"]:
        print(f"     - {ob}")

    print("\n🔒 Veri Güvenliği (GDPR / KVKK):")
    for g in res["data_privacy"]:
        print(f"   - {g}")

    print(f"\n⚠️ Yasal Not: {res['statutory_disclaimer']}")

if __name__ == "__main__":
    main()
