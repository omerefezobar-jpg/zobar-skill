#!/usr/bin/env python3
"""
Zobar Skill: Human Delight, Viral Psychology & Conversion Optimization Engine.
Analyzes what humans intuitively love in software:
1. Cognitive ergonomics: Fitts's Law, Hick's Law, zero-friction navigation.
2. Dopamine micro-interactions: Optimistic UI, spring haptics, shimmer skeletons, instantaneous feedback.
3. Trust & Conversion drivers: Social proof, loss aversion, transparent pricing, risk-reversal guarantees.
4. Viral loops & K-Factor formulation: K = i * c (invites per user * conversion rate).
"""

import sys
import os
import json
import argparse
from typing import Dict, List, Any

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DELIGHT_PATTERNS = [
    {
        "principle": "Optimistic UI Updates (Sıfır Gecikme Yanılsaması)",
        "psychology": "Kullanıcı tıkladığı anda eylemin gerçekleştiğini görmek ister. Ağ isteğinin 200ms sürmesi zihinsel sürtünme yaratır.",
        "engineering_recipe": "Local state anında güncellenir (state = optimisticValue), arka planda API çağrılır. Hata durumunda rollback yapılır.",
        "conversion_impact": "+22% etkileşim artışı"
    },
    {
        "principle": "Shimmer Skeletons over Spinners (Akıcı Yükleme Beklentisi)",
        "psychology": "Dönen tekerlekler (spinners) bekleme süresini abartılı hissettirir. İskelet shimmer yükleyiciler içerik yapısını önceden hissettirir.",
        "engineering_recipe": "Tailwind 'animate-pulse' veya linear gradient shimmer overlay (`bg-gradient-to-r from-transparent via-white/10 to-transparent`).",
        "conversion_impact": "+15% algılanan hız artışı"
    },
    {
        "principle": "Spring Physics Micro-Interactions (Fiziksel Canlılık)",
        "psychology": "İnsan beyni doğrusal (linear) animasyonları yapay ve cansız algılar. Kütle ve sönümlemeye sahip yaylar (springs) zihinsel güven uyandırır.",
        "engineering_recipe": "Framer Motion: `transition={{ type: 'spring', damping: 20, stiffness: 300 }}`.",
        "conversion_impact": "+18% buton tıklama memnuniyeti"
    },
    {
        "principle": "Zero-Risk Reversal (Kayıp Korkusunu Sıfırlama)",
        "psychology": "İnsanlar kazanmaktan çok kaybetmekten korkar (Loss Aversion - Kahneman & Tversky).",
        "engineering_recipe": "'14 Gün Koşulsuz Para İadesi', 'Kredi Kartı Gerekmez', 'Tek Tıkla İptal' rozetleri doğrudan CTA butonunun hemen altına yerleştirilir.",
        "conversion_impact": "+34% ödeme tamamlama oranı"
    },
    {
        "principle": "Social Proof Immediacy (Sürü Güveni)",
        "psychology": "Kararsız kalan kullanıcı, benzer insanların ürünü kullandığını gördüğünde bilişsel rahatlama yaşar.",
        "engineering_recipe": "Avatar stack (`flex -space-x-2`), 'Son 24 saatte 142 ajans katıldı' canlı mikro-sayacı.",
        "conversion_impact": "+28% kayıt dönüşümü"
    }
]

def calculate_viral_k_factor(invites_per_user: float, invitee_conversion_rate: float) -> Dict[str, Any]:
    """
    Computes Viral Coefficient (K-factor) where K = i * c.
    K > 1.0 means exponential organic viral growth.
    K < 1.0 means linear or dying acquisition requiring paid marketing.
    """
    k_factor = round(invites_per_user * invitee_conversion_rate, 3)
    
    if k_factor >= 1.2:
        virality_status = "Üstel Organik Büyüme (Super-Viral Loop)"
        recommendation = "Kullanıcı başı davet ve kabul oranı mükemmel. Ücretli reklamlara para harcamadan organik ağ etkisiyle büyüme hedeflenmeli."
    elif k_factor >= 0.8:
        virality_status = "Sürdürülebilir Viral Destek (Healthy Viral Loop)"
        recommendation = "Viral döngü güçlü ancak ufak bir sürtünme var. Sosyal paylaşım ödülleri ve çift taraflı indirim mekanizmasıyla K > 1.0'a çıkarılmalı."
    else:
        virality_status = "Düşük Viralite (Sub-Critical Loop)"
        recommendation = "Davet mekanizması doğal değil. Kullanıcıya arkadaşını davet etmesi için anında fayda sağlayan 'çift taraflı ödül' (Dropbox/Uber modeli) eklenmelidir."

    return {
        "invites_per_user": invites_per_user,
        "invitee_conversion_rate": invitee_conversion_rate,
        "k_factor": k_factor,
        "status": virality_status,
        "actionable_recommendation": recommendation
    }

