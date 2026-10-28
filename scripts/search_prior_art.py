#!/usr/bin/env python3
"""
Patent & Prior Art Screener for Frontier Innovator Skill.
Queries Google Patents public data without external dependencies for preliminary
prior art screening and landscape exploration.

LEGAL DISCLAIMER:
This tool provides preliminary automated prior art screening for technical research
purposes only. It DOES NOT constitute legal advice or an official Freedom-to-Operate
(FTO) patent infringement clearance opinion. Consult a registered patent attorney for
definitive legal validity and clearance.
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
        print(f"[-] Patent tarama uyarısı (Hizmet yanıt vermedi): {e}", file=sys.stderr)
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
        assignee = pat.get("assignee", "Bilinmeyen Başvuran / Şirket")
        filing_date = pat.get("filing_date", "Tarih Belirtilmemiş")
        snippet = pat.get("snippet", "").strip().replace("\n", " ")
        patent_url = f"https://patents.google.com/patent/{pub_number}/en"

        results.append({
            "id": pub_number,
            "title": title,
            "assignee": assignee,
            "filing_date": filing_date,
            "url": patent_url,
            "legal_nature": "Öncelikli Teknik (Prior Art Referansı)",
            "snippet": snippet[:280] + "..." if len(snippet) > 280 else snippet
        })

    return results

def main():
    parser = argparse.ArgumentParser(description="Preliminary patent and prior art screening.")
    parser.add_argument("query", help="Invention concept or technology to search patents for")
    parser.add_argument("--max", type=int, default=5, help="Maximum number of patents (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚖️ ÖN PATENT & ÖNCEKİ TEKNİK (PRIOR ART) TARAMASI: '{args.query}'")
    print(f" ⚠️ Yasal Uyarı: Bu tarama FTO (Faaliyet Serbestisi) garantisi vermez.")
    print(f"=======================================================\n")

    patents = search_patents(args.query, args.max)
    if not patents:
        print("[-] Uygun patent kaydı bulunamadı veya servis geçici olarak kullanılamıyor.")
        return

    for idx, p in enumerate(patents, 1):
        print(f"[{idx}] {p['title']}")
        print(f"    📜 Tescil No  : {p['id']}")
        print(f"    🏢 Sahip / IP : {p['assignee']}")
        print(f"    📅 Tarih      : {p['filing_date']}")
        print(f"    🔗 İncele     : {p['url']}")
        if p['snippet']:
            print(f"    📝 Özet       : {p['snippet']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
