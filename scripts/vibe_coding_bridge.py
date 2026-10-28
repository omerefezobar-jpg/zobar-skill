"""
Universal Vibe Coding Bridge & Multi-IDE Rules Generator
Zobar Skill — Claude, Cursor, Windsurf, Copilot/Codex & Antigravity Integrator

Automatically generates and syncs production-ready configuration and prompt files:
- Cursor: .cursorrules & .cursor/rules/zobar.mdc
- Claude Code: CLAUDE.md
- Windsurf: .windsurfrules
- GitHub Copilot / Codex: .github/copilot-instructions.md
- Antigravity / Gemini: GEMINI.md
"""

import os
from typing import Dict, Any, List, Optional


class VibeCodingBridge:
    def __init__(self, target_dir: Optional[str] = None):
        if target_dir:
            self.target_dir = target_dir
        else:
            self.target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    def generate_unified_prompt_rules(self) -> str:
        return """# ⚡ ZOBAR SKILL: UNIVERSAL VIBE CODING & ARCHITECTURE STANDARD

You are operating under the ZOBAR SKILL master engineering protocol. You are not a generic coding bot; you are a Principal Systems Architect, Master Prompt Engineer, and Deep-Tech Researcher.

## 1. FIRST PRINCIPLES & PERFORMANCE (SUB-MILLISECOND MANDATE)
- Zero-copy data pipelines, lock-free concurrency, and cache-friendly contiguous memory (ECS / Data-Oriented Design) are prioritized over deep polymorphic class hierarchies.
- Pure standard library first: Do not introduce heavy runtime dependencies unless mathematically necessary.
- Memory & Latency: Enforce sub-millisecond execution, PagedAttention KV-cache principles, and semantic caching before triggering heavy LLM calls.

## 2. CODE QUALITY & HARDENING
- Write 100% deterministic, offline-testable unit tests for every critical logic module.
- Multi-tenancy and data isolation must be enforced at the database level via PostgreSQL Row-Level Security (RLS) and pgvector HNSW indexing.
- Zero-Tolerance on Security: No unsanitized string interpolations in SQL or shell executions; strict CSP and XSS sanitization in UI outputs.

## 3. ASYMMETRIC VALUE & LEAN FINOPS
- Every architecture must have a FinOps cost model: Route simple tasks to Tier 1 lightweight models; reserve Tier 2 frontier models only for deep architectural proofs.
- Design with LTV/CAC > 3.0 and zero-capital cloud leverage (Cloudflare Workers, Supabase free-tier, local quantized models).

## 4. DESIGN & USER EXPERIENCE (S-TIER STANDARD)
- Follow the 202 S-Tier Design Vault layout paradigms (Linear-style command palettes, Bento Grids, Spring physics micro-interactions).
- Never output sloppy, unstyled generic HTML. Always output production-grade modern UI tokens.
"""

    def export_all_ide_configs(self) -> Dict[str, str]:
        """
        Exports configuration files for all major vibe coding IDEs and AI tools.
        """
        rules_text = self.generate_unified_prompt_rules()
        exported = {}

        # 1. Cursor (.cursorrules)
        cursor_path = os.path.join(self.target_dir, ".cursorrules")
        with open(cursor_path, "w", encoding="utf-8") as f:
            f.write(rules_text)
        exported[".cursorrules"] = cursor_path

        # 1b. Cursor MDC Rule (.cursor/rules/zobar.mdc)
        cursor_mdc_dir = os.path.join(self.target_dir, ".cursor", "rules")
        os.makedirs(cursor_mdc_dir, exist_ok=True)
        cursor_mdc_path = os.path.join(cursor_mdc_dir, "zobar.mdc")
        with open(cursor_mdc_path, "w", encoding="utf-8") as f:
            f.write(f"---\ndescription: Zobar Skill Core Engineering Standard\nglobs: *\n---\n\n{rules_text}")
        exported[".cursor/rules/zobar.mdc"] = cursor_mdc_path

        # 2. Claude Code (CLAUDE.md)
        claude_path = os.path.join(self.target_dir, "CLAUDE.md")
        with open(claude_path, "w", encoding="utf-8") as f:
            f.write(f"# Claude Code Guidance\n\n{rules_text}")
        exported["CLAUDE.md"] = claude_path

        # 3. Windsurf (.windsurfrules)
        windsurf_path = os.path.join(self.target_dir, ".windsurfrules")
        with open(windsurf_path, "w", encoding="utf-8") as f:
            f.write(rules_text)
        exported[".windsurfrules"] = windsurf_path

        # 4. GitHub Copilot / Codex (.github/copilot-instructions.md)
        copilot_dir = os.path.join(self.target_dir, ".github")
        os.makedirs(copilot_dir, exist_ok=True)
        copilot_path = os.path.join(copilot_dir, "copilot-instructions.md")
        with open(copilot_path, "w", encoding="utf-8") as f:
            f.write(f"# GitHub Copilot & Codex Instructions\n\n{rules_text}")
        exported[".github/copilot-instructions.md"] = copilot_path

        # 5. Gemini / Antigravity (GEMINI.md)
        gemini_path = os.path.join(self.target_dir, "GEMINI.md")
        with open(gemini_path, "w", encoding="utf-8") as f:
            f.write(f"# Google Antigravity & Gemini Project Context\n\n{rules_text}")
        exported["GEMINI.md"] = gemini_path

        return exported


if __name__ == "__main__":
    import sys
    # Ensure stdout handles UTF-8 on Windows cp1254
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    bridge = VibeCodingBridge()
    files = bridge.export_all_ide_configs()
    print("=" * 65)
    print("[*] EVRENSEL VIBE CODING VE AI-IDE ENTEGRASYON KOPRUSU")
    print("=" * 65)
    for ide, path in files.items():
        print(f"[*] Senkronize Edildi: {ide:30} -> {path}")
