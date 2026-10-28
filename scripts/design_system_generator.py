"""
Modern Design Styles & UI Token Generator
Zobar Skill — Glassmorphism, Aurora Gradients, Neo-Brutalism, Cyberpunk HUD & Bento

Provides production-ready, copy-pasteable CSS, Tailwind CSS classes,
and React/JSX component snippets for trending S-Tier design paradigms.
"""

import os
import json
from typing import Dict, Any, List, Optional

DESIGN_STYLES = {
    "glassmorphism": {
        "name": "Glassmorphism (Frosted / Glassy Design)",
        "description": "Ultra-sleek translucent frosted glass aesthetic popularized by Apple macOS/iOS and visionOS.",
        "tailwind_classes": "bg-white/10 dark:bg-black/20 backdrop-blur-xl border border-white/20 dark:border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.37)] rounded-2xl",
        "css_properties": {
            "background": "rgba(255, 255, 255, 0.08)",
            "backdrop-filter": "blur(16px) saturate(180%)",
            "-webkit-backdrop-filter": "blur(16px) saturate(180%)",
            "border": "1px solid rgba(255, 255, 255, 0.125)",
            "box-shadow": "0 8px 32px 0 rgba(0, 0, 0, 0.37)",
            "border-radius": "16px",
        },
        "react_component_snippet": (
            "export function GlassCard({ children }: { children: React.ReactNode }) {\n"
            "  return (\n"
            "    <div className='relative overflow-hidden rounded-2xl border border-white/20 bg-white/10 p-6 shadow-2xl backdrop-blur-xl dark:border-white/10 dark:bg-black/30'>\n"
            "      <div className='pointer-events-none absolute -inset-px opacity-50 bg-gradient-to-br from-white/30 to-transparent' />\n"
            "      <div className='relative z-10'>{children}</div>\n"
            "    </div>\n"
            "  );\n"
            "}"
        ),
        "best_for": "Modal dialogs, sticky navigation bars, floating HUD widgets, visionOS spatial panels",
    },
    "aurora_mesh_gradient": {
        "name": "Aurora / Mesh Gradient Glow",
        "description": "Fluid, multi-layered glowing light orbs with deep blur, popularized by Stripe, Linear, and Vercel.",
        "tailwind_classes": "relative overflow-hidden bg-slate-950 before:absolute before:-top-40 before:-left-40 before:w-96 before:h-96 before:bg-purple-600/30 before:rounded-full before:blur-[128px] after:absolute after:-bottom-40 after:-right-40 after:w-96 after:h-96 after:bg-cyan-600/30 after:rounded-full after:blur-[128px]",
        "css_properties": {
            "background-color": "#030712",
            "background-image": "radial-gradient(at 0% 0%, rgba(147, 51, 234, 0.3) 0px, transparent 50%), radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.3) 0px, transparent 50%)",
        },
        "react_component_snippet": (
            "export function AuroraBackground({ children }: { children: React.ReactNode }) {\n"
            "  return (\n"
            "    <div className='relative min-h-screen w-full bg-slate-950 text-white overflow-hidden'>\n"
            "      <div className='absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-gradient-to-tr from-indigo-500/30 via-purple-500/20 to-pink-500/30 rounded-full blur-[140px] pointer-events-none animate-pulse' />\n"
            "      <div className='relative z-10'>{children}</div>\n"
            "    </div>\n"
            "  );\n"
            "}"
        ),
        "best_for": "Hero sections, landing page backdrops, feature showcase headers",
    },
    "neo_brutalism": {
        "name": "Neo-Brutalism (Bold Pop & Hard Shadows)",
        "description": "Vibrant, unapologetic design style with thick black borders, hard unblurred drop-shadows, and high contrast typography (Gumroad, Figma community).",
        "tailwind_classes": "bg-amber-300 border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all font-bold text-black rounded-lg p-4",
        "css_properties": {
            "background-color": "#fde047",
            "border": "2px solid #000000",
            "box-shadow": "4px 4px 0px 0px #000000",
            "border-radius": "8px",
            "transition": "all 0.15s ease-in-out",
        },
        "react_component_snippet": (
            "export function NeoButton({ label, onClick }: { label: string; onClick?: () => void }) {\n"
            "  return (\n"
            "    <button onClick={onClick} className='rounded-lg border-2 border-black bg-lime-400 px-6 py-3 font-extrabold text-black shadow-[4px_4px_0px_0px_#000] transition-all hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_#000] active:translate-x-[4px] active:translate-y-[4px] active:shadow-none'>\n"
            "      {label}\n"
            "    </button>\n"
            "  );\n"
            "}"
        ),
        "best_for": "Creator tools, playful developer platforms, fintech for Gen-Z, bold CTA buttons",
    },
    "cyberpunk_hud": {
        "name": "Cyberpunk / Sci-Fi HUD (Tech Telemetry)",
        "description": "Futuristic aerospace & military telemetry aesthetic with chamfered angular clips, cyan/amber glowing borders, and scanlines.",
        "tailwind_classes": "bg-slate-900/90 border border-cyan-500/50 shadow-[0_0_15px_rgba(6,182,212,0.3)] font-mono text-cyan-400 [clip-path:polygon(0_0,calc(100%-12px)_0,100%_12px,100%_100%,12px_100%,0_calc(100%-12px))] p-5",
        "css_properties": {
            "background": "rgba(15, 23, 42, 0.9)",
            "border": "1px solid rgba(6, 182, 212, 0.6)",
            "box-shadow": "0 0 15px rgba(6, 182, 212, 0.35)",
            "clip-path": "polygon(0 0, calc(100% - 12px) 0, 100% 12px, 100% 100%, 12px 100%, 0 calc(100% - 12px))",
            "font-family": "monospace",
        },
        "react_component_snippet": (
            "export function SciFiHudCard({ title, value }: { title: string; value: string }) {\n"
            "  return (\n"
            "    <div className='relative bg-black/80 border border-cyan-500/60 p-4 font-mono shadow-[0_0_20px_rgba(6,182,212,0.25)] [clip-path:polygon(0_0,calc(100%-14px)_0,100%_14px,100%_100%,14px_100%,0_calc(100%-14px))]'>\n"
            "      <div className='flex items-center justify-between text-xs text-cyan-500 tracking-widest uppercase'>\n"
            "        <span>{title}</span>\n"
            "        <span className='h-2 w-2 rounded-full bg-cyan-400 animate-ping' />\n"
            "      </div>\n"
            "      <div className='mt-2 text-2xl font-black text-cyan-300'>{value}</div>\n"
            "    </div>\n"
            "  );\n"
            "}"
        ),
        "best_for": "System telemetry dashboards, gaming interfaces, trading terminals, cybersecurity monitors",
    },
    "dark_mode_bento": {
        "name": "Dark Mode Bento Grid",
        "description": "Linear and Apple style structured modular grid with subtle edge gradients, dark elevation, and spring physics hover states.",
        "tailwind_classes": "grid grid-cols-12 gap-4 auto-rows-[180px] max-w-7xl mx-auto p-4",
        "css_properties": {
            "display": "grid",
            "grid-template-columns": "repeat(12, minmax(0, 1fr))",
            "gap": "16px",
        },
        "react_component_snippet": (
            "export function BentoItem({ className, children }: { className?: string; children: React.ReactNode }) {\n"
            "  return (\n"
            "    <div className={`group relative rounded-3xl border border-white/10 bg-zinc-900/80 p-6 backdrop-blur-md transition-all duration-300 hover:border-white/20 hover:shadow-2xl hover:shadow-indigo-500/10 ${className}`}>\n"
            "      <div className='absolute inset-0 rounded-3xl bg-gradient-to-b from-white/5 to-transparent opacity-0 transition-opacity duration-300 group-hover:opacity-100' />\n"
            "      <div className='relative z-10 h-full flex flex-col justify-between'>{children}</div>\n"
            "    </div>\n"
            "  );\n"
            "}"
        ),
        "best_for": "Product feature overviews, SaaS landing pages, portfolio grids",
    },
    "claymorphism": {
        "name": "Claymorphism (Soft Inflatable 3D)",
        "description": "Friendly, tactile 3D clay aesthetic with dual internal specular lighting and deep exterior drop shadows.",
        "tailwind_classes": "bg-indigo-500/90 rounded-3xl shadow-[0_20px_40px_rgba(0,0,0,0.15)] [box-shadow:inset_0_-8px_12px_rgba(0,0,0,0.2),inset_0_8px_12px_rgba(255,255,255,0.4)] p-6 text-white",
        "css_properties": {
            "background-color": "#6366f1",
            "border-radius": "24px",
            "box-shadow": "0 20px 40px rgba(0,0,0,0.15), inset 0 -8px 12px rgba(0,0,0,0.2), inset 0 8px 12px rgba(255,255,255,0.4)",
        },
        "react_component_snippet": (
            "export function ClayButton({ children }: { children: React.ReactNode }) {\n"
            "  return (\n"
            "    <button className='rounded-2xl bg-indigo-600 px-6 py-3 font-semibold text-white shadow-[0_12px_24px_rgba(0,0,0,0.15)] [box-shadow:inset_0_-6px_8px_rgba(0,0,0,0.25),inset_0_6px_8px_rgba(255,255,255,0.35)] transition-transform active:scale-95'>\n"
            "      {children}\n"
            "    </button>\n"
            "  );\n"
            "}"
        ),
        "best_for": "Mobile app cards, onboarding buttons, educational platforms, metaverse / playful UIs",
    }
}


