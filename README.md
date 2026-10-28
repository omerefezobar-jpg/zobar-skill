# ⚡ Zobar Skill: Deep-Tech, Market & Radical Invention Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI & Quality Gate](https://github.com/omerefezobar-jpg/zobar-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/omerefezobar-jpg/zobar-skill/actions)
[![Benchmark Score: 100%](https://img.shields.io/badge/Benchmark-100%25%20Verified-brightgreen.svg)](./benchmarks/BENCHMARK_REPORT.md)
[![Antigravity Compatible](https://img.shields.io/badge/Antigravity-Agent%20Skill-8A2BE2.svg)](https://github.com/omerefezobar-jpg/zobar-skill)
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

## 🏆 Doğruluk & Kalite Benchmark Skorkartı

Zobar Skill, sektörde bir ilki gerçekleştirerek çıktı doğruluğunu, yasal madde isabetini ve kanıt taksonomisini **otomatik bir test ortamında (`benchmarks/run_benchmarks.py`)** ölçer:

```bash
python benchmarks/run_benchmarks.py
```

| Test Kodu | Test Edilen Vaka | Hedeflenen Yasal & Mimari Kriter | Başarı Skoru |
| :--- | :--- | :--- | :--- |
| **CASE-01** | Kritik Tıbbi Teşhis ve Otonom Karar Sistemi | EU AI Act Madde 6 & Ek III (Yüksek Risk) + Rust | **100/100** |
| **CASE-02** | Yüksek Başarımlı AST Derleyici & Analiz Motoru | EU AI Act Madde 69 (Genel Yazılım) + Rust AST | **100/100** |
| **CASE-03** | Üretken Kod Asistanı & Otonom LLM Ajanı | EU AI Act Madde 50 (Şeffaflık) + Hibrit Mimari | **100/100** |

Detaylı denetim raporu için [BENCHMARK_REPORT.md](./benchmarks/BENCHMARK_REPORT.md) dosyasını inceleyin.

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
├── benchmarks/                       # Doğruluk ve kalite ölçüm sistemi
│   ├── run_benchmarks.py             # Otomatik benchmark çalıştırıcısı
│   ├── BENCHMARK_REPORT.md           # Üretilen denetim ve başarı skorkartı
│   └── benchmark_results.json        # Makine tarafından okunabilir benchmark çıktısı
├── references/                       # Zihinsel modeller, First Principles, TRIZ matrisi
├── tests/                            # 12/12 Çevrimdışı mock'lu deterministik birim test paketi
└── examples/                         # Örnek rapor (Markdown + HTML formatında)
```

---

## 🧪 Testler (Unit Testing)

Tüm modüller, güvenlik duvarları ve ayrıştırıcılar sıfır harici ağ bağımlılığıyla mock'lanmış birim testlerle korunur:

```bash
python -m unittest discover tests
```
*(12/12 Test — 0.003s içinde kusursuz başarıyla tamamlanır).*

---

## 🚀 Kurulum (Installation)

### Seçenek 1: Antigravity Projenize Eklemek (Önerilen)
Projenizin kök dizininde `.agents/skills/` altına bu repoyu klonlayın:

```bash
mkdir -p .agents/skills
git clone https://github.com/omerefezobar-jpg/zobar-skill.git .agents/skills/zobar-skill
```

### Seçenek 2: Global Olarak Tüm Projelerinizde Kullanmak
Tüm bilgisayarınızdaki Antigravity oturumlarında geçerli olması için:

```bash
# Windows (PowerShell)
git clone https://github.com/omerefezobar-jpg/zobar-skill.git "$env:USERPROFILE\.gemini\config\skills\zobar-skill"

# macOS / Linux
git clone https://github.com/omerefezobar-jpg/zobar-skill.git ~/.gemini/config/skills/zobar-skill
```

---

## ⚖️ Yasal ve Bilimsel Sorumluluk Reddi
1. **Akademik Kanıt Düzeyi:** `fetch_academic_papers.py` betiği, açık erişimli pre-print deposu olan arXiv üzerinden veri çeker. Pre-print'ler en son bilimsel gelişmeleri yansıtmakla birlikte henüz hakemli dergi onayından geçmemiş olabilir.
2. **Fikri Mülkiyet & Mevzuat:** `search_prior_art.py` ve `scan_regulations.py` araçları yalnızca teknik araştırma ve madde bazlı ön analiz sağlar; Baro üyesi bir avukatın resmi Faaliyet Serbestisi (FTO) veya hukuki mütalaası yerine geçmez.

---

## 📄 Lisans
Bu proje [MIT Lisansı](./LICENSE) kapsamında açık kaynak olarak sunulmuştur.
