#!/usr/bin/env python3
"""
Multi-Source User Sentiment & Friction Miner for Zobar Skill.
Extracts real developer complaints, pain points, and friction points across
Hacker News (Algolia API) and Reddit (Public JSON API) with zero dependencies.
Includes clause-level syntax parsing, adversative conjunction handling,
and negation-aware friction scoring.
"""

import sys
import re
import html
import json
import datetime
import urllib.request
import urllib.parse
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Weighted friction vocabulary
HIGH_FRICTION_KEYWORDS = [
    "hate", "broken", "terrible", "worst", "unusable", "horrible",
    "garbage", "disaster", "painful", "nightmare", "crash", "corrupt",
    "berbat", "rezalet", "çöküyor", "kullanılamaz"
]

MODERATE_FRICTION_KEYWORDS = [
    "slow", "issue", "problem", "bug", "confusing", "fail", "expensive",
    "annoying", "frustrat", "waste", "overkill", "bloat", "clunky", "hard to",
    "yavaş", "sorun", "pahalı", "karmaşık", "zahmetli"
]

# Adversative conjunctions that delimit distinct sentiment clauses
ADVERSATIVE_CONJUNCTIONS = [
    "but", "however", "although", "though", "yet", "except", "despite",
    "nevertheless", "whereas", "while", "ama", "fakat", "lakin", "ancak", "oysa", "rağmen"
]

# Negation words that neutralize adjacent friction words within the same clause
NEGATIONS = [
    "not", "isn't", "aren't", "wasn't", "weren't", "don't", "doesn't", "didn't",
    "won't", "can't", "cannot", "couldn't", "no", "never", "hardly", "barely",
    "scarcely", "neither", "nor", "değil", "yok", "hiç"
]

def clean_html(raw_html: str) -> str:
    """Strips HTML tags, collapses whitespaces, and unescapes entities."""
    cleanr = re.compile(r'<.*?>')
    text = re.sub(cleanr, ' ', raw_html)
    return html.unescape(text).strip()

def split_into_clauses(text: str):
    """
    Splits text into sentences and sub-clauses based on punctuation and adversative conjunctions.
    E.g. 'Performance is great, but the crash rate is terrible.' -> 2 distinct clauses.
    """
    # First split by sentence boundaries (. ? ! ;)
    raw_sentences = re.split(r'[.?!;]\s+', text)
    clauses = []

    for sentence in raw_sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        # Split sentence by commas or adversative conjunctions
        pattern = r'\b(' + '|'.join(ADVERSATIVE_CONJUNCTIONS) + r')\b|,'
        sub_segments = re.split(pattern, sentence, flags=re.IGNORECASE)

        for seg in sub_segments:
            if seg and seg.strip() and seg.lower() not in ADVERSATIVE_CONJUNCTIONS:
                clauses.append(seg.strip())

    return clauses if clauses else [text]

def calculate_clause_friction(clause: str):
    """
    Calculates friction score for an individual syntactic clause,
    strictly localizing negations so they do not bleed across boundaries.
    """
    lowered = clause.lower()

    # Handle special multi-word constructions
    # E.g. 'not only ... but also' shouldn't trigger naive 'not' negation
    has_not_only = "not only" in lowered

    tokens = re.findall(r"[a-z0-9'-]+", lowered)
    score = 0
    detected_words = []

    for idx, token in enumerate(tokens):
        # Look behind up to 3 words within this clause for negation
        is_negated = False
        lookback_start = max(0, idx - 3)
        for prev in tokens[lookback_start:idx]:
            if prev in NEGATIONS and not has_not_only:
                is_negated = True
                break

        if is_negated:
            continue

        if any(token.startswith(kw) or token == kw for kw in HIGH_FRICTION_KEYWORDS):
            score += 2
            detected_words.append(token)
        elif any(token.startswith(kw) or token == kw for kw in MODERATE_FRICTION_KEYWORDS):
            score += 1
            detected_words.append(token)

    return score, detected_words

def calculate_friction_score(text: str) -> int:
    """
    Calculates aggregate friction score by summing clause-level scores.
    """
    clauses = split_into_clauses(text)
    total_score = 0

    for clause in clauses:
        score, _ = calculate_clause_friction(clause)
        total_score += score

    return total_score

def extract_primary_pain_points(text: str, max_points: int = 2):
    """
    Extracts the highest friction clauses as concrete quoted pain points.
    """
    clauses = split_into_clauses(text)
    scored_clauses = []

    for c in clauses:
        score, words = calculate_clause_friction(c)
        if score > 0:
            scored_clauses.append({
                "clause": c,
                "score": score,
                "keywords": words
            })

    scored_clauses.sort(key=lambda x: x["score"], reverse=True)
    return scored_clauses[:max_points]