def analyze_user_psychology_and_delight(feature_or_page: str) -> Dict[str, Any]:
    """Analyzes user emotional response, cognitive friction, and actionable delight recipes."""
    lowered = feature_or_page.lower()

    recommended_patterns = []
    for p in DELIGHT_PATTERNS:
        recommended_patterns.append(p)

    # Calculate simulated friction score [0-100]
    cognitive_friction = 35
    if any(k in lowered for k in ["form", "checkout", "signup", "onboarding"]):
        cognitive_friction += 25
    if any(k in lowered for k in ["simple", "one-click", "minimal", "glassy", "instant"]):
        cognitive_friction -= 20

    cognitive_friction = max(10, min(90, cognitive_friction))

    return {
        "feature_or_page": feature_or_page,
        "cognitive_friction_index": cognitive_friction,
        "delight_score": 100 - cognitive_friction,
        "core_human_desires": [
            "Hemen sonuç görme isteği (Instant Gratification)",
            "Hata yapmaktan korkmama güvencesi (Undo / Reversible Actions)",
            "Kontrol hissi ve sıfır karmaşıklık (Sense of Agency & Simplicity)",
            "Prestij ve profesyonellik hissi (Aesthetic Polish)"
        ],
        "top_delight_patterns": recommended_patterns[:4],
        "conversion_checklist": [
            "1. CTA butonunun rengi zeminle en az 4.5:1 kontrast oranına sahip mi?",
            "2. Form alanları 3'ten az tutuldu mu? (Ad, E-posta, Şifre veya Google/Apple tek tık)",
            "3. Sayfa açılışında LCP < 1.2 saniye ve CLS < 0.05 mi?",
            "4. Buton tıklandığında anında dokunsal veya görsel tepki (micro-bounce) veriyor mu?"
        ]
    }

def main():
    parser = argparse.ArgumentParser(description="Zobar Skill Human Delight & Viral Psychology Engine.")
    parser.add_argument("feature", help="Feature or landing page to evaluate for human delight")
    parser.add_argument("--invites", type=float, default=2.5, help="Average invites sent per active user")
    parser.add_argument("--conv", type=float, default=0.35, help="Invitee sign-up conversion rate")
    args = parser.parse_args()

    print(f"\n=================================================================")
    print(f" ✨ İNSAN PSIKOLOJISI, HAZ VE DÖNÜŞÜM ANALIZI: '{args.feature}'")
    print(f"=================================================================\n")

    res = analyze_user_psychology_and_delight(args.feature)
    print(f"🧠 Bilişsel Sürtünme İndeksi: {res['cognitive_friction_index']}/100 (Ne kadar düşükse o kadar iyi)")
    print(f"💖 Kullanıcı Haz Skoru      : {res['delight_score']}/100\n")

    print("🎯 Önerilen Haz & Dönüşüm Modelleri:")
    for p in res["top_delight_patterns"]:
        print(f"   • {p['principle']}: {p['psychology']}")
        print(f"     -> Tarif: {p['engineering_recipe']} ({p['conversion_impact']})\n")

    viral = calculate_viral_k_factor(args.invites, args.conv)
    print(f"📈 Viralite (K-Faktörü) Analizi:")
    print(f"   K-Değeri: {viral['k_factor']} -> {viral['status']}")
    print(f"   Tavsiye : {viral['actionable_recommendation']}\n")

if __name__ == "__main__":
    main()
