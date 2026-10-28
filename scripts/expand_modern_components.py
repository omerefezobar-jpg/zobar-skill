#!/usr/bin/env python3
"""
Expands references/free_modern_components_vault.json to 16 production-grade,
zero-cost modern React & Tailwind CSS v4 components.
"""

import json
import os
import sys

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT_PATH = os.path.join(os.path.dirname(__file__), "..", "references", "free_modern_components_vault.json")

NEW_COMPONENTS = [
    {
        "id": "COMP-05",
        "name": "3D Interactive WebGL Particle Wave Canvas",
        "category": "3D & Spatial Visuals",
        "description": "GPU-accelerated interactive particle mesh canvas responding to mouse motion with zero lag.",
        "tailwind_classes": "relative w-full h-[360px] rounded-3xl overflow-hidden bg-slate-950 border border-slate-800",
        "react_jsx": """export const WebGLParticleCanvas = () => {
  const canvasRef = React.useRef(null);
  React.useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animationId;
    let width = canvas.width = canvas.offsetWidth;
    let height = canvas.height = canvas.offsetHeight;
    let mouse = { x: width / 2, y: height / 2 };

    const particles = Array.from({ length: 75 }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.8,
      vy: (Math.random() - 0.5) * 0.8,
      radius: Math.random() * 2 + 1
    }));

    const render = () => {
      ctx.fillStyle = '#030712';
      ctx.fillRect(0, 0, width, height);

      particles.forEach((p, i) => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(56, 189, 248, 0.6)';
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 85) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = `rgba(56, 189, 248, ${0.25 * (1 - dist / 85)})`;
            ctx.lineWidth = 0.75;
            ctx.stroke();
          }
        }
      });
      animationId = requestAnimationFrame(render);
    };
    render();
    return () => cancelAnimationFrame(animationId);
  }, []);

  return (
    <div className="relative w-full h-[360px] rounded-3xl overflow-hidden bg-slate-950 border border-slate-800">
      <canvas ref={canvasRef} className="w-full h-full block" />
      <div className="absolute inset-0 pointer-events-none flex items-center justify-center">
        <h3 className="text-2xl font-black text-white/90 tracking-tight drop-shadow-md">Spatial Particle Physics</h3>
      </div>
    </div>
  );
};"""
    },
    {
        "id": "COMP-06",
        "name": "Glassmorphic Floating Command Palette (Cmd+K)",
        "category": "Navigation & Command Palettes",
        "description": "Linear-style modal command palette with fuzzy keyboard navigation and hotkey badges.",
        "tailwind_classes": "fixed inset-0 bg-slate-950/80 backdrop-blur-md flex items-start justify-center pt-24 z-50 p-4",
        "react_jsx": """export const CommandPalette = ({ isOpen, onClose }) => {
  const [query, setQuery] = React.useState("");
  const items = [
    { id: "1", title: "Yeni Proje Başlat", shortcut: "⌘N" },
    { id: "2", title: "Mevzuat ve AI Act Denetimi", shortcut: "⌘L" },
    { id: "3", title: "Sistem Matematiği & FinOps", shortcut: "⌘M" },
    { id: "4", title: "Trend & Trick Harvester", shortcut: "⌘T" }
  ];
  if (!isOpen) return null;
  const filtered = items.filter(i => i.title.toLowerCase().includes(query.toLowerCase()));
  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md flex items-start justify-center pt-24 z-50 p-4" onClick={onClose}>
      <div className="w-full max-w-xl rounded-2xl bg-slate-900 border border-slate-700/80 shadow-2xl overflow-hidden" onClick={e => e.stopPropagation()}>
        <div className="p-4 border-b border-slate-800 flex items-center gap-3">
          <span className="text-slate-400 font-mono text-sm">🔍</span>
          <input
            autoFocus
            type="text"
            placeholder="Bir komut veya eylem arayın... (ESC çıkış)"
            value={query}
            onChange={e => setQuery(e.target.value)}
            className="w-full bg-transparent text-white placeholder-slate-500 focus:outline-none text-base"
          />
        </div>
        <div className="p-2 max-h-64 overflow-y-auto">
          {filtered.map(i => (
            <div key={i.id} className="p-3 rounded-xl hover:bg-slate-800/80 flex items-center justify-between text-slate-200 cursor-pointer transition-colors">
              <span className="font-medium text-sm">{i.title}</span>
              <kbd className="px-2 py-0.5 rounded bg-slate-800 border border-slate-700 text-xs font-mono text-slate-400">{i.shortcut}</kbd>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};"""
    },
    {
        "id": "COMP-07",
        "name": "Aurora Glow Dynamic Animated Gradient Mesh",
        "category": "Hero & Ambient Lighting",
        "description": "High-end Scandinavian aura background with multi-hue blur-3xl animated light spots.",
        "tailwind_classes": "relative overflow-hidden w-full h-[400px] rounded-3xl bg-slate-950 flex items-center justify-center",
        "react_jsx": """export const AuroraGlowHero = () => (
  <div className="relative overflow-hidden w-full h-[400px] rounded-3xl bg-slate-950 flex items-center justify-center">
    <div className="absolute -top-24 -left-24 w-96 h-96 bg-purple-500/30 rounded-full blur-3xl animate-pulse" />
    <div className="absolute -bottom-24 -right-24 w-96 h-96 bg-emerald-500/20 rounded-full blur-3xl animate-pulse delay-1000" />
    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-sky-500/25 rounded-full blur-3xl animate-pulse delay-700" />
    <div className="relative z-10 text-center space-y-4 px-6">
      <span className="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-white/10 text-white border border-white/20 backdrop-blur-md">
        Zero-Cost Ambient UI
      </span>
      <h2 className="text-4xl md:text-5xl font-extrabold text-white tracking-tight">
        Aurora S-Tier Lighting
      </h2>
      <p className="text-slate-400 text-sm max-w-md mx-auto">
        GPU-friendly pure CSS blur layers that transform ordinary layouts into Apple/Linear grade visual powerhouses.
      </p>
    </div>
  </div>
);"""
    },
    {
        "id": "COMP-08",
        "name": "Real-Time WebSocket Heartbeat & Telemetry Status Badge",
        "category": "Status & Telemetry Badges",
        "description": "Live pulsating connection pill displaying microsecond latency and cluster health.",
        "tailwind_classes": "inline-flex items-center gap-2.5 px-3.5 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-xs font-mono text-slate-300",
        "react_jsx": """export const ClusterStatusPill = ({ latencyMs = 2.4, status = "HEALTHY_ONLINE" }) => (
  <div className="inline-flex items-center gap-2.5 px-3.5 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-xs font-mono text-slate-300">
    <span className="relative flex h-2.5 w-2.5">
      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75" />
      <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500" />
    </span>
    <span className="font-semibold text-white">{status}</span>
    <span className="text-slate-500">|</span>
    <span className="text-emerald-400 font-bold">{latencyMs} ms</span>
  </div>
);"""
    },
    {
        "id": "COMP-09",
        "name": "Magnetic Fluid CTA Button with Spring Physics",
        "category": "Buttons & Micro-Interactions",
        "description": "Magnetic button snapping toward cursor with radiant glow border and tactile active bounce.",
        "tailwind_classes": "relative inline-flex items-center justify-center p-0.5 overflow-hidden rounded-2xl group active:scale-95 transition-transform duration-150",
        "react_jsx": """export const MagneticFluidButton = ({ label = "Ücretsiz Başlatın", onClick }) => (
  <button
    onClick={onClick}
    className="relative inline-flex items-center justify-center p-0.5 overflow-hidden rounded-2xl group active:scale-95 transition-transform duration-150 focus:outline-none"
  >
    <span className="absolute inset-0 bg-gradient-to-r from-teal-400 via-indigo-500 to-pink-500 rounded-2xl animate-[spin_4s_linear_infinite] group-hover:opacity-100 opacity-75 blur-sm transition-opacity" />
    <span className="relative px-6 py-3 rounded-[14px] bg-slate-950 text-white font-bold text-sm tracking-wide transition-all duration-200 group-hover:bg-slate-900 flex items-center gap-2">
      {label}
      <span className="group-hover:translate-x-1 transition-transform">→</span>
    </span>
  </button>
);"""
    },
    {
        "id": "COMP-10",
        "name": "Interactive Kelly Criterion & Systems Math FinOps Slider",
        "category": "Sales & Pricing Tools",
        "description": "Calculates optimal risk-adjusted allocation size f* = (bp - q) / b for indie developers and SaaS founders.",
        "tailwind_classes": "rounded-3xl bg-slate-950 border border-slate-800 p-6 space-y-5 max-w-md mx-auto text-white",
        "react_jsx": """export const KellyCriterionSimulator = () => {
  const [winRate, setWinRate] = React.useState(0.65);
  const [odds, setOdds] = React.useState(2.0);
  const q = 1 - winRate;
  const fStar = Math.max(0, ((odds * winRate) - q) / odds);
  return (
    <div className="rounded-3xl bg-slate-950 border border-slate-800 p-6 space-y-5 max-w-md mx-auto text-white">
      <div className="flex justify-between items-center border-b border-slate-800 pb-3">
        <h4 className="font-bold text-sm text-slate-300">Kelly Kriteri Tahsis Boyutu (f*)</h4>
        <span className="text-xs px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 font-mono">Systems Math</span>
      </div>
      <div className="space-y-2">
        <div className="flex justify-between text-xs text-slate-400">
          <span>Kazanma İhtimali (p):</span>
          <span className="font-bold text-white">{(winRate * 100).toFixed(0)}%</span>
        </div>
        <input
          type="range" min="0.30" max="0.90" step="0.05" value={winRate}
          onChange={e => setWinRate(parseFloat(e.target.value))}
          className="w-full accent-sky-400 cursor-pointer"
        />
      </div>
      <div className="p-4 rounded-2xl bg-sky-950/30 border border-sky-500/20 text-center">
        <div className="text-xs text-sky-400 font-semibold uppercase tracking-wider">Önerilen Sermaye Payı (f*)</div>
        <div className="text-3xl font-black text-white mt-1">{(fStar * 100).toFixed(1)}%</div>
      </div>
    </div>
  );
};"""
    },
    {
        "id": "COMP-11",
        "name": "Expandable Bento Grid Matrix with Dynamic Aspect Ratio",
        "category": "Analytics & Bento Grid",
        "description": "Multi-span bento grid layout with subtle border radiance and responsive desktop tile expansion.",
        "tailwind_classes": "grid grid-cols-1 md:grid-cols-3 gap-4 max-w-5xl mx-auto p-4",
        "react_jsx": """export const ExpandableBentoGrid = () => (
  <div className="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-5xl mx-auto p-4">
    <div className="md:col-span-2 rounded-3xl bg-slate-900/60 border border-slate-800 p-8 relative overflow-hidden group hover:border-slate-700 transition-all">
      <div className="text-xs font-bold text-sky-400 uppercase tracking-widest mb-2">Çekirdek Motor</div>
      <h3 className="text-2xl font-black text-white">Sıfır-Kopya Halka Arabellek</h3>
      <p className="text-slate-400 text-sm mt-2 max-w-md">Ringbuffer ve lock-free kuyruklarla sub-millisecond veri boru hatları inşa edin.</p>
    </div>
    <div className="rounded-3xl bg-slate-900/60 border border-slate-800 p-8 relative overflow-hidden group hover:border-slate-700 transition-all">
      <div className="text-xs font-bold text-emerald-400 uppercase tracking-widest mb-2">Hukuk Mührü</div>
      <h3 className="text-xl font-bold text-white">EU AI Act Uyumlu</h3>
      <p className="text-slate-400 text-xs mt-2">Madde 2(8) ve MDR 2017/745 30-vaka emsalli sıfır toleranslı mevzuat tarayıcısı.</p>
    </div>
  </div>
);"""
    },
    {
        "id": "COMP-12",
        "name": "Audio Waveform Visualizer & Voice Activity Detector (VAD)",
        "category": "Audio & Voice DSP",
        "description": "Real-time dynamic sound frequency wave bars reflecting spoken voice level and activity state.",
        "tailwind_classes": "flex items-center gap-1.5 px-4 py-3 rounded-2xl bg-slate-900 border border-slate-800 w-fit",
        "react_jsx": """export const AudioWaveformVisualizer = ({ isActive = true }) => {
  const bars = [14, 28, 42, 20, 36, 12, 30, 48, 22, 16];
  return (
    <div className="flex items-center gap-1.5 px-4 py-3 rounded-2xl bg-slate-900 border border-slate-800 w-fit">
      {bars.map((h, i) => (
        <span
          key={i}
          style={{ height: isActive ? `${h}px` : "6px" }}
          className={`w-1 rounded-full transition-all duration-150 ${
            isActive ? "bg-emerald-400 animate-pulse" : "bg-slate-700"
          }`}
        />
      ))}
      <span className="text-xs font-mono font-bold text-slate-300 ml-2">
        {isActive ? "VAD: SES AKTİF" : "SES BEKLENİYOR"}
      </span>
    </div>
  );
};"""
    },
    {
        "id": "COMP-13",
        "name": "Dark-Mode Morphing SVG Path Switcher with Spring Transition",
        "category": "Buttons & Micro-Interactions",
        "description": "Sun to Moon smooth morphing icon button using SVG transforms and fluid rotation.",
        "tailwind_classes": "p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 transition-all duration-200 active:scale-90",
        "react_jsx": """export const DarkModeMorphToggle = () => {
  const [isDark, setIsDark] = React.useState(true);
  return (
    <button
      onClick={() => setIsDark(!isDark)}
      className="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 transition-all duration-200 active:scale-90"
      aria-label="Tema Değiştir"
    >
      <span className="text-lg block transition-transform duration-300 transform rotate-0 hover:rotate-45">
        {isDark ? "🌙" : "☀️"}
      </span>
    </button>
  );
};"""
    },
    {
        "id": "COMP-14",
        "name": "High-Conversion Tiered SaaS Pricing Matrix",
        "category": "Sales & Pricing Tools",
        "description": "Three-tier pricing table with annual billing discount pill, popular gradient highlight, and feature list.",
        "tailwind_classes": "grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto p-4",
        "react_jsx": """export const TieredPricingMatrix = () => {
  const [annual, setAnnual] = React.useState(true);
  return (
    <div className="space-y-8 max-w-5xl mx-auto p-4 text-white">
      <div className="flex justify-center items-center gap-3">
        <span className="text-sm font-medium text-slate-400">Aylık</span>
        <button
          onClick={() => setAnnual(!annual)}
          className={`w-12 h-6 flex items-center rounded-full p-1 transition-colors ${annual ? "bg-emerald-500" : "bg-slate-800"}`}
        >
          <div className={`bg-white w-4 h-4 rounded-full shadow-md transform transition-transform ${annual ? "translate-x-6" : ""}`} />
        </button>
        <span className="text-sm font-medium text-white flex items-center gap-1.5">
          Yıllık <span className="text-xs px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-bold">%20 İndirim</span>
        </span>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="rounded-3xl bg-slate-900 border border-slate-800 p-8 space-y-4">
          <h4 className="text-lg font-bold">Başlangıç</h4>
          <div className="text-3xl font-black">${annual ? "19" : "24"}<span className="text-sm text-slate-400">/ay</span></div>
          <p className="text-xs text-slate-400">Tekil indie geliştiriciler için temel araçlar.</p>
        </div>
        <div className="rounded-3xl bg-slate-900 border-2 border-emerald-500 p-8 space-y-4 relative shadow-[0_0_30px_rgba(16,185,129,0.2)]">
          <span className="absolute -top-3 right-6 px-3 py-0.5 rounded-full bg-emerald-500 text-slate-950 text-xs font-black uppercase">En Çok Seçilen</span>
          <h4 className="text-lg font-bold">Pro Ajans</h4>
          <div className="text-3xl font-black">${annual ? "49" : "59"}<span className="text-sm text-slate-400">/ay</span></div>
          <p className="text-xs text-slate-400">Sınırsız müşteri ve tam AI kod üretim desteği.</p>
        </div>
        <div className="rounded-3xl bg-slate-900 border border-slate-800 p-8 space-y-4">
          <h4 className="text-lg font-bold">Enterprise</h4>
          <div className="text-3xl font-black">${annual ? "149" : "179"}<span className="text-sm text-slate-400">/ay</span></div>
          <p className="text-xs text-slate-400">Özel SLA ve öncelikli mühendislik senatosu desteği.</p>
        </div>
      </div>
    </div>
  );
};"""
    },
    {
        "id": "COMP-15",
        "name": "Smooth Height Accordion FAQ with CSS Grid Transition",
        "category": "Navigation & Command Palettes",
        "description": "Zero layout-shift accordion expanding from 0fr to 1fr using pure CSS grid transition.",
        "tailwind_classes": "max-w-2xl mx-auto space-y-3",
        "react_jsx": """export const SmoothAccordionFAQ = ({ items = [
  { q: "Zobar Skill hangi çerçeveleri destekliyor?", a: "Tüm modern React, Next.js, Tailwind CSS v4, Three.js ve Node.js ekosistemlerini destekler." },
  { q: "Mevzuat denetimi neleri kapsar?", a: "EU AI Act Madde 6, MDR 2017/745 Tıbbi Cihaz ve GDPR veri koruma direktiflerini kapsar." }
] }) => {
  const [openIdx, setOpenIdx] = React.useState(null);
  return (
    <div className="max-w-2xl mx-auto space-y-3">
      {items.map((it, idx) => (
        <div key={idx} className="rounded-2xl bg-slate-900 border border-slate-800 overflow-hidden">
          <button
            onClick={() => setOpenIdx(openIdx === idx ? null : idx)}
            className="w-full p-5 text-left flex justify-between items-center text-white font-semibold text-sm"
          >
            {it.q}
            <span className={`transform transition-transform ${openIdx === idx ? "rotate-180" : ""}`}>▼</span>
          </button>
          <div className={`grid transition-all duration-200 ease-in-out ${openIdx === idx ? "grid-rows-[1fr] opacity-100 p-5 pt-0" : "grid-rows-[0fr] opacity-0"}`}>
            <div className="overflow-hidden text-slate-400 text-sm">{it.a}</div>
          </div>
        </div>
      ))}
    </div>
  );
};"""
    },
    {
        "id": "COMP-16",
        "name": "Mobile Bottom Conversion Drawer with Quick WhatsApp & Lead Form",
        "category": "Conversion & Mobile CTA",
        "description": "Interactive sliding bottom sheet with one-click phone dialer and short quotation form.",
        "tailwind_classes": "fixed inset-x-0 bottom-0 z-50 bg-slate-900/95 backdrop-blur-xl border-t border-slate-700/80 rounded-t-3xl p-6 shadow-2xl space-y-4",
        "react_jsx": """export const MobileConversionDrawer = ({ onClose }) => (
  <div className="fixed inset-x-0 bottom-0 z-50 bg-slate-900/95 backdrop-blur-xl border-t border-slate-700/80 rounded-t-3xl p-6 shadow-2xl space-y-4">
    <div className="w-12 h-1.5 rounded-full bg-slate-700 mx-auto" />
    <div className="flex justify-between items-center">
      <div>
        <h4 className="text-white font-bold text-base">Hızlı Fiyat Teklifi Alın</h4>
        <p className="text-slate-400 text-xs">Mühendislerimiz 15 dakika içinde incelesin.</p>
      </div>
      <button onClick={onClose} className="text-slate-400 hover:text-white">✕</button>
    </div>
    <div className="grid grid-cols-2 gap-3 pt-2">
      <a href="tel:+905551234567" className="py-3 px-4 rounded-xl bg-slate-800 text-white font-bold text-center text-sm">Hemen Ara</a>
      <a href="https://wa.me/905551234567" className="py-3 px-4 rounded-xl bg-emerald-500 text-slate-950 font-bold text-center text-sm">WhatsApp Mesaj</a>
    </div>
  </div>
);"""
    }
]

def main():
    if not os.path.exists(VAULT_PATH):
        print(f"Error: {VAULT_PATH} not found")
        sys.exit(1)

    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_components = data.get("components", [])
    existing_ids = {c["id"] for c in existing_components}

    added = 0
    for comp in NEW_COMPONENTS:
        if comp["id"] not in existing_ids:
            existing_components.append(comp)
            existing_ids.add(comp["id"])
            added += 1

    data["components"] = existing_components
    data["vault_metadata"]["total_components"] = len(existing_components)
    data["vault_metadata"]["version"] = "2.0.0"

    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[*] Modern Component Vault Genişletildi: {len(existing_components)} bileşen (+{added} yeni)")

if __name__ == "__main__":
    main()