class ModernDesignStylesEngine:
    def __init__(self):
        self.styles = DESIGN_STYLES

    def get_style(self, style_key: str) -> Optional[Dict[str, Any]]:
        return self.styles.get(style_key.lower().strip())

    def list_styles(self) -> List[Dict[str, str]]:
        return [
            {"key": k, "name": v["name"], "description": v["description"], "best_for": v["best_for"]}
            for k, v in self.styles.items()
        ]

    def export_vault_json(self, output_path: Optional[str] = None) -> str:
        if not output_path:
            output_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "references", "modern_design_styles_vault.json")
            )
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({
                "version": "1.0.0",
                "total_styles": len(self.styles),
                "styles": self.styles,
            }, f, indent=2, ensure_ascii=False)
        return output_path


if __name__ == "__main__":
    engine = ModernDesignStylesEngine()
    out = engine.export_vault_json()
    print("=" * 65)
    print(f"[*] MODERN TASARIM VE CAM EFEKTLERİ (GLASSY) HAVUZU OLUŞTURULDU")
    print(f"[*] Toplam Tasarım Stili: {len(engine.styles)}")
    print(f"[*] Kayıt Yeri          : {out}")
    print("=" * 65)
    for s in engine.list_styles():
        print(f"• {s['name']} -> {s['best_for']}")
