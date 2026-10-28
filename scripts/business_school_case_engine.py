"""
Business School Case Engine & Wealth Compounding Analyzer
Zobar Skill — HBS, Stanford GSB, Wharton & INSEAD Strategic Frameworks

Analiz Katmanları:
1. Harvard Business School (HBS): Michael Porter 5 Rekabet Gücü & Değer Zinciri.
2. INSEAD: Mavi Okyanus Stratejisi (Değer İnovasyonu & 4 Eylem Çerçevesi).
3. Wharton / Columbia: Tarihsel Servet Katlama Modelleri (Arbitraj, Float, Kod/Medya Kaldıracı).
4. Yalın İş Gücü ve Yapay Zekâ Kaldıraç Modeli (1 Kişilik Unicorn / Micro-Enterprise).
"""

import sys
from typing import Dict, Any, List, Optional


class BusinessSchoolCaseEngine:
    # Historical Wealth Multipliers
    HISTORICAL_MODELS = {
        "venetian_arbitrage": {
            "name": "Venedik Tüccarı (Mekânsal & Bilgi Arbitrajı)",
            "era": "14. - 16. Yüzyıl",
            "principle": "Bilginin veya emtianın bol olduğu yerden ucuza alıp, kıt olduğu pazarda fahiş kârla satmak.",
            "modern_equivalent": "Sınır ötesi dijital hizmetler, e-ticaret arbitrajı, API fiyatlama arbitrajı.",
            "capital_required": "Orta",
            "leverage_type": "Fiziksel Ticaret & Bilgi Asimetrisi",
        },
        "rockefeller_monopoly": {
            "name": "Standard Oil / Carnegie (Dikey Entegrasyon & Ölçek Ekonomisi)",
            "era": "19. Yüzyıl Sonu",
            "principle": "Üretimden dağıtıma tüm tedarik zincirini ele geçirip birim maliyeti rakiplerin batacağı seviyeye düşürmek.",
            "modern_equivalent": "AWS altyapısı, TSMC yarı iletken fabrikaları, dikey entegre donanım-yazılım (Apple).",
            "capital_required": "Çok Yüksek",
            "leverage_type": "Endüstriyel Sermaye & Lojistik",
        },
        "buffett_float": {
            "name": "Berkshire Hathaway (Sigorta 'Float' & Kalıcı Hendek / Moat)",
            "era": "20. Yüzyıl Ortası",
            "principle": "Müşterilerden önceden toplanan parayı (float) sıfır maliyetli sermaye olarak kullanarak yüksek kâr marjlı tekellere yatırım yapmak.",
            "modern_equivalent": "Yıllık peşin ödenen SaaS abonelikleri (negatif işletme sermayesi), pazar yeri bakiye havuzları.",
            "capital_required": "Yüksek",
            "leverage_type": "Finansal Kaldıraç & Fikri Mülkiyet",
        },
        "constellation_rollup": {
            "name": "Constellation Software / Mark Leonard (Dikey Yazılım Toplama)",
            "era": "21. Yüzyıl Başı",
            "principle": "Küçük, niş, terkedilme riski sıfır (mission-critical) dikey B2B yazılımları satın alıp nakit akışını yeniden yatırıma yönlendirmek.",
            "modern_equivalent": "Mikro SaaS portföy yönetimi, tek sektörlü ERP/CRM araçları.",
            "capital_required": "Orta - Yüksek",
            "leverage_type": "Sermaye Tahsisi & Yüksek ROIC",
        },
        "naval_permissionless_leverage": {
            "name": "Naval Ravikant (İzinsiz Kaldıraç: Kod ve Medya)",
            "era": "Günümüz (Yapay Zekâ Çağı)",
            "principle": "Uykundayken bile çalışan, marjinal çoğaltma maliyeti sıfır olan kod ve içerik üretmek. İzin istemek yok, sermaye gereksinimi sıfır.",
            "modern_equivalent": "Yapay zekâ ajanları, açık kaynak kütüphaneler, otomatize SaaS sistemleri.",
            "capital_required": "Sıfır",
            "leverage_type": "Kod & Medya (Sonsuz Asimetrik Kaldıraç)",
        },
    }

    @classmethod
    def analyze_porter_five_forces(cls, industry: str) -> Dict[str, Any]:
        """
        Harvard Business School: Michael Porter's 5 Forces Dynamic Analysis.
        Dynamically adjusts scores, threat levels, and defenses based on the target industry.
        """
        ind = industry.lower()

        # 1. Biotech / Pharma / Clinical
        if any(w in ind for w in ["biotech", "pharma", "ilaç", "klinik", "medical", "sağlık", "genetik"]):
            archetype = "Regulated Life Sciences & Biotech"
            entrants = {"level": "Düşük (1/10)", "score": 1, "reason": "FDA/MDR regülasyonları, 10 yıllık klinik deneyler ve patent duvarları.", "defense": "Tescilli molekül/algoritma patentleri ve münhasır lisanslar."}
            buyers = {"level": "Düşük - Orta (3/10)", "score": 3, "reason": "Hayati önem taşıyan tedavilerde sigorta ve hastanelerin fiyat esnekliği düşüktür.", "defense": "Klinik sonuç üstünlüğü ve geri ödeme (reimbursement) kodları."}
            suppliers = {"level": "Yüksek (8/10)", "score": 8, "reason": "Özel biyoreaktörler, saflaştırılmış enzimler ve CRO laboratuvar tekelindedir.", "defense": "Çoklu tedarikçi anlaşmaları ve kritik bileşenleri dikey entegre etme."}
            substitutes = {"level": "Düşük (2/10)", "score": 2, "reason": "Onaylı bir ilacın veya klinik cihazın ikamesi yıllarca çıkamaz.", "defense": "Patent süresi uzatma (evergreening) ve endikasyon genişletme."}
            rivalry = {"level": "Orta (5/10)", "score": 5, "reason": "Pazar oligopolistiktir; şirketler fiyatla değil Ar-Ge ile yarışır.", "defense": "İlk giren avantajı (first-in-class) ve küresel dağıtım ortaklıkları."}

        # 2. FinTech / Banking / Payments
        elif any(w in ind for w in ["fintech", "bank", "ödeme", "kredi", "sigorta", "crypto", "defi", "trading"]):
            archetype = "Regulated Financial Services & FinTech"
            entrants = {"level": "Orta (5/10)", "score": 5, "reason": "Bankacılık lisansları ve BDDK/SEC/MiFID II uyum maliyeti korur; ancak API-first çözümler artmaktadır.", "defense": "Düzenleyici lisanslar ve doğrudan takas ağı (SWIFT/SEPA/FAST) entegrasyonu."}
            buyers = {"level": "Yüksek (7/10)", "score": 7, "reason": "Finansal tüketiciler ve kurumlar en düşük komisyonu ve en yüksek faizi arar.", "defense": "Gömülü finans (Embedded Finance) ile ERP sistemlerinin içine kilitlenme."}
            suppliers = {"level": "Yüksek (7/10)", "score": 7, "reason": "Kart şemaları (Visa/Mastercard) ve ana bankacılık sağlayıcıları komisyon dayatır.", "defense": "Açık bankacılık (Account-to-Account) ve çoklu borsa likidite yönlendirmesi."}
            substitutes = {"level": "Yüksek (7/10)", "score": 7, "reason": "Kripto varlıklar, doğrudan takas ve alternatif ödeme yöntemleri hızla ikame yaratır.", "defense": "Hız, sıfır dolandırıcılık garantisi ve mevzuat zırhı."}
            rivalry = {"level": "Şiddetli (8/10)", "score": 8, "reason": "Geleneksel bankalar ile çevik neobank'lar aynı mevduat için yarışır.", "defense": "Niş B2B dikeylerine (örn. sadece sınır ötesi lojistikçilere kredi) odaklanma."}

        # 3. Hardware / Automotive / Robotics
        elif any(w in ind for w in ["hardware", "donanım", "robot", "otomotiv", "automotive", "araba", "üretim", "fabrika"]):
            archetype = "Capital-Intensive Industrial & Hardware"
            entrants = {"level": "Düşük - Orta (3/10)", "score": 3, "reason": "Takım tezgahı, kalıp maliyetleri (NRE) ve fabrika yatırımları gerektirir.", "defense": "Tescilli donanım mimarisi ve tedarik zinciri hacim indirimleri."}
            buyers = {"level": "Yüksek (8/10)", "score": 8, "reason": "Büyük alıcılar (OEM'ler) her çeyrek marj kırma baskısı yapar.", "defense": "Donanıma gömülü abonelik yazılımı (Hardware-enabled SaaS) satmak."}
            suppliers = {"level": "Aşırı Yüksek (9/10)", "score": 9, "reason": "TSMC yarı iletken fabrikaları, lityum madenleri ve sensör tedarikçileri kısıtlıdır.", "defense": "Kritik çiplerde ikili kaynak (dual-sourcing) ve stratejik stoklama."}
            substitutes = {"level": "Düşük (3/10)", "score": 3, "reason": "Fiziksel bir robotun veya aracın yerini salt yazılım tutamaz.", "defense": "Modüler genişleme yuvaları ve uzun ömürlü endüstriyel güvenilirlik."}
            rivalry = {"level": "Yüksek (7/10)", "score": 7, "reason": "Global üreticiler arasındaki birim maliyet ve enerji verimliliği savaşı.", "defense": "Sensör füzyonu ve üstün yazılım/firmware optimizasyonu."}

        # 4. Consumer Apps / E-Commerce / Retail
        elif any(w in ind for w in ["consumer", "tüketici", "e-ticaret", "retail", "perakende", "moda", "social"]):
            archetype = "High-Churn Consumer & E-Commerce"
            entrants = {"level": "Aşırı Yüksek (9/10)", "score": 9, "reason": "Shopify veya App Store üzerinde dakikalar içinde yeni rakip doğabilir.", "defense": "Güçlü marka kimliği, organik topluluk ve viral döngü (K-factor > 1)."}
            buyers = {"level": "Aşırı Yüksek (10/10)", "score": 10, "reason": "Sıfır geçiş maliyeti (switching cost); kullanıcı tek tıkla rakibe geçer.", "defense": "Sadakat puanları, kişiselleştirilmiş AI önerileri ve anında teslimat."}
            suppliers = {"level": "Düşük - Orta (4/10)", "score": 4, "reason": "Toptancı ve fason üretici bolluğu mevcuttur.", "defense": "Doğrudan tüketiciye (D2C) satış ile aracı komisyonlarını kesmek."}
            substitutes = {"level": "Yüksek (8/10)", "score": 8, "reason": "Binlerce alternatif eğlence ve alışveriş kanalı mevcuttur.", "defense": "Benzersiz kullanıcı deneyimi ve alışkanlık döngüleri (Hook Model)."}
            rivalry = {"level": "Kanlı Kırmızı Okyanus (10/10)", "score": 10, "reason": "Fiyat kırma ve reklam açık artırması (CAC enflasyonu) çok yüksektir.", "defense": "Ücretli reklamlara bağımlılığı kesip organik dağıtım kanalları kurmak."}

        # 5. Default: B2B SaaS, Cloud & Developer Tools
        else:
            archetype = "B2B Software, Cloud & AI Engineering"
            entrants = {"level": "Yüksek (8/10)", "score": 8, "reason": "Yapay zekâ ve vibe coding ile kod yazım bariyeri sıfırlandı; yeni SaaS klonları hızla türer.", "defense": "Tescilli veri seti, derin veritabanı entegrasyonu ve yüksek geçiş maliyeti."}
            buyers = {"level": "Orta - Yüksek (6/10)", "score": 6, "reason": "B2B müşterileri bütçe kısıntısında ilk olarak gereksiz yazılım aboneliklerini iptal eder.", "defense": "Şirketin ana gelir akışını sağlayan vazgeçilmez (mission-critical) sistem olmak."}
            suppliers = {"level": "Orta (5/10)", "score": 5, "reason": "OpenAI, Anthropic ve AWS fiyat kırsa da tescilli modellere bağımlılık riski vardır.", "defense": "Açık kaynak yerel modeller (Llama, Mistral) ve çoklu model router kullanmak."}
            substitutes = {"level": "Yüksek (7/10)", "score": 7, "reason": "Açık kaynak GitHub projeleri ve şirket içi dahili araçlar hızla alternatif olur.", "defense": "Sadece yazılım satmayıp doğrudan ölçülebilir iş sonucu ve SLA garantisi sunmak."}
            rivalry = {"level": "Şiddetli (8/10)", "score": 8, "reason": "Silikon Vadisi ve küresel mikro-SaaS girişimcilerinin yoğun rekabeti.", "defense": "Mavi Okyanus stratejisiyle hiper-niş bir dikey uzmanlığa odaklanmak."}

        # Calculate Overall Industry Profitability Attractiveness (0-100)
        # Lower total threat scores mean higher structural profitability attractiveness
        total_threat = entrants["score"] + buyers["score"] + suppliers["score"] + substitutes["score"] + rivalry["score"]
        attractiveness_index = max(min(int(100 - (total_threat - 5) * (100 / 45)), 100), 5)

        return {
            "framework": "Harvard Business School (HBS) — Porter's 5 Forces",
            "target_industry": industry,
            "detected_archetype": archetype,
            "industry_attractiveness_index": attractiveness_index,
            "profitability_outlook": "YÜKSEK YAPISAL KÂRLILIK" if attractiveness_index >= 65 else ("ORTA KÂRLILIK / DİKKATLİ NİŞLEŞME GEREKİR" if attractiveness_index >= 40 else "ZORLU / KANLI KIRMIZI OKYANUS"),
            "forces": {
                "threat_of_new_entrants": entrants,
                "bargaining_power_of_buyers": buyers,
                "bargaining_power_of_suppliers": suppliers,
                "threat_of_substitutes": substitutes,
                "competitive_rivalry": rivalry,
            }
        }

    @classmethod
    def calculate_lean_ai_workforce_multiplier(
        cls,
        current_human_headcount: int = 10,
        avg_annual_salary_usd: float = 75000.0,
        ai_agent_tier1_budget_monthly_usd: float = 300.0,
        human_specialists_retained: int = 2,
    ) -> Dict[str, Any]:
        """
        Computes financial transformation from traditional bloated headcount
        to a 1-to-2 person AI-orchestrated micro-enterprise.
        """
        traditional_payroll_annual = current_human_headcount * avg_annual_salary_usd
        new_payroll_annual = human_specialists_retained * avg_annual_salary_usd
        ai_tools_annual = ai_agent_tier1_budget_monthly_usd * 12.0
        new_total_cost_annual = new_payroll_annual + ai_tools_annual

        annual_savings = traditional_payroll_annual - new_total_cost_annual
        savings_percentage = (annual_savings / max(traditional_payroll_annual, 1.0)) * 100.0

        return {
            "traditional_workforce": {
                "headcount": current_human_headcount,
                "annual_cost_usd": traditional_payroll_annual,
            },
            "lean_ai_enterprise": {
                "human_specialists": human_specialists_retained,
                "ai_agent_infrastructure_cost_usd": ai_tools_annual,
                "total_annual_cost_usd": new_total_cost_annual,
            },
            "annual_savings_usd": round(annual_savings, 2),
            "cost_reduction_percent": round(savings_percentage, 1),
            "productivity_multiplier": f"{round(current_human_headcount / max(human_specialists_retained, 1), 1)}x kişi başı çıktı kaldıracı",
            "operating_principle": "Rutin işleri (Tier-1) yapay zekâya bırak, insanı sadece nihai kalite onayında (HITL) tut.",
        }


if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    engine = BusinessSchoolCaseEngine()
    print("=" * 65)
    print("[*] İŞLETME FAKÜLTELERİ (HBS, INSEAD, WHARTON) VAKA MOTORU")
    print("=" * 65)
    
    workforce = engine.calculate_lean_ai_workforce_multiplier(current_human_headcount=8, avg_annual_salary_usd=60000.0)
    print(f"[*] Geleneksel Yıllık Bordro: ${workforce['traditional_workforce']['annual_cost_usd']:,}")
    print(f"[*] Yapay Zekâ Hibrit Model: ${workforce['lean_ai_enterprise']['total_annual_cost_usd']:,}")
    print(f"[*] Yıllık Net Kâr Tasarrufu: ${workforce['annual_savings_usd']:,} (%{workforce['cost_reduction_percent']})")
    print(f"[*] Operasyonel İlke       : {workforce['operating_principle']}")
