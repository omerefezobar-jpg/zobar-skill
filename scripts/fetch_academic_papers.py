#!/usr/bin/env python3
"""
Academic Paper Fetcher for Frontier Innovator Skill.
Queries the official arXiv API without external dependencies to extract
ground-truth academic papers, abstracts, and authors for a given domain.
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
        "User-Agent": "FrontierInnovatorBot/1.0 (academic research tool)"
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read()
    except Exception as e:
        print(f"[-] Error fetching academic papers: {e}", file=sys.stderr)
        return []

    root = ET.fromstring(xml_data)
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    
    entries = []
    for entry in root.findall("atom:entry", namespace):
        title = entry.find("atom:title", namespace).text.strip().replace("\n", " ")
        summary = entry.find("atom:summary", namespace).text.strip().replace("\n", " ")
        published = entry.find("atom:published", namespace).text.strip()[:10]
        id_url = entry.find("atom:id", namespace).text.strip()
        
        authors = [
            author.find("atom:name", namespace).text.strip()
            for author in entry.findall("atom:author", namespace)
        ]
        
        entries.append({
            "title": title,
            "authors": ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else ""),
            "published": published,
            "summary": summary[:350] + "..." if len(summary) > 350 else summary,
            "url": id_url
        })
        
    return entries

def main():
    parser = argparse.ArgumentParser(description="Fetch academic papers from arXiv.")
    parser.add_argument("query", help="Topic or query string to search academic papers for")
    parser.add_argument("--max", type=int, default=5, help="Maximum number of papers (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 🏛️ AKADEMİK LİTERATÜR TARAMASI: '{args.query}'")
    print(f"=======================================================\n")

    papers = fetch_arxiv_papers(args.query, args.max)
    if not papers:
        print("[-] Uygun akademik makale bulunamadı veya bağlantı kurulamadı.")
        return

    for idx, p in enumerate(papers, 1):
        print(f"[{idx}] {p['title']}")
        print(f"    👨‍🔬 Yazarlar : {p['authors']}")
        print(f"    📅 Tarih    : {p['published']}")
        print(f"    🔗 Bağlantı : {p['url']}")
        print(f"    📝 Özet     : {p['summary']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