def search_hn_sentiment(query: str, max_comments: int = 4):
    """Mines user sentiment and complaints from Hacker News via Algolia API."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://hn.algolia.com/api/v1/search?query={encoded_query}&tags=comment&hitsPerPage={max_comments * 3}"

    headers = {"User-Agent": "ZobarSkillBot/3.0 (Developer Sentiment Research)"}
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
        pain_points = extract_primary_pain_points(cleaned)

        results.append({
            "source": "Hacker News",
            "author": author,
            "date": created_at,
            "title": story_title,
            "url": url,
            "text": cleaned[:420] + "..." if len(cleaned) > 420 else cleaned,
            "friction_score": score,
            "pain_points": [p["clause"] for p in pain_points]
        })

    results.sort(key=lambda x: x["friction_score"], reverse=True)
    return {"status": "ok", "comments": results[:max_comments]}

def search_reddit_sentiment(query: str, max_comments: int = 4):
    """Mines developer feedback and complaints from Reddit via public JSON endpoint."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.reddit.com/search.json?q={encoded_query}&sort=relevance&limit={max_comments * 2}"

    headers = {"User-Agent": "ZobarSkillBot/3.0 (Sentiment Miner by /u/zobarskill)"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        return {"status": "error", "error": str(e), "comments": []}

    children = data.get("data", {}).get("children", [])
    results = []

    for child in children:
        post = child.get("data", {})
        selftext = post.get("selftext", "")
        title = post.get("title", "")
        full_text = f"{title}. {selftext}".strip()

        if len(full_text) < 40:
            continue

        cleaned = clean_html(full_text)
        author = post.get("author", "redditor")
        created_utc = post.get("created_utc", 0)
        date_str = datetime.datetime.fromtimestamp(created_utc, tz=datetime.timezone.utc).strftime("%Y-%m-%d") if created_utc else "Tarih Yok"
        permalink = post.get("permalink", "")
        url = f"https://reddit.com{permalink}" if permalink else "https://reddit.com"

        score = calculate_friction_score(cleaned)
        pain_points = extract_primary_pain_points(cleaned)

        results.append({
            "source": "Reddit",
            "author": author,
            "date": date_str,
            "title": title,
            "url": url,
            "text": cleaned[:420] + "..." if len(cleaned) > 420 else cleaned,
            "friction_score": score,
            "pain_points": [p["clause"] for p in pain_points]
        })

    results.sort(key=lambda x: x["friction_score"], reverse=True)
    return {"status": "ok", "comments": results[:max_comments]}

import time
from typing import Dict, Tuple, Any

_SENTIMENT_MEM_CACHE: Dict[str, Tuple[float, Dict[str, Any]]] = {}

def search_sentiment(query: str, max_comments: int = 5):
    """
    Queries both Hacker News and Reddit, reporting per-source health,
    clause-level friction scores, and primary pain points.
    Includes in-memory TTL caching for sub-millisecond execution.
    """
    cache_key = f"{query.lower().strip()}_{max_comments}"
    now = time.time()
    if cache_key in _SENTIMENT_MEM_CACHE:
        ts, cached_res = _SENTIMENT_MEM_CACHE[cache_key]
        if now - ts < 600:
            return cached_res

    hn_res = search_hn_sentiment(query, max_comments=max_comments)
    reddit_res = search_reddit_sentiment(query, max_comments=max_comments)

    combined = []
    sources_status = []

    if hn_res["status"] == "ok":
        combined.extend(hn_res["comments"])
        sources_status.append(f"Hacker News ({len(hn_res['comments'])} kayıt)")
    else:
        sources_status.append(f"Hacker News (Hata: {hn_res.get('error', 'bilinmiyor')[:30]})")

    if reddit_res["status"] == "ok":
        combined.extend(reddit_res["comments"])
        sources_status.append(f"Reddit ({len(reddit_res['comments'])} kayıt)")
    else:
        sources_status.append(f"Reddit (Hata: {reddit_res.get('error', 'bilinmiyor')[:30]})")

    combined.sort(key=lambda x: x["friction_score"], reverse=True)

    result = {
        "comments": combined[:max_comments],
        "summary": " | ".join(sources_status)
    }
    _SENTIMENT_MEM_CACHE[cache_key] = (now, result)
    return result

def main():
    parser = argparse.ArgumentParser(description="Multi-source user sentiment and friction miner.")
    parser.add_argument("query", help="Target topic or keyword to search")
    parser.add_argument("--max", type=int, default=5, help="Maximum number of comments (default: 5)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 💬 ÇOK KAYNAKLI KULLANICI ŞİKAYET & SÜRTÜNME MADENCİLİĞİ: '{args.query}'")
    print(f"=======================================================\n")

    res = search_sentiment(args.query, args.max)
    print(f"📡 Kaynak Durumu: {res['summary']}\n")

    if not res["comments"]:
        print("[-] Belirtilen arama kriterlerine uyan şikayet verisi bulunamadı.")
        return

    for idx, c in enumerate(res["comments"], 1):
        friction_tag = "🔴 Yüksek Sürtünme" if c["friction_score"] >= 3 else ("🟡 Orta Sürtünme" if c["friction_score"] >= 1 else "⚪ Nötr / Düşük")
        print(f"[{idx}] {friction_tag} (Skor: {c['friction_score']}) — {c['source']} (@{c['author']} - {c['date']})")
        print(f"    Başlık  : {c['title']}")
        print(f"    Bağlantı: {c['url']}")
        if c.get("pain_points"):
            print(f"    🎯 Tespit Edilen Odak Acı Noktaları:")
            for p in c["pain_points"]:
                print(f"       • \"{p}\"")
        print(f"    Görüş   : {c['text']}")
        print("-" * 55)

if __name__ == "__main__":
    main()
