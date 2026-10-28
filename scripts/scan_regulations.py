#!/usr/bin/env python3
"""
Intended-Purpose-Aware Statutory Compliance Screener for Zobar Skill.
Evaluates regulatory risk tiers based on codified statutory criteria and intended purpose:
- EU AI Act (Regulation (EU) 2024/1689)
- Medical Device Regulation (Regulation (EU) 2017/745 - MDR Rule 11)
- GDPR (Regulation (EU) 2016/679) & EDPB Guidelines on Automated Decision-Making

DISCLAIMER:
Provides automated technical issue-spotting and statutory mapping based on European Union
regulations. It does not constitute formal legal counsel. Intended purpose and clinical/market
context determine definitive compliance classification.
"""

import sys
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def evaluate_compliance(domain_keywords: str):
    """
    Evaluates regulatory compliance incorporating intended purpose, clinical risk,
    and statutory exemptions (e.g. Article 2(8) research/internal development exemption).
    """
    lowered = domain_keywords.lower()

    # 1. Prohibited AI Practices (Article 5)
    # Strictly prohibited by law regardless of intent
    if any(k in lowered for k in ["subliminal", "social score", "untargeted facial", "facial recognition database", "predictive policing on individuals"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1) (Bilinçaltı manipülasyon, sosyal puanlama veya izinsiz biyometrik veri kazıma)",
                "official_precedent": "EU AI Act 2024/1689 Article 5(1)(a)-(h)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Sistemin AB pazarında piyasaya sürülmesi, hizmete sunulması veya kullanımı kesin olarak yasaktır (Madde 5).",
                    "İdari yaptırım: Küresel cironun %7'sine veya 35 milyon Avro'ya kadar para cezası (Madde 99)."
                ]
            },
            "data_privacy": ["Kritik Gizlilik Riski: Özel nitelikli biyometrik verilerin işlenmesi (GDPR Madde 9)."],
            "statutory_disclaimer": "Sistem AB genelinde yasaklanmış uygulamalar kapsamındadır; derhal hukuki inceleme başlatılmalıdır."
        }

    # 2. Healthcare & Medical Systems — Intended Purpose Discrimination
    # Crucial distinction: Administrative/Hospital Management vs Clinical Decision Support
    if any(k in lowered for k in ["medical", "health", "patient", "clinical", "hospital"]):
        if any(k in lowered for k in ["administrative", "scheduling", "billing", "inventory", "shift"]):
            # Administrative hospital software is NOT High-Risk under AI Act
            return {
                "domain": domain_keywords,
                "eu_ai_act": {
                    "tier": "Minimal / Düşük Risk (İdari Sağlık Yazılımı)",
                    "statutory_basis": "EU AI Act Recital 34 & MDR (AB) 2017/745 Kapsam Dışı (İdari amaçlı yazılımlar tıbbi cihaz veya yüksek risk sayılmaz)",
                    "official_precedent": "MDR (EU) 2017/745 Annex VIII Rule 11 (Klinik karar içermeyen idari sistem muafiyeti)",
                    "confidence": "Yüksek (Kullanım Amacı İdari/Yönetimsel)",
                    "requires_expert_counsel": False,
                    "obligations": [
                        "AI Act kapsamında yüksek risk yükümlülüklerine tabi değildir.",
                        "GDPR Madde 6 ve Madde 9 uyarınca hasta randevu ve kimlik verilerinin korunması yeterlidir."
                    ]
                },
                "data_privacy": ["GDPR Madde 6 & 9: İdari hasta verilerinin yetkisiz erişime karşı şifrelenmesi."],
                "statutory_disclaimer": "Sistemin kullanım amacı idari/yönetimsel olduğundan yüksek risk sınıfına girmez."
            }
        else:
            # Clinical diagnosis, physiological telemetry, or patient treatment recommendations
            return {
                "domain": domain_keywords,
                "eu_ai_act": {
                    "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                    "statutory_basis": "EU AI Act Madde 6(1), Ek I & MDR (AB) 2017/745 Kural 11 (Teşhis ve tedavi kararlarına destek sağlayan yazılımlar)",
                    "official_precedent": "MDR (EU) 2017/745 Sınıf IIa/IIb & AI Act Annex I/III",
                    "confidence": "Yüksek (Klinik Teşhis/Karar Amacı)",
                    "requires_expert_counsel": True,
                    "obligations": [
                        "MDR Kural 11 uyarınca Onaylanmış Kuruluş (Notified Body) CE denetimi.",
                        "EU AI Act Madde 9-15: Risk yönetim sistemi, önyargısız klinik veri setleri ve sürekli loglama.",
                        "Madde 14: Hekim denetimi (Human-in-the-loop / Physician oversight) zorunluluğu."
                    ]
                },
                "data_privacy": [
                    "GDPR Madde 9: Sağlık verilerinin işlenmesinde açık rıza veya hekim sırrı hukuki dayanağı şarttır.",
                    "GDPR Madde 35: Veri Koruma Etki Değerlendirmesi (DPIA) zorunludur."
                ],
                "statutory_disclaimer": "Klinik karar ve hasta sağlığına doğrudan etkisi olan sistemler yüksek risk ve CE belgelendirmesine tabidir."
            }

    # 3. Essential Private & Public Services (Credit Scoring & Recruitment)
    elif any(k in lowered for k in ["credit score", "creditworthiness", "recruitment", "hiring evaluation", "critical infrastructure safety", "border surveillance"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 5(b) (Kredi puanlaması ve temel hizmetlere erişim)",
                "official_precedent": "EDPB Guidelines WP251 & AI Act Annex III Point 5(b)",
                "confidence": "Yüksek (Ek III Kapsamında Listelenen Alan)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Sürekli risk yönetim sistemi (Madde 9).",
                    "Ayrımcılığı önleyen eğitim ve test verisi yönetişimi (Madde 10).",
                    "Kullanıcının skorlama mantığını anlama ve itiraz etme hakkı (GDPR Madde 22 & AI Act Madde 86)."
                ]
            },
            "data_privacy": ["GDPR Madde 22: Tamamen otomatik kararlara tabi olmama hakkı."],
            "statutory_disclaimer": "Tüketici finansal erişimini etkileyen yapay zeka modelleri Ek III uyarınca yüksek risklidir."
        }

    # 4. Interactive & Generative Systems — Transparency (Article 50)
    # Natural person interaction or public-facing generative synthetic content
    elif any(k in lowered for k in ["conversational bot", "chatbot", "deepfake", "public synthetic media"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
                "statutory_basis": "EU AI Act Madde 50 (İnsanlarla doğrudan etkileşime giren yapay zeka sistemleri)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 50(1) & (2)",
                "confidence": "Doğrulanmış (Kullanıcıyla Doğrudan Etkileşim)",
                "requires_expert_counsel": False,
                "obligations": [
                    "Kullanıcıya açık ve anlaşılır şekilde bir yapay zeka ile konuştuğunun bildirilmesi (Madde 50(1)).",
                    "Üretilen sentetik medyanın makine tarafından okunabilir filigran/etiket içermesi."
                ]
            },
            "data_privacy": ["GDPR Madde 13/14: Sohbet verilerinin toplanmasına ilişkin şeffaf aydınlatma metni."],
            "statutory_disclaimer": "Doğrudan kullanıcıyla konuşan veya kamuya açık medya üreten sistemler Madde 50 şeffaflığına tabidir."
        }

    # 5. Developer Tools, Compilers, Static Analyzers (Article 2(8) Research/Dev Exemption)
    # Pure developer tooling, internal AST parsers, code linters are exempt from AI Act deployment duties
    elif any(k in lowered for k in ["ast", "parser", "compiler", "linter", "code analysis", "refactor", "static analysis"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Minimal / Düşük Risk (Geliştirici Aracı / AI Act Muafiyeti)",
                "statutory_basis": "EU AI Act Madde 2(8) & Recital 34 (Ar-Ge, test ve geliştirici araçları için muafiyet)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 2(8) (Geliştirme ve araştırma aşamasındaki yazılımlar)",
                "confidence": "Yüksek (Geliştirici Aracı / Operasyonel Karar Vermez)",
                "requires_expert_counsel": False,
                "obligations": [
                    "AI Act kapsamında özel bir yükümlülük bulunmamaktadır.",
                    "Açık kaynak lisansları (SPDX) ve ticari sır koruması geçerlidir."
                ]
            },
            "data_privacy": ["Telif Hakları Direktifi (2019/790) Madde 4: Kod analizinde lisans uyumluluğu."],
            "statutory_disclaimer": "Geliştirici araçları ve statik analizörler AI Act yüksek risk veya şeffaflık kapsamı dışındadır."
        }

    # 6. General Software & Internal Infrastructure
    else:
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Minimal / Düşük Risk (Genel Yazılım Kapsamı)",
                "statutory_basis": "EU AI Act Resmî Gerekçesi (Recital 34: Ek III ve Madde 5 dışındaki standart sistemler)",
                "official_precedent": "Regulation (EU) 2024/1689 Recital 34",
                "confidence": "Yüksek (Özel bir AI Act yükümlülüğü tetiklenmedi)",
                "requires_expert_counsel": False,
                "obligations": [
                    "AI Act kapsamında özel bir zorunluluk bulunmamaktadır; genel AB tüketici ve veri koruma mevzuatına tabidir."
                ]
            },
            "data_privacy": ["GDPR Madde 25: Varsayılan olarak veri koruma (Data Protection by Design)."],
            "statutory_disclaimer": "Sistem doğrudan AI Act yüksek risk sınıflarına girmemektedir."
        }

