#!/usr/bin/env python3
"""
Frontier Innovator — Unified Deep-Tech Research & Dossier Orchestrator
Executes multi-source academic pre-print retrieval, community friction mining,
and preliminary patent prior-art screening. Outputs both Markdown dossiers
and sanitized, XSS-hardened HTML dashboards.
"""

import sys
import argparse
import datetime
from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.mine_user_sentiment import search_sentiment
from scripts.search_prior_art import search_patents
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
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    print(f"[*] Hedef Konu / Problem: {topic}")
    print(f"[*] Başlangıç Zamanı     : {now_str}")
    print("[*] Canlı veri toplama ve analiz başlatılıyor...\n")

    # 1. Akademik Ön Baskılar (arXiv)
    print("[1/3] 🏛️ arXiv üzerinden akademik literatür ve ön baskılar (pre-prints) taranıyor...")
    papers = fetch_arxiv_papers(topic, max_results=3)
    if papers:
        print(f"      -> {len(papers)} adet akademik ön baskı (pre-print) tespit edildi.")
    else:
        print("      [-] arXiv araması sonuç vermedi veya bağlantı kurulamadı.")

    # 2. Topluluk Kullanıcı Acıları & Sürtünme Madenciliği (HN + Reddit)
    print("[2/3] 💬 Hacker News ve Reddit topluluklarından gerçek kullanıcı sürtünmeleri çekiliyor...")
    sentiment_data = search_sentiment(topic, max_comments=4)
    comments = sentiment_data.get("comments", []) if isinstance(sentiment_data, dict) else sentiment_data
    sources_summary = sentiment_data.get("summary", "") if isinstance(sentiment_data, dict) else ""
    if comments:
        print(f"      -> {len(comments)} adet filtrelenmiş kullanıcı deneyimi/şikayeti analiz edildi. {sources_summary}")
    else:
        print("      [-] Topluluk kanallarından filtrelenmiş şikayet kaydı bulunamadı.")

    # 3. Ön Patent & Prior Art Taraması (Google Patents)
    print("[3/3] ⚖️ Google Patents üzerinden öncelikli teknik (prior art) ve tescil haritası taranıyor...")
    patents = search_patents(topic, max_results=3)
    if patents:
        print(f"      -> {len(patents)} adet öncelikli teknik (prior art) ve patent başvurusu tespit edildi.")
    else:
        print("      [-] Patent veritabanından eşleşen kayıt bulunamadı veya arama zaman aşımına uğradı.\n")

    # Rapor Taslağını İnşa Et
    dossier_lines = [
        f"# FRONTIER INNOVATOR DOSYASI: {topic.upper()}",
        f"**Oluşturulma Tarihi:** {now_str} | **Motor:** Frontier Innovator v2.0-Hardened\n",
        "---",
        "## 🏛️ FAZ 1: Akademik Zemin & Ön Baskı Literatürü (arXiv)",
        "> ⚠️ **Akademik Kanıt Notu:** Aşağıdaki çalışmalar arXiv açık erişim ön baskı (pre-print) deposundan derlenmiştir. Bu çalışmalar en güncel teorik sınırları sunmakla birlikte henüz hakemli dergi onayından geçmemiş olabilir.\n",
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
    dossier_lines.append(f"> 📌 **Veri Kapsamı:** {sources_summary if sources_summary else 'Hacker News ve Reddit toplulukları'}. Sürtünme skorları bağlamsal acı ve şikayet yoğunluğunu gösterir.\n")

    if comments:
        for i, c in enumerate(comments, 1):
            friction_level = "Yüksek Acı" if c.get("friction_score", 0) >= 2 else "Geri Bildirim"
            dossier_lines.append(f"### Şikayet #{i} [{c.get('source', 'Topluluk')}] — {friction_level} (@{c['author']} — {c['date']})")
            dossier_lines.append(f"- **Konu / Gönderi:** {c['title']}")
            dossier_lines.append(f"- **Kaynak URL:** {c['url']}")
            dossier_lines.append(f"- **Kullanıcı İfadesi:** > {c['text']}\n")
    else:
        dossier_lines.append("[-] Belirtilen arama kriterlerine uyan şikayet verisi bulunamadı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## ⚖️ FAZ 4: Ön Patent & Prior Art İncelemesi")
    dossier_lines.append("> ⚠️ **Yasal Sorumluluk Reddi:** Bu tarama yalnızca teknik öncelikli teknik (prior art) taramasıdır. Resmi patent geçerliliği veya Faaliyet Serbestisi (Freedom to Operate - FTO) garantisi vermez.\n")

    if patents:
        for i, pt in enumerate(patents, 1):
            dossier_lines.append(f"### Kayıt #{i}: {pt['title']}")
            dossier_lines.append(f"- **Referans No:** {pt['id']} | **Hak Sahibi/Başvuran:** {pt['assignee']} ({pt['filing_date']})")
            dossier_lines.append(f"- **Patent URL:** {pt['url']}")
            if pt.get('snippet'):
                dossier_lines.append(f"- **Kapsam Özeti:** {pt['snippet']}\n")
    else:
        dossier_lines.append("[-] Bu konuyla doğrudan ilgili açık patent kaydı bulunamadı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## ⚔️ FAZ 3, 5 & 6: İcra ve Doğrulama Yönergesi")
    dossier_lines.append("Ajan yukarıdaki bulguları kullanarak şu zorunlu çıktıları üretmelidir:")
    dossier_lines.append("1. **Rakip Teardown & 10x Moat:** Rakiplerin yapısal kör noktaları.")
    dossier_lines.append("2. **Teknik Mimari & Bileşenler:** Dil, kütüphane ve UI seçimi.")
    dossier_lines.append("3. **Fizibilite Kanıtlı Radikal İcatlar (Zorunlu):**")
    dossier_lines.append("   - Her icat için: `TRL Olgunluk Seviyesi (Model Tahmini)`, `ICE Skoru`, `WTP & Ödeme Gerekçesi`, `Kritik Hata Modları`.")
    dossier_lines.append("   - Sistem mimarisini ve inovasyon akışını gösteren **Mermaid diyagramı**.\n")

    full_dossier = "\n".join(dossier_lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_dossier)
        print(f"[+] Araştırma dosyası (Markdown) kaydedildi: {output_path}")

    if html_path:
        # STRICT SECURITY: Always use export_to_html for safe title escaping and HTML conversion
        rendered_html = export_to_html(full_dossier, title=f"Frontier Dossier: {topic}")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"[+] Güvenlik zırhlı görsel Dashboard (HTML/Mermaid) kaydedildi: {html_path}")

    if not output_path and not html_path:
        print(full_dossier)

def main():
    parser = argparse.ArgumentParser(description="Frontier Innovator Unified Research Orchestrator")
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
