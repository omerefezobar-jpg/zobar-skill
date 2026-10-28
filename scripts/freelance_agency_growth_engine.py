#!/usr/bin/env python3
"""
Zobar Skill: Freelance, Agency & Indie-Hacker Growth Engine.
Empowers solo developers, agencies, and web freelancers to:
1. Generate high-margin, low-competition client project ideas with recurring retainers.
2. Produce cold audit outreach emails & Upwork proposals that close deals with quantified ROI.
3. Calculate agency recurring maintenance revenue models (MRR).
4. Provide structured conversion funnels and high-ticket sales scripts.
"""

import sys
import os
import json
import argparse
from typing import Dict, List, Any

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

NICHE_OPPORTUNITIES = [
    {
        "niche": "Özel Klinikler & Estetik Doktorları (Medical & Aesthetic Clinics)",
        "pain_point": "Telefonla randevu alırken sekreterin meşgul olması veya mesai dışı gelen hastaların kaybedilmesi (%32 randevu kaybı).",
        "solution_offer": "WhatsApp Entegreli Akıllı Randevu & Ön Bilgilendirme Portalı",
        "pricing_setup_usd": 1800,
        "monthly_retainer_usd": 300,
        "deliverables": ["Next.js / Tailwind mobil uyumlu hızlı sayfa", "WhatsApp Bot & SMS randevu hatırlatıcı", "SEO yerel harita optimizasyonu"],
        "client_roi_pitch": "Ayda sadece 2 ek estetik hasta kazandırdığında sistem kendi maliyetini ilk 30 günde tamamen amorti eder."
    },
    {
        "niche": "Güneş Enerjisi (Solar) & Çatı İzolasyon Firmaları (Home Contractors)",
        "pain_point": "Müşterilerin 'Acaba bana kaça mal olur?' sorusuna anında yanıt bulamadığı için siteden çıkması (%65 terk oranı).",
        "solution_offer": "3 Adımlı İnteraktif Maliyet & Tasarruf Hesaplama Hunisi (Instant Quote Funnel)",
        "pricing_setup_usd": 2400,
        "monthly_retainer_usd": 400,
        "deliverables": ["Framer Motion slider'lı dinamik fiyat hesaplayıcı", "Otomatik PDF teklif üretimi", "HubSpot / Webhook CRM entegrasyonu"],
        "client_roi_pitch": "Gelen lead'lerin dönüşüm oranını 3 katına çıkararak Google reklam bütçesinden elde edilen geliri maksimize eder."
    },
    {
        "niche": "Butik Oteller & Villa Kiralama (Boutique Hospitality)",
        "pain_point": "Booking.com ve Airbnb'ye her rezervasyonda %15 - %20 komisyon ödenmesi.",
        "solution_offer": "Sıfır Komisyonlu Doğrudan Rezervasyon & Sanal Tur Sitesi",
        "pricing_setup_usd": 2800,
        "monthly_retainer_usd": 350,
        "deliverables": ["Stripe / Sanal POS entegrasyonu", "iCal otomatik takvim senkronizasyonu", "Lüks koyu/açık modern tasarım"],
        "client_roi_pitch": "Yılda 100.000$ ciro yapan butik otelin komisyonculardan kurtardığı 18.000$ doğrudan cebinde kalır."
    },
    {
        "niche": "Gourmet Restoranlar & Kahveciler (Gourmet Eateries)",
        "pain_point": "Yemeksepeti / Getir komisyonları (%25-38) ve hantal masa sipariş menüleri.",
        "solution_offer": "QR Dijital Sipariş, Sadakat Puanı & Masa Başı Ödeme Web Uygulaması",
        "pricing_setup_usd": 1200,
        "monthly_retainer_usd": 200,
        "deliverables": ["Sıfır indirme gerektiren PWA web menü", "Mutfak ekranı (KDS) canlı sipariş takibi", "Müşteri SMS sadakat puanı"],
        "client_roi_pitch": "Paket servis komisyonlarını sıfırlayarak aylık net kâr marjını doğrudan %15 artırır."
    }
]

