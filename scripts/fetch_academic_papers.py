#!/usr/bin/env python3
"""
Academic Literature & Pre-print Fetcher for Frontier Innovator Skill.
Queries the official arXiv API without external dependencies to extract
theoretical models, academic pre-prints, and professor/researcher insights.

DISCLAIMER: arXiv is an open-access archive for scholarly pre-prints.
Pre-prints provide cutting-edge theoretical groundwork but may not yet have
undergone formal journal peer review.
"""

import sys
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import argparse

# Ensure UTF-8 output on all operating systems and Windows codepages
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def fetch_arxiv_papers(query: str, max_results: int = 5):
    encoded_query = urllib.parse.quote(f"all:{query}")
    url = f"http://export.arxiv.org/api/query?search_query={encoded_query}&start=0&max_results={max_results}&sortBy=relevance&sortOrder=descending"

    headers = {
        "User-Agent": "FrontierInnovatorBot/1.0 (Academic pre-print research tool)"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read()
    except Exception as e:
        print(f"[-] Akademik makale çekme hatası: {e}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(xml_data)
    except Exception as e:
        print(f"[-] XML çözümleme hatası: {e}", file=sys.stderr)
        return []

    namespace = {"atom": "http://www.w3.org/2005/Atom"}

    entries = []
    for entry in root.findall("atom:entry", namespace):
        title_el = entry.find("atom:title", namespace)
        summary_el = entry.find("atom:summary", namespace)
        published_el = entry.find("atom:published", namespace)
        id_el = entry.find("atom:id", namespace)

        title = title_el.text.strip().replace("\n", " ") if title_el is not None and title_el.text else "Başlıksız Çalışma"
        summary = summary_el.text.strip().replace("\n", " ") if summary_el is not None and summary_el.text else ""
        published = published_el.text.strip()[:10] if published_el is not None and published_el.text else "Tarih Yok"
        id_url = id_el.text.strip() if id_el is not None and id_el.text else ""

        authors = [
            author.find("atom:name", namespace).text.strip()
            for author in entry.findall("atom:author", namespace)
            if author.find("atom:name", namespace) is not None and author.find("atom:name", namespace).text
        ]

        entries.append({
            "title": title,
            "authors": ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else ""),
            "published": published,
            "evidence_grade": "Akademik Ön Baskı (arXiv Pre-print)",
            "summary": summary[:380] + "..." if len(summary) > 380 else summary,
            "url": id_url
        })

    return entries

def main():
    parser = argparse.ArgumentParser(description="Fetch academic pre-prints from arXiv.")
    parser.add_argument("query", help="Topic or query string to search academic papers for")
    parser.add_argument("--max", type=int, default=5, help="Maximum number of papers (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 🏛️ AKADEMİK LİTERATÜR & ÖN BASKI (PRE-PRINT) TARAMASI: '{args.query}'")
    print(f"=======================================================\n")

    papers = fetch_arxiv_papers(args.query, args.max)
    if not papers:
        print("[-] Uygun akademik makale bulunamadı veya bağlantı kurulamadı.")
        return

    for idx, p in enumerate(papers, 1):
        print(f"[{idx}] {p['title']}")
        print(f"    👨‍🔬 Yazarlar     : {p['authors']}")
        print(f"    📅 Tarih        : {p['published']}")
        print(f"    🏷️ Kanıt Düzeyi : {p['evidence_grade']}")
        print(f"    🔗 Bağlantı     : {p['url']}")
        print(f"    📝 Özet         : {p['summary']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
