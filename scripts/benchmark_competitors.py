#!/usr/bin/env python3
"""
Full-Spectrum Hybrid Competitor Benchmark Engine for Frontier Innovator.
Combines live GitHub telemetry with a curated Commercial & Proprietary Competitor
Index, providing pricing tiers, deployment models, and structural blindspots.
"""

import sys
import json
import urllib.request
import urllib.parse
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Curated knowledge graph of commercial/closed-source market incumbents
COMMERCIAL_LANDSCAPE_INDEX = [
    {
        "keywords": ["code analysis", "linter", "static analysis", "sonarqube", "code quality", "refactor"],
        "incumbents": [
            {
                "name": "SonarQube (SonarSource)",
                "type": "Ticari / Open-Core",
                "pricing_tier": "Community (Ücretsiz) / Enterprise ($15,000+/yıl)",
                "deployment": "Cloud (SonarCloud) & Self-Hosted",
                "core_weakness": "Kural tabanlı statik tarama; semantik bağlam eksikliği sebebiyle yüksek false-positive oranı; sadece uyarı verir, çalışan yama üretmez.",
                "url": "https://www.sonarsource.com/products/sonarqube/"
            },
            {
                "name": "Snyk Code",
                "type": "Ticari SaaS",
                "pricing_tier": "Freemium / Team ($98/ay) / Enterprise",
                "deployment": "SaaS Multi-tenant",
                "core_weakness": "Lisans ve bağımlılık taramasında güçlü fakat derin iş mantığı (business logic) açıklarını ve concurrency hatalarını kaçırır.",
                "url": "https://snyk.io/product/snyk-code/"
            },
            {
                "name": "GitHub Advanced Security (CodeQL)",
                "type": "Kurumsal Eklenti",
                "pricing_tier": "$49/aktif committer/ay",
                "deployment": "GitHub Enterprise Cloud / Server",
                "core_weakness": "CodeQL sorgularını yazmak ve optimize etmek uzmanlık gerektirir; küçük ekipler için kurulum maliyeti ve öğrenme eğrisi yüksektir.",
                "url": "https://github.com/features/security"
            }
        ]
    },
    {
        "keywords": ["agent", "autonomous", "ai agent", "multi-agent", "orchestration"],
        "incumbents": [
            {
                "name": "AutoGPT / Forge",
                "type": "Açık Kaynak + Ticari Platform",
                "pricing_tier": "Open Source / Cloud Kredi Bazlı",
                "deployment": "Cloud & Docker Local",
                "core_weakness": "Sonsuz döngülere (infinite loops) girme eğilimi, token tüketim maliyetinin kontrol edilememesi ve deterministik test eksikliği.",
                "url": "https://agpt.co"
            },
            {
                "name": "CrewAI Enterprise",
                "type": "Ticari Orkestrasyon Platformu",
                "pricing_tier": "Free Core / Pro ($25/ay) / Enterprise",
                "deployment": "Managed Cloud & Local Python",
                "core_weakness": "Rol bazlı işbirliklerinde ajanlar arası bağlam kirlenmesi (context drift) ve deterministik hata izolasyonunun zorluğu.",
                "url": "https://crewai.com"
            }
        ]
    }
]

def search_commercial_incumbents(query: str):
    """Finds curated commercial incumbents matching the domain query."""
    lowered = query.lower()
    matched_incumbents = []
    
    for category in COMMERCIAL_LANDSCAPE_INDEX:
        if any(kw in lowered for kw in category["keywords"]):
            matched_incumbents.extend(category["incumbents"])
            
    return matched_incumbents

def fetch_github_telemetry(query: str, max_results: int = 3):
    """Fetches real-time open-source project metrics from GitHub API."""
    encoded_query = urllib.parse.quote(f"{query} in:name,description")
    url = f"https://api.github.com/search/repositories?q={encoded_query}&sort=stars&order=desc&per_page={max_results}"

    headers = {
        "User-Agent": "FrontierInnovatorBot/2.5 (Competitor Benchmark Tool)",
        "Accept": "application/vnd.github.v3+json"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"status": "error", "error": str(e), "projects": []}

    items = data.get("items", [])
    projects = []

    for item in items:
        projects.append({
            "name": item.get("full_name", "Bilinmeyen Repo"),
            "url": item.get("html_url", ""),
            "description": (item.get("description") or "Açıklama yok")[:200] + "...",
            "stars": item.get("stargazers_count", 0),
            "forks": item.get("forks_count", 0),
            "open_issues": item.get("open_issues_count", 0),
            "license": item.get("license", {}).get("spdx_id") if item.get("license") else "Belirtilmemiş",
            "language": item.get("language") or "Çoklu Dil",
            "last_active": item.get("pushed_at", "")[:10]
        })

    return {
        "status": "success",
        "projects": projects,
        "total_ecosystem_count": data.get("total_count", 0)
    }

def benchmark_competitors(query: str, max_results: int = 3):
    """
    Executes full hybrid benchmark combining commercial incumbents and open-source telemetry.
    """
    gh_data = fetch_github_telemetry(query, max_results=max_results)
    commercial_data = search_commercial_incumbents(query)

    return {
        "domain": query,
        "commercial_incumbents": commercial_data,
        "open_source_telemetry": gh_data.get("projects", []),
        "ecosystem_size": gh_data.get("total_ecosystem_count", 0),
        "status": "success"
    }

def main():
    parser = argparse.ArgumentParser(description="Hybrid Competitor & Ecosystem Benchmark Engine.")
    parser.add_argument("query", help="Domain or product query to benchmark")
    parser.add_argument("--max", type=int, default=3, help="Max open source competitors (default: 3)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" ⚔️ HİBRİT RAKİP & PAZAR BENCHMARK'I: '{args.query}'")
    print(f"=======================================================\n")

    res = benchmark_competitors(args.query, args.max)

    print("🏢 1. TİCARİ VE PAZAR LİDERİ RAKİPLER (Commercial Incumbents):")
    if res["commercial_incumbents"]:
        for idx, inc in enumerate(res["commercial_incumbents"], 1):
            print(f"[{idx}] {inc['name']} ({inc['type']})")
            print(f"    💰 Fiyatlandırma : {inc['pricing_tier']}")
            print(f"    ☁️ Dağıtım Modeli : {inc['deployment']}")
            print(f"    ⚠️ Yapısal Zaaf   : {inc['core_weakness']}")
            print(f"    🔗 İncele         : {inc['url']}")
            print("-" * 55)
    else:
        print("[-] Bu niş için kayıtlı kurumsal rakip bulunamadı; açık kaynak projeler taranıyor.\n")

    print("\n🌐 2. AÇIK KAYNAK EKOSİSTEMİ & GITHUB TELEMETRİSİ:")
    print(f"[*] İlgili Ekosistem Büyüklüğü: {res['ecosystem_size']} proje\n")
    for idx, p in enumerate(res["open_source_telemetry"], 1):
        print(f"[{idx}] {p['name']} (⭐️ {p['stars']:,} | 🍴 {p['forks']:,} | ⚠️ {p['open_issues']} Issue)")
        print(f"    🛠️ Dil: {p['language']} | Lisans: {p['license']} | Son Commit: {p['last_active']}")
        print(f"    🔗 {p['url']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
