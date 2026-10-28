#!/usr/bin/env python3
"""
S-Tier Component & UI/UX Design Pattern Recommender for Zobar Skill (Phase 5).
Maps any technology domain, problem statement, or software system to real-world
S-Tier benchmark products (e.g., Netflix, Stripe, Linear, Apple, Spotify, Vercel)
from the curated 102+ Design Vault.
"""

import sys
import os
import json
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT_PATH = os.path.join(os.path.dirname(__file__), "..", "references", "s_tier_design_vault.json")

def load_design_vault():
    """Loads the 100+ S-Tier Design Vault JSON database."""
    if not os.path.exists(VAULT_PATH):
        return {"categories": []}
    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def match_s_tier_patterns(query: str, max_results: int = 4):
    """
    Intelligently matches user query against S-Tier sites, design paradigms,
    and component features.
    """
    vault = load_design_vault()
    lowered = query.lower()
    
    # Keyword domain affinity mapping
    domain_category_weights = {
        "Heavy Pro Desktop & Creative Powerhouses": ["steam", "excel", "premiere", "blender", "vscode", "ableton", "unreal", "davinci", "photoshop", "autocad", "unity", "fl studio", "desktop", "timeline", "daw", "cad", "3d", "video editing", "workstation"],
        "Heavy Grid & Spreadsheet Operating Systems": ["spreadsheet", "excel", "sheets", "airtable", "grid", "rows", "table", "cells", "calculation", "formula", "retool", "coda"],
        "Gaming, Esports & Game Launchers": ["gaming", "game", "steam", "epic games", "riot", "esports", "tournament", "match", "bracket", "launcher", "speedrun", "roblox"],
        "Streaming & Immersive Entertainment": ["stream", "video", "media", "audio", "music", "movie", "film", "player", "watch", "content", "netflix", "spotify", "entertainment"],
        "Developer Tools & Cloud Infrastructure": ["developer", "code", "compiler", "ast", "cli", "terminal", "cloud", "infra", "git", "api", "database", "sql", "deploy", "linter", "parser", "telemetry", "devops", "linear", "vercel"],
        "Developer Platforms, Cloud & Modern APIs": ["api", "postman", "docker", "kubernetes", "postgres", "redis", "sentry", "auth", "clerk", "resend", "neon", "turso"],
        "Enterprise Data, Analytics & BI": ["analytics", "bi", "snowflake", "palantir", "grafana", "metrics", "tableau", "charts", "sql", "dashboard", "mixpanel", "posthog"],
        "Security, Identity & Cloud Operations": ["security", "password", "firewall", "vpn", "zero trust", "crowdstrike", "tailscale", "audit", "vault", "1password", "bitwarden", "wiz"],
        "High-End FinTech & Banking": ["fintech", "finance", "bank", "pay", "credit", "money", "wallet", "crypto", "trading", "investment", "invoice", "spend", "treasury", "stripe", "ramp", "loan"],
        "Modern AI & Generative Intelligence": ["ai", "llm", "agent", "prompt", "model", "generative", "neural", "vision", "chat", "voice", "speech", "diffusion", "openai", "perplexity", "claude"],
        "Design, Creative & Collaborative Canvas": ["design", "canvas", "graphic", "vector", "creative", "draw", "ui", "ux", "figma", "framer", "pitch", "deck", "slide", "animation", "motion"],
        "Productivity, Notes & Workspace": ["note", "calendar", "task", "project", "doc", "team", "collaborat", "work", "schedule", "chat", "message", "slack", "notion", "amie"],
        "E-Commerce & High-End Brand Showcase": ["shop", "store", "commerce", "product", "cart", "brand", "retail", "shoes", "car", "apple", "nike", "airbnb", "checkout"],
        "Luxury, Architecture & Industrial Design": ["luxury", "watch", "car", "porsche", "leica", "architecture", "furniture", "industrial", "rimowa", "rolex", "vitra"],
        "Education, EdTech & Interactive Learning": ["learn", "course", "quiz", "student", "duolingo", "education", "practice", "leetcode", "khan academy", "edx", "coursera"],
        "Modern Social, Creator Economy & Community": ["social", "creator", "community", "feed", "patreon", "twitter", "threads", "reddit", "donation", "product hunt", "gumroad"],
        "Design Systems & Component Libraries": ["component", "system", "token", "library", "primitive", "accessible", "radix", "tailwind", "shadcn", "theme", "dark mode"],
        "Web3, Decentralized & Crypto Ecosystems": ["web3", "crypto", "blockchain", "nft", "token", "defi", "swap", "solana", "ethereum", "wallet", "decentralized", "dao"],
        "Editorial, Media & Publishing": ["editorial", "article", "blog", "news", "read", "magazine", "post", "medium", "substack", "verge", "typography", "journal"]
    }

    scored_categories = []
    for cat in vault.get("categories", []):
        cat_name = cat["category_name"]
        keywords = domain_category_weights.get(cat_name, [])
        score = 0
        for kw in keywords:
            if kw in lowered:
                score += 3
        # Match against site names or descriptions in category
        for site in cat.get("sites", []):
            if site["name"].lower() in lowered:
                score += 5
            if any(k in site["component_features"].lower() for k in lowered.split()):
                score += 1
        scored_categories.append((score, cat))

    scored_categories.sort(key=lambda x: x[0], reverse=True)

    matched_sites = []
    selected_categories = []

    # If matches found, take top categories; else fallback to top generalist
    for score, cat in scored_categories:
        if score > 0 or len(matched_sites) < max_results:
            selected_categories.append(cat["category_name"])
            for s in cat.get("sites", []):
                matched_sites.append({
                    "category": cat["category_name"],
                    "design_paradigm": cat["design_paradigm"],
                    "recommended_libraries": cat["recommended_libraries"],
                    **s
                })
                if len(matched_sites) >= max_results:
                    break
        if len(matched_sites) >= max_results:
            break

    # If still empty (e.g. obscure query), provide the gold-standard S-tier benchmark (Linear, Stripe, Apple, Netflix)
    if not matched_sites:
        for cat in vault.get("categories", [])[:3]:
            if cat.get("sites"):
                matched_sites.append({
                    "category": cat["category_name"],
                    "design_paradigm": cat["design_paradigm"],
                    "recommended_libraries": cat["recommended_libraries"],
                    **cat["sites"][0]
                })

    return {
        "query": query,
        "matched_sites": matched_sites[:max_results],
        "total_vault_size": vault.get("vault_metadata", {}).get("total_sites", 102)
    }

