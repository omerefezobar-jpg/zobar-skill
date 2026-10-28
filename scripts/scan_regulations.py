#!/usr/bin/env python3
"""
Statutory Intended-Purpose & Context-Aware Regulatory Screener for Zobar Skill (Phase 4).
Codifies the European Union Artificial Intelligence Act (Regulation (EU) 2024/1689),
Medical Device Regulation (Regulation (EU) 2017/745 - MDR Annex VIII Rule 11),
and General Data Protection Regulation (Regulation (EU) 2016/679 - GDPR Articles 6, 9, 22).

DISCLAIMER:
Provides automated technical issue-spotting and codified statutory mapping.
Intended purpose and operational deployment boundaries dictate definitive legal status.
Where high risk or prohibitions arise, engagement with qualified regulatory counsel is mandatory.
"""

import sys
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def evaluate_compliance(domain_keywords: str):
    """
    Evaluates regulatory compliance incorporating intended purpose, sector classification,
    and codified statutory exemptions (e.g. Article 2(8) R&D exemption).
    """
    lowered = domain_keywords.lower()

    # =========================================================================
    # 1. PROHIBITED AI PRACTICES (Regulation (EU) 2024/1689 Article 5)
    # =========================================================================

    # 1a. Subliminal Manipulation (Article 5(1)(a))
    if any(k in lowered for k in ["subliminal", "manipulation for harm", "subconscious distortion"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1)(a) (Bilinçaltı manipülasyon ve davranış çarpıtma)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 5(1)(a)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Sistemin AB pazarında piyasaya sürülmesi, hizmete sunulması veya kullanımı kesin olarak yasaktır (Madde 5).",
                    "İdari yaptırım: Küresel cironun %7'sine veya 35 milyon Avro'ya kadar para cezası (Madde 99)."
                ]
            },
            "data_privacy": ["GDPR Madde 5(1)(a): Hukuka, dürüstlüğe ve şeffaflığa aykırı veri işleme yasağı."],
            "statutory_disclaimer": "Sistem AB pazarında mutlak olarak yasaklanan kategoridedir; derhal durdurulmalıdır."
        }

    # 1b. Social Scoring (Article 5(1)(c))
    if any(k in lowered for k in ["social scoring", "social score", "vatandaş puanlama"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1)(c) (Sosyal puanlama yasağı)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 5(1)(c)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Bireylerin sosyal davranışlarına veya kişilik özelliklerine dayalı puanlama yapılması yasaktır.",
                    "Madde 99 kapsamında en üst sınır olan 35 milyon Avro veya %7 küresel ciro cezası uygulanır."
                ]
            },
            "data_privacy": ["GDPR Madde 9 ve Madde 22: Özel nitelikli kişisel profilleme yasağı."],
            "statutory_disclaimer": "Sosyal puanlama sistemleri kamu veya özel aktörler tarafından AB'de kullanılamaz."
        }

    # 1c. Individual Predictive Policing (Article 5(1)(d))
    if any(k in lowered for k in ["predictive policing", "recidivism assessment", "crime prediction on individual"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1)(d) (Bireysel suç ve tekerrür tahmini yasağı)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 5(1)(d)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Bireylerin kişilik özelliklerine veya geçmişine bakarak suç işleme olasılığı kestirimi yasaktır."
                ]
            },
            "data_privacy": ["GDPR Madde 10: Ceza mahkumiyeti ve suçlara ilişkin verilerin işlenmesi yasağı."],
            "statutory_disclaimer": "Bireysel suç tahmini algoritmaları AB AI Act Madde 5(1)(d) altında yasaktır."
        }

    # 1d. Untargeted Biometric Facial Scraping (Article 5(1)(e))
    if any(k in lowered for k in ["untargeted facial", "facial recognition database", "cctv scraping"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1)(e) (İnternet veya CCTV'den hedefsiz yüz kazıma yasağı)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 5(1)(e)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Yüz tanıma veri tabanı oluşturmak için internetten veya kamera kayıtlarından görsel çekmek yasaktır."
                ]
            },
            "data_privacy": ["GDPR Madde 9: Biyometrik verilerin rızasız ve amaçsız toplanması ihlali."],
            "statutory_disclaimer": "Hedefsiz yüz kazıma veri tabanı oluşturmak kesinlikle yasaklanmıştır."
        }

    # 1e. Emotion Recognition in Workplace / Education (Article 5(1)(f))
    if any(k in lowered for k in ["workplace emotion", "emotion recognition in school", "işyeri duygu analizi", "student emotion"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1)(f) (İşyeri ve eğitim kurumlarında duygu tanıma yasağı)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 5(1)(f)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Çalışanların veya öğrencilerin duygusal durumlarını tespit etmeye yönelik sistemler yasaktır."
                ]
            },
            "data_privacy": ["GDPR Madde 9: Özel nitelikli biyometrik/psikolojik veri işleme yasağı."],
            "statutory_disclaimer": "İşyerinde ve okullarda duygu analizi AB genelinde yasaktır."
        }

    # =========================================================================
    # 2. HEALTHCARE & MEDICAL SYSTEMS (MDR 2017/745 & AI ACT ARTICLE 6(1))
    # =========================================================================
    if any(k in lowered for k in ["medical", "health", "patient", "clinical", "hospital", "radiology"]):
        # Exclusion: Administrative Hospital Systems
        if any(k in lowered for k in ["administrative", "scheduling", "billing", "inventory", "shift"]):
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
                        "GDPR Madde 6 uyarınca hasta randevu ve idari verilerin korunması yeterlidir."
                    ]
                },
                "data_privacy": ["GDPR Madde 6: Randevu yönetimi için sözleşmesel veri işleme."],
                "statutory_disclaimer": "Sistem idari kullanım amacı taşıdığından MDR Kural 11 ve AI Act yüksek risk dışındadır."
            }
        else:
            # Clinical Decision Support / Diagnostic Imaging
            return {
                "domain": domain_keywords,
                "eu_ai_act": {
                    "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                    "statutory_basis": "EU AI Act Madde 6(1), Ek I & MDR (AB) 2017/745 Kural 11 (Teşhis ve tedavi kararlarına destek sağlayan yazılımlar)",
                    "official_precedent": "MDR (EU) 2017/745 Annex VIII Rule 11 & Regulation (EU) 2024/1689 Article 6(1)",
                    "confidence": "Yüksek (Klinik Teşhis/Karar Amacı)",
                    "requires_expert_counsel": True,
                    "obligations": [
                        "MDR Kural 11 uyarınca Onaylanmış Kuruluş (Notified Body) CE denetimi zorunludur.",
                        "EU AI Act Madde 9-15: Risk yönetim sistemi, klinik veri setleri ve sürekli loglama.",
                        "Madde 14: Hekim gözetimi (Physician oversight) zorunluluğu."
                    ]
                },
                "data_privacy": [
                    "GDPR Madde 9: Sağlık verilerinin işlenmesinde açık rıza veya hekim sırrı hukuki dayanağı şarttır.",
                    "GDPR Madde 35: Veri Koruma Etki Değerlendirmesi (DPIA) zorunludur."
                ],
                "statutory_disclaimer": "Klinik karar ve hasta sağlığına doğrudan etkisi olan sistemler MDR ve AI Act yüksek riskine tabidir."
            }

    # =========================================================================
    # 3. HIGH-RISK AI SYSTEMS (ANNEX III & ANNEX I)
    # =========================================================================

    # 3a. Employment & HR Recruitment (Annex III Point 4(a))
    if any(k in lowered for k in ["recruitment", "hiring", "resume screening", "cv screening", "worker management"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 4(a) (İstihdam ve işe alım kararları)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex III Point 4(a)",
                "confidence": "Yüksek (Ek III Kapsamında Listelenen Alan)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Madde 10: İşe alım algoritmalarında cinsiyet, ırk ve yaş ayrımcılığına karşı veri seti denetimi.",
                    "Madde 13/14: İnsan kaynakları yöneticisinin algoritmik kararı geçersiz kılma yetkisi (Human oversight)."
                ]
            },
            "data_privacy": ["GDPR Madde 22: Otomatik filtreleme kararlarında adayın itiraz hakkı."],
            "statutory_disclaimer": "İşe alım ve özgeçmiş eleme araçları AI Act Ek III uyarınca yüksek risklidir."
        }

    # 3b. Education & Vocational Assessment (Annex III Point 3(a))
    if any(k in lowered for k in ["exam grading", "student assessment", "educational testing", "admission evaluation"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 3(a) (Eğitimde değerlendirme ve sınav puanlama)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex III Point 3(a)",
                "confidence": "Yüksek (Ek III Kapsamında Listelenen Alan)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Sınav sonuçlarını veya kabul kararlarını belirleyen yapay zeka modelleri şeffaf ve denetlenebilir olmalıdır."
                ]
            },
            "data_privacy": ["GDPR Madde 8/22: Öğrenci verilerinin korunması ve otomatik karar itirazı."],
            "statutory_disclaimer": "Eğitim ve sınav değerlendirme yazılımları Ek III kapsamında yüksek risklidir."
        }

    # 3c. Critical Infrastructure Safety Components (Annex III Point 2)
    if any(k in lowered for k in ["critical infrastructure", "power grid", "water management scada", "energy grid safety"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 2 (Kritik altyapı güvenlik bileşenleri)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex III Point 2",
                "confidence": "Yüksek (Ek III Kritik Altyapı)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Elektrik, su veya gaz altyapılarında fiziksel güvenlik ve kesintisiz siber direnç (Madde 15)."
                ]
            },
            "data_privacy": ["NIS2 Direktifi (EU 2022/2555) ile uyumlu siber güvenlik protokolleri."],
            "statutory_disclaimer": "Kritik altyapı güvenlik sistemleri AI Act Ek III kapsamında yüksek risklidir."
        }

    # 3d. Autonomous Vehicles & Machinery Safety Components (Annex I)
    if any(k in lowered for k in ["autonomous vehicle", "braking safety", "vehicle telemetry", "automotive safety component"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(1) ve Ek I (Makine ve Taşıt Güvenlik Bileşenleri)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex I & Machinery Regulation (EU) 2023/1230",
                "confidence": "Yüksek (Ulaşım ve Taşıt Güvenlik Bileşeni)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Tip onayı (Type-approval) ve üçüncü taraf bağımsız güvenlik sertifikasyonu zorunludur."
                ]
            },
            "data_privacy": ["GDPR Madde 25: Taşıt telemetrisi ve konum verilerinin anonimleştirilmesi."],
            "statutory_disclaimer": "Otonom araç güvenlik bileşenleri Ek I uyarınca yüksek risk sınıfındadır."
        }

    # 3e. Credit Scoring & Essential Financial Services (Annex III Point 5(b))
    if any(k in lowered for k in ["credit score", "creditworthiness", "financial risk consumer loan"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 5(b) (Kredi puanlaması ve temel hizmetlere erişim)",
                "official_precedent": "EDPB Guidelines WP251 & Regulation (EU) 2024/1689 Annex III Point 5(b)",
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

    # =========================================================================
    # 4. TRANSPARENCY OBLIGATIONS (ARTICLE 50)
    # =========================================================================

    # 4a. Conversational Chatbots interacting with humans (Article 50(1))
    if any(k in lowered for k in ["conversational bot", "chatbot", "chat bot", "customer service chatbot"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
                "statutory_basis": "EU AI Act Madde 50(1) (İnsanlarla doğrudan etkileşime giren yapay zeka sistemleri)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 50(1)",
                "confidence": "Doğrulanmış (Kullanıcıyla Doğrudan Etkileşim)",
                "requires_expert_counsel": False,
                "obligations": [
                    "Kullanıcıya açık ve anlaşılır şekilde bir yapay zeka ile konuştuğunun bildirilmesi (Madde 50(1)).",
                    "Konuşma geçmişi toplanıyorsa aydınlatma yapılması."
                ]
            },
            "data_privacy": ["GDPR Madde 13/14: Sohbet verilerinin toplanmasına ilişkin şeffaf aydınlatma metni."],
            "statutory_disclaimer": "Doğrudan kullanıcıyla konuşan sistemler Madde 50(1) şeffaflığına tabidir."
        }

    # 4b. Synthetic Media & Deepfakes (Article 50(2))
    if any(k in lowered for k in ["deepfake", "public synthetic media", "synthetic voice", "synthetic video generation"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
                "statutory_basis": "EU AI Act Madde 50(2) (Sentetik görsel, ses ve video içeriği işaretleme)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 50(2)",
                "confidence": "Doğrulanmış (Sentetik Medya Üretimi)",
                "requires_expert_counsel": False,
                "obligations": [
                    "Üretilen sentetik medyanın makine tarafından okunabilir filigran (machine-readable watermark) içermesi zorunludur."
                ]
            },
            "data_privacy": ["GDPR Madde 6: Kişi taklidi içeren ses/görüntülerin işlenmesinde hukuka uygunluk."],
            "statutory_disclaimer": "Sentetik medya üreticileri Madde 50(2) uyarınca filigranlama zorunluluğuna tabidir."
        }

    # =========================================================================
    # 5. DEVELOPER TOOLS & R&D EXEMPTION (ARTICLE 2(8))
    # =========================================================================
    if any(k in lowered for k in ["ast", "parser", "compiler", "linter", "code analysis", "refactor", "static analysis", "git workflow"]):
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

    # =========================================================================
    # 6. GENERAL SOFTWARE & MINIMAL RISK (RECITAL 34)
    # =========================================================================
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
        "statutory_disclaimer": "Sistem doğrudan AI Act yüksek risk veya yasaklı sınıflarına girmemektedir."
    }

def main():
    parser = argparse.ArgumentParser(description="Statutory Intended-Purpose & Context-Aware Regulatory Screener.")
    parser.add_argument("domain", help="Technology or domain description to evaluate")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚖️ KULLANIM AMACI VE MADDE BAZLI MEVZUAT DENETİMİ: '{args.domain}'")
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
