# ⚡ Zobar Skill: Deep-Tech, Market & Radical Invention Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI & Quality Gate](https://github.com/omerefezobar-jpg/zobar-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/omerefezobar-jpg/zobar-skill/actions)
[![Regression Suite](https://img.shields.io/badge/Regression%20Suite-6%2F6%20Passing-blue.svg)](./benchmarks/BENCHMARK_REPORT.md)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-12%2F12%20Passing-brightgreen.svg)](https://github.com/omerefezobar-jpg/zobar-skill/actions)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Security: XSS Hardened](https://img.shields.io/badge/Security-XSS%20Hardened%20(No%20Eval)-green.svg)](https://github.com/omerefezobar-jpg/zobar-skill)

**Zobar Skill**, yapay zeka ajanlarını yüzeysel cevaplar veren asistanlardan; bir konuyu **akademik ön baskı literatürü (arXiv)**, **olumsuzlama farkındalıklı çok kaynaklı kullanıcı sürtünmeleri (HN + Reddit)**, **hibrit pazar ve rakip analizi (Ticari Liderler + GitHub)**, **madde bazlı yasal mevzuat (EU AI Act Madde 5/6/50 & GDPR)**, **otomatik teknik mimari sentezi** ve **fizibilitesi kanıtlanmış radikal icatlarla** sıfırdan kurgulayan **uçtan uca otonom bir Deep-Tech Ar-Ge ve İnovasyon Motorudur**.

---

## 🎯 Zobar Skill Farkı & Temel Mimari

Sıradan bir prompt veya yapay zeka asistanı afaki ve süslü laflar üretirken; **Zobar Skill** her analizde 6 fazı ampirik veriler ve kanıt taksonomisiyle işletir:

* 🏛️ **Akademik Zemin (Faz 1):** HTTPS üzerinden arXiv ön baskı (pre-print) deposunu tarar; teorik sınırları ve seminal makaleleri çeker.
* 💬 **Çok Kaynaklı Kullanıcı Sürtünmesi (Faz 2):** Hacker News ve Reddit topluluklarında olumsuzlama ifadelerini (*"not slow" = 0 puan*) filtreleyerek gerçek acı noktalarını ağırlıklandırır.
* ⚔️ **Hibrit Rakip Benchmark'ı (Faz 3):** Hem kurumsal/kapalı kaynaklı pazar liderlerinin (SonarQube, Snyk, GitHub Security vb.) fiyat ve dağıtım modellerini hem de GitHub açık kaynak projelerinin canlı telemetrisini (yıldız, fork, açık issue) haritalandırır.
* ⚖️ **Madde Bazlı Hukuki Zırh (Faz 4):** Google Patents öncelikli teknik (prior art) taraması yapar; **EU AI Act Madde 5(1) (Yasaklı), Madde 6 & Ek III (Yüksek Risk), Madde 50 (Şeffaflık)** ve GDPR Madde 5/25/32 üzerinden madde bazlı regülasyon analizi sunar.
* 🛠️ **Otomatik Sistem Mimarisi (Faz 5):** Bilişsel yükü sıfırlayan Tauri v2 + Radix UI ve yüksek performanslı Rust/Go çekirdek seçimini otomatik gerekçelendirir.
* 🚀 **TRIZ Radikal İcatları & Fizibilite Kapısı (Faz 6):** Sistem çelişkilerini TRIZ prensipleriyle çözer. Üretilen her icat için **TRL seviyesi, ICE skoru, WTP hipotezi, 3 kritik hata modu ve Mermaid mimari şeması** otomatik üretilir.

---

## 🖥️ Hızlı Başlangıç: Tek Komutla 6 Fazlı Canlı Araştırma (CLI)

```bash
# Markdown Raporu + Güvenlik Zırhlı Mermaid & Dark Mode HTML Paneli:
python run_innovator.py "Autonomous Code Analysis" --output analiz.md --html panel.html
```

---

## 🧪 Regresyon & Doğruluk Benchmark Skorkartı

Zobar Skill, çıktı tutarlılığını, yasal madde isabetini ve kanıt taksonomisini **otomatik bir test ortamında (`benchmarks/run_benchmarks.py`)** denetler:

```bash
python benchmarks/run_benchmarks.py
```

| Kod | Test Edilen Senaryo | Resmî Hukuki Emsal / Yasal Dayanak | Durum |
| :--- | :--- | :--- | :--- |
| **CASE-01** | Klinik Tıbbi Teşhis ve Hasta Karar Desteği | MDR (AB) 2017/745 Kural 11 & AI Act Madde 6(1) (Yüksek Risk) | **100/100 (Başarılı)** |
| **CASE-02** | Hastane İdari Randevu & Vardiya Planlama | MDR 2017/745 Ek VIII Kural 11 (İdari Yazılım Muafiyeti) | **100/100 (Başarılı)** |
| **CASE-03** | Geliştirici Aracı, AST Ayrıştırıcı & Statik Analiz | EU AI Act Madde 2(8) (Ar-Ge ve Geliştirici Aracı Muafiyeti) | **100/100 (Başarılı)** |
| **CASE-04** | Kullanıcıyla Doğrudan Etkileşen Sohbet Botu | EU AI Act Madde 50(1) (Doğrudan İnsan Etkileşimi Şeffaflığı) | **100/100 (Başarılı)** |
| **CASE-05** | Sosyal Puanlama & İzinsiz Biyometrik Veri | EU AI Act Madde 5(1)(a)-(h) (Yasaklı Uygulama) | **100/100 (Başarılı)** |
| **CASE-06** | Tüketici Kredi Puanlama ve Finansal Risk | EU AI Act Ek III Nokta 5(b) & EDPB WP251 (Yüksek Risk) | **100/100 (Başarılı)** |
| **CASE-07** | Dağıtık Mikro-Servis Ağı & API Gateway | EU AI Act Recital 34 (Genel Altyapı / Minimal Risk) | **100/100 (Başarılı)** |

Detaylı denetim günlüğü için [BENCHMARK_REPORT.md](./benchmarks/BENCHMARK_REPORT.md) dosyasını inceleyin.

---

## 📁 Proje Yapısı

```text
zobar-skill/
├── SKILL.md                          # Zobar Skill ana talimatnamesi ve icra protokolü
├── README.md                         # Vitrin dokümantasyonu, benchmark ve kurulum
├── LICENSE                           # Açık kaynak lisansı (MIT)
├── run_innovator.py                  # 6 Fazlı otonom araştırma ve sentez CLI'ı
├── scripts/                          # Sıfır-bağımlılık yerleşik CLI motorları
│   ├── fetch_academic_papers.py      # arXiv API üzerinden akademik makale çekici (HTTPS)
│   ├── mine_user_sentiment.py        # Hacker News & Reddit olumsuzlama filtreli şikayet madencisi
│   ├── benchmark_competitors.py      # Hibrit rakip motoru: Ticari pazar liderleri + GitHub telemetrisi
│   ├── search_prior_art.py           # Google Patents üzerinden ön patent & prior art tarayıcı
│   ├── scan_regulations.py           # Madde bazlı mevzuat denetleyicisi (EU AI Act Madde 5/6/50, GDPR)
│   ├── synthesize_architecture.py    # Faz 5: Otomatik sistem mimarisi ve UI spesifikasyon motoru
│   ├── validate_inventions.py        # Faz 6: TRIZ radikal icat, TRL/WTP doğrulama ve Mermaid mimarı
│   └── export_html_report.py         # XSS korumalı, CSP uyumlu ('unsafe-eval' içermez) HTML çevirici
├── benchmarks/                       # Regresyon ve doğrulama denetim sistemi
│   ├── run_benchmarks.py             # Sıfır toleranslı otomatik benchmark çalıştırıcısı
│   ├── BENCHMARK_REPORT.md           # Üretilen denetim ve başarı skorkartı
│   └── benchmark_results.json        # Makine tarafından okunabilir benchmark çıktısı
├── references/                       # Zihinsel modeller, First Principles, TRIZ matrisi
├── tests/                            # 12/12 Çevrimdışı mock'lu deterministik birim test paketi
└── examples/                         # Örnek rapor (Markdown + HTML formatında)
```

---

## ⚖️ Metodolojik Sınırlar ve Doğruluk Beyanı
1. **Benchmark Kapsamı:** Benchmark testleri, sistemin kodlanmış yasal mantık kuralları ve mimari seçimlerle **iç regresyon tutarlılığını** doğrular. Bağımsız bir baro avukatının hukuki görüşü veya pazar gelir garantisi yerine geçmez.
2. **Akademik Kanıt Düzeyi:** `fetch_academic_papers.py` betiği, açık erişimli pre-print deposu olan arXiv üzerinden veri çeker. Pre-print'ler en son bilimsel gelişmeleri yansıtmakla birlikte henüz hakemli dergi onayından geçmemiş olabilir.
3. **Fikri Mülkiyet & Mevzuat:** `search_prior_art.py` ve `scan_regulations.py` araçları yalnızca teknik araştırma ve madde bazlı ön analiz sağlar; resmi Faaliyet Serbestisi (FTO) incelemesi yerine geçmez.

---

## 📄 Lisans
Bu proje [MIT Lisansı](./LICENSE) kapsamında açık kaynak olarak sunulmuştur.