def generate_cold_audit_proposal(target_business: str, niche_key: str = "clinic", client_website: str = "example.com") -> Dict[str, Any]:
    """
    Synthesizes a high-converting, non-spammy cold audit proposal that offers immediate value.
    """
    selected_niche = next((n for n in NICHE_OPPORTUNITIES if niche_key.lower() in n["niche"].lower()), NICHE_OPPORTUNITIES[0])

    email_subject = f"Hızlı Bir İnceleme: {target_business} İçin Kaçırılan Randevuları Yakalama Önerisi"
    
    email_body = f"""Merhaba {target_business} Ekibi,

Web sitenizi ({client_website}) mobil cihaz üzerinden inceledim. Tasarımınız şık ancak kritik bir dönüşüm sızıntısı fark ettim:

Mobil kullanıcı sitenize girdiğinde randevu/fiyat almak için 3 farklı sayfada gezinmek zorunda kalıyor ve sayfa yüklenme süresi ~3.8 saniye. Google verilerine göre 3 saniyeyi aşan mobil sitelerde kullanıcıların %32'si işlemi tamamlamadan çıkıyor.

Sizin için hiçbir ücret talep etmeden 10 kat daha hızlı çalışan ve doğrudan WhatsApp/SMS ile teyit alan modern bir 'Hızlı Randevu & Teklif Prototipi' hazırladım:
👉 Önizleme Linki: https://demo-preview.zobarskill.dev/{target_business.lower().replace(' ', '-')}-preview

Bu sistemle:
1. Mesai saatleri dışında gelen hastalar doğrudan otomatik randevu oluşturabiliyor.
2. Form doldurma süresi 15 saniyeye iniyor.
3. Ayda ortalama 8-15 ek rezervasyon doğrudan sisteme düşüyor.

Eğer bu tasarımı canlıya almak veya geliştirmek isterseniz 10 dakikalık kısa bir görüşmede kurulum sürecini (7 gün içinde anahtar teslim) konuşabiliriz. Beğenmezseniz de hazırladığım tasarım ve hız optimizasyonu raporu sizde kalabilir.

İyi çalışmalar dilerim,
[Adınız] — Bağımsız Yazılım Mühendisi & Web Dönüşüm Uzmanı
"""

    return {
        "target_business": target_business,
        "niche_data": selected_niche,
        "outreach_strategy": {
            "email_subject": email_subject,
            "cold_email_body": email_body,
            "follow_up_sms_script": f"Merhaba {target_business}, siteniz için hazırladığım ücretsiz hızlı rezervasyon prototipini e-posta ile iletmiştim. İnceleme şansınız oldu mu? Demo: demo-preview.zobarskill.dev/{target_business.lower().replace(' ', '-')}"
        },
        "retainer_monetization_plan": {
            "initial_project_fee": f"${selected_niche['pricing_setup_usd']}",
            "monthly_maintenance_retainer": f"${selected_niche['monthly_retainer_usd']}/ay",
            "retainer_services": [
                "Aylık Cloudflare CDN & Vercel sunucu barındırma ve 99.99% kesintisiz çalışma garantisi",
                "Düzenli menü/fiyat güncellemesi ve içerik revizyonları",
                "Aylık dönüşüm ve kaçırılan müşteri analiz raporu",
                "Acil teknik destek ve SSL/Güvenlik güncellemeleri"
            ]
        }
    }

def calculate_agency_retainer_growth(client_count: int = 10, avg_monthly_fee: float = 300.0) -> Dict[str, Any]:
    """Calculates MRR (Monthly Recurring Revenue) and annual financial security for freelancers."""
    monthly_mrr = client_count * avg_monthly_fee
    annual_arr = monthly_mrr * 12

    return {
        "active_retainer_clients": client_count,
        "avg_monthly_fee_per_client": f"${avg_monthly_fee:.2f}",
        "monthly_recurring_revenue_mrr": f"${monthly_mrr:,.2f}",
        "annual_run_rate_arr": f"${annual_arr:,.2f}",
        "financial_stability_assessment": (
            "Freelance proje avcılığından (feast-and-famine döngüsü) kurtulup öngörülebilir sabit gelire geçiş. "
            f"{client_count} aktif müşteriyle her ay sabit ${monthly_mrr:,.2f} nakit akışı garantilenir."
        )
    }

def main():
    parser = argparse.ArgumentParser(description="Zobar Skill Freelance & Agency Growth Engine.")
    parser.add_argument("business", help="Target client business name (e.g. 'Apex Dental Clinic')")
    parser.add_argument("--niche", default="clinic", help="Niche keyword (clinic, contractor, hotel, restaurant)")
    args = parser.parse_args()

    print(f"\n=================================================================")
    print(f" 💼 FREELANCE & AJANS MÜŞTERİ KAZANMA MOTORU: '{args.business}'")
    print(f"=================================================================\n")

    proposal = generate_cold_audit_proposal(args.business, niche_key=args.niche)
    print(f"🎯 Hedef Sektör         : {proposal['niche_data']['niche']}")
    print(f"💰 Kurulum Ücreti       : {proposal['retainer_monetization_plan']['initial_project_fee']}")
    print(f"🔄 Aylık Bakım (MRR)    : {proposal['retainer_monetization_plan']['monthly_maintenance_retainer']}")
    print(f"💎 Müşteriye Sunulan ROI: {proposal['niche_data']['client_roi_pitch']}\n")

    print(f"📧 Hazır Soğuk Denetim E-Postası (Subject: {proposal['outreach_strategy']['email_subject']}):")
    print("-" * 65)
    print(proposal["outreach_strategy"]["cold_email_body"])
    print("-" * 65)

    growth = calculate_agency_retainer_growth(client_count=10, avg_monthly_fee=float(proposal['niche_data']['monthly_retainer_usd']))
    print(f"\n📊 10 Müşterili Ajans Finansal Büyüme Modeli:")
    print(f"   Aylık Sabit Gelir (MRR): {growth['monthly_recurring_revenue_mrr']}")
    print(f"   Yıllık Sabit Gelir (ARR): {growth['annual_run_rate_arr']}")

if __name__ == "__main__":
    main()
