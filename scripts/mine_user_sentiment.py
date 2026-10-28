#!/usr/bin/env python3
"""
Multi-Source User Sentiment & Friction Miner for Frontier Innovator.
Extracts real developer complaints, pain points, and friction points across
Hacker News (Algolia API) and Reddit (Public JSON API) with zero dependencies.
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

FRICTION_KEYWORDS = [
    "slow", "hate", "issue", "problem", "broken", "pain", "expensive", 
    "crash", "annoying", "terrible", "worst", "bug", "confusing", "fail",
    "frustrat", "unusable", "horrible", "waste", "garbage", "overkill"
]

def clean_html(raw_html: str) -> str:
    """Strips HTML tags, collapses whitespaces, and unescapes entities."""
    cleanr = re.compile(r'<.*?>')
    text = re.sub(cleanr, ' ', raw_html)
    return html.unescape(text).strip()

def search_hn_sentiment(query: str, max_comments: int = 4):
    """Mines user sentiment and complaints from Hacker News via Algolia API."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://hn.algolia.com/api/v1/search?query={encoded_query}&tags=comment&hitsPerPage={max_comments * 2}"

    headers = {"User-Agent": "FrontierInnovatorBot/1.0 (Developer Sentiment Research)"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"[-] HN Arama Hatası: {e}", file=sys.stderr)
        return []

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

        score = sum(1 for kw in FRICTION_KEYWORDS if kw in cleaned.lower())

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
    return results[:max_comments]

def search_reddit_sentiment(query: str, max_comments: int = 4):
    """Mines user complaints and feedback from Reddit public search JSON."""
    encoded_query = urllib.parse.quote(f"{query} (slow OR hate OR bug OR problem OR terrible)")
    url = f"https://www.reddit.com/search.json?q={encoded_query}&type=comment&limit={max_comments * 2}&sort=relevance"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) FrontierInnovator/1.0"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception:
        # Reddit may rate-limit anonymous requests; fail silently and rely on HN
        return []

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

        score = sum(1 for kw in FRICTION_KEYWORDS if kw in cleaned.lower())

        results.append({
            "source": f"Reddit ({subreddit})",
            "author": author,
            "date": "Güncel",
            "title": f"{subreddit} Gönderisi",
            "url": url,
            "friction_score": score + 1,  # Reddit search specifically targeted complaints
            "text": cleaned[:380] + "..." if len(cleaned) > 380 else cleaned
        })

    results.sort(key=lambda x: x["friction_score"], reverse=True)
    return results[:max_comments]

def search_sentiment(query: str, max_comments: int = 5):
    """Aggregates and ranks user complaints from multiple community channels."""
    hn_results = search_hn_sentiment(query, max_comments=max_comments)
    reddit_results = search_reddit_sentiment(query, max_comments=max_comments)

    combined = hn_results + reddit_results
    combined.sort(key=lambda x: x["friction_score"], reverse=True)
    return combined[:max_comments]

def main():
    parser = argparse.ArgumentParser(description="Multi-source user friction and sentiment miner.")
    parser.add_argument("query", help="Keyword or product to mine complaints for")
    parser.add_argument("--max", type=int, default=5, help="Number of comments to return (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 💬 ÇOK KAYNAKLI KULLANICI ŞİKAYET MADENCİLİĞİ: '{args.query}'")
    print(f"=======================================================\n")

    comments = search_sentiment(args.query, args.max)
    if not comments:
        print("[-] Uygun kullanıcı yorumu veya eleştiri bulunamadı.")
        return

    for idx, c in enumerate(comments, 1):
        friction_tag = "⚠️ YÜKSEK SÜRTÜNME/ŞİKAYET" if c["friction_score"] >= 2 else "📌 KULLANICI GERİ BİLDİRİMİ"
        print(f"[{idx}] {friction_tag} [{c['source']}] (Yazar: @{c['author']} | Tarih: {c['date']})")
        print(f"    📖 Başlık   : {c['title']}")
        print(f"    🔗 Kaynak   : {c['url']}")
        print(f"    🗣️ Yorum    : {c['text']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
