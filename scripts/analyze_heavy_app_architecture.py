#!/usr/bin/env python3
"""
Heavy Pro Desktop & Monolithic Application Architecture Teardown Engine (Phase 5).
Analyzes massive desktop software (Steam, Excel, Premiere Pro, Blender, DaVinci Resolve,
Ableton Live, VS Code, Unreal Engine 5), explaining how they were built, their structural
friction points, and concrete technical blueprints on how to rebuild them 10x better.
"""

import sys
import os
import json
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BLUEPRINT_PATH = os.path.join(os.path.dirname(__file__), "..", "references", "heavy_apps_engineering_blueprints.json")

def load_blueprints():
    if not os.path.exists(BLUEPRINT_PATH):
        return {"blueprints": []}
    with open(BLUEPRINT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def match_heavy_app_blueprint(query: str):
    """
    Matches query against heavy desktop monolithic apps and returns 10x blueprints.
    """
    data = load_blueprints()
    lowered = query.lower()

    app_keywords = {
        "Steam": ["steam", "game launcher", "valve", "gaming library", "game store"],
        "Microsoft Excel": ["excel", "spreadsheet", "sheets", "grid", "formula", "calc", "table"],
        "Adobe Premiere Pro": ["premiere", "video editor", "nle", "timeline", "video cutting", "montage", "video editing"],
        "Blender": ["blender", "3d", "sculpt", "mesh", "shader", "render", "cycles", "eevee", "3d modeling"],
        "DaVinci Resolve": ["davinci", "resolve", "color grading", "fairlight", "fusion", "blackmagic", "grading"],
        "Ableton Live": ["ableton", "daw", "music", "audio workstation", "audio editing", "midi", "vst", "live performance"],
        "Visual Studio Code": ["vscode", "vs code", "code editor", "monaco", "ide", "programming tool"],
        "Unreal Engine 5": ["unreal", "ue5", "game engine", "nanite", "lumen", "realtime 3d"]
    }

    matched = []
    for bp in data.get("blueprints", []):
        app_name = bp["app_name"]
        keywords = app_keywords.get(app_name, [app_name.lower()])
        if any(kw in lowered for kw in keywords):
            matched.append(bp)

    return {
        "query": query,
        "matched_blueprints": matched
    }

def main():
    parser = argparse.ArgumentParser(description="Heavy Desktop Application 10x Re-Engineering Blueprint.")
    parser.add_argument("query", help="Target heavy application or domain (e.g. steam, excel, premiere)")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 🏗️ BÜYÜK UYGULAMA MİMARİ ANALİZİ & 10x YENİDEN İNŞA: '{args.query}'")
    print(f"=======================================================\n")

    res = match_heavy_app_blueprint(args.query)
    matched = res.get("matched_blueprints", [])

    if not matched:
        print("[-] Doğrudan eşleşen monolitik uygulama bulunamadı. Genel mimari kurallar uygulanıyor.")
        return

    for idx, bp in enumerate(matched, 1):
        print(f"[{idx}] {bp['app_name']} ({bp['category']} — {bp['vendor']})")
        print(f"    🔗 Resmî URL: {bp['official_url']}")
        print("\n    ⚙️ NASIL YAPILMIŞ (HOW IT WAS BUILT):")
        hw = bp['how_it_was_built']
        print(f"       • Mimari   : {hw['architecture']}")
        print(f"       • Runtime  : {hw['runtime']}")
        print(f"       • Render   : {hw['rendering']}")
        print(f"       • IPC      : {hw['ipc']}")

        print("\n    ⚠️ YAPISAL KÖR NOKTALAR & ZAFAYETLER:")
        for sb in bp['structural_blindspots']:
            print(f"       • {sb}")

        print("\n    🚀 BİZ NASIL 10x DAHA İYİSİNİ YAPARIZ (10x RE-ENGINEERING):")
        hw10 = bp['how_we_build_it_10x_better']
        print(f"       • Çekirdek Teknoloji : {hw10['core_technology']}")
        print(f"       • Bellek & RAM       : {hw10['memory_optimization']}")
        print(f"       • Render Motoru      : {hw10['rendering_engine']}")

        print("\n    🧩 BİLEŞEN MİMARİSİ (COMPONENT BLUEPRINT):")
        for kc in bp['key_components']:
            print(f"       • {kc}")
        print("-" * 55)

if __name__ == "__main__":
    main()
