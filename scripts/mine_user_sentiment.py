#!/usr/bin/env python3
"""
User Sentiment & Friction Miner for Frontier Innovator Skill.
Extracts real user complaints, frustrations, and discussions from Hacker News
via Algolia Search API without requiring any API keys or external packages.
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

def clean_html(raw_html: str) -> str:
    """Strips HTML tags and unescapes entities."""
    cleanr = re.compile('<.*?>')
    text = re.sub(cleanr, ' ', raw_html)
    return html.unescape(text).strip()

def search_sentiment(query: str, max_comments: int = 5):
    encoded_query = urllib.parse.quote(query)
    # Search comments containing user feedback
    url = f"https://hn.algolia.com/api/v1/search?query={encoded_query}&tags=comment&hitsPerPage={max_comments * 2}"

    headers = {
        "User-Agent": "FrontierInnovatorBot/1.0 (sentiment analysis tool)"
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"[-] Hata: Yorumlar çekilemedi: {e}", file=sys.stderr)
        return []

    hits = data.get("hits", [])
    results = []
    
    # Friction keywords to prioritize complaints and pain points
    friction_keywords = ["slow", "hate", "issue", "problem", "broken", "pain", "expensive", 
                         "crash", "annoying", "terrible", "worst", "bug", "confusing", "fail"]

    for hit in hits:
        comment_text = hit.get("comment_text")
        if not comment_text:
            continue
            
        cleaned = clean_html(comment_text)
        if len(cleaned) < 40:
            continue
            
        story_title = hit.get("story_title") or "Bilinmeyen Başlık"
        created_at = hit.get("created_at", "")[:10]
        author = hit.get("author", "anon")
        url = f"https://news.ycombinator.com/item?id={hit.get('objectID')}"

        # Calculate a friction score
        score = sum(1 for kw in friction_keywords if kw in cleaned.lower())

        results.append({
            "author": author,
            "date": created_at,
            "title": story_title,
            "url": url,
            "friction_score": score,
            "text": cleaned[:400] + "..." if len(cleaned) > 400 else cleaned
        })

    # Sort by friction score descending to bring biggest complaints to the top
    results.sort(key=lambda x: x["friction_score"], reverse=True)
    return results[:max_comments]

def main():
    parser = argparse.ArgumentParser(description="Mine user complaints and friction points.")
    parser.add_argument("query", help="Keyword or product to mine complaints for")
    parser.add_argument("--max", type=int, default=5, help="Number of comments to return (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 💬 KULLANICI GERÇEĞİ & ŞİKAYET MADENCİLİĞİ: '{args.query}'")
    print(f"=======================================================\n")

    comments = search_sentiment(args.query, args.max)
    if not comments:
        print("[-] Uygun kullanıcı yorumu veya eleştiri bulunamadı.")
        return

    for idx, c in enumerate(comments, 1):
        friction_tag = "⚠️ YÜKSEK SÜRTÜNME/ŞİKAYET" if c["friction_score"] >= 2 else "📌 KULLANICI DENEYİMİ"
        print(f"[{idx}] {friction_tag} (Yazar: @{c['author']} | Tarih: {c['date']})")
        print(f"    📖 Konu     : {c['title']}")
        print(f"    🔗 Kaynak   : {c['url']}")
        print(f"    🗣️ Yorum    : {c['text']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