def main():
    parser = argparse.ArgumentParser(description="Recommend S-Tier UI/UX Patterns from 100+ Design Vault.")
    parser.add_argument("query", help="Domain or problem statement")
    parser.add_argument("--max", type=int, default=4, help="Maximum number of S-tier benchmarks to return (default: 4)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 🎨 S-TİER TASARIM ÖRNEKLERİ & BİLEŞEN HAVUZU: '{args.query}'")
    print(f"=======================================================\n")

    res = match_s_tier_patterns(args.query, args.max)
    print(f"🔍 Toplam {res['total_vault_size']} S-Tier site arasından eşleşen referanslar:\n")

    for idx, s in enumerate(res["matched_sites"], 1):
        print(f"[{idx}] {s['name']} — {s['category']}")
        print(f"    🔗 Canlı Site URL   : {s['url']}")
        print(f"    📐 Tasarım Paradigması: {s['design_paradigm']}")
        print(f"    🌟 Hero Deseni       : {s['hero_pattern']}")
        print(f"    🧩 Bileşen Nitelikleri: {s['component_features']}")
        print(f"    ⚡ Mikro-Etkileşimler : {s['key_interactions']}")
        print(f"    🎨 Renk Tokenları   : Arka Plan: {s['color_tokens']['background']} | Vurgu: {s['color_tokens']['accent']}")
        print(f"    🛠️ Önerilen Kütüphane : {', '.join(s['recommended_libraries'])}")
        print("-" * 55)

if __name__ == "__main__":
    main()
