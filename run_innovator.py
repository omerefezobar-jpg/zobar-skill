#!/usr/bin/env python3
"""
Frontier Innovator — Interactive CLI Research Dossier Generator
Executes live academic literature extraction & real-world user friction mining,
synthesizing an actionable research dossier for the 6-Phase Innovation Protocol.
"""

import sys
import argparse
import os
from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.mine_user_sentiment import search_sentiment
from scripts.search_prior_art import search_patents
from scripts.export_html_report import parse_markdown_to_html, HTML_TEMPLATE

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
    print(f"[*] Hedef Konu / Problem: {topic}")
    print("[*] Canlı veri toplama ve analiz başlatılıyor...\n")

    # Faz 1: Akademik Makaleler
    print("[1/3] 🏛️ arXiv üzerinden akademik literatür ve seminal paper'lar taranıyor...")
    papers = fetch_arxiv_papers(topic, max_results=3)
    print(f"      -> {len(papers)} adet hakemli akademik çalışma tespit edildi.")

    # Faz 2: Kullanıcı Acıları & Şikayet Madenciliği
    print("[2/3] 💬 Topluluklardan gerçek kullanıcı şikayetleri ve sürtünmeler çekiliyor...")
    comments = search_sentiment(topic, max_comments=3)
    print(f"      -> {len(comments)} adet filtrelenmiş kullanıcı deneyimi ve acı noktası tespit edildi.")

    # Faz 4: Patent & Önceki Teknik (Prior Art)
    print("[3/3] ⚖️ Google Patents üzerinden fikri mülkiyet ve patent haritası taranıyor...")
    patents = search_patents(topic, max_results=3)
    print(f"      -> {len(patents)} adet tescilli patent ve kurumsal buluş tespit edildi.\n")

    # Rapor Taslağını İnşa Et
    dossier_lines = [
        f"# FRONTIER INNOVATOR DOSYASI: {topic.upper()}",
        f"*Oluşturulma Tarihi:* 2026 | *Motor:* Frontier Innovator Engine v1.0\n",
        "---",
        "## 🏛️ FAZ 1: Doğrudan Akademik Zemin (arXiv Canlı Çıktıları)",
    ]

    if papers:
        for i, p in enumerate(papers, 1):
            dossier_lines.append(f"### {i}. {p['title']}")
            dossier_lines.append(f"- **Yazarlar:** {p['authors']}")
            dossier_lines.append(f"- **Yayın Tarihi:** {p['published']}")
            dossier_lines.append(f"- **Paper Linki:** {p['url']}")
            dossier_lines.append(f"- **Özet/Tez:** {p['summary']}\n")
    else:
        dossier_lines.append("[-] Bu konuyla doğrudan eşleşen arXiv makalesi bulunamadı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## 💬 FAZ 2: Sahadaki Kullanıcı Acıları & Nefret Sebepleri")

    if comments:
        for i, c in enumerate(comments, 1):
            dossier_lines.append(f"### Şikayet #{i} (@{c['author']} — {c['date']})")
            dossier_lines.append(f"- **Bağlam / Konu:** {c['title']}")
            dossier_lines.append(f"- **Kaynak:** {c['url']}")
            dossier_lines.append(f"- **Filtresiz Görüş:** > {c['text']}\n")
    else:
        dossier_lines.append("[-] Bu konuyla ilgili filtrelenmiş şikayet kaydı bulunamadı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## ⚖️ FAZ 4: Patent & Fikri Mülkiyet Zırhı (Prior Art)")

    if patents:
        for i, pt in enumerate(patents, 1):
            dossier_lines.append(f"### Patent #{i}: {pt['title']}")
            dossier_lines.append(f"- **Tescil No:** {pt['id']} | **Sahip:** {pt['assignee']} ({pt['filing_date']})")
            dossier_lines.append(f"- **Patent Linki:** {pt['url']}")
            if pt['snippet']:
                dossier_lines.append(f"- **İddia Özeti:** {pt['snippet']}\n")
    else:
        dossier_lines.append("[-] Bu konuyla ilgili kayıtlı patent bulunamadı veya arama zaman aşımına uğradı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## ⚔️ FAZ 3, 5 & 6: Ajan İçin İcra Yönergesi")
    dossier_lines.append("Yukarıdaki akademik doğrular, kullanıcı acıları ve patent sınırlarını kullanarak:")
    dossier_lines.append("1. **Rakip Teardown:** Mevcut pazar liderlerinin yapısal açıklarını listele.")
    dossier_lines.append("2. **Teknik Mimari:** Rust/Go/TypeScript bileşen mimarisini seç.")
    dossier_lines.append("3. **Radikal İcat:** Patent ihlali yapmayan, sınırları zorlayan 2-3 yeni icat kurgula ve Mermaid şemasıyla çiz.\n")

    full_dossier = "\n".join(dossier_lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_dossier)
        print(f"[+] Araştırma dosyası (Markdown) kaydedildi: {output_path}")

    if html_path:
        parsed_html = parse_markdown_to_html(full_dossier)
        rendered_html = HTML_TEMPLATE.replace("{{title}}", f"Frontier Dossier: {topic}").replace("{{content}}", parsed_html)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"[+] Görsel Dashboard (HTML/Mermaid) kaydedildi: {html_path}")

    if not output_path and not html_path:
        print(full_dossier)

def main():
    parser = argparse.ArgumentParser(description="Frontier Innovator CLI Dossier Generator")
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
