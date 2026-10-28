#!/usr/bin/env python3
"""
Patent & Prior Art Searcher for Frontier Innovator Skill.
Queries Google Patents public data without external dependencies to verify
patent landscapes, freedom to operate (FTO), and existing corporate inventions.
"""

import sys
import json
import urllib.request
import urllib.parse
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def search_patents(query: str, max_results: int = 5):
    encoded_query = urllib.parse.quote(query)
    url = f"https://patents.google.com/xhr/query?url=q%3D{encoded_query}&exp="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"[-] Hata: Patent araması başarısız: {e}", file=sys.stderr)
        return []

    results = []
    clusters = data.get("results", {}).get("cluster", [])
    if not clusters:
        return []

    patent_entries = clusters[0].get("result", [])

    for entry in patent_entries[:max_results]:
        pat = entry.get("patent", {})
        pub_number = pat.get("publication_number", "Bilinmiyor")
        title = pat.get("title", "Başlıksız Patent").strip().replace("\n", " ")
        assignee = pat.get("assignee", "Bilinmeyen Başvuran")
        filing_date = pat.get("filing_date", "Bilinmeyen Tarih")
        snippet = pat.get("snippet", "").strip().replace("\n", " ")
        patent_url = f"https://patents.google.com/patent/{pub_number}/en"

        results.append({
            "id": pub_number,
            "title": title,
            "assignee": assignee,
            "filing_date": filing_date,
            "url": patent_url,
            "snippet": snippet[:280] + "..." if len(snippet) > 280 else snippet
        })

    return results

def main():
    parser = argparse.ArgumentParser(description="Search public patents and prior art.")
    parser.add_argument("query", help="Invention concept or technology to search patents for")
    parser.add_argument("--max", type=int, default=5, help="Maximum number of patents (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚖️ PATENT & ÖNCEKİ TEKNİK (PRIOR ART) TARAMASI: '{args.query}'")
    print(f"=======================================================\n")

    patents = search_patents(args.query, args.max)
    if not patents:
        print("[-] Uygun patent kaydı bulunamadı veya arama zaman aşımına uğradı.")
        return

    for idx, p in enumerate(patents, 1):
        print(f"[{idx}] {p['title']}")
        print(f"    📜 Patent No: {p['id']}")
        print(f"    🏢 Sahip    : {p['assignee']}")
        print(f"    📅 Başvuru  : {p['filing_date']}")
        print(f"    🔗 İncele   : {p['url']}")
        if p['snippet']:
            print(f"    📝 Özet     : {p['snippet']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
