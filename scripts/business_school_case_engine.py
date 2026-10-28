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
        Harvard Business School: Michael Porter's 5 Forces Analysis.
        """
        return {
            "framework": "Harvard Business School (HBS) — Porter's 5 Forces",
            "target_industry": industry,
            "forces": {
                "threat_of_new_entrants": {
                    "level": "Yüksek (Yapay Zekâ ile kodlama kolaylaştı)",
                    "defense": "Fikri mülkiyet, tescilli veri seti ve yüksek müşteri geçiş maliyeti (switching cost) kurun."
                },
                "bargaining_power_of_buyers": {
                    "level": "Orta - Yüksek",
                    "defense": "Ağ etkisi (Network Effects) ve derin entegrasyon ile alternatifsiz hale gelin."
                },
                "bargaining_power_of_suppliers": {
                    "level": "Orta (Büyük model sağlayıcıları OpenAI/Anthropic fiyat kırıyor)",
                    "defense": "Açık kaynak yerel modeller (Llama, Mistral) ve çoklu model yönlendiricisi kullanın."
                },
                "threat_of_substitutes": {
                    "level": "Yüksek",
                    "defense": "Yalnızca yazılım satmayın; kullanıcıya doğrudan iş sonucu (outcome) sunun."
                },
                "competitive_rivalry": {
                    "level": "Şiddetli",
                    "defense": "Mavi Okyanus stratejisiyle rekabetin olmadığı niş dikey pazara odaklanın."
                }
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
