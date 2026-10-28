#!/usr/bin/env python3
"""
Frontier Innovator — End-to-End 6-Phase Research & Invention Orchestrator
Executes live academic pre-print retrieval, multi-source community friction mining,
empirical competitor benchmarking, patent prior art screening, and regulatory mapping.
Outputs sanitized Markdown dossiers and XSS-hardened HTML dashboards.
"""

import sys
import argparse
import datetime
from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.mine_user_sentiment import search_sentiment
from scripts.benchmark_competitors import benchmark_competitors
from scripts.search_prior_art import search_patents
from scripts.scan_regulations import evaluate_compliance
from scripts.export_html_report import export_to_html

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BANNER = r"""
========================================================================
   ⚡ FRONTIER INNOVATOR — DEEP-TECH & RADICAL INVENTION ENGINE ⚡
========================================================================
"""

def generate_dossier(topic: str, output_path: str = None, html_path: str = None):
    print(BANNER)
    # Explicit UTC timestamp conversion
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"[*] Hedef Konu / Problem: {topic}")
    print(f"[*] Başlangıç Zamanı     : {now_utc}")
    print("[*] 6 Fazlı canlı araştırma akışı başlatılıyor...\n")

    # 1. Akademik Ön Baskılar (arXiv HTTPS)
    print("[1/5] 🏛️ FAZ 1: arXiv üzerinden akademik literatür ve ön baskılar taranıyor...")
    papers = fetch_arxiv_papers(topic, max_results=3)
    if papers:
        print(f"      -> {len(papers)} adet akademik ön baskı (pre-print) tespit edildi.")
    else:
        print("      [-] arXiv araması sonuç vermedi veya bağlantı kurulamadı.")

    # 2. Topluluk Kullanıcı Acıları & Sürtünme Madenciliği (HN + Reddit)
    print("[2/5] 💬 FAZ 2: Hacker News ve Reddit topluluklarından gerçek kullanıcı sürtünmeleri çekiliyor...")
    sentiment_data = search_sentiment(topic, max_comments=4)
    comments = sentiment_data.get("comments", [])
    sources_summary = sentiment_data.get("summary", "")
    if comments:
        print(f"      -> {len(comments)} adet filtrelenmiş kullanıcı deneyimi analiz edildi. ({sources_summary})")
    else:
        print("      [-] Topluluk kanallarından filtrelenmiş şikayet kaydı bulunamadı.")

    # 3. Canlı Rakip & Ekosistem Benchmark'ı (GitHub API)
    print("[3/5] ⚔️ FAZ 3: GitHub ekosistemi üzerinden pazar lideri ve açık kaynak rakipler taranıyor...")
    comp_res = benchmark_competitors(topic, max_results=3)
    competitors = comp_res.get("competitors", [])
    if competitors:
        print(f"      -> {len(competitors)} adet aktif rakip proje tespit edildi (Toplam havuz: {comp_res.get('total_found', 0)}).")
    else:
        print("      [-] Doğrudan eşleşen rakip repo bulunamadı.")

    # 4. Ön Patent & Prior Art Taraması (Google Patents)
    print("[4/5] ⚖️ FAZ 4A: Google Patents üzerinden öncelikli teknik (prior art) taranıyor...")
    patents = search_patents(topic, max_results=3)
    if patents:
        print(f"      -> {len(patents)} adet öncelikli teknik (prior art) ve patent başvurusu tespit edildi.")
    else:
        print("      [-] Patent veritabanından eşleşen kayıt bulunamadı veya arama zaman aşımına uğradı.")

    # 5. Regülasyon & Mevzuat Taraması (EU AI Act & KVKK/GDPR)
    print("[5/5] 📜 FAZ 4B: EU AI Act, KVKK/GDPR ve açık kaynak lisans sınırları taranıyor...")
    compliance = evaluate_compliance(topic)
    print(f"      -> Regülasyon Seviyesi: {compliance['eu_ai_act']['tier']}\n")

    # Rapor Taslağını İnşa Et
    dossier_lines = [
        f"# FRONTIER INNOVATOR DOSYASI: {topic.upper()}",
        f"**Rapor Tarihi (UTC):** {now_utc} | **Motor:** Frontier Innovator v2.5-Autonomous\n",
        "---",
        "## 🏛️ FAZ 1: Akademik Zemin & Ön Baskı Literatürü (arXiv)",
        "> ⚠️ **Akademik Kanıt Notu:** Aşağıdaki çalışmalar arXiv açık erişim ön baskı (pre-print) deposundan derlenmiştir. Bu çalışmalar en güncel teorik sınırları sunmakla birlikte henüz hakemli dergi onayından geçmemiş olabilir. Bulgular [Literatür Ön Baskısı] olarak etiketlenmiştir.\n",
    ]

    if papers:
        for i, p in enumerate(papers, 1):
            dossier_lines.append(f"### {i}. {p['title']}")
            dossier_lines.append(f"- **Yazarlar:** {p['authors']}")
            dossier_lines.append(f"- **Tarih:** {p['published']} | **Kanıt Türü:** {p.get('evidence_grade', 'Ön Baskı')}")
            dossier_lines.append(f"- **Bağlantı:** {p['url']}")
            dossier_lines.append(f"- **Teorik Özet:** {p['summary']}\n")
    else:
        dossier_lines.append("[-] Bu konuyla doğrudan eşleşen arXiv makalesi bulunamadı veya servis zaman aşımına uğradı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## 💬 FAZ 2: Sahadaki Kullanıcı Sürtünmeleri & Şikayet Madenciliği")
    dossier_lines.append(f"> 📌 **Veri Kapsamı:** {sources_summary if sources_summary else 'Hacker News ve Reddit'}. Bu veriler örnekleme niteliğinde olup tüm pazar evrenini temsil etmeyebilir; eğilim analizi sağlar.\n")

    if comments:
        for i, c in enumerate(comments, 1):
            friction_level = "Yüksek Acı (Ağır Şikayet)" if c.get("friction_score", 0) >= 3 else "Kullanıcı Geri Bildirimi"
            dossier_lines.append(f"### Şikayet #{i} [{c.get('source', 'Topluluk')}] — {friction_level} (@{c['author']} — {c['date']})")
            dossier_lines.append(f"- **Konu / Başlık:** {c['title']}")
            dossier_lines.append(f"- **Doğrudan URL:** {c['url']}")
            dossier_lines.append(f"- **Ağırlıklı Sürtünme Skoru:** {c.get('friction_score', 0)}")
            dossier_lines.append(f"- **Filtresiz Görüş:** > {c['text']}\n")
    else:
        dossier_lines.append("[-] Belirtilen arama kriterlerine uyan şikayet verisi bulunamadı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## ⚔️ FAZ 3: Canlı Rakip Teardown & Ekosistem Benchmark'ı")
    dossier_lines.append("> 📊 **Veri Kaynağı:** GitHub API Canlı Metrikleri. Projelerin popülaritesi, bakım sıklığı ve açık issue yükü incelenmiştir.\n")

    if competitors:
        for i, cp in enumerate(competitors, 1):
            dossier_lines.append(f"### Rakip #{i}: {cp['name']} (⭐️ {cp['stars']:,} | 🍴 {cp['forks']:,} | ⚠️ {cp['open_issues']} Issue)")
            dossier_lines.append(f"- **Açıklama:** {cp['description']}")
            dossier_lines.append(f"- **Teknoloji / Lisans:** {cp['language']} | Lisans: {cp['license']}")
            dossier_lines.append(f"- **Son Aktivite:** {cp['last_active']}")
            dossier_lines.append(f"- **Repo Bağlantısı:** {cp['url']}\n")
    else:
        dossier_lines.append("[-] Canlı GitHub rakip kaydı bulunamadı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## ⚖️ FAZ 4: Hukuki Zırh, Regülasyon & Ön Patent Taraması")
    dossier_lines.append("> ⚠️ **Yasal Sorumluluk Reddi:** Bu tarama yalnızca teknik öncelikli teknik (prior art) taraması ve regülasyon ön değerlendirmesidir; resmi patent geçerliliği veya Faaliyet Serbestisi (FTO) teşkil etmez.\n")

    dossier_lines.append(f"### 🇪🇺 EU AI Act Seviyesi: {compliance['eu_ai_act']['tier']}")
    dossier_lines.append(f"- **Gerekçe:** {compliance['eu_ai_act']['justification']}\n")

    dossier_lines.append("### 🔒 Veri Egemenliği & Gizlilik (KVKK / GDPR):")
    for priv in compliance["data_privacy"]:
        dossier_lines.append(f"- {priv}")
    dossier_lines.append("")

    if patents:
        dossier_lines.append("### 📜 Önceki Teknik (Prior Art) Kayıtları:")
        for i, pt in enumerate(patents, 1):
            dossier_lines.append(f"- **Kayıt #{i}:** [{pt['id']}] {pt['title']} — *Hak Sahibi:* {pt['assignee']} ({pt['filing_date']})")
            dossier_lines.append(f"  *Bağlantı:* {pt['url']}")
            if pt.get('snippet'):
                dossier_lines.append(f"  *Özet:* {pt['snippet']}")
        dossier_lines.append("")
    else:
        dossier_lines.append("[-] Bu konuyla doğrudan ilgili açık patent kaydı bulunamadı veya arama zaman aşımına uğradı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## 🚀 FAZ 5 & 6: İcat & Fizibilite Doğrulama Yönergesi")
    dossier_lines.append("Ajan yukarıdaki ampirik verileri temel alarak aşağıdaki zorunlu alanları doldurmalıdır:")
    dossier_lines.append("1. **Teknik Mimari (Faz 5):** Sürdürülebilir dil ve modern UI bileşen yığını.")
    dossier_lines.append("2. **Fizibilitesi Kanıtlanmış Radikal İcatlar (Faz 6):**")
    dossier_lines.append("   - **TRL Olgunluk Seviyesi:** [Model Tahmini / Literatür İspatı]")
    dossier_lines.append("   - **ICE Skoru:** Etki: /10 | Güven: /10 | Kolaylık: /10")
    dossier_lines.append("   - **Ticari Talep & WTP:** [Pazar Hipotezi mi, Müşteri Verisi Mi? Alternatif Maliyet]")
    dossier_lines.append("   - **Kritik Hata Modları:** Extreme koşullarda çökme senaryoları ve mimari çözümleri.")
    dossier_lines.append("3. **Sistem Mimarisi (Mermaid):** İcatların veri akışını gösteren şema.\n")

    full_dossier = "\n".join(dossier_lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_dossier)
        print(f"[+] Araştırma dosyası (Markdown) kaydedildi: {output_path}")

    if html_path:
        rendered_html = export_to_html(full_dossier, title=f"Frontier Dossier: {topic}")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"[+] Güvenlik zırhlı görsel Dashboard (HTML/Mermaid) kaydedildi: {html_path}")

    if not output_path and not html_path:
        print(full_dossier)

def main():
    parser = argparse.ArgumentParser(description="Frontier Innovator Full-Spectrum Research Orchestrator")
    parser.add_argument("topic", nargs="?", help="Araştırılacak ve inovasyon yapılacak konu")
    parser.add_argument("--output", "-o", help="Çıktının kaydedileceği Markdown dosya yolu (örn: dossier.md)")
    parser.add_argument("--html", help="Görsel HTML Dashboard olarak kaydedilecek yol (örn: report.html)")
    args = parser.parse_args()

    topic = args.topic
    if not topic:
        topic = input("Lütfen araştırılacak veya inovasyon yapılacak konuyu girin: ").strip()
        if not topic:
            print("[-] Konu belirtilmedi. Çıkılıyor.")
            sys.exit(1)

    generate_dossier(topic, args.output, args.html)

if __name__ == "__main__":
    main()
