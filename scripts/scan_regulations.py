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

    # 1b. Social Scoring & Behavioral Profiling (Article 5(1)(c))
    if any(k in lowered for k in [
        "social scoring", "social score", "vatandaş puanlama",
        "behavioral scoring", "citizen scoring", "ranking citizens",
        "social credit", "davranış puanlama"
    ]):
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

    # 1f. Biometric Categorization for Sensitive Beliefs/Orientation (Article 5(1)(g))
    if any(k in lowered for k in ["biometric categorization", "political orientation", "sexual orientation", "religious belief discrimination"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1)(g) (Hassas nitelikleri çıkaran biyometrik kategorizasyon yasağı)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 5(1)(g)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Kişilerin siyasi, dini, felsefi inançlarını veya cinsel yönelimlerini biyometrik verilerden çıkaran sistemler mutlak olarak yasaktır."
                ]
            },
            "data_privacy": ["GDPR Madde 9: Özel nitelikli kişisel verilerin işlenmesi yasağı."],
            "statutory_disclaimer": "Hassas biyometrik kategorizasyon Madde 5(1)(g) altında kesin olarak yasaktır."
        }

    # 1g. Real-Time Remote Biometric Identification in Public Spaces (Article 5(1)(h))
    if any(k in lowered for k in [
        "realtime remote biometric identification", "remote biometric in public",
        "public facial tracking", "biometric identification in public",
        "mass surveillance camera", "pedestrian faces", "police databases"
    ]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklanmış Yapay Zeka Uygulaması (Prohibited AI Practice)",
                "statutory_basis": "EU AI Act Madde 5(1)(h) (Kamusal alanda gerçek zamanlı uzaktan biyometrik kimlik tespiti yasağı)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 5(1)(h)",
                "confidence": "Kritik / Kesin Yasak",
                "requires_expert_counsel": True,
                "obligations": [
                    "Kolluk kuvvetleri dahil kamusal alanda gerçek zamanlı yüz/biyometri tanıma çok katı adli istisnalar haricinde yasaktır."
                ]
            },
            "data_privacy": ["GDPR Madde 9 ve Madde 10: Kamu gözetimi ve kitlesel biyometri işleme yasağı."],
            "statutory_disclaimer": "Kamusal alanda gerçek zamanlı uzaktan biyometrik takip genel kural olarak yasaktır."
        }

    # 1h. Circumvention of Technological Protection Measures & DRM Piracy (DMCA 1201(a)(1) & Directive 2001/29/EC)
    if any(k in lowered for k in [
        "drm bypass", "anti-tamper", "denuvo", "software crack",
        "game piracy", "license crack", "telif koruma bypass", "drm cracker"
    ]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasaklı / Yasa Dışı İhlal (Prohibited Copyright Infringement & DRM Circumvention)",
                "statutory_basis": "DMCA 17 U.S.C. § 1201(a)(1) & EU InfoSoc Direktifi (2001/29/EC) Madde 6",
                "official_precedent": "Directive 2001/29/EC Article 6 & 17 U.S.C. § 1201(a)(1)",
                "confidence": "Kritik / Yasa Dışı",
                "requires_expert_counsel": True,
                "obligations": [
                    "Yazılım ve oyunların teknolojik koruma önlemlerini kırmak ve telifli kodları izinsiz bypass etmek yasa dışıdır.",
                    "Fikri mülkiyet ihlali nedeniyle cezai ve hukuki tazminat sorumluluğu doğar."
                ]
            },
            "data_privacy": ["Telif Hakları Mevzuatı: Fikri mülkiyet ihlali ve korsanlık yasağı."],
            "statutory_disclaimer": "Korsanlık veya DRM korumalarını aşma amaçlı araçlar hukuken yasaklanmıştır."
        }

    # =========================================================================
    # 2. HEALTHCARE & MEDICAL SYSTEMS (MDR 2017/745 & AI ACT ARTICLE 6(1))
    # =========================================================================
    if any(k in lowered for k in ["medical", "health", "patient", "clinical", "hospital", "radiology", "mammography", "cancer", "ecg", "cardiology"]):
        # Exclusion 1: Insurance Underwriting (Evaluated under Annex III Point 5(a))
        if any(k in lowered for k in ["insurance", "underwriting", "policy eligibility"]):
            pass
        # Exclusion 2: Administrative Hospital Systems
        elif any(k in lowered for k in ["administrative", "scheduling", "billing", "inventory", "shift"]):
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
    if any(k in lowered for k in [
        "critical infrastructure", "power grid", "water management scada",
        "energy grid safety", "water infrastructure", "dam management",
        "flood control", "scada", "autonomous drone", "drone dispatch",
        "avionics", "flight navigation", "autopilot", "aerospace"
    ]):
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

    # 3f. Workplace Algorithmic Dismissal & Task Monitoring (Annex III Point 4(b))
    if any(k in lowered for k in ["workplace algorithmic termination", "task allocation", "performance dismissal decision", "worker task allocation"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 4(b) (Çalışan görev dağılımı, fesih ve performans izleme)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex III Point 4(b)",
                "confidence": "Yüksek (Ek III İstihdam ve Çalışma İlişkileri)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Madde 10: Performans değerlendirme modellerinde ayrımcılığı engelleyen adil veri yönetişimi.",
                    "Madde 14: İnsan denetimi (Human oversight); fesih ve disiplin kararlarının yalnızca algoritmaya dayandırılamaması.",
                    "Madde 26: Çalışan temsilcilerine ve işyeri sendikalarına sistemin kullanımı hakkında önceden bildirim yapılması."
                ]
            },
            "data_privacy": ["GDPR Madde 22: Çalışanların otomatik işten çıkarma kararlarına karşı insan incelemesi talep hakkı."],
            "statutory_disclaimer": "Çalışanların performans takibi ve işten çıkarma süreçlerine müdahil sistemler Ek III uyarınca yüksek risklidir."
        }

    # 3g. Life and Health Insurance Underwriting Risk (Annex III Point 5(a))
    if any(k in lowered for k in ["life health insurance", "insurance underwriting risk", "policy eligibility determination"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 5(a) (Hayat ve sağlık sigortası risk değerlendirmesi ve prim fiyatlandırması)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex III Point 5(a)",
                "confidence": "Yüksek (Ek III Temel Özel Hizmetlere Erişim)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Madde 9: Aktüeryal risk modellerinin sistematik yanlılık ve haksız dışlama denetimi.",
                    "Madde 13: Sigortalıya prim artışı veya poliçe reddi gerekçelerinin şeffaf açıklaması."
                ]
            },
            "data_privacy": ["GDPR Madde 9: Sağlık ve genetik verilerin sigorta primleme amacıyla işlenmesinde yasal dayanak zorunluluğu."],
            "statutory_disclaimer": "Hayat ve sağlık sigortası risk derecelendirme yazılımları Ek III kapsamında yüksek risklidir."
        }

    # 3h. Emergency 112 Dispatch Call Triage & Response (Annex III Point 5(d))
    if any(k in lowered for k in ["emergency 112", "dispatch call triage", "ambulance emergency response"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 5(d) (Acil durum 112 sevk ve önceliklendirme sistemleri)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex III Point 5(d)",
                "confidence": "Yüksek (Ek III Acil Müdahale ve Kamu Hizmetleri)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Madde 14: İtfaiye, polis veya ambulans yönlendirmede operatörün manuel müdahale ve öncelik ezme yetkisi.",
                    "Madde 15: %99.999 yüksek erişilebilirlik ve kesintisiz acil servis operasyonel direnci."
                ]
            },
            "data_privacy": ["GDPR Madde 6(1)(d): Hayati menfaatlerin (vital interests) korunması kapsamında acil çağrı verisi işleme."],
            "statutory_disclaimer": "Acil durum çağrı ve müdahale önceliklendirme sistemleri Ek III uyarınca yüksek risklidir."
        }

    # 3i. Judicial Authorities Evidence & Dispute Resolution (Annex III Point 8(a))
    if any(k in lowered for k in ["judicial authority", "sentencing evidence", "court legal fact finding", "dispute resolution"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yüksek Riskli Sistem (High-Risk AI System)",
                "statutory_basis": "EU AI Act Madde 6(2) ve Ek III Nokta 8(a) (Adli makamlar için delil değerlendirme ve hukuki karar desteği)",
                "official_precedent": "Regulation (EU) 2024/1689 Annex III Point 8(a)",
                "confidence": "Yüksek (Ek III Adalet Sistemi ve Demokratik Süreçler)",
                "requires_expert_counsel": True,
                "obligations": [
                    "Madde 14: Yargı bağımsızlığı gereği hakimin kesin ve tek karar verici olması (Algoritma yalnızca istişari destek verebilir).",
                    "Madde 13: Delil ve içtihat analiz modellerinde tam açıklanabilirlik ve tarafsızlık denetimi."
                ]
            },
            "data_privacy": ["GDPR Madde 10: Ceza yargılaması ve adli sicil verilerinin mutlak gizliliği."],
            "statutory_disclaimer": "Mahkemeler ve adli merciler için geliştirilen karar destek sistemleri Ek III uyarınca yüksek risklidir."
        }

    # =========================================================================
    # 4. GENERAL PURPOSE AI (GPAI) MODELS WITH SYSTEMIC RISK (ARTICLES 51 & 52)
    # =========================================================================
    if any(k in lowered for k in ["frontier general purpose", "gpai model", "systemic risk", "10^25 flops", "systemic gpai"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Sistemik Riskli GPAI Modeli (Systemic Risk GPAI Model)",
                "statutory_basis": "EU AI Act Madde 51 ve 52 (Sistemik risk taşıyan genel amaçlı yapay zeka modelleri)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 51 & 52",
                "confidence": "Kritik / Sistemik Risk Rejimi",
                "requires_expert_counsel": True,
                "obligations": [
                    "Madde 51: Kümülatif işlem gücü > 10^25 FLOPs modellerin AB Yapay Zeka Ofisi'ne (AI Office) bildirimi.",
                    "Madde 53: Model değerlendirmesi ve bağımsız kırmızı takım (adversarial red-teaming) testleri.",
                    "Madde 55: Sistemik risklerin azaltılması, siber güvenlik koruması ve ciddi olay raporlama (serious incident reporting)."
                ]
            },
            "data_privacy": ["Telif Hakları Direktifi (2019/790) Madde 4(3): Eğitim verisi için Text and Data Mining (TDM) opt-out haklarına uyum."],
            "statutory_disclaimer": "Sistemik risk eşiğini aşan genel amaçlı yapay zeka modelleri AI Act Madde 51-55 özel rejimine tabidir."
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

    # 4b. Satirical / Parody Deepfake Exemption & Journalistic Transparency (Article 50(4))
    if any(k in lowered for k in ["investigative journalism", "parody", "artistic satire", "satirical deepfake", "artistic freedom"]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Belirli Şeffaflık Yükümlülüğü (Transparency Obligations)",
                "statutory_basis": "EU AI Act Madde 50(4) (Sanat, parodi ve gazetecilik amacıyla sentetik içerik şeffaflık istisnası)",
                "official_precedent": "Regulation (EU) 2024/1689 Article 50(4)",
                "confidence": "Doğrulanmış (İfade Özgürlüğü ve Şeffaflık Uyarlaması)",
                "requires_expert_counsel": False,
                "obligations": [
                    "Eserin parodi, hiciv veya sanatsal niteliğini bozmayacak uygun biçimde sentetik içerik açıklaması yapılması.",
                    "Haber ve kamu yararı araştırmalarında basın özgürlüğü (Charter of Fundamental Rights Art 11) dengesi."
                ]
            },
            "data_privacy": ["GDPR Madde 85: Gazetecilik ve sanatsal ifade özgürlüğü istisnaları."],
            "statutory_disclaimer": "Parodi ve sanatsal eserler için filigranlama zorunluluğu eserin doğasını zedelemeyecek şekilde uyarlanır."
        }

    # 4c. Synthetic Media & Deepfakes (Article 50(2))
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

    # 5b. Reverse Engineering for Interoperability Safe Harbor (Directive 2009/24/EC Article 6 & DMCA 1201(f))
    if any(k in lowered for k in [
        "reverse engineering", "interoperability", "clean room", "can bus",
        "decompiler", "disassembler", "birlikte çalışabilirlik", "tersine mühendislik"
    ]):
        return {
            "domain": domain_keywords,
            "eu_ai_act": {
                "tier": "Yasal Muafiyet / Birlikte Çalışabilirlik Güvencesi (Legal Exemption / Interoperability Safe Harbor)",
                "statutory_basis": "Directive 2009/24/EC Madde 6 & DMCA 17 U.S.C. § 1201(f)",
                "official_precedent": "EU Directive 2009/24/EC Article 6 & DMCA 1201(f) (Decompilation for Interoperability)",
                "confidence": "Yüksek (Yasal Birlikte Çalışabilirlik Güvencesi)",
                "requires_expert_counsel": False,
                "obligations": [
                    "Birlikte çalışabilirlik için zorunlu olan kısımlarla sınırlı kalınmalıdır.",
                    "Bağımsız geliştirme ve temiz oda (Clean-Room Specification) şartlarına riayet edilmelidir."
                ]
            },
            "data_privacy": ["Telif Direktifi (2009/24/EC): Fikri mülkiyet birlikte çalışabilirlik güvencesi."],
            "statutory_disclaimer": "Temiz oda şartlarında birlikte çalışabilirlik amaçlı tersine mühendislik yasal güvence altındadır."
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
