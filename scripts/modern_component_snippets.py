#!/usr/bin/env python3
"""
Zobar Skill: Modern Component Snippets Engine.
Queries and retrieves ready-to-copy, zero-cost, modern React & Tailwind CSS v4 component snippets.
"""

import sys
import os
import json
import argparse
from typing import Dict, List, Any, Optional

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "references", "free_modern_components_vault.json"))

class ModernComponentsEngine:
    def __init__(self, vault_path: Optional[str] = None):
        self.path = vault_path or VAULT_PATH
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"components": []}

    def search_components(self, query: str = "") -> List[Dict[str, Any]]:
        q_lower = query.lower()
        results = []
        for c in self.data.get("components", []):
            if not query or q_lower in c["name"].lower() or q_lower in c["category"].lower() or q_lower in c["description"].lower():
                results.append(c)
        return results

    def get_component_by_id(self, comp_id: str) -> Optional[Dict[str, Any]]:
        for c in self.data.get("components", []):
            if c["id"].lower() == comp_id.lower():
                return c
        return None

def main():
    parser = argparse.ArgumentParser(description="Zobar Skill Free Modern UI Components Engine.")
    parser.add_argument("query", nargs="?", default="", help="Search query (e.g. 'skeleton', 'whatsapp', 'roi', 'bento')")
    args = parser.parse_args()

    engine = ModernComponentsEngine()
    results = engine.search_components(args.query)

    print(f"\n=================================================================")
    print(f" 🎨 MODERN VE ÜCRETSİZ UI BİLEŞENLERİ: '{args.query}' ({len(results)} sonuç)")
    print(f"=================================================================\n")

    for c in results:
        print(f"📌 [{c['id']}] {c['name']} ({c['category']})")
        print(f"   Açıklama: {c['description']}")
        print(f"   Sınıflar: {c['tailwind_classes']}")
        print(f"   React Kodu:\n{c['react_jsx']}\n")

if __name__ == "__main__":
    main()
