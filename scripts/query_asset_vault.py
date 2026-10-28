"""
Asset & 3D Vault Query Engine
Zobar Skill — Hazır 3D Varlıklar, PBR Dokular, UI Bileşenleri ve Ses Veritabanı Arayıcısı

Kategoriler:
- 3d_models_and_meshes (Kenney, Poly Pizza, Quaternius, Mixamo, NASA, Spline)
- pbr_textures_and_materials (Poly Haven, ambientCG, ShareTextures)
- ui_component_and_animation_libraries (Aceternity UI, Magic UI, Shadcn, 21st.dev, Tremor)
- icons_and_vector_design_systems (Lucide, Phosphor, Simple Icons, SVGL)
- audio_sfx_and_soundtracks (Kenney Audio, Freesound, Soniss GDC)
"""

import os
import sys
import json
from typing import Dict, Any, List, Optional


class AssetVaultQueryEngine:
    def __init__(self, vault_path: Optional[str] = None):
        if vault_path:
            self.vault_path = vault_path
        else:
            self.vault_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "references", "free_assets_and_3d_vault.json")
            )
        self.data: Dict[str, Any] = {"categories": {}, "total_resources": 0}
        self.load()

    def load(self) -> None:
        if os.path.exists(self.vault_path):
            try:
                with open(self.vault_path, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception:
                pass

    def search(
        self,
        query: str = "",
        category: Optional[str] = None,
        preferred_format: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        query_lower = query.lower().strip()
        results: List[Dict[str, Any]] = []

        categories_to_search = (
            [category] if category and category in self.data["categories"]
            else list(self.data["categories"].keys())
        )

        for cat in categories_to_search:
            for item in self.data["categories"].get(cat, []):
                # Format check
                if preferred_format:
                    formats_lower = [f.lower() for f in item.get("formats", [])]
                    if not any(preferred_format.lower() in f for f in formats_lower):
                        continue

                # Query check
                if not query_lower:
                    item_with_cat = dict(item)
                    item_with_cat["category"] = cat
                    results.append(item_with_cat)
                    continue

                searchable_text = (
                    f"{item.get('name', '')} {item.get('description', '')} "
                    f"{item.get('best_for', '')} {' '.join(item.get('formats', []))} "
                    f"{item.get('license', '')}"
                ).lower()

                if any(word in searchable_text for word in query_lower.split()):
                    item_with_cat = dict(item)
                    item_with_cat["category"] = cat
                    results.append(item_with_cat)

        return results

    def get_summary(self) -> Dict[str, Any]:
        return {
            "total_resources": self.data.get("total_resources", 0),
            "categories": {cat: len(items) for cat, items in self.data.get("categories", {}).items()},
        }


if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    engine = AssetVaultQueryEngine()
    print("=" * 65)
    print(f"[*] HAZIR 3D & ASSET HAVUZU: {engine.get_summary()['total_resources']} DOĞRULANMIŞ KAYNAK")
    print("=" * 65)

    search_term = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "3d"
    matches = engine.search(search_term)
    print(f"\n[+] '{search_term}' araması için {len(matches)} kaynak bulundu:\n")
    for m in matches[:6]:
        print(f"• {m['name']} ({m['category']})")
        print(f"  URL: {m['url']}")
        print(f"  Formatlar: {', '.join(m['formats'])} | Lisans: {m['license'][:40]}...")
        print(f"  En iyi kullanım: {m['best_for']}\n")
