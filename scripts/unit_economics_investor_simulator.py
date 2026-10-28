"""
Unit Economics & Zero-Capital Investor Simulator
Zobar Skill — Asymmetric Upside & Lean Startup Financial Engine

Finansal Prensipler:
1. Asimetrik Fırsat: Maksimum kayıp 0$ (emek/ücretsiz bulut), potansiyel getiri sınırsız (yüksek marjlı ARR).
2. Birim Ekonomi (Unit Economics):
   - LTV (Lifetime Value) > 3x CAC (Customer Acquisition Cost)
   - CAC Geri Ödeme Süresi (Payback Period) < 12 Ay
   - Brüt Kâr Marjı (Gross Margin) > %80
3. Sıfır Maliyetli Dağıtım & Viral Döngü (K-Factor > 1.0).
"""

from typing import Dict, Any, List, Optional


class UnitEconomicsSimulator:
    def __init__(
        self,
        arpu_monthly_usd: float = 49.0,
        monthly_churn_rate: float = 0.04,     # 4% monthly churn
        gross_margin: float = 0.85,           # 85% gross margin
        cac_usd: float = 120.0,               # Customer acquisition cost
    ):
        self.arpu = arpu_monthly_usd
        self.churn = max(monthly_churn_rate, 0.001)
        self.gross_margin = gross_margin
        self.cac = cac_usd

    def calculate_metrics(self) -> Dict[str, Any]:
        # Lifetime (in months) = 1 / churn
        avg_customer_lifetime_months = 1.0 / self.churn
        
        # LTV = ARPU * Gross Margin * Lifetime
        ltv = self.arpu * self.gross_margin * avg_customer_lifetime_months
        
        # LTV / CAC Ratio
        ltv_cac_ratio = ltv / max(self.cac, 0.01)

        # Payback period (months) = CAC / (ARPU * Gross Margin)
        monthly_gross_profit_per_user = self.arpu * self.gross_margin
        payback_months = self.cac / max(monthly_gross_profit_per_user, 0.01)

        # Investor grading
        is_tier1_investor_grade = (ltv_cac_ratio >= 3.0) and (payback_months <= 12.0) and (self.gross_margin >= 0.75)

        return {
            "arpu_monthly_usd": self.arpu,
            "monthly_churn_percent": round(self.churn * 100.0, 1),
            "gross_margin_percent": round(self.gross_margin * 100.0, 1),
            "cac_usd": self.cac,
            "avg_customer_lifetime_months": round(avg_customer_lifetime_months, 1),
            "ltv_usd": round(ltv, 2),
            "ltv_cac_ratio": round(ltv_cac_ratio, 2),
            "payback_period_months": round(payback_months, 1),
            "is_tier1_investor_grade": is_tier1_investor_grade,
            "verdict": "TIER-1 YATIRIMCI ONAYLI (LTV/CAC > 3, Payback < 12 Ay)" if is_tier1_investor_grade else "BİRİM EKONOMİ DÜZELTİLMELİ",
        }

    def simulate_asymmetric_payoff(
        self,
        months: int = 12,
        initial_customers: int = 10,
        monthly_growth_rate: float = 0.20,
        zero_capital_cloud_cost_monthly_usd: float = 0.0,
    ) -> Dict[str, Any]:
        """
        Simulates asymmetric compounding with 0$ initial capital.
        """
        current_users = float(initial_customers)
        monthly_revenue_history: List[float] = []

        for m in range(months):
            # Compound growth with churn
            new_users = current_users * monthly_growth_rate
            churned = current_users * self.churn
            current_users = max(current_users + new_users - churned, 0.0)
            mrr = current_users * self.arpu
            monthly_revenue_history.append(round(mrr, 2))

        final_mrr = monthly_revenue_history[-1]
        final_arr = final_mrr * 12.0
        annual_cloud_expenses = zero_capital_cloud_cost_monthly_usd * months
        net_profit_annual = (final_arr * self.gross_margin) - annual_cloud_expenses

        return {
            "simulation_months": months,
            "final_paying_users": int(current_users),
            "ending_mrr_usd": round(final_mrr, 2),
            "ending_arr_usd": round(final_arr, 2),
            "capital_invested_usd": annual_cloud_expenses,
            "estimated_annual_net_profit_usd": round(net_profit_annual, 2),
            "downside_risk": "0$ (Ücretsiz Cloudflare/Supabase/GitHub katmanı, sermaye kaybı yok)",
            "upside_potential": f"${round(final_arr, 2):,} ARR (Sınırsız ölçeklenebilir asimetrik kâr)",
        }


if __name__ == "__main__":
    sim = UnitEconomicsSimulator(arpu_monthly_usd=59.0, monthly_churn_rate=0.035, gross_margin=0.88, cac_usd=95.0)
    metrics = sim.calculate_metrics()
    print("=" * 65)
    print("📈 ASİMETRİK GİRİŞİMCİLİK BİRİM EKONOMİSİ SKORKARTI 📈")
    print("=" * 65)
    for k, v in metrics.items():
        print(f"[*] {k:30}: {v}")

    payoff = sim.simulate_asymmetric_payoff(months=18, initial_customers=15, monthly_growth_rate=0.18)
    print("\n[+] 18 Aylık Sıfır Sermayeli Büyüme Simülasyonu:")
    print(f"    Son Ay MRR   : ${payoff['ending_mrr_usd']:,}")
    print(f"    Yıllık ARR   : ${payoff['ending_arr_usd']:,}")
    print(f"    Maksimum Risk: {payoff['downside_risk']}")