def main():
    parser = argparse.ArgumentParser(description="Intended-Purpose-Aware Statutory Compliance Screener.")
    parser.add_argument("domain", help="Technology or domain description to evaluate")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚖️ KULLANIM AMACI ODAKLI MEVZUAT DENETİMİ: '{args.domain}'")
    print(f"=======================================================\n")

    res = evaluate_compliance(args.domain)
    ai = res["eu_ai_act"]
    print(f"🇪🇺 EU AI Act Seviyesi      : {ai['tier']}")
    print(f"   Mevzuat Maddesi         : {ai['statutory_basis']}")
    print(f"   Resmi Emsal / Dayanak   : {ai['official_precedent']}")
    print(f"   Güven Derecesi          : {ai['confidence']}")
    print(f"   Hukuki Mütalaa Gerekli  : {'Evet (Kritik)' if ai['requires_expert_counsel'] else 'Hayır'}")
    print("   Zorunlu Yasal Yükümlülükler:")
    for ob in ai["obligations"]:
        print(f"     - {ob}")

    print("\n🔒 Veri Güvenliği (GDPR):")
    for g in res["data_privacy"]:
        print(f"   - {g}")

    print(f"\n⚠️ Yasal Not: {res['statutory_disclaimer']}")

if __name__ == "__main__":
    main()
