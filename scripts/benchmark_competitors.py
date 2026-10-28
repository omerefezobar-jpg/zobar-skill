#!/usr/bin/env python3
"""
Competitor & Ecosystem Benchmark Engine for Frontier Innovator.
Queries public GitHub repository search API to fetch live, empirical competitor
metrics (stars, forks, open issues, license, and last commit dates) with zero API keys.
"""

import sys
import json
import urllib.request
import urllib.parse
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def benchmark_competitors(query: str, max_results: int = 4):
    """
    Fetches real-world competitor data from public GitHub repositories.
    Returns stars, forks, issues, license, and activity level.
    """
    encoded_query = urllib.parse.quote(f"{query} in:name,description")
    url = f"https://api.github.com/search/repositories?q={encoded_query}&sort=stars&order=desc&per_page={max_results}"

    headers = {
        "User-Agent": "FrontierInnovatorBot/2.0 (Competitor Benchmark Tool)",
        "Accept": "application/vnd.github.v3+json"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"status": "error", "error": str(e), "competitors": []}

    items = data.get("items", [])
    competitors = []

    for item in items:
        name = item.get("full_name", "Bilinmeyen Repo")
        desc = item.get("description") or "Açıklama belirtilmemiş."
        stars = item.get("stargazers_count", 0)
        forks = item.get("forks_count", 0)
        open_issues = item.get("open_issues_count", 0)
        license_info = item.get("license")
        license_name = license_info.get("spdx_id") if license_info else "Belirtilmemiş"
        updated_at = item.get("pushed_at", "")[:10]
        html_url = item.get("html_url", "")
        language = item.get("language") or "Çoklu Dil"

        competitors.append({
            "name": name,
            "url": html_url,
            "description": desc[:250] + "..." if len(desc) > 250 else desc,
            "stars": stars,
            "forks": forks,
            "open_issues": open_issues,
            "license": license_name,
            "language": language,
            "last_active": updated_at
        })

    return {
        "status": "success",
        "competitors": competitors,
        "total_found": data.get("total_count", 0)
    }

def main():
    parser = argparse.ArgumentParser(description="Live competitor benchmark extractor.")
    parser.add_argument("query", help="Product domain or competitor query")
    parser.add_argument("--max", type=int, default=4, help="Max competitors (default: 4)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚔️ CANLI RAKİP & EKOSİSTEM BENCHMARK'I: '{args.query}'")
    print(f"=======================================================\n")

    res = benchmark_competitors(args.query, args.max)
    if res["status"] != "success" or not res["competitors"]:
        print(f"[-] Rakip verisi çekilemedi: {res.get('error', 'Kayıt bulunamadı')}")
        return

    print(f"[*] Toplam {res['total_found']} ilgili açık kaynak/endüstriyel proje bulundu.\n")
    for idx, c in enumerate(res["competitors"], 1):
        print(f"[{idx}] {c['name']} (⭐️ {c['stars']:,} | 🍴 {c['forks']:,} | ⚠️ {c['open_issues']} Issue)")
        print(f"    📖 Açıklama  : {c['description']}")
        print(f"    🛠️ Teknoloji : {c['language']} | Lisans: {c['license']}")
        print(f"    📅 Son Commit: {c['last_active']}")
        print(f"    🔗 Repo URL  : {c['url']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
