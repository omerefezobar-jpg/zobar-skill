#!/usr/bin/env python3
"""
Multi-Source User Sentiment & Friction Miner for Frontier Innovator.
Extracts real developer complaints, pain points, and friction points across
Hacker News (Algolia API) and Reddit (Public JSON API) with zero dependencies.
Includes source health tracking and weighted sentiment scoring.
"""

import sys
import re
import html
import json
import urllib.request
import urllib.parse
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Weighted friction vocabulary
HIGH_FRICTION_KEYWORDS = [
    "hate", "broken", "terrible", "worst", "unusable", "horrible",
    "garbage", "disaster", "painful", "nightmare", "crash", "corrupt"
]

MODERATE_FRICTION_KEYWORDS = [
    "slow", "issue", "problem", "bug", "confusing", "fail", "expensive",
    "annoying", "frustrat", "waste", "overkill", "bloat", "clunky", "hard to"
]

def clean_html(raw_html: str) -> str:
    """Strips HTML tags, collapses whitespaces, and unescapes entities."""
    cleanr = re.compile(r'<.*?>')
    text = re.sub(cleanr, ' ', raw_html)
    return html.unescape(text).strip()

def calculate_friction_score(text: str) -> int:
    """Calculates weighted friction score based on severity and keyword density."""
    lowered = text.lower()
    high_count = sum(2 for kw in HIGH_FRICTION_KEYWORDS if kw in lowered)
    mod_count = sum(1 for kw in MODERATE_FRICTION_KEYWORDS if kw in lowered)
    return high_count + mod_count

def search_hn_sentiment(query: str, max_comments: int = 4):
    """Mines user sentiment and complaints from Hacker News via Algolia API."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://hn.algolia.com/api/v1/search?query={encoded_query}&tags=comment&hitsPerPage={max_comments * 3}"

    headers = {"User-Agent": "FrontierInnovatorBot/2.0 (Developer Sentiment Research)"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        return {"status": "error", "error": str(e), "comments": []}

    hits = data.get("hits", [])
    results = []

    for hit in hits:
        comment_text = hit.get("comment_text")
        if not comment_text:
            continue

        cleaned = clean_html(comment_text)
        if len(cleaned) < 35:
            continue

        story_title = hit.get("story_title") or "Hacker News Tartışması"
        created_at = hit.get("created_at", "")[:10]
        author = hit.get("author", "anon")
        url = f"https://news.ycombinator.com/item?id={hit.get('objectID')}"

        score = calculate_friction_score(cleaned)

        results.append({
            "source": "Hacker News",
            "author": author,
            "date": created_at,
            "title": story_title,
            "url": url,
            "friction_score": score,
            "text": cleaned[:380] + "..." if len(cleaned) > 380 else cleaned
        })

    results.sort(key=lambda x: x["friction_score"], reverse=True)
    return {"status": "success", "comments": results[:max_comments]}

def search_reddit_sentiment(query: str, max_comments: int = 4):
    """Mines user complaints and feedback from Reddit public search JSON."""
    encoded_query = urllib.parse.quote(f"{query} (slow OR hate OR bug OR problem OR terrible OR broken)")
    url = f"https://www.reddit.com/search.json?q={encoded_query}&type=comment&limit={max_comments * 3}&sort=relevance"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) FrontierInnovator/2.0"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        return {"status": "rate-limited/error", "error": str(e), "comments": []}

    items = data.get("data", {}).get("children", [])
    results = []

    for item in items:
        c_data = item.get("data", {})
        body = c_data.get("body", "")
        if not body or len(body) < 35:
            continue

        cleaned = clean_html(body)
        author = c_data.get("author", "redditor")
        permalink = c_data.get("permalink", "")
        url = f"https://reddit.com{permalink}" if permalink else "https://reddit.com"
        subreddit = c_data.get("subreddit_name_prefixed", "r/reddit")

        score = calculate_friction_score(cleaned)

        results.append({
            "source": f"Reddit ({subreddit})",
            "author": author,
            "date": "Güncel Gönderi",
            "title": f"{subreddit} Tartışması",
            "url": url,
            "friction_score": score,
            "text": cleaned[:380] + "..." if len(cleaned) > 380 else cleaned
        })

    results.sort(key=lambda x: x["friction_score"], reverse=True)
    return {"status": "success", "comments": results[:max_comments]}

def search_sentiment(query: str, max_comments: int = 5):
    """
    Aggregates and ranks user complaints from multiple community channels.
    Returns structured dict with both comments list and sources summary metadata.
    """
    hn_res = search_hn_sentiment(query, max_comments=max_comments)
    reddit_res = search_reddit_sentiment(query, max_comments=max_comments)

    combined = hn_res.get("comments", []) + reddit_res.get("comments", [])
    combined.sort(key=lambda x: x["friction_score"], reverse=True)
    selected = combined[:max_comments]

    active_sources = []
    if hn_res.get("status") == "success":
        active_sources.append(f"Hacker News ({len(hn_res.get('comments', []))} veri)")
    else:
        active_sources.append(f"Hacker News (Hata: {hn_res.get('error', 'bağlantı')})")

    if reddit_res.get("status") == "success":
        active_sources.append(f"Reddit ({len(reddit_res.get('comments', []))} veri)")
    else:
        active_sources.append("Reddit (Açık API kısıtı/bağlantı)")

    summary = f"Taranan Kanallar: {', '.join(active_sources)}"

    return {
        "comments": selected,
        "summary": summary,
        "hn_status": hn_res.get("status"),
        "reddit_status": reddit_res.get("status")
    }

def main():
    parser = argparse.ArgumentParser(description="Multi-source user friction and sentiment miner.")
    parser.add_argument("query", help="Keyword or product to mine complaints for")
    parser.add_argument("--max", type=int, default=5, help="Number of comments to return (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 💬 ÇOK KAYNAKLI KULLANICI ŞİKAYET MADENCİLİĞİ: '{args.query}'")
    print(f"=======================================================\n")

    result = search_sentiment(args.query, args.max)
    comments = result["comments"]
    print(f"[*] Durum: {result['summary']}\n")

    if not comments:
        print("[-] Uygun kullanıcı yorumu veya eleştiri bulunamadı.")
        return

    for idx, c in enumerate(comments, 1):
        friction_tag = "⚠️ YÜKSEK SÜRTÜNME (AĞIR ŞİKAYET)" if c["friction_score"] >= 3 else "📌 KULLANICI SÜRTÜNME/GERİ BİLDİRİMİ"
        print(f"[{idx}] {friction_tag} [{c['source']}] (Yazar: @{c['author']} | Tarih: {c['date']})")
        print(f"    📖 Başlık   : {c['title']}")
        print(f"    🔗 Kaynak   : {c['url']}")
        print(f"    📊 Skor     : {c['friction_score']}")
        print(f"    🗣️ Yorum    : {c['text']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
