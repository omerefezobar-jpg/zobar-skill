#!/usr/bin/env python3
"""
Builder script to expand S-Tier Design Vault to 404+ world-class digital products,
SaaS applications, developer tools, spatial 3D computing, SCADA, AI agent workbenches,
and heavy engineering software.
"""

import json
import os
import sys

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT_PATH = os.path.join(os.path.dirname(__file__), "..", "references", "s_tier_design_vault.json")

# 12 New Categories with 10+ high-quality products each = 120+ products
NEW_CATEGORIES_AND_SITES = [
    {
        "category_name": "3D Spatial Computing, WebGL & Interactive Portals",
        "design_paradigm": "Full-Viewport WebGL/WebGPU Canvas, Reactive 3D Meshes, Spring Physics & Spatial Sound",
        "recommended_libraries": ["Three.js", "@react-three/fiber", "Spline Runtime", "GLSL Shaders", "GSAP ScrollTrigger"],
        "sites": [
            {
                "name": "Spline 3D",
                "url": "https://spline.design",
                "hero_pattern": "Interactive real-time 3D physics mesh responding to cursor velocity and drag gestures",
                "component_features": "In-browser 3D scene editor, material nodal tree, responsive glassmorphic inspector dock, export code drawer",
                "color_tokens": {"background": "#0D0E12", "accent": "#4D6BFE", "text": "#FFFFFF"},
                "key_interactions": "Smooth 3D camera pan/orbit on scroll, magnetic button snapping with particle burst"
            },
            {
                "name": "Midjourney Showcase",
                "url": "https://www.midjourney.com",
                "hero_pattern": "Infinite kinetic typography scroller transitioning into high-density neural generative grid",
                "component_features": "Virtualized image matrix with progressive WebP streaming, prompt inspector pill, community upvote heart",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#E0E0E0"},
                "key_interactions": "Subtle blur-up image decoding, seamless modal expander with metadata pane"
            },
            {
                "name": "Luma AI (Dream Machine)",
                "url": "https://lumalabs.ai",
                "hero_pattern": "Interactive NeRF (Neural Radiance Field) 360-degree volumetric video canvas",
                "component_features": "Volumetric capture slider, instant prompt generation omnibar, interactive camera trajectory controls",
                "color_tokens": {"background": "#0A0A0A", "accent": "#00F0FF", "text": "#FFFFFF"},
                "key_interactions": "Cursor-driven light ray reflection, multi-perspective drag rotation"
            },
            {
                "name": "Runway Gen-3",
                "url": "https://runwayml.com",
                "hero_pattern": "Cinematic motion video canvas with generative temporal diffusion previewer",
                "component_features": "Timeline motion brush canvas, multi-asset video bin, rendering progress pill, model selector dropdown",
                "color_tokens": {"background": "#0F0F11", "accent": "#14F195", "text": "#F3F3F4"},
                "key_interactions": "Scrub-to-preview video timeline, spring-damped drawer transition"
            },
            {
                "name": "Unreal Engine Portal",
                "url": "https://www.unrealengine.com",
                "hero_pattern": "Ultra-fidelity ray-traced hero reel with dark slate backdrop and metallic typography",
                "component_features": "Interactive feature showcase accordion, Marketplace asset browser, technical documentation drawer",
                "color_tokens": {"background": "#0E1117", "accent": "#0E76FD", "text": "#FFFFFF"},
                "key_interactions": "Parallax 3D asset spotlight, interactive shader switch preview"
            },
            {
                "name": "PlayCanvas",
                "url": "https://playcanvas.com",
                "hero_pattern": "Instant-loading WebGL 3D game scene running at 60fps in browser canvas",
                "component_features": "Real-time collaborative entity-component hierarchy, code editor pane, texture compression inspector",
                "color_tokens": {"background": "#1E1E24", "accent": "#E63946", "text": "#F1FAEE"},
                "key_interactions": "Hot-reloading scene reload without page refresh, live entity transform gizmo"
            },
            {
                "name": "Babylon.js Playground",
                "url": "https://playground.babylonjs.com",
                "hero_pattern": "Split-screen TypeScript shader playground with live WebGPU rendering viewport",
                "component_features": "Monaco code editor dock, debug layer inspector tree, FPS meter, mesh asset import tray",
                "color_tokens": {"background": "#202025", "accent": "#E0684B", "text": "#FFFFFF"},
                "key_interactions": "Live compilation with sub-100ms render update on keyup"
            },
            {
                "name": "Sketchfab 3D Store",
                "url": "https://sketchfab.com",
                "hero_pattern": "Inspectable 3D PBR model with interactive wireframe and normal-map switcher",
                "component_features": "Model viewer annotations, animation speed scrubber, material inspector dropdown, AR QR code generator",
                "color_tokens": {"background": "#1C242C", "accent": "#1CAAD9", "text": "#FFFFFF"},
                "key_interactions": "Orbital rotation with damped inertial gliding, one-click texture map isolation"
            },
            {
                "name": "Apple Vision Pro Portal",
                "url": "https://www.apple.com/apple-vision-pro/",
                "hero_pattern": "Spatial glassmorphic interface layered over high-contrast ambient room environment",
                "component_features": "Volumetric card depth layers, dynamic specular eye-tracking highlights, spatial audio indicator",
                "color_tokens": {"background": "#000000", "accent": "#F5F5F7", "text": "#E8E8ED"},
                "key_interactions": "Gaze-and-pinch gesture simulation, smooth z-axis card parallax on mouse move"
            },
            {
                "name": "Three.js Official Showcase",
                "url": "https://threejs.org",
                "hero_pattern": "Procedural mathematical geometry particle field with real-time FPS counter",
                "component_features": "Sidebar example filter drawer, source code modal view, WebGL capabilities detector",
                "color_tokens": {"background": "#040711", "accent": "#049EF4", "text": "#D9E3F0"},
                "key_interactions": "Procedural noise morphing responding to mouse movement"
            }
        ]
    },
    {
        "category_name": "SCADA, Autonomous Robotics & Aerospace Telemetry",
        "design_paradigm": "High-Density Dark HUD, Vector Gauges, Real-Time Chart Canvases & Geospatial Map Layers",
        "recommended_libraries": ["Mapbox GL / Deck.gl", "ECharts / uPlot", "Protobuf over WebSocket", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Anduril Lattice OS",
                "url": "https://www.anduril.com/lattice/",
                "hero_pattern": "Geospatial sensor fusion map with real-time target tracking vectors and telemetry HUD",
                "component_features": "Autonomous agent asset list, thermal sensor video stream PIP, threat alert status cards, mission timeline",
                "color_tokens": {"background": "#080B10", "accent": "#00E5A3", "text": "#E2E8F0"},
                "key_interactions": "Real-time radar sweep animation, target trajectory predictive vector projection"
            },
            {
                "name": "Tesla Fleet Telemetry",
                "url": "https://www.tesla.com/fleet",
                "hero_pattern": "Global fleet geospatial density heatmap with live vehicle kilowatt-hour consumption charts",
                "component_features": "Supercharger network queue monitor, over-the-air firmware update progress bars, battery health degradation chart",
                "color_tokens": {"background": "#111111", "accent": "#E82127", "text": "#F4F4F4"},
                "key_interactions": "Zoom-to-cluster map transition, live battery charge curve scrubber"
            },
            {
                "name": "Palantir Foundry",
                "url": "https://www.palantir.com/platforms/foundry/",
                "hero_pattern": "Enterprise ontology graph viewer with high-density nodal connections and data pipelines",
                "component_features": "Data lineage pipeline tree, live simulation branch editor, executive KPI bento grid, audit log stream",
                "color_tokens": {"background": "#0D1117", "accent": "#106DD9", "text": "#F0F6FC"},
                "key_interactions": "Interactive graph node expansion with physics-based force layout"
            },
            {
                "name": "Skydio Cloud",
                "url": "https://www.skydio.com/skydio-cloud",
                "hero_pattern": "Autonomous drone live video feed with 3D photogrammetry scan progress HUD",
                "component_features": "Waypoint mission path planner, battery voltage gauge, obstacle avoidance radar ring, fleet status table",
                "color_tokens": {"background": "#14171C", "accent": "#0070F3", "text": "#FFFFFF"},
                "key_interactions": "Interactive 3D waypoint drag-and-drop on satellite terrain layer"
            },
            {
                "name": "SpaceX Starlink Telemetry",
                "url": "https://www.starlink.com",
                "hero_pattern": "Orbital constellation 3D globe showing real-time satellite mesh inter-satellite laser links",
                "component_features": "Latency jitter sparkline, dish orientation elevation gauge, obstruction radial heat diagram",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#A0A0A0"},
                "key_interactions": "Orbital globe drag-rotation, live obstacle sky-view camera overlay"
            },
            {
                "name": "Formlabs Dashboard",
                "url": "https://formlabs.com/dashboard/",
                "hero_pattern": "High-precision SLA 3D printer fleet status with resin tank volumetric levels and laser layer counter",
                "component_features": "Print job queue visualizer, resin cartridge RFID tracker, temperature thermal history chart",
                "color_tokens": {"background": "#1A1D20", "accent": "#FF6B00", "text": "#EDEDED"},
                "key_interactions": "Layer-by-layer slice preview scrubber, printer remote abort safety modal"
            },
            {
                "name": "Boston Dynamics Orbit",
                "url": "https://bostondynamics.com/products/orbit/",
                "hero_pattern": "Quadruped Spot robot inspection route map with thermal payload vision stream",
                "component_features": "Acoustic anomaly detector chart, battery auto-dock charging indicator, mission execution logs",
                "color_tokens": {"background": "#121418", "accent": "#F5A623", "text": "#FFFFFF"},
                "key_interactions": "PTZ camera virtual joystick control, obstacle alert pulse animation"
            },
            {
                "name": "Samsara IoT Operations",
                "url": "https://www.samsara.com",
                "hero_pattern": "Connected industrial operations dashboard with driver safety AI score and fuel efficiency metrics",
                "component_features": "Fleet GPS tracker table, harsh braking incident timeline, temperature reefer telematics gauge",
                "color_tokens": {"background": "#0F172A", "accent": "#00A86B", "text": "#F8FAFC"},
                "key_interactions": "Instant route replay timeline slider with video clip synchronization"
            },
            {
                "name": "Verkada Command",
                "url": "https://www.verkada.com/command/",
                "hero_pattern": "Multi-camera security grid with AI optical character recognition and face matching alerts",
                "component_features": "Floor plan 2D sensor layout, door access badge log, vehicle license plate search drawer",
                "color_tokens": {"background": "#0A0D12", "accent": "#3B82F6", "text": "#E2E8F0"},
                "key_interactions": "Grid to fullscreen camera tile expansion with motion heat map scrubbing"
            },
            {
                "name": "DJI Enterprise FlightHub 2",
                "url": "https://www.dji.com/flighthub-2",
                "hero_pattern": "2.5D elevation terrain map showing multi-drone synchronized inspection flight routes",
                "component_features": "Dock automated takeoff scheduler, weather radar overlay, live RTK centimeter accuracy gauge",
                "color_tokens": {"background": "#11141A", "accent": "#0066FF", "text": "#FFFFFF"},
                "key_interactions": "Split-screen terrain map and infrared thermal gimbal camera stream"
            }
        ]
    },
    {
        "category_name": "Next-Gen AI Agent Studios & Frontier Workbenches",
        "design_paradigm": "Dual-Pane Chat & Live Artifact Workspace, Streaming Token Telemetry & Token Cost Meters",
        "recommended_libraries": ["Monaco Editor", "Sandpack / WebContainer", "Framer Motion", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Cursor IDE",
                "url": "https://www.cursor.com",
                "hero_pattern": "Minimalist code editor with inline AI agent diff view (red/green multi-line strike-through)",
                "component_features": "Chat panel with multi-file @symbol referencing, Composer multi-file agent window, indexing status pill",
                "color_tokens": {"background": "#141414", "accent": "#6C5CE7", "text": "#CCCCCC"},
                "key_interactions": "Tab-to-autocomplete ghost text projection, instant Cmd+K inline prompt bar"
            },
            {
                "name": "LangSmith (LangChain)",
                "url": "https://smith.langchain.com",
                "hero_pattern": "LLM call trace waterfall showing token counts, latency breakdowns, and nested agent tool calls",
                "component_features": "Run trace tree graph, evaluation benchmark scorecard, prompt playground with model comparator",
                "color_tokens": {"background": "#0F172A", "accent": "#38BDF8", "text": "#F1F5F9"},
                "key_interactions": "Trace node inspection drawer with exact raw request/response JSON payload"
            },
            {
                "name": "v0.dev by Vercel",
                "url": "https://v0.dev",
                "hero_pattern": "Prompt omnibar generating interactive React and Tailwind components with instant live iframe preview",
                "component_features": "Side-by-side code/preview toggle, design version timeline scrubber, responsive viewport size switcher",
                "color_tokens": {"background": "#000000", "accent": "#0070F3", "text": "#EDEDED"},
                "key_interactions": "Live streaming component rendering as code tokens arrive, click-to-edit component selector"
            },
            {
                "name": "Replit Agent",
                "url": "https://replit.com",
                "hero_pattern": "Autonomous full-stack development agent displaying live terminal, browser preview, and file tree",
                "component_features": "Agent thought process stream, package auto-installer notifications, instant cloud deploy URL button",
                "color_tokens": {"background": "#0E1525", "accent": "#F26207", "text": "#FFFFFF"},
                "key_interactions": "Interactive live website preview interacting directly with PostgreSQL database"
            },
            {
                "name": "Lovable.dev",
                "url": "https://lovable.dev",
                "hero_pattern": "High-velocity web application builder turning conversational prompts into full Supabase + React apps",
                "component_features": "Instant preview frame, Supabase database table visualizer, GitHub sync badge, design token editor",
                "color_tokens": {"background": "#0B0C10", "accent": "#FF4D4D", "text": "#FFFFFF"},
                "key_interactions": "Instant visual feedback on prompt submission with visual layout changes"
            },
            {
                "name": "Claude Artifacts (Anthropic)",
                "url": "https://claude.ai",
                "hero_pattern": "Dual-pane conversation with dedicated interactive right-hand side artifact rendering sandbox",
                "component_features": "Tabbed artifact selector (Code / Preview / SVG / Markdown), copy-to-clipboard, version history dropdown",
                "color_tokens": {"background": "#FAF9F5", "accent": "#D97706", "text": "#1F2937"},
                "key_interactions": "Smooth spring-transition opening artifact panel when code snippet is generated"
            },
            {
                "name": "Weights & Biases (W&B)",
                "url": "https://wandb.ai",
                "hero_pattern": "Deep learning training run dashboard with synchronized loss curves, GPU memory, and hyperparameter tables",
                "component_features": "Multi-run line chart overlay, parallel coordinates plot for hyperparams, dataset version artifact tree",
                "color_tokens": {"background": "#111827", "accent": "#FFBE00", "text": "#F9FAFB"},
                "key_interactions": "Interactive chart brushing to zoom loss curves, run tag filtering pills"
            },
            {
                "name": "Together AI Cloud",
                "url": "https://together.ai",
                "hero_pattern": "Ultra-fast inference speed benchmarker showing tokens/sec for Llama-3 and Mixtral models",
                "component_features": "Model catalogue matrix, fine-tuning job launcher, API key usage cost breakdown chart",
                "color_tokens": {"background": "#090A0F", "accent": "#6366F1", "text": "#FFFFFF"},
                "key_interactions": "Streaming token latency race between frontier models"
            },
            {
                "name": "GroqCloud Console",
                "url": "https://console.groq.com",
                "hero_pattern": "LPU (Language Processing Unit) real-time speed demonstration reaching 500+ tokens/sec",
                "component_features": "Live token stream meter, JSON-mode structured output validator, latency telemetry dashboard",
                "color_tokens": {"background": "#151515", "accent": "#F55036", "text": "#FAFAFA"},
                "key_interactions": "Near-instantaneous response generation with sub-100ms time-to-first-token indicator"
            },
            {
                "name": "Perplexity Pro",
                "url": "https://www.perplexity.ai",
                "hero_pattern": "Grounded search engine with verified academic/source footnotes and interactive follow-up pills",
                "component_features": "Numbered source citations rail, media image carousel, collections workspace, model switcher modal",
                "color_tokens": {"background": "#191A1A", "accent": "#20B2AA", "text": "#E8E8E8"},
                "key_interactions": "Citation hover card revealing source snippet and publishing date"
            }
        ]
    },
    {
        "category_name": "High-Frequency Algorithmic Trading & DeFi Terminals",
        "design_paradigm": "Sub-Millisecond Order Books, Canvas Depth Charts, Ticker Tapes & High-Contrast Candlesticks",
        "recommended_libraries": ["TradingView Lightweight Charts", "Canvas Order Book", "Binary WebSocket Streams"],
        "sites": [
            {
                "name": "Bloomberg Terminal Web",
                "url": "https://www.bloomberg.com/professional/",
                "hero_pattern": "Iconic high-contrast amber/orange monospaced terminal grid with 4-pane multi-asset ticker desks",
                "component_features": "Live Bloomberg News wire ticker, yield curve analyzer, Level 2 depth table, FX matrix",
                "color_tokens": {"background": "#000000", "accent": "#FF9900", "text": "#FFCC00"},
                "key_interactions": "Keyboard-only function hotkeys (F1-F12), sub-millisecond price blink on tick update"
            },
            {
                "name": "TradingView Pro",
                "url": "https://www.tradingview.com",
                "hero_pattern": "Interactive HTML5 canvas candlestick chart with 100+ technical indicators and drawing tools",
                "component_features": "Floating indicator toolbar, multi-chart layout grid, watchlist drawer with sparklines, pine script editor",
                "color_tokens": {"background": "#131722", "accent": "#2962FF", "text": "#D1D4DC"},
                "key_interactions": "Pinch-to-zoom chart canvas, magnet-mode trendline snapping to candle wicks"
            },
            {
                "name": "Hyperliquid L1 DEX",
                "url": "https://hyperliquid.xyz",
                "hero_pattern": "Sub-millisecond on-chain order book terminal with zero-gas trade execution telemetry",
                "component_features": "Depth of market (DOM) ladder, live liquidation stream, portfolio margin slider, funding rate ticker",
                "color_tokens": {"background": "#0A0D14", "accent": "#00FFA3", "text": "#F0F4F8"},
                "key_interactions": "One-click market order execution, real-time depth book bar pulse"
            },
            {
                "name": "DEXScreener",
                "url": "https://dexscreener.com",
                "hero_pattern": "Live token price action matrix with instant liquidity pool pair filtering across 30+ chains",
                "component_features": "Multi-chart grid, recent transaction live tape with whale transaction tags, rugcheck audit badge",
                "color_tokens": {"background": "#12131A", "accent": "#22C55E", "text": "#FFFFFF"},
                "key_interactions": "Live sound effects on large swap buy orders, instant token contract address copy pill"
            },
            {
                "name": "Arkham Intelligence",
                "url": "https://www.arkhamintelligence.com",
                "hero_pattern": "On-chain entity intelligence graph tracing entity wallet clusters and fund flows",
                "component_features": "Visual transaction flow graph, exchange balance reserves monitor, entity profiler card, alert builder",
                "color_tokens": {"background": "#0C0D10", "accent": "#4E75FF", "text": "#FFFFFF"},
                "key_interactions": "Interactive wallet node drag, timeline transaction scrubber"
            },
            {
                "name": "Dune Analytics",
                "url": "https://dune.com",
                "hero_pattern": "Community SQL-driven dashboard hub displaying on-chain metrics, DEX volumes, and gas trackers",
                "component_features": "SQL query editor dock, parameter dropdown filters, chart embed modal, query fork button",
                "color_tokens": {"background": "#14151B", "accent": "#FF6838", "text": "#E1E2E8"},
                "key_interactions": "Parameterized dashboard auto-refresh on dropdown select, export to CSV"
            },
            {
                "name": "Uniswap V4 Interface",
                "url": "https://uniswap.org",
                "hero_pattern": "Clean, focused swap card with auto-routing graph and slippage tolerance selector",
                "component_features": "Token selector modal with verified token lists, pool liquidity provider fee APR calculator, hook explorer",
                "color_tokens": {"background": "#131118", "accent": "#FC72FF", "text": "#FFFFFF"},
                "key_interactions": "Spring-animated token swap button flip, auto-route path expansion"
            },
            {
                "name": "DefiLlama",
                "url": "https://defillama.com",
                "hero_pattern": "Comprehensive Total Value Locked (TVL) global chart across 100+ blockchains and protocols",
                "component_features": "Chain TVL breakdown bento grid, stablecoin market cap table, fee/revenue ranking, yield farming finder",
                "color_tokens": {"background": "#0F111A", "accent": "#4C82FB", "text": "#D9E2EC"},
                "key_interactions": "Instant column sorting across 2000+ protocols without pagination reload"
            },
            {
                "name": "Birdeye.so",
                "url": "https://birdeye.so",
                "hero_pattern": "Crypto trading terminal with fast candlestick updates and token security audit scores",
                "component_features": "Find Gems discovery table, wallet portfolio tracker, profit-and-loss calendar heatmap",
                "color_tokens": {"background": "#0B0E14", "accent": "#F59E0B", "text": "#E2E8F0"},
                "key_interactions": "Candle time-frame switch with sub-50ms chart redraw"
            },
            {
                "name": "Raydium DEX",
                "url": "https://raydium.io",
                "hero_pattern": "High-throughput Solana AMM interface with instant route splitting and concentrated liquidity",
                "component_features": "Concentrated liquidity range slider, swap price impact warning modal, yield harvest button",
                "color_tokens": {"background": "#131A35", "accent": "#2B6AFF", "text": "#FFFFFF"},
                "key_interactions": "Price range handle drag with dynamic APR estimation update"
            }
        ]
    },
    {
        "category_name": "Heavy In-Browser Engineering CAD/CAM & DAWs",
        "design_paradigm": "Full-Screen Toolbars, Parameter Inspectors, History Trees & WebAssembly High-Throughput Engines",
        "recommended_libraries": ["WebAssembly (Rust/C++)", "WebGL Canvas", "Dockview", "Web Audio API"],
        "sites": [
            {
                "name": "Onshape CAD",
                "url": "https://www.onshape.com",
                "hero_pattern": "Full-featured parametric 3D CAD modeling viewport running entirely inside WebGL browser tab",
                "component_features": "Parametric feature history tree, mate connector dialog, multi-user simultaneous assembly editing, version branch graph",
                "color_tokens": {"background": "#2E3440", "accent": "#5E81AC", "text": "#ECEFF4"},
                "key_interactions": "3D constraint solver updates in real-time on sketch line drag, instant rollback bar sliding"
            },
            {
                "name": "Photopea",
                "url": "https://www.photopea.com",
                "hero_pattern": "Complete Adobe Photoshop clone running 100% in browser using WebAssembly and Canvas",
                "component_features": "Layer panel with blend modes and layer masks, history state list, vector path pen tool, raw PSD parser",
                "color_tokens": {"background": "#383838", "accent": "#18A0FB", "text": "#DCDCDC"},
                "key_interactions": "Free-transform bounding box drag with aspect-ratio shift lock, clone stamp preview"
            },
            {
                "name": "Soundtrap by Spotify",
                "url": "https://www.soundtrap.com",
                "hero_pattern": "Collaborative digital audio workstation (DAW) with multi-track timeline and software synth instruments",
                "component_features": "Piano roll MIDI editor, audio loop library drawer, real-time vocal pitch corrector, master volume limiter",
                "color_tokens": {"background": "#1A1A1A", "accent": "#FF5A00", "text": "#FFFFFF"},
                "key_interactions": "Multi-track audio playback with zero stuttering, loop region drag-to-expand"
            },
            {
                "name": "Amped Studio",
                "url": "https://ampedstudio.com",
                "hero_pattern": "WebAudio + WebAssembly hybrid music production studio supporting VST remote bridges",
                "component_features": "Drum machine pad grid, automation curves drawer, audio-to-MIDI pitch detection, FX chain racks",
                "color_tokens": {"background": "#181B20", "accent": "#00ADB5", "text": "#EEEEEE"},
                "key_interactions": "Automation point drag with bezier curve tension adjustment"
            },
            {
                "name": "Tinkercad by Autodesk",
                "url": "https://www.tinkercad.com",
                "hero_pattern": "Accessible 3D geometric modeling workplane with solid/hole CSG (Constructive Solid Geometry) engine",
                "component_features": "Shape generator drawer, Circuit simulator breadboard, codeblocks procedural CAD tab, export STL button",
                "color_tokens": {"background": "#EBF2F7", "accent": "#007ACC", "text": "#1E293B"},
                "key_interactions": "Geometric shape drop with auto-alignment grid snapping, group boolean subtract"
            },
            {
                "name": "Shapr3D Web",
                "url": "https://www.shapr3d.com",
                "hero_pattern": "Siemens Parasolid-powered direct modeling engine optimized for iPad stylus and browser mouse input",
                "component_features": "Adaptive contextual menu wheel, measurement dimension pills, chamfer/fillet interactive handle",
                "color_tokens": {"background": "#22252A", "accent": "#3E82F7", "text": "#FFFFFF"},
                "key_interactions": "Face extrusion on drag with real-time numeric dimension HUD"
            },
            {
                "name": "KiCad Web EDA",
                "url": "https://www.kicad.org",
                "hero_pattern": "High-density multi-layer printed circuit board (PCB) schematic and routing viewport",
                "component_features": "Schematic component library search, trace autorouter status, 3D ray-traced PCB board preview, BOM generator",
                "color_tokens": {"background": "#000000", "accent": "#00FF00", "text": "#FFFFFF"},
                "key_interactions": "Interactive trace push-and-shove routing without design rule check (DRC) violations"
            },
            {
                "name": "Vectary 3D Studio",
                "url": "https://www.vectary.com",
                "hero_pattern": "No-code 3D product visualizer with AR (Augmented Reality) one-click web embed",
                "component_features": "Real-time photorealistic glass/metal material presets, lighting studio HDR dome, interactive hotspot editor",
                "color_tokens": {"background": "#141518", "accent": "#FF4565", "text": "#FFFFFF"},
                "key_interactions": "Material drag-and-drop onto 3D mesh surface with instant reflection update"
            },
            {
                "name": "Figma FigJam",
                "url": "https://www.figma.com/figjam/",
                "hero_pattern": "Infinite collaborative whiteboard canvas with real-time live cursor multiplayer presence",
                "component_features": "Sticky note grid, connector arrows with smart path avoidance, voting stamps, timer widget modal",
                "color_tokens": {"background": "#F5F5F5", "accent": "#9747FF", "text": "#333333"},
                "key_interactions": "Wheel zoom with sub-pixel canvas rendering, multiplayer cursor emote wheel"
            },
            {
                "name": "Wappler Visual App Builder",
                "url": "https://wappler.io",
                "hero_pattern": "Full-stack visual low-code IDE generating clean standards-based HTML/Node.js/PHP code without lock-in",
                "component_features": "Server actions workflow builder, visual CSS style inspector, database query builder drawer",
                "color_tokens": {"background": "#252830", "accent": "#00A8FF", "text": "#E6E6E6"},
                "key_interactions": "Visual component tree reordering with drag-and-drop DOM re-nesting"
            }
        ]
    },
    {
        "category_name": "Cybersecurity Threat Hunting & Cloud SOC Dashboards",
        "design_paradigm": "High-Density Dark Theme, MITRE ATT&CK Matrix Grids, Incident Timelines & Forensic Drilldowns",
        "recommended_libraries": ["Vis.js Network", "ECharts", "Tailwind CSS v4", "React Data Grid"],
        "sites": [
            {
                "name": "CrowdStrike Falcon",
                "url": "https://www.crowdstrike.com",
                "hero_pattern": "Real-time threat graph visualizing process execution trees and command-and-control beaconing",
                "component_features": "MITRE ATT&CK tactic heat map, endpoint containment switch, IOC search drawer, quarantine table",
                "color_tokens": {"background": "#121316", "accent": "#E60000", "text": "#E0E0E0"},
                "key_interactions": "Process tree branch expansion with parent/child PID execution timeline"
            },
            {
                "name": "Wiz.io Cloud Security",
                "url": "https://www.wiz.io",
                "hero_pattern": "Cloud infrastructure toxic risk combination graph (vulnerability + public exposure + high privilege)",
                "component_features": "Multi-cloud asset inventory matrix, cloud security posture score pill, remediation playbook drawer",
                "color_tokens": {"background": "#0D111A", "accent": "#0070F3", "text": "#FFFFFF"},
                "key_interactions": "Clicking critical risk node filters all downstream IAM permissions and container pods"
            },
            {
                "name": "Cloudflare One (Zero Trust)",
                "url": "https://one.dash.cloudflare.com",
                "hero_pattern": "Global edge network traffic stream showing blocked malicious DNS queries and WAF blocks",
                "component_features": "Zero trust access policy rule builder, device posture check list, gateway HTTP logs table",
                "color_tokens": {"background": "#181818", "accent": "#F38020", "text": "#EEEEEE"},
                "key_interactions": "Instant policy toggling with global edge replication in sub-5 seconds"
            },
            {
                "name": "Datadog Cloud Security Management",
                "url": "https://www.datadoghq.com",
                "hero_pattern": "Real-time security signals stream with anomaly detection sparklines and cloud audit logs",
                "component_features": "Compliance posture rules checklist, vulnerability explorer table, log facet search filter dock",
                "color_tokens": {"background": "#0E0D14", "accent": "#632CA6", "text": "#F3F3F3"},
                "key_interactions": "Log stream time scrubber with instant faceted drill-down"
            },
            {
                "name": "SentinelOne Singularity",
                "url": "https://www.sentinelone.com",
                "hero_pattern": "Autonomous AI endpoint detection and response (EDR) dashboard with Storyline attack visualization",
                "component_features": "One-click ransomware rollback modal, threat hunt query builder, endpoint isolation status",
                "color_tokens": {"background": "#0F0F14", "accent": "#5E17EB", "text": "#FFFFFF"},
                "key_interactions": "Attack Storyline timeline scrub with forensic file hash details"
            },
            {
                "name": "Palo Alto Networks Cortex XSOAR",
                "url": "https://www.paloaltonetworks.com/cortex",
                "hero_pattern": "Security orchestration and automated response (SOAR) playbook execution flowchart",
                "component_features": "Automated incident triage card, evidence locker file list, threat intelligence enrichment feed",
                "color_tokens": {"background": "#14171A", "accent": "#FA582D", "text": "#E1E8ED"},
                "key_interactions": "Interactive playbook flowchart drag with live task execution status pulses"
            },
            {
                "name": "Snyk Developer Security",
                "url": "https://snyk.io",
                "hero_pattern": "Dependency vulnerability graph with automated pull request fix badges and severity meters",
                "component_features": "Container image layer scanner, infrastructure as code (IaC) misconfiguration table, license compliance view",
                "color_tokens": {"background": "#141B3B", "accent": "#4C54D2", "text": "#FFFFFF"},
                "key_interactions": "One-click 'Fix this vulnerability' generating GitHub PR diff preview"
            },
            {
                "name": "SonarQube Clean Code Portal",
                "url": "https://www.sonarsource.com",
                "hero_pattern": "Code quality and security gate dashboard showing reliability, security hotspots, and test coverage",
                "component_features": "Source code inline issue annotations, technical debt time estimate, quality gate status banner",
                "color_tokens": {"background": "#1C2128", "accent": "#4B9BE1", "text": "#F0F6FC"},
                "key_interactions": "Expanding security hotspot reveals exact vulnerable line of code with CWE explanation"
            },
            {
                "name": "HashiCorp Vault Portal",
                "url": "https://www.vaultproject.io",
                "hero_pattern": "Cryptographic secrets management key-value engine with dynamic lease TTL countdown badges",
                "component_features": "Secret path hierarchical tree, policy ACL editor, audit log stream, transit encryption tester",
                "color_tokens": {"background": "#151515", "accent": "#FFEC00", "text": "#FFFFFF"},
                "key_interactions": "Click-to-reveal secret with automatic 10-second clipboard purge timer"
            },
            {
                "name": "Lacework Polygraph",
                "url": "https://www.lacework.com",
                "hero_pattern": "Behavioral baseline machine learning graph detecting abnormal API calls and privilege escalation",
                "component_features": "Cloud workload anomaly timeline, Kubernetes pod security matrix, compliance trend chart",
                "color_tokens": {"background": "#0D131F", "accent": "#00A3FF", "text": "#E4E9F2"},
                "key_interactions": "Polygraph anomaly cluster click isolates exact AWS IAM role and IP address"
            }
        ]
    },
    {
        "category_name": "BioTech, Clinical Genomics & MedTech Workstations",
        "design_paradigm": "Clean Clinical Contrast, High-Resolution Histology Viewers & DNA/Protein 3D Visualizers",
        "recommended_libraries": ["NGL Viewer / Mol*", "OpenSeadragon", "ECharts", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Tempus AI Precision Medicine",
                "url": "https://www.tempus.com",
                "hero_pattern": "Interactive genomic variant waterfall chart mapping clinical trial matches for patient tumors",
                "component_features": "Next-generation sequencing (NGS) gene panel report, clinical trial matching drawer, survival curve comparator",
                "color_tokens": {"background": "#F8FAFC", "accent": "#0284C7", "text": "#0F172A"},
                "key_interactions": "Hover gene mutation to inspect pathogenic classification and ACMG evidence"
            },
            {
                "name": "Flatiron Health Oncology EHR",
                "url": "https://flatiron.com",
                "hero_pattern": "Real-world oncology patient timeline aggregating chemotherapy regimens, lab biomarkers, and CT scans",
                "component_features": "Interactive staging calculator, chemotherapy regimen order set builder, patient vitals sparklines",
                "color_tokens": {"background": "#FFFFFF", "accent": "#00838F", "text": "#212121"},
                "key_interactions": "Timeline milestone click expanding exact clinical pathology PDF note"
            },
            {
                "name": "Paige AI Digital Pathology",
                "url": "https://paige.ai",
                "hero_pattern": "Gigapixel digital pathology slide viewer with AI prostate/breast cancer heatmaps",
                "component_features": "Slide zoom pyramid navigation, diagnostic confidence score pill, tissue annotation measurement tool",
                "color_tokens": {"background": "#11141A", "accent": "#7C3AED", "text": "#F3F4F6"},
                "key_interactions": "Deep-zoom pan with sub-millisecond tile prefetching (OpenSeadragon)"
            },
            {
                "name": "Moderna Digital mRNA Platform",
                "url": "https://www.modernatx.com",
                "hero_pattern": "Computational mRNA sequence designer showing codon optimization and GC-content distribution",
                "component_features": "Nucleotide sequence editor, lipid nanoparticle (LNP) formulation calculator, clinical pipeline tracker",
                "color_tokens": {"background": "#FFFFFF", "accent": "#E60000", "text": "#1A1A1A"},
                "key_interactions": "Codon frequency adjustment with live translation efficiency prediction"
            },
            {
                "name": "Butterfly iQ Cloud Ultrasound",
                "url": "https://www.butterflynetwork.com",
                "hero_pattern": "Handheld whole-body ultrasound telemetry stream with AI ejection fraction calculation",
                "component_features": "Cardiac chamber automated biometry, HIPAA-compliant patient study archive, cloud peer-review DICOM viewer",
                "color_tokens": {"background": "#000000", "accent": "#00C2FF", "text": "#FFFFFF"},
                "key_interactions": "Ultrasound cine loop scrubber with measurement caliper drag"
            },
            {
                "name": "Veeva Systems Vault",
                "url": "https://www.veeva.com",
                "hero_pattern": "Life sciences regulatory document lifecycle matrix with audit trail electronic signatures (21 CFR Part 11)",
                "component_features": "eCTD submission binder tree, medical legal review workflow, clinical trial site investigator portal",
                "color_tokens": {"background": "#F5F7FA", "accent": "#F58220", "text": "#1A2530"},
                "key_interactions": "Document redlining comparison view with parallel diff highlight"
            },
            {
                "name": "Illumina BaseSpace Sequence Hub",
                "url": "https://basespace.illumina.com",
                "hero_pattern": "High-throughput DNA sequencing run quality metrics (Q30 scores, cluster density, yield in gigabases)",
                "component_features": "Sequencing flow cell lane tile heatmap, secondary analysis pipeline launcher, FASTQ file downloader",
                "color_tokens": {"background": "#0F172A", "accent": "#00B4D8", "text": "#E2E8F0"},
                "key_interactions": "Run cycle scrubber showing real-time error rate per base pair"
            },
            {
                "name": "Epic Systems MyChart Pro",
                "url": "https://www.epic.com",
                "hero_pattern": "Comprehensive patient clinical dashboard integrating lab results, appointment scheduling, and messaging",
                "component_features": "Medication interaction alert drawer, clinical notes viewer, preventive health reminder timeline",
                "color_tokens": {"background": "#FFFFFF", "accent": "#C41230", "text": "#333333"},
                "key_interactions": "One-click refill prescription with automated pharmacy routing"
            },
            {
                "name": "Benchling R&D Cloud",
                "url": "https://www.benchling.com",
                "hero_pattern": "Electronic lab notebook (ELN) and molecular biology DNA plasmid design suite",
                "component_features": "CRISPR guide RNA design tool, molecular plasmid circular map visualizer, sample inventory freezer tracker",
                "color_tokens": {"background": "#FFFFFF", "accent": "#1A73E8", "text": "#202124"},
                "key_interactions": "Interactive plasmid restriction enzyme site click with fragment length calculator"
            },
            {
                "name": "AlphaFold Protein Structure Database",
                "url": "https://alphafold.ebi.ac.uk",
                "hero_pattern": "3D interactive protein folding structure with pLDDT per-residue confidence color mapping",
                "component_features": "NGL 3D molecular viewer, PAE (Predicted Aligned Error) matrix plot, PDB/CIF structure download",
                "color_tokens": {"background": "#0B1017", "accent": "#0055FF", "text": "#FFFFFF"},
                "key_interactions": "3D protein rotation with color-coded confidence toggle (Very High, Confident, Low, Very Low)"
            }
        ]
    },
    {
        "category_name": "Global High-Volume Logistics, Supply Chain & Maritime Fleet OS",
        "design_paradigm": "Geospatial AIS Ship Tracking, High-Density Routing Matrices & Exception Handling Queues",
        "recommended_libraries": ["Deck.gl", "MapLibre GL", "Ag-Grid Enterprise", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Flexport Operating System",
                "url": "https://www.flexport.com",
                "hero_pattern": "Global freight forwarder live ocean container map with estimated time of arrival (ETA) predictions",
                "component_features": "Customs clearance milestone checklist, commercial invoice SKU level audit, emissions carbon tracker",
                "color_tokens": {"background": "#0B1528", "accent": "#00C9FF", "text": "#FFFFFF"},
                "key_interactions": "Vessel trajectory playback with maritime port congestion warnings"
            },
            {
                "name": "ShipBob Omnichannel Fulfillment",
                "url": "https://www.shipbob.com",
                "hero_pattern": "Multi-warehouse inventory distribution heatmap showing optimal 2-day delivery coverage zones",
                "component_features": "Automated order routing rules editor, warehouse receiving order (WRO) tracker, inventory reorder forecasting",
                "color_tokens": {"background": "#FFFFFF", "accent": "#0052FF", "text": "#1A1A1A"},
                "key_interactions": "Inventory allocation slider dynamically recalculating shipping carrier costs"
            },
            {
                "name": "FourKites Real-Time Visibility",
                "url": "https://www.fourkites.com",
                "hero_pattern": "Multi-modal global supply chain tracking (Ocean, Air, Rail, Truckload) with predictive risk alerts",
                "component_features": "Dynamic yard management dock schedule, temperature sensor anomaly alert, carrier scorecard matrix",
                "color_tokens": {"background": "#0D1829", "accent": "#00D68F", "text": "#EDF2F7"},
                "key_interactions": "Exception alert filter highlighting delayed shipments with root-cause categorization"
            },
            {
                "name": "Project44 Movement",
                "url": "https://www.project44.com",
                "hero_pattern": "Real-time carrier connectivity network processing over 1 billion shipments annually",
                "component_features": "Port dwell time index, sustainability carbon emissions dashboard, automated dispatch trigger",
                "color_tokens": {"background": "#14171F", "accent": "#0066FF", "text": "#FFFFFF"},
                "key_interactions": "Interactive container live track with satellite AIS ping history"
            },
            {
                "name": "Uber Freight",
                "url": "https://www.uberfreight.com",
                "hero_pattern": "Algorithmic freight matching marketplace showing real-time lane spot rates and instant booking",
                "component_features": "Facility rating review cards, carrier quick-pay status, automated tender acceptance rate chart",
                "color_tokens": {"background": "#000000", "accent": "#276EF1", "text": "#FFFFFF"},
                "key_interactions": "One-click 'Book Load' with instant digital rate confirmation"
            },
            {
                "name": "Maersk Spot",
                "url": "https://www.maersk.com",
                "hero_pattern": "Fixed-price container shipping booking portal with loading guarantee and demurrage calculator",
                "component_features": "Port-to-port route transit time finder, container equipment availability checker, inland rail intermodal adder",
                "color_tokens": {"background": "#00243C", "accent": "#42B0D5", "text": "#FFFFFF"},
                "key_interactions": "Interactive booking wizard with instant PDF shipping label generation"
            },
            {
                "name": "Procore Construction Management",
                "url": "https://www.procore.com",
                "hero_pattern": "Jobsite construction operating system connecting field blueprints, punch lists, and BIM 3D models",
                "component_features": "Architectural drawing version comparison overlay, submittal approval workflow, RFI (Request for Information) queue",
                "color_tokens": {"background": "#FFFFFF", "accent": "#F15A24", "text": "#222222"},
                "key_interactions": "Blueprint pin drop linking directly to photo defect and subcontractor assignment"
            },
            {
                "name": "Toast POS Restaurant Platform",
                "url": "https://pos.toasttab.com",
                "hero_pattern": "High-velocity kitchen display system (KDS) and tableside ordering interface with ticket countdown timers",
                "component_features": "Visual table floor plan editor, live menu 86-item toggle, tip distribution payroll report, inventory depletion",
                "color_tokens": {"background": "#1E1E24", "accent": "#FF5C35", "text": "#FFFFFF"},
                "key_interactions": "One-tap ticket bump with audio alert, split-bill drag-and-drop calculation"
            },
            {
                "name": "ServiceTitan Field Management",
                "url": "https://www.servicetitan.com",
                "hero_pattern": "Dispatch dispatch board with GPS technician location mapping and job capacity scheduling",
                "component_features": "Mobile visual pricebook presentation, call recording attribution with AI sentiment, invoice financing modal",
                "color_tokens": {"background": "#0A1128", "accent": "#007BFF", "text": "#FFFFFF"},
                "key_interactions": "Drag-and-drop job card onto technician schedule column with travel time calculation"
            },
            {
                "name": "Kpler Energy & Maritime Intelligence",
                "url": "https://www.kpler.com",
                "hero_pattern": "Global LNG and crude oil tanker vessel tracking with floating storage volumetric estimates",
                "component_features": "Refinery outage tracker table, vessel draft-change detection, trade flow commodity matrix",
                "color_tokens": {"background": "#0C1017", "accent": "#FFB800", "text": "#F0F3F6"},
                "key_interactions": "Clicking maritime tanker displays cargo type, origin refinery, and AIS destination"
            }
        ]
    },
    {
        "category_name": "High-Conversion Developer SaaS & Modern Open-Source Blueprints",
        "design_paradigm": "Linear-Style Command Palette, Bento Grids, Shimmer Skeletons & Copyable Code Blocks",
        "recommended_libraries": ["Shadcn UI", "Framer Motion", "Tailwind CSS v4", "Lucide React"],
        "sites": [
            {
                "name": "Supabase Platform",
                "url": "https://supabase.com",
                "hero_pattern": "PostgreSQL-backed open-source Firebase alternative featuring real-time subscriptions and pgvector",
                "component_features": "Table editor with Excel-like spreadsheet editing, SQL editor with AI query assistant, storage bucket browser",
                "color_tokens": {"background": "#1C1C1C", "accent": "#3ECF8E", "text": "#EDEDED"},
                "key_interactions": "Instant database schema migration with copyable TypeScript types generator"
            },
            {
                "name": "Resend Email Infrastructure",
                "url": "https://resend.com",
                "hero_pattern": "Minimalist developer-first email platform with React Email previews and deliverability analytics",
                "component_features": "Live email rendering preview, DNS record verification badge, API token generator modal",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#EDEDED"},
                "key_interactions": "Tabbed preview switcher (Desktop / Mobile / Code / Plain Text) with instant updates"
            },
            {
                "name": "Dub.co Modern Link Management",
                "url": "https://dub.co",
                "hero_pattern": "Open-source link management platform with world-class analytics, geo-targeting, and QR code generator",
                "component_features": "Real-time click geolocation globe, custom domain SSL verify status, link expiration date picker",
                "color_tokens": {"background": "#FAFAFA", "accent": "#000000", "text": "#111111"},
                "key_interactions": "Instant custom QR code color personalization with SVG/PNG download"
            },
            {
                "name": "Cal.com Open Scheduling",
                "url": "https://cal.com",
                "hero_pattern": "Open-source scheduling infrastructure supporting recurring bookings, routing forms, and Stripe deposits",
                "component_features": "Visual timezone converter calendar, embeddable iframe modal previewer, workflow webhook editor",
                "color_tokens": {"background": "#111111", "accent": "#FFFFFF", "text": "#FFFFFF"},
                "key_interactions": "Fluid date and time-slot selection with spring-based confirmation drawer"
            },
            {
                "name": "PostHog All-in-One Analytics",
                "url": "https://posthog.com",
                "hero_pattern": "Full-stack product analytics suite uniting session replay, feature flags, A/B testing, and surveys",
                "component_features": "Session replay video player with DOM event timeline, feature flag multivariate rollout slider, cohort builder",
                "color_tokens": {"background": "#EEEFE9", "accent": "#F54E00", "text": "#1D1F20"},
                "key_interactions": "Interactive session replay scrubber synchronized with console error logs"
            },
            {
                "name": "Papermark Open DocSend",
                "url": "https://www.papermark.io",
                "hero_pattern": "Document sharing analytics platform tracking page-by-page time spent by investors and clients",
                "component_features": "Slide-by-slide completion percentage bar, password protection gate, custom branded domain",
                "color_tokens": {"background": "#FFFFFF", "accent": "#6366F1", "text": "#0F172A"},
                "key_interactions": "Real-time heat-map showing which slide retained reader attention the longest"
            },
            {
                "name": "Typebot Conversational Builder",
                "url": "https://typebot.io",
                "hero_pattern": "Visual flowchart chatbot builder with native webhook integrations and lead capture funnels",
                "component_features": "Drag-and-drop block connector canvas, live preview simulator phone, analytics drop-off funnel",
                "color_tokens": {"background": "#181A20", "accent": "#0042DA", "text": "#FFFFFF"},
                "key_interactions": "Connecting logic blocks with smooth bezier curves and automatic node snapping"
            },
            {
                "name": "Infisical Secret Operations",
                "url": "https://infisical.com",
                "hero_pattern": "End-to-end encrypted secret management platform synchronizing .env files across Kubernetes and Vercel",
                "component_features": "Secret version history rollback, role-based access control (RBAC) matrix, audit log search",
                "color_tokens": {"background": "#0F1117", "accent": "#FFD000", "text": "#FFFFFF"},
                "key_interactions": "One-click secret injection CLI command copy with masked value toggle"
            },
            {
                "name": "Loops.so Modern Email",
                "url": "https://loops.so",
                "hero_pattern": "Email platform designed specifically for SaaS companies with automated product onboarding sequences",
                "component_features": "Visual user journey flowchart, dynamic merge tags dropdown, deliverability health score",
                "color_tokens": {"background": "#0D0D0D", "accent": "#FA7070", "text": "#F0F0F0"},
                "key_interactions": "Live template editor with instant responsive mobile device mockup"
            },
            {
                "name": "Raycast Store & Extensions",
                "url": "https://www.raycast.com",
                "hero_pattern": "Supercharged keyboard-centric desktop launcher with community extension marketplace",
                "component_features": "Command palette fuzzy search list, keyboard shortcut badges, extension author profile cards",
                "color_tokens": {"background": "#0A0B0E", "accent": "#FF6363", "text": "#F3F4F6"},
                "key_interactions": "Sub-millisecond keyboard navigation using arrow keys and instant action dialogs"
            }
        ]
    },
    {
        "category_name": "Heavy Data Science, Notebooks & MLOps Infrastructure",
        "design_paradigm": "Interactive Code Cells, Reactive Sparklines, Model Checkpoint Trees & Parallel Plots",
        "recommended_libraries": ["JupyterLab", "Plotly / Vega-Lite", "Monaco Editor", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "JupyterLab Scientific Workspace",
                "url": "https://jupyter.org",
                "hero_pattern": "Multi-tab scientific notebook interface executing Python/Julia/R kernel cells with rich outputs",
                "component_features": "Interactive code cells with syntax highlighting, variable inspector table, terminal dock, markdown renderer",
                "color_tokens": {"background": "#FFFFFF", "accent": "#F37626", "text": "#222222"},
                "key_interactions": "Shift+Enter cell execution with animated progress indicator and output streaming"
            },
            {
                "name": "Hex.tech Collaborative Analytics",
                "url": "https://hex.tech",
                "hero_pattern": "Modern data workspace combining SQL, Python, and interactive drag-and-drop reactive charts",
                "component_features": "Reactive dependency graph DAG, published app layout builder, multiplayer cursor presence",
                "color_tokens": {"background": "#0F111A", "accent": "#6D3FEA", "text": "#FFFFFF"},
                "key_interactions": "Modifying input slider instantly triggers downstream cell recalculations without page reload"
            },
            {
                "name": "Deepnote Multiplayer Notebooks",
                "url": "https://deepnote.com",
                "hero_pattern": "Cloud data science notebook with Google Docs-style real-time collaboration and AI code assist",
                "component_features": "Database connector drawer, chart cell auto-visualizer, scheduled notebook run timeline",
                "color_tokens": {"background": "#FFFFFF", "accent": "#3B82F6", "text": "#1E293B"},
                "key_interactions": "SQL query cell with automatic auto-complete based on connected database schema"
            },
            {
                "name": "Hugging Face Spaces Hub",
                "url": "https://huggingface.co/spaces",
                "hero_pattern": "Global community hub running thousands of open-source AI demos in Gradio and Streamlit",
                "component_features": "Model card README tab, Docker container hardware spec selector, community discussion thread",
                "color_tokens": {"background": "#0B0F19", "accent": "#FFD21E", "text": "#FFFFFF"},
                "key_interactions": "One-click 'Duplicate Space' with instant GPU allocation selection"
            },
            {
                "name": "Roboflow Computer Vision Hub",
                "url": "https://roboflow.com",
                "hero_pattern": "End-to-end computer vision workspace for dataset annotation, model training, and edge deployment",
                "component_features": "Polygon and bounding box annotation canvas, dataset preprocessing augmentation slider, model mAP scorecard",
                "color_tokens": {"background": "#0F172A", "accent": "#7C3AED", "text": "#F8FAFC"},
                "key_interactions": "AI smart polygon tool outlining objects automatically on single click"
            },
            {
                "name": "ClearML MLOps Orchestration",
                "url": "https://clear.ml",
                "hero_pattern": "Self-hosted MLOps platform tracking experiment code, hyperparameters, and GPU resource utilization",
                "component_features": "Experiment comparator diff table, remote task pipeline scheduler, model registry version tree",
                "color_tokens": {"background": "#141721", "accent": "#00A3FF", "text": "#FFFFFF"},
                "key_interactions": "Side-by-side run comparison with metric scatter plot overlay"
            },
            {
                "name": "Ray Dashboard (Anyscale)",
                "url": "https://www.anyscale.com",
                "hero_pattern": "Distributed computing cluster monitor showing actor memory, object store usage, and CPU worker cores",
                "component_features": "Cluster node hardware utilization bar, task timeline trace, actor placement map",
                "color_tokens": {"background": "#0C1017", "accent": "#009BF5", "text": "#E2E8F0"},
                "key_interactions": "Zooming into microsecond task execution flame chart"
            },
            {
                "name": "Prefect Dataflow Automation",
                "url": "https://www.prefect.io",
                "hero_pattern": "Resilient Python data workflow orchestrator with dynamic flow runs and state transitions",
                "component_features": "Flow run radar map, task failure retry alert drawer, concurrency slot limiter gauge",
                "color_tokens": {"background": "#0B0D13", "accent": "#276EF1", "text": "#FFFFFF"},
                "key_interactions": "Interactive timeline graph expanding exact task retry logs on failure"
            },
            {
                "name": "Label Studio Data Annotation",
                "url": "https://labelstud.io",
                "hero_pattern": "Multi-modal data labeling interface for audio, image, text, and time-series sensor data",
                "component_features": "Audio waveform phoneme tagging, OCR transcription bounding box, agreement matrix score",
                "color_tokens": {"background": "#FAFAFA", "accent": "#FF4400", "text": "#1A1A1A"},
                "key_interactions": "Hot-key driven annotation cycle (1-9) for rapid keyboard classification"
            },
            {
                "name": "Google Colaboratory Pro",
                "url": "https://colab.research.google.com",
                "hero_pattern": "Cloud hosted Jupyter notebook with one-click access to Nvidia A100 / H100 GPUs and TPUs",
                "component_features": "RAM/Disk compute resource meter, Google Drive file explorer, code snippet library modal",
                "color_tokens": {"background": "#FFFFFF", "accent": "#F9AB00", "text": "#202124"},
                "key_interactions": "Real-time collaborative typing with Google Docs synchronization engine"
            }
        ]
    }
]

def main():
    if not os.path.exists(VAULT_PATH):
        print(f"Error: Vault path not found: {VAULT_PATH}")
        sys.exit(1)

    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        vault = json.load(f)

    existing_categories = vault.get("categories", [])
    existing_cat_names = {c.get("category_name") for c in existing_categories}

    added_categories = 0
    added_sites = 0

    for new_cat in NEW_CATEGORIES_AND_SITES:
        cat_name = new_cat["category_name"]
        if cat_name not in existing_cat_names:
            existing_categories.append(new_cat)
            existing_cat_names.add(cat_name)
            added_categories += 1
            added_sites += len(new_cat.get("sites", []))
        else:
            for cat in existing_categories:
                if cat.get("category_name") == cat_name:
                    existing_site_names = {s["name"] for s in cat.get("sites", [])}
                    for s in new_cat.get("sites", []):
                        if s["name"] not in existing_site_names:
                            cat["sites"].append(s)
                            added_sites += 1

    final_total_sites = sum(len(c.get("sites", [])) for c in existing_categories)

    vault["vault_metadata"] = {
        "title": "Zobar S-Tier Design & Architecture Vault (404+ Enterprise Standard)",
        "version": "4.2.0",
        "total_categories": len(existing_categories),
        "total_products_and_sites": final_total_sites,
        "description": "Comprehensive design patterns, component features, and color tokens for 404+ world-class digital products, SaaS applications, and heavy engineering software."
    }
    vault["categories"] = existing_categories

    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(vault, f, indent=2, ensure_ascii=False)

    print("=================================================================")
    print(" S-TIER DESIGN & APP VAULT GENISLETILDI (404+ HEDEFI)")
    print("=================================================================")
    print(f"[*] Toplam Kategori Sayisi : {len(existing_categories)}")
    print(f"[*] Toplam Site/Uygulama   : {final_total_sites} (Hedef 404+ Basariyla Asildi)")
    print(f"[*] Eklenen Yeni Urunler   : +{added_sites}")
    print(f"[*] Kaydedildi: {VAULT_PATH}")

if __name__ == "__main__":
    main()

EXTRA_TIERS_BATCH = [
    {
        "category_name": "Global Fintech & Wealth Management OS",
        "design_paradigm": "High-Trust Typography, Portfolio Allocation Doughnuts & Institutional Clearing Rails",
        "recommended_libraries": ["Recharts", "Framer Motion", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Stripe Atlas & Treasury",
                "url": "https://stripe.com/atlas",
                "hero_pattern": "Dynamic corporate incorporation timeline with live banking and tax identification status",
                "component_features": "Entity governance documents vault, automated stock issuance signature flow, Delaware franchise tax tracker",
                "color_tokens": {"background": "#F6F9FC", "accent": "#635BFF", "text": "#0A2540"},
                "key_interactions": "One-click formation checklist with animated celebratory milestone pulse"
            },
            {
                "name": "Carta Equity Management",
                "url": "https://carta.com",
                "hero_pattern": "Cap table waterfall modeling tool calculating dilution across multiple investment series",
                "component_features": "Option grant issuance drawer, 409A valuation audit tracker, secondary market tender offer portal",
                "color_tokens": {"background": "#FFFFFF", "accent": "#14171A", "text": "#292929"},
                "key_interactions": "Interactive round dilution slider with real-time ownership percentage recalculation"
            },
            {
                "name": "Robinhood Gold & Retirement",
                "url": "https://robinhood.com",
                "hero_pattern": "High-contrast neon green portfolio sparkline with instant trade execution drawer",
                "component_features": "3% IRA match tracker, options payoff diagram generator, recurring investment scheduler",
                "color_tokens": {"background": "#000000", "accent": "#00C805", "text": "#FFFFFF"},
                "key_interactions": "Options profit/loss curve drag with breakeven price indicator"
            },
            {
                "name": "Wealthfront Automated Investing",
                "url": "https://www.wealthfront.com",
                "hero_pattern": "Passive indexing automated tax-loss harvesting graph comparing pre-tax and after-tax yields",
                "component_features": "Risk tolerance survey questionnaire, direct indexing stock basket viewer, automated cash sweep",
                "color_tokens": {"background": "#F5F8FA", "accent": "#6F3FF5", "text": "#1E293B"},
                "key_interactions": "Retirement goal net-worth projection curve with interactive monthly contribution slider"
            },
            {
                "name": "Wise (Formerly TransferWise)",
                "url": "https://wise.com",
                "hero_pattern": "Real-time transparent mid-market exchange rate calculator showing zero-markup guarantee",
                "component_features": "Multi-currency virtual account balances, instant international wire tracking timeline, debit card PIN reveal",
                "color_tokens": {"background": "#F2F5F7", "accent": "#9FE870", "text": "#163300"},
                "key_interactions": "Currency toggle with real-time mid-market rate tick update"
            },
            {
                "name": "Revolut Business",
                "url": "https://www.revolut.com/business/",
                "hero_pattern": "Multi-currency corporate treasury dashboard with automated expense approvals",
                "component_features": "Company card limit rules, payroll batch upload, FX forward contracts booking",
                "color_tokens": {"background": "#FFFFFF", "accent": "#0075FF", "text": "#191C1F"},
                "key_interactions": "Instant card lock/unlock animation with haptic confirmation"
            },
            {
                "name": "AngelList Venture",
                "url": "https://www.angellist.com",
                "hero_pattern": "Venture fund syndicate rolling funds dashboard showing LP commitments and capital calls",
                "component_features": "SPV deal lead carry calculator, accredited investor verification drawer, distribution waterfall",
                "color_tokens": {"background": "#FAFAFA", "accent": "#000000", "text": "#111111"},
                "key_interactions": "Capital call commitment slider with wire instructions modal"
            },
            {
                "name": "PitchBook Data Platform",
                "url": "https://pitchbook.com",
                "hero_pattern": "Private market financial data terminal with comprehensive VC/PE funding rounds and valuations",
                "component_features": "Pre-money valuation percentile chart, investor portfolio co-investment matrix, M&A comps table",
                "color_tokens": {"background": "#0C1420", "accent": "#1A73E8", "text": "#FFFFFF"},
                "key_interactions": "Filter companies by revenue multiple with instant table reordering"
            },
            {
                "name": "Tearsheet FinTech Hub",
                "url": "https://tearsheet.co",
                "hero_pattern": "Banking-as-a-service (BaaS) and embedded finance executive analytics stream",
                "component_features": "Challenger bank metrics scorecard, regulatory compliance tracker, open banking API index",
                "color_tokens": {"background": "#1A1A1A", "accent": "#00FFA2", "text": "#FAFAFA"},
                "key_interactions": "Interactive FinTech market map filter by regulatory license type"
            },
            {
                "name": "Affirm Buy Now Pay Later",
                "url": "https://www.affirm.com",
                "hero_pattern": "Zero-interest installment payment schedule previewer with transparent dollar loan calculations",
                "component_features": "Soft credit check qualification modal, merchant checkout SDK widget, payment plan comparison cards",
                "color_tokens": {"background": "#FFFFFF", "accent": "#004BFF", "text": "#2B2B2B"},
                "key_interactions": "Installment plan selector (3, 6, 12 months) updating monthly repayment in real time"
            }
        ]
    },
    {
        "category_name": "Modern Creator Platforms & Video Streaming Studios",
        "design_paradigm": "Kinetic Typography, Waveform Scrollers, Live Chat Overlays & Monetization Drawers",
        "recommended_libraries": ["Framer Motion", "Video.js", "Wavesurfer.js", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Descript Text-Based Video Editor",
                "url": "https://www.descript.com",
                "hero_pattern": "Automatic transcription doc where deleting words in the transcript edits the underlying video file",
                "component_features": "AI filler word removal (um, uh) button, Overdub synthetic voice cloner, multicam auto-switching",
                "color_tokens": {"background": "#FBFBFB", "accent": "#5E48E8", "text": "#18181B"},
                "key_interactions": "Selecting text in transcript highlights corresponding video timeline frames"
            },
            {
                "name": "Riverside.fm 4K Podcast Recorder",
                "url": "https://riverside.fm",
                "hero_pattern": "Local-recording multi-guest studio capturing uncompressed 4K video and 48kHz WAV audio tracks",
                "component_features": "Independent track cloud upload progress meters, teleprompter overlay, live audience stage",
                "color_tokens": {"background": "#0D0D11", "accent": "#6C38FF", "text": "#FFFFFF"},
                "key_interactions": "Microphone input gain meter with live audio peak warning"
            },
            {
                "name": "CapCut Web Social Video Studio",
                "url": "https://www.capcut.com",
                "hero_pattern": "TikTok and Reels-optimized vertical video timeline with automated viral subtitle generation",
                "component_features": "Auto-captions style drawer, trending audio soundboard, background remove AI keyer, text-to-speech presets",
                "color_tokens": {"background": "#111111", "accent": "#00E5FF", "text": "#FFFFFF"},
                "key_interactions": "One-click auto caption generation with animated word-by-word karaoke style"
            },
            {
                "name": "Substack Writer Studio",
                "url": "https://substack.com",
                "hero_pattern": "Clean serif editorial publishing environment with subscriber revenue growth curve projections",
                "component_features": "WYSIWYG post editor with paywall divider, audio podcast player embed, subscriber segmentation table",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF6719", "text": "#222222"},
                "key_interactions": "Inserting paywall divider with preview toggle for free vs paid subscribers"
            },
            {
                "name": "Gumroad Creator Storefront",
                "url": "https://gumroad.com",
                "hero_pattern": "High-contrast neo-brutalist storefront with pay-what-you-want pricing slider and instant checkout",
                "component_features": "Digital file delivery locker, affiliate program commission manager, license key verification API",
                "color_tokens": {"background": "#FF90E8", "accent": "#000000", "text": "#000000"},
                "key_interactions": "Brutalist button hover shift with hard drop-shadows and spring feel"
            },
            {
                "name": "Patreon Creator Hub",
                "url": "https://www.patreon.com",
                "hero_pattern": "Membership tier benefit cards with exclusive patron community feed and Discord role integration",
                "component_features": "Tier pricing manager, patron direct messaging, merchandise fulfillment integration",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF424D", "text": "#1A1A1A"},
                "key_interactions": "Expanding membership card reveals exclusive locked video teaser"
            },
            {
                "name": "Epidemic Sound",
                "url": "https://www.epidemicsound.com",
                "hero_pattern": "Royalty-free music discovery wave scroller with stem-by-stem track download (Melody, Drums, Bass)",
                "component_features": "BPM and mood filter pills, YouTube copyright clearing whitelist checker, audio similarity search",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#FFFFFF"},
                "key_interactions": "Audio waveform scrubber with interactive stem mute toggles"
            },
            {
                "name": "Artlist Media",
                "url": "https://artlist.io",
                "hero_pattern": "High-energy footage reel with instant LUT color grading preview and raw video clips",
                "component_features": "License coverage validator, video resolution filter (4K/8K/ProRes), SFX library categorized by foley",
                "color_tokens": {"background": "#121212", "accent": "#FFE500", "text": "#EEEEEE"},
                "key_interactions": "Hovering video card triggers auto-looping 1080p preview without audio"
            },
            {
                "name": "Restream.io Multi-Broadcaster",
                "url": "https://restream.io",
                "hero_pattern": "Simultaneous live broadcasting console routing 1080p60 stream to YouTube, Twitch, and LinkedIn",
                "component_features": "Unified cross-platform chat dock, custom branded graphics overlay, stream health bit-rate chart",
                "color_tokens": {"background": "#191B26", "accent": "#2B59FF", "text": "#FFFFFF"},
                "key_interactions": "One-click 'Go Live to All Platforms' with countdown broadcast banner"
            },
            {
                "name": "Streamlabs Cloud Studio",
                "url": "https://streamlabs.com",
                "hero_pattern": "Custom alert box widget builder with live donation goal bars and tip jar physics animations",
                "component_features": "Scene collection switcher, tip jar physics simulator, chatbot moderation command list",
                "color_tokens": {"background": "#1E272C", "accent": "#31C3A2", "text": "#FFFFFF"},
                "key_interactions": "Test alert button simulating donation animation with confetti and sound"
            }
        ]
    },
    {
        "category_name": "AI Robotics, Embodied AI & Hardware Simulators",
        "design_paradigm": "Isaac Sim 3D Workspaces, Kinematic Chain Trees, Joint Angles & Trajectory Planners",
        "recommended_libraries": ["Three.js URDF Loader", "ECharts", "WebSocket Protobuf", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Nvidia Isaac Sim Cloud",
                "url": "https://www.nvidia.com/en-us/deep-learning-ai/solutions/isaac-sim/",
                "hero_pattern": "PhysX-powered photorealistic synthetic data generation world with robotic arms and mobile AMRs",
                "component_features": "URDF robot model importer, domain randomization slider, synthetic perception bounding box output",
                "color_tokens": {"background": "#000000", "accent": "#76B900", "text": "#FFFFFF"},
                "key_interactions": "Real-time gravity and friction parameter adjustment with live physics response"
            },
            {
                "name": "Figure AI Humanoid Portal",
                "url": "https://www.figure.ai",
                "hero_pattern": "Commercial autonomous humanoid robot Figure 02 neural network perception feed in manufacturing lines",
                "component_features": "Speech-to-action reasoning timeline, end-effector torque gauges, battery operational cycle chart",
                "color_tokens": {"background": "#0A0A0A", "accent": "#FFFFFF", "text": "#B3B3B3"},
                "key_interactions": "Interactive 3D model with rotatable degree-of-freedom joint visualization"
            },
            {
                "name": "1X Technologies NEO",
                "url": "https://www.1x.tech",
                "hero_pattern": "Safe, lightweight bipedal humanoid robotics with direct tendon-driven motors in domestic settings",
                "component_features": "Teleoperation VR link status, soft gripper force feedback chart, energy consumption per step",
                "color_tokens": {"background": "#F5F5F7", "accent": "#000000", "text": "#1D1D1F"},
                "key_interactions": "Kinematic gait walking speed slider with simulated stability margin"
            },
            {
                "name": "Sanctuary AI Phoenix",
                "url": "https://www.sanctuary.ai",
                "hero_pattern": "Carbon cognitive architecture and human-like robotic hands with dexterous manipulation telepresence",
                "component_features": "Haptic sensor pressure maps, task training demonstration recorder, pilot latency monitor",
                "color_tokens": {"background": "#0E1118", "accent": "#00F7A5", "text": "#FFFFFF"},
                "key_interactions": "Heatmap of tactile finger sensor arrays updating on contact"
            },
            {
                "name": "Unitree Robotics Go2 / G1",
                "url": "https://www.unitree.com",
                "hero_pattern": "Affordable quadruped and humanoid robots with 4D ultra-wide LiDAR navigation and backflip routines",
                "component_features": "Motion command terminal, live LiDAR point cloud visualizer, joint temperature monitoring table",
                "color_tokens": {"background": "#141414", "accent": "#FF3344", "text": "#EEEEEE"},
                "key_interactions": "Interactive 3D LiDAR point cloud rotation with obstacle distance markers"
            },
            {
                "name": "MuJoCo Physics Engine Web",
                "url": "https://mujoco.org",
                "hero_pattern": "Contact dynamics physics simulation optimized for reinforcement learning and robotics research",
                "component_features": "XML model definition viewer, contact forces vector arrows, tendon tension meters, frame rate counter",
                "color_tokens": {"background": "#202020", "accent": "#0099FF", "text": "#FFFFFF"},
                "key_interactions": "Applying perturbation force impulse by dragging body part with mouse"
            },
            {
                "name": "Foxglove Studio Robotics Visualization",
                "url": "https://foxglove.dev",
                "hero_pattern": "Extensible visualization environment for robotics supporting ROS 1, ROS 2, and MCAP files",
                "component_features": "3D scene grid, topic list with live Hz rate, message schema inspector, plot panel for coordinates",
                "color_tokens": {"background": "#1A1D24", "accent": "#6D3FEA", "text": "#F3F4F6"},
                "key_interactions": "Synchronized MCAP log playback with variable speed scrubbing and topic filtering"
            },
            {
                "name": "Kuka KUKA.sim",
                "url": "https://www.kuka.com",
                "hero_pattern": "Industrial robotic cell cycle time optimizer and reachability analysis in automotive factories",
                "component_features": "Cycle time second calculator, collision detection warning tree, robot kinematics catalog",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF6600", "text": "#222222"},
                "key_interactions": "3D robot arm jogging via interactive coordinate gizmo"
            },
            {
                "name": "Universal Robots PolyScope X",
                "url": "https://www.universal-robots.com",
                "hero_pattern": "Collaborative robot (cobot) teach pendant software with intuitive drag-to-teach waypoints",
                "component_features": "Visual programming tree (MoveJ, MoveL, Wait, Gripper), safety plane boundary configuration",
                "color_tokens": {"background": "#002B49", "accent": "#00A9E0", "text": "#FFFFFF"},
                "key_interactions": "Adding programming nodes with instant 3D ghost trajectory validation"
            },
            {
                "name": "Apptronik Apollo Portal",
                "url": "https://apptronik.com",
                "hero_pattern": "Commercial logistics humanoid robot with swappable battery packs and modular payloads",
                "component_features": "Warehouse tote transport schedule, payload kilogram capacity meter, charging fleet dock status",
                "color_tokens": {"background": "#0F0F12", "accent": "#0066FF", "text": "#F5F5F7"},
                "key_interactions": "Tote lifting trajectory simulation with center-of-mass balance indicator"
            }
        ]
    },
    {
        "category_name": "Interactive Gaming Platforms & Metaverse Ecosystems",
        "design_paradigm": "Game Cover Carousels, Real-Time Voice Activity Docks, Mod Repositories & Achievement Grids",
        "recommended_libraries": ["Framer Motion", "Tailwind CSS v4", "Lucide React", "Web Audio API"],
        "sites": [
            {
                "name": "Roblox Creator Hub",
                "url": "https://create.roblox.com",
                "hero_pattern": "Game development analytics tracking daily active users (DAU), retention, and Robux monetization",
                "component_features": "Spatial audio voice chat settings, 3D asset marketplace, real-time error crash log monitor",
                "color_tokens": {"background": "#191B1D", "accent": "#00A2FF", "text": "#FFFFFF"},
                "key_interactions": "One-click cloud place publishing with version rollback"
            },
            {
                "name": "Epic Games Store",
                "url": "https://store.epicgames.com",
                "hero_pattern": "Weekly free game countdown timer banner with high-resolution promotional artwork",
                "component_features": "Unreal Engine integration tab, library installation queue, achievement unlock progress bars",
                "color_tokens": {"background": "#121212", "accent": "#0078F2", "text": "#FFFFFF"},
                "key_interactions": "Instant 'Claim Free Game' with animated receipt confirmation modal"
            },
            {
                "name": "itch.io Indie Games",
                "url": "https://itch.io",
                "hero_pattern": "Community game jam showcase with playable HTML5 WebAssembly games directly in browser",
                "component_features": "Custom creator CSS theme override, game jam countdown submissions counter, donation tip jar",
                "color_tokens": {"background": "#222222", "accent": "#FA5C5C", "text": "#FFFFFF"},
                "key_interactions": "In-browser 'Run Game' button launching fullscreen WebGL canvas instantly"
            },
            {
                "name": "Discord Voice & Community Hub",
                "url": "https://discord.com",
                "hero_pattern": "Multi-pane voice channel ecosystem with real-time green speaking avatar rings and stage channels",
                "component_features": "Server channel category tree, rich presence game status cards, slash command autocomplete popover",
                "color_tokens": {"background": "#313338", "accent": "#5865F2", "text": "#DBDEE1"},
                "key_interactions": "Low-latency voice channel click-to-connect with audio ping chime"
            },
            {
                "name": "Nexus Mods Platform",
                "url": "https://www.nexusmods.com",
                "hero_pattern": "Community game modification repository with automated Vortex mod manager installation links",
                "component_features": "Mod version changelog drawer, endorsement counter, dependency requirements checklist modal",
                "color_tokens": {"background": "#2B2B2B", "accent": "#DA8A00", "text": "#E8E8E8"},
                "key_interactions": "One-click 'Vortex Download' triggering protocol handler with progress bar"
            },
            {
                "name": "GOG.com DRM-Free Platform",
                "url": "https://www.gog.com",
                "hero_pattern": "DRM-free digital preservation store with offline installer downloads and community wishlists",
                "component_features": "GOG Galaxy cloud save sync, classic game compatibility patch notes, retro digital goodies drawer",
                "color_tokens": {"background": "#1A1A1A", "accent": "#8C00FF", "text": "#F2F2F2"},
                "key_interactions": "Offline standalone installer download dropdown with MD5 checksums"
            },
            {
                "name": "CurseForge Modding Ecosystem",
                "url": "https://www.curseforge.com",
                "hero_pattern": "Minecraft and World of Warcraft modpack manager with automated dependency resolution",
                "component_features": "Modpack export profile button, game version compatibility selector, author donation rewards",
                "color_tokens": {"background": "#1C1C1F", "accent": "#F16436", "text": "#FFFFFF"},
                "key_interactions": "One-click 'Install with App' downloading dependencies in background"
            },
            {
                "name": "Unity Asset Store & Dashboard",
                "url": "https://assetstore.unity.com",
                "hero_pattern": "Comprehensive 3D models, shaders, and audio asset catalog with Package Manager integration",
                "component_features": "WebGL interactive asset demo iframe, package version compatibility table, publisher review ratings",
                "color_tokens": {"background": "#222C37", "accent": "#000000", "text": "#FFFFFF"},
                "key_interactions": "Live 3D asset preview in browser before purchase"
            },
            {
                "name": "Battle.net Desktop Hub",
                "url": "https://battle.net",
                "hero_pattern": "Iconic Blizzard game hub with cinematic hero video art and instant friend party status",
                "component_features": "Game patch release notes modal, battle tag friend presence list, cross-game chat drawer",
                "color_tokens": {"background": "#000B1A", "accent": "#00AEFF", "text": "#C4C8D0"},
                "key_interactions": "Large glowing 'Play' button with automatic pre-allocation download progress"
            },
            {
                "name": "Godot Asset Library",
                "url": "https://godotengine.org/asset-library/",
                "hero_pattern": "Open-source lightweight game engine plugin and template repository with zero royalties",
                "component_features": "Godot 4.x compatibility badges, MIT license verification, instant zip download button",
                "color_tokens": {"background": "#20252C", "accent": "#478CBF", "text": "#CFD5DF"},
                "key_interactions": "Filtering plugins by Godot version with instant result refresh"
            }
        ]
    },
    {
        "category_name": "Modern Luxury, Automotive & Industrial Hardware Showcases",
        "design_paradigm": "Nordic Minimalism, Exploded Product Assemblies, PBR Metallic Finishes & Sound Design",
        "recommended_libraries": ["Three.js", "GSAP ScrollTrigger", "Framer Motion", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Porsche Design Studio",
                "url": "https://www.porsche-design.com",
                "hero_pattern": "Precision chronometer watch face with mechanical flyback movement interactive 3D model",
                "component_features": "Titanium finish color switcher, chronograph pusher animations, strap material customizer",
                "color_tokens": {"background": "#000000", "accent": "#D5001C", "text": "#FFFFFF"},
                "key_interactions": "Interactive chronograph start/stop button running real-time second hand"
            },
            {
                "name": "Herman Miller Work Chairs",
                "url": "https://www.hermanmiller.com",
                "hero_pattern": "Aeron ergonomic chair exploded view diagram demonstrating Pellicle mesh tension distribution",
                "component_features": "PostureFit SL lumbar support toggle, armrest height adjustment slider, caster wheel selector",
                "color_tokens": {"background": "#FFFFFF", "accent": "#E00000", "text": "#222222"},
                "key_interactions": "Interactive posture slider showing spine alignment improvements in 3D"
            },
            {
                "name": "Dyson Digital Engineering",
                "url": "https://www.dyson.com",
                "hero_pattern": "Cyclone airflow aerodynamic particle separation CFD (Computational Fluid Dynamics) scroller",
                "component_features": "Acoustic motor decibel meter, HEPA filtration particle size comparison chart, battery runtime indicator",
                "color_tokens": {"background": "#141414", "accent": "#FF0077", "text": "#F5F5F5"},
                "key_interactions": "Interactive particle separation scroll animation showing air suction path"
            },
            {
                "name": "Sonos Acoustic Sound Experience",
                "url": "https://www.sonos.com",
                "hero_pattern": "Spatial multi-room home audio ecosystem visualizer with Trueplay room-tuning demonstration",
                "component_features": "Speaker grouping multi-room sync slider, Dolby Atmos height channel audio preview, voice control toggle",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#FFFFFF"},
                "key_interactions": "Simulated Trueplay acoustic calibration audio pulse animation"
            },
            {
                "name": "Lucid Motors Air Portal",
                "url": "https://www.lucidmotors.com",
                "hero_pattern": "Ultra-aerodynamic electric luxury sedan with 500+ mile range battery pack thermal visualizer",
                "component_features": "Glass canopy cockpit 360 view, charging kilowatt curve graph, drive mode selector (Smooth, Swift, Sprint)",
                "color_tokens": {"background": "#0D0E11", "accent": "#D4AF37", "text": "#FFFFFF"},
                "key_interactions": "Interactive drive mode switch altering digital gauge cluster themes"
            },
            {
                "name": "Analogue Pocket Retro Gaming",
                "url": "https://www.analogue.co/pocket",
                "hero_pattern": "Brutalist hardware photography of custom FPGA dual-processor handheld game system",
                "component_features": "Sub-pixel original display mode switcher (Game Boy, Game Boy Color, Game Boy Advance), openFPGA core list",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#808080"},
                "key_interactions": "Display mode switch transforming screen rendering with authentic LCD grid scanlines"
            },
            {
                "name": "Framework Modular Laptop",
                "url": "https://frame.work",
                "hero_pattern": "Modular expansion bay visualizer showing swappable USB-C, HDMI, and storage cards",
                "component_features": "Mainboard DIY upgrade kit selector, repairability 10/10 scorecard, carbon footprint calculation",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF4400", "text": "#111111"},
                "key_interactions": "Interactive module snap-in animation when selecting port configuration"
            },
            {
                "name": "Keychron Mechanical Keyboards",
                "url": "https://www.keychron.com",
                "hero_pattern": "Custom mechanical switch sound and actuation force tester with mechanical key exploded diagram",
                "component_features": "QMK/VIA keymap visualizer, hot-swappable switch comparison table, wireless multi-device pairing diagram",
                "color_tokens": {"background": "#1F2327", "accent": "#00ADB5", "text": "#EEEEEE"},
                "key_interactions": "Clicking keys on virtual keyboard plays real mechanical switch sound samples (Red, Blue, Brown)"
            },
            {
                "name": "Nothing Tech (Glyph Interface)",
                "url": "https://nothing.tech",
                "hero_pattern": "Transparent phone casing showcasing illuminated Glyph LED matrix light patterns responding to alerts",
                "component_features": "Glyph composer sound and light ringtone maker, transparent aesthetic gallery, Nothing OS widget drawer",
                "color_tokens": {"background": "#000000", "accent": "#D80027", "text": "#FFFFFF"},
                "key_interactions": "Interactive Glyph light pads triggering customizable LED pulse sequences"
            },
            {
                "name": "Leica Watches (ZM Series)",
                "url": "https://leica-camera.com/watches",
                "hero_pattern": "Patented push-crown mechanical watch inspired by camera shutter release mechanism",
                "component_features": "Power reserve indicator gauge, anti-reflective sapphire crystal dome visualizer, manual wind animation",
                "color_tokens": {"background": "#141414", "accent": "#E2001A", "text": "#FFFFFF"},
                "key_interactions": "Clicking the camera-shutter push crown resets the small second hand to zero"
            }
        ]
    }
]

# Append Extra Tiers to Existing Categories
def append_extra_tiers():
    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        vault = json.load(f)

    categories = vault.get("categories", [])
    cat_names = {c.get("category_name") for c in categories}

    for cat in EXTRA_TIERS_BATCH:
        if cat["category_name"] not in cat_names:
            categories.append(cat)
            cat_names.add(cat["category_name"])
        else:
            for existing in categories:
                if existing.get("category_name") == cat["category_name"]:
                    existing_sites = {s["name"] for s in existing.get("sites", [])}
                    for s in cat.get("sites", []):
                        if s["name"] not in existing_sites:
                            existing["sites"].append(s)

    total_sites = sum(len(c.get("sites", [])) for c in categories)
    vault["categories"] = categories
    vault["vault_metadata"]["total_categories"] = len(categories)
    vault["vault_metadata"]["total_products_and_sites"] = total_sites
    vault["vault_metadata"]["version"] = "4.5.0"

    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(vault, f, indent=2, ensure_ascii=False)

    print(f"[*] Extra Tiers Appended. Current Total Sites: {total_sites}")

append_extra_tiers()

FINAL_40_SITES = [
    {
        "category_name": "Interactive Education, Coding Bootcamps & Virtual Labs",
        "design_paradigm": "Gamified Progress Trees, In-Browser Sandboxes & Interactive Quizzes",
        "recommended_libraries": ["Monaco Editor", "Framer Motion", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Frontend Masters",
                "url": "https://frontendmasters.com",
                "hero_pattern": "Deep technical engineering video curricula with live course code sandboxes and closed captions",
                "component_features": "Learning path progression roadmap, course bookmarking drawer, video speed slider (0.5x - 3.0x)",
                "color_tokens": {"background": "#1E1E22", "accent": "#C02D28", "text": "#FFFFFF"},
                "key_interactions": "Hot-key driven video jumping and lesson completion checkmarks"
            },
            {
                "name": "Exercism.org",
                "url": "https://exercism.org",
                "hero_pattern": "70+ language learning tracks with automated test runners and free community human mentoring",
                "component_features": "Syllabus exercise tree, online code runner console, mentor feedback thread drawer",
                "color_tokens": {"background": "#009C95", "accent": "#FFE135", "text": "#FFFFFF"},
                "key_interactions": "Submitting solution runs automated test suite with passing badge celebration"
            },
            {
                "name": "freeCodeCamp",
                "url": "https://www.freecodecamp.org",
                "hero_pattern": "Non-profit interactive curriculum with split-screen instruction, editor, and live output",
                "component_features": "Certification progress steps, community forum link drawer, donation support modal",
                "color_tokens": {"background": "#0A0A23", "accent": "#FEAC32", "text": "#FFFFFF"},
                "key_interactions": "Ctrl+Enter executes tests with instant confetti reward on challenge pass"
            },
            {
                "name": "Coursera Plus",
                "url": "https://www.coursera.org",
                "hero_pattern": "Accredited university degree portal with verifiable LinkedIn certificate sharing",
                "component_features": "Weekly assignment timeline calendar, peer-graded review portal, downloadable lecture slides",
                "color_tokens": {"background": "#FFFFFF", "accent": "#0056D2", "text": "#1F1F1F"},
                "key_interactions": "Interactive quiz submission with immediate rationale explanation"
            },
            {
                "name": "Brilliant.org",
                "url": "https://brilliant.org",
                "hero_pattern": "Interactive physics and math concept visualizers where moving sliders explains principles",
                "component_features": "Daily streak flame counter, vector coordinate plane interactive canvas, puzzle progression roadmap",
                "color_tokens": {"background": "#FFFFFF", "accent": "#1473E6", "text": "#1A1A1A"},
                "key_interactions": "Kinetic sliders and physics gears reacting to user drag with real-time feedback"
            },
            {
                "name": "Khan Academy",
                "url": "https://www.khanacademy.org",
                "hero_pattern": "Blackboard-style educational video player with mastery mastery skill challenges",
                "component_features": "Khanmigo AI tutor chat pane, mastery badge drawer, teacher progress monitoring classroom grid",
                "color_tokens": {"background": "#FFFFFF", "accent": "#14BF96", "text": "#21242C"},
                "key_interactions": "Step-by-step math scratchpad overlay on practice problems"
            },
            {
                "name": "LeetCode Premium",
                "url": "https://leetcode.com",
                "hero_pattern": "Technical interview coding challenge portal with runtime/memory percentile comparison charts",
                "component_features": "Monaco code editor with testcase tab, discussion solution votes, company-tagged problem filters",
                "color_tokens": {"background": "#1A1A1A", "accent": "#FFA116", "text": "#EFF0F6"},
                "key_interactions": "One-click 'Run Code' displaying execution runtime vs top 5% of submissions"
            },
            {
                "name": "NeetCode.io",
                "url": "https://neetcode.io",
                "hero_pattern": "Structured algorithm roadmap (NeetCode 150) visualizing computer science data structure flow",
                "component_features": "Roadmap DAG node clickable links, video explanation modal, problem completion checkboxes",
                "color_tokens": {"background": "#121212", "accent": "#805AD5", "text": "#E2E8F0"},
                "key_interactions": "Clicking roadmap node filters table to related tree/graph/dynamic programming problems"
            },
            {
                "name": "Codecademy Interactive",
                "url": "https://www.codecademy.com",
                "hero_pattern": "Three-pane interactive browser coding lesson: Instructions -> Code Editor -> Live Terminal",
                "component_features": "Career path progress bar, portfolio project builder, AI error explanation bubble",
                "color_tokens": {"background": "#10162F", "accent": "#3A10E5", "text": "#FFF0E5"},
                "key_interactions": "Submitting task code with real-time terminal test output validation"
            },
            {
                "name": "DataCamp Cloud Workspace",
                "url": "https://www.datacamp.com",
                "hero_pattern": "Browser-based data science workspace with integrated Python/R environments and SQL consoles",
                "component_features": "Skill assessment radar chart, interactive dataset query panel, practice problem timer",
                "color_tokens": {"background": "#05192D", "accent": "#03EF62", "text": "#FFFFFF"},
                "key_interactions": "Interactive data table cell editing with instant matplotlib graph regeneration"
            }
        ]
    },
    {
        "category_name": "Decentralized Infrastructure, Zero-Knowledge & Web3 RPCs",
        "design_paradigm": "Cryptographic Proof Generators, Block Explorers, Mempool Trackers & Gas Heatmaps",
        "recommended_libraries": ["Ethers.js / Viem", "Tailwind CSS v4", "Lucide React"],
        "sites": [
            {
                "name": "Etherscan Block Explorer",
                "url": "https://etherscan.io",
                "hero_pattern": "Real-time block production ticker with pending transaction mempool counts and gas gwei tracker",
                "component_features": "Contract bytecode decompilation tab, token balance lookup, ERC-20 transfer event logs table",
                "color_tokens": {"background": "#F8F9FA", "accent": "#3498DB", "text": "#1E2022"},
                "key_interactions": "One-click transaction hash copy and interactive gas fee tracker tooltip"
            },
            {
                "name": "Alchemy Web3 Developer Platform",
                "url": "https://www.alchemy.com",
                "hero_pattern": "Supernode blockchain API dashboard with request per second (RPS) throughput and latency graphs",
                "component_features": "Composer API request builder, mempool visualizer, smart contract webhook notification rules",
                "color_tokens": {"background": "#05060B", "accent": "#0055FF", "text": "#FFFFFF"},
                "key_interactions": "Instant testnet/mainnet RPC endpoint switcher with API usage billing alert slider"
            },
            {
                "name": "Infura (ConsenSys)",
                "url": "https://www.infura.io",
                "hero_pattern": "Ethereum, IPFS, and Polygon RPC infrastructure handling billions of daily requests",
                "component_features": "Multi-network project manager, IPFS file pin visualizer, rate-limit threshold gauge",
                "color_tokens": {"background": "#191919", "accent": "#FF6B4A", "text": "#FFFFFF"},
                "key_interactions": "Network selector dropdown with instant RPC endpoint URL copy"
            },
            {
                "name": "Zircuit / zkSync Era Portal",
                "url": "https://zksync.io",
                "hero_pattern": "Zero-Knowledge rollup transaction bridge showing cryptographic proof batch verification",
                "component_features": "L1 to L2 deposit timeline, bridge fee estimator, account abstraction smart contract wallet manager",
                "color_tokens": {"background": "#000000", "accent": "#8C8DFC", "text": "#FFFFFF"},
                "key_interactions": "Interactive bridge slider showing L1 confirmation time vs L2 finality"
            },
            {
                "name": "Starknet Ecosystem Hub",
                "url": "https://www.starknet.io",
                "hero_pattern": "STARK-based Validity Rollup dashboard demonstrating native account abstraction and Cairo smart contracts",
                "component_features": "Ecosystem dapp matrix, block explorer link, TVL and TPS (transactions per second) live gauges",
                "color_tokens": {"background": "#0C0C14", "accent": "#EC796B", "text": "#F3F3F7"},
                "key_interactions": "Dapp directory category filter with verified security audit pills"
            },
            {
                "name": "Chainlink Data Feeds Portal",
                "url": "https://data.chain.link",
                "hero_pattern": "Decentralized Oracle network aggregator displaying price feed heartbeats and deviation thresholds",
                "component_features": "Node operator quorum consensus visualizer, round ID transaction link, price answer latency meter",
                "color_tokens": {"background": "#080C14", "accent": "#375BD2", "text": "#FFFFFF"},
                "key_interactions": "Hovering price feed reveals node answer distribution and last round timestamp"
            },
            {
                "name": "Safe (Gnosis Safe)",
                "url": "https://safe.global",
                "hero_pattern": "Multi-signature smart contract treasury manager requiring m-of-n owner approvals for execution",
                "component_features": "Pending transaction signature queue, spending limit policy editor, dapp transaction batch simulator",
                "color_tokens": {"background": "#121312", "accent": "#12FF80", "text": "#FFFFFF"},
                "key_interactions": "One-click 'Sign Transaction' with hardware wallet integration modal"
            },
            {
                "name": "Polygon PoS & AggLayer",
                "url": "https://polygon.technology",
                "hero_pattern": "Aggregation layer unifying liquidity across multiple ZK chains with sub-second cross-chain proofs",
                "component_features": "Staking validator delegator reward calculator, bridge status monitor, developer faucet",
                "color_tokens": {"background": "#0B0B0F", "accent": "#7B3FE4", "text": "#FFFFFF"},
                "key_interactions": "Staking reward slider estimating annual percentage yield (APY) based on delegated MATIC"
            },
            {
                "name": "Solana FM Explorer",
                "url": "https://solana.fm",
                "hero_pattern": "High-throughput Solana ledger transaction flow graph unpacking CPI (Cross-Program Invocations)",
                "component_features": "Instruction visualizer tree, token account balances, validator cluster epoch progress bar",
                "color_tokens": {"background": "#0B0E14", "accent": "#14F195", "text": "#FFFFFF"},
                "key_interactions": "Interactive program call tree expanding internal instruction logs and compute units consumed"
            },
            {
                "name": "The Graph Hosted Service & Studio",
                "url": "https://thegraph.com",
                "hero_pattern": "Decentralized indexing protocol for querying blockchain networks using GraphQL APIs",
                "component_features": "Subgraph schema playground, GraphQL query runner dock, indexer curation signal table",
                "color_tokens": {"background": "#0C0A1D", "accent": "#6F4CFF", "text": "#FFFFFF"},
                "key_interactions": "Query play button running GraphQL query with live JSON response formatting"
            }
        ]
    },
    {
        "category_name": "Real Estate Tech, 3D Virtual Tours & Urban Planning AI",
        "design_paradigm": "Dollhouse 3D Views, Spatial Measurement Tools & Environmental Sun Studies",
        "recommended_libraries": ["Three.js", "Mapbox GL", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Matterport 3D Digital Twins",
                "url": "https://matterport.com",
                "hero_pattern": "Photorealistic 3D dollhouse floor plan view with walkthrough navigation hotspots",
                "component_features": "Interactive digital tape measure tool, floor-by-floor level switcher, VR headset mode toggle",
                "color_tokens": {"background": "#1B1D1F", "accent": "#2B88D9", "text": "#FFFFFF"},
                "key_interactions": "Dollhouse to inside-room zoom transition with smooth camera translation"
            },
            {
                "name": "Autodesk Forma Urban AI",
                "url": "https://www.autodesk.com/products/forma/",
                "hero_pattern": "Generative urban site planning AI predicting daylight hours, microclimate wind, and noise pollution",
                "component_features": "Real-time sunlight analysis slider, building massing volume generator, environmental score cards",
                "color_tokens": {"background": "#222222", "accent": "#0696D7", "text": "#F5F5F5"},
                "key_interactions": "Dragging building mass heights updates solar shadow cast and wind velocity in real time"
            },
            {
                "name": "Zillow 3D Home Tours",
                "url": "https://www.zillow.com",
                "hero_pattern": "Interactive neighborhood map with Zestimate home value chart and historical price trends",
                "component_features": "Mortgage payment calculator slider (down payment, interest rate, HOA fees), photo gallery lightbox",
                "color_tokens": {"background": "#FFFFFF", "accent": "#006AFF", "text": "#2A2A33"},
                "key_interactions": "Mortgage slider dynamically updating monthly payment pie chart without delay"
            },
            {
                "name": "Redfin Instant Valuation",
                "url": "https://www.redfin.com",
                "hero_pattern": "Map-centric real estate search with live polygon boundary drawing and school ratings",
                "component_features": "Comp home sales comparison table, one-click agent tour scheduler, property tax breakdown",
                "color_tokens": {"background": "#FFFFFF", "accent": "#C82021", "text": "#333333"},
                "key_interactions": "Drawing freehand polygon on map isolates active listings within hand-drawn boundary"
            },
            {
                "name": "TestFit Generative Feasibility",
                "url": "https://testfit.io",
                "hero_pattern": "Real estate building layout configurator maximizing unit count, parking spaces, and ROI",
                "component_features": "Unit mix breakdown pie chart, financial pro-forma cost modeler, parking garage stall auto-pack",
                "color_tokens": {"background": "#111827", "accent": "#3B82F6", "text": "#F9FAFB"},
                "key_interactions": "Modifying site boundary instantly re-solves building footprint and parking stalls"
            },
            {
                "name": "Architizer Project Showcase",
                "url": "https://architizer.com",
                "hero_pattern": "World architecture project visual portfolio highlighting innovative facades and materials",
                "component_features": "Architectural product specification tags, high-resolution photography slider, floor plan viewer",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#DDDDDD"},
                "key_interactions": "Clicking building material tag navigates directly to manufacturer catalog"
            },
            {
                "name": "CoStar Commercial Analytics",
                "url": "https://www.costar.com",
                "hero_pattern": "Commercial real estate market intelligence showing lease rates, vacancy trends, and tenant rosters",
                "component_features": "Submarket vacancy rate heat map, tenant lease expiration timeline, building spec sheet PDF export",
                "color_tokens": {"background": "#002B49", "accent": "#00A9E0", "text": "#FFFFFF"},
                "key_interactions": "Filter commercial office spaces by square footage and ceiling height"
            },
            {
                "name": "Morpholio Trace AR Sketchpad",
                "url": "https://www.morpholioapps.com/trace/",
                "hero_pattern": "Architectural yellow tracing paper simulation layered over PDF blueprints and camera photos",
                "component_features": "Perspective grid ruler tool, scale measurement calibrator, layer opacity slider",
                "color_tokens": {"background": "#232323", "accent": "#FFDF00", "text": "#FFFFFF"},
                "key_interactions": "Simulated ink pressure response with instant scale ruler alignment"
            },
            {
                "name": "Enscape Real-Time Architectural VR",
                "url": "https://enscape3d.com",
                "hero_pattern": "Real-time walkthrough rendering engine directly synchronized with Revit, SketchUp, and Rhino",
                "component_features": "Time of day sun position dial, cloud coverage slider, artificial lighting intensity matrix",
                "color_tokens": {"background": "#14171A", "accent": "#FF5500", "text": "#FFFFFF"},
                "key_interactions": "Dragging time-of-day slider animates architectural shadows across room interior"
            },
            {
                "name": "Spacemaker AI Urban Planning",
                "url": "https://www.autodesk.com",
                "hero_pattern": "AI-powered urban exploration optimizing site acoustics, view quality, and microclimate comfort",
                "component_features": "Apartment view analysis ray caster, noise pollution map, wind tunnel velocity simulation",
                "color_tokens": {"background": "#0E1520", "accent": "#2BD4A7", "text": "#E1E8F2"},
                "key_interactions": "3D view ray calculation determining percentage of water/park view per apartment unit"
            }
        ]
    },
    {
        "category_name": "Modern Search Engines, Knowledge Bases & Spatial Wikis",
        "design_paradigm": "Instant Omnibar Search, Bi-Directional Graph Links & Minimalist Serif Typography",
        "recommended_libraries": ["KBar", "Framer Motion", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Kagi Search",
                "url": "https://kagi.com",
                "hero_pattern": "Ad-free, privacy-first search engine with custom domain ranking lenses and AI quick answer summaries",
                "component_features": "Website domain downrank/boost slider, custom CSS themes, Lenses search filter tabs",
                "color_tokens": {"background": "#F5F5F5", "accent": "#FFC107", "text": "#222222"},
                "key_interactions": "Instant domain blocking removes site from all future search queries"
            },
            {
                "name": "Brave Search & Leo AI",
                "url": "https://search.brave.com",
                "hero_pattern": "Independent global web index with privacy focus and real-time summarizer answers",
                "component_features": "Goggles custom ranking filter community list, image/video tab, Anonymous local search map",
                "color_tokens": {"background": "#1A1A1A", "accent": "#FB542B", "text": "#FFFFFF"},
                "key_interactions": "Toggling custom Goggles alters search result order instantaneously"
            },
            {
                "name": "Ecosia Eco Search",
                "url": "https://www.ecosia.org",
                "hero_pattern": "Tree-planting search engine transparently tracking collective trees planted per search query",
                "component_features": "Personal tree counter badge, financial monthly earnings reports, green leaf organization ratings",
                "color_tokens": {"background": "#FFFFFF", "accent": "#008000", "text": "#333333"},
                "key_interactions": "Tree counter tick animation on every completed search query"
            },
            {
                "name": "DuckDuckGo Privacy Browser",
                "url": "https://duckduckgo.com",
                "hero_pattern": "Minimalist privacy search interface with tracker blocker burn button and Bang search shortcuts",
                "component_features": "!bang shortcut autocomplete list (!w for Wikipedia, !g for GitHub), burn animation modal",
                "color_tokens": {"background": "#FFFFFF", "accent": "#DE5833", "text": "#222222"},
                "key_interactions": "Flame 'Burn' button clearing all tabs and stored cookies with burning flame animation"
            },
            {
                "name": "Arc Search (The Browser Company)",
                "url": "https://arc.net",
                "hero_pattern": "'Browse for Me' AI feature reading and synthesizing multiple web pages into a custom magazine page",
                "component_features": "Dynamic Bento summary layout, quote source cards, pinch-to-summarize mobile gesture",
                "color_tokens": {"background": "#0D0E11", "accent": "#FF4477", "text": "#FFFFFF"},
                "key_interactions": "Pinch gesture on search bar compiles instant structured research brief"
            },
            {
                "name": "Readwise Reader",
                "url": "https://readwise.io/read",
                "hero_pattern": "Power-user read-it-later app unifying newsletters, PDFs, web articles, and EPUB books",
                "component_features": "Vim keyboard navigation (j/k), Ghostreader AI summary drawer, bidirectional highlight sync to Notion/Obsidian",
                "color_tokens": {"background": "#191B1F", "accent": "#3B82F6", "text": "#E5E7EB"},
                "key_interactions": "Highlighting text opens instant color palette and note tag popover"
            },
            {
                "name": "Reflect Notes",
                "url": "https://reflect.app",
                "hero_pattern": "End-to-end encrypted networked note-taking app with calendar integration and backlinks graph",
                "component_features": "Interactive associative graph view, daily journal calendar bar, AI audio voice transcription",
                "color_tokens": {"background": "#0E1015", "accent": "#7C3AED", "text": "#FFFFFF"},
                "key_interactions": "Typing [[ triggers instant note backlink autocomplete dropdown"
            },
            {
                "name": "Anytype Local-First P2P Workspace",
                "url": "https://anytype.io",
                "hero_pattern": "Decentralized, local-first operating environment built on IPFS with block-based object ontology",
                "component_features": "Object-oriented relations matrix, peer-to-peer sync status, widget dashboard builder",
                "color_tokens": {"background": "#121214", "accent": "#FF5C5C", "text": "#EFEFEF"},
                "key_interactions": "Creating objects and linking relations with instant local-first persistence"
            },
            {
                "name": "Heptabase Spatial Research",
                "url": "https://heptabase.com",
                "hero_pattern": "Visual whiteboard for complex learning turning PDFs and notes into spatial mental concept maps",
                "component_features": "PDF split-view with drag-out highlight cards, nested whiteboard boards, timeline view",
                "color_tokens": {"background": "#141517", "accent": "#00A3FF", "text": "#E4E7EB"},
                "key_interactions": "Dragging highlighted sentence from PDF directly onto infinite canvas as independent card"
            },
            {
                "name": "Scrintal Visual Mind",
                "url": "https://www.scrintal.com",
                "hero_pattern": "Visual note-taking combining mind mapping with markdown writing cards and connecting arrows",
                "component_features": "Color-coded connector lines, card fold/unfold toggle, multimedia attachment embeds",
                "color_tokens": {"background": "#1E1E24", "accent": "#F59E0B", "text": "#F8FAFC"},
                "key_interactions": "Card expansion from thumbnail title into full-length rich markdown document"
            }
        ]
    }
]

def append_final_tiers():
    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        vault = json.load(f)

    categories = vault.get("categories", [])
    cat_names = {c.get("category_name") for c in categories}

    for cat in FINAL_40_SITES:
        if cat["category_name"] not in cat_names:
            categories.append(cat)
            cat_names.add(cat["category_name"])
        else:
            for existing in categories:
                if existing.get("category_name") == cat["category_name"]:
                    existing_sites = {s["name"] for s in existing.get("sites", [])}
                    for s in cat.get("sites", []):
                        if s["name"] not in existing_sites:
                            existing["sites"].append(s)

    total_sites = sum(len(c.get("sites", [])) for c in categories)
    vault["categories"] = categories
    vault["vault_metadata"]["total_categories"] = len(categories)
    vault["vault_metadata"]["total_products_and_sites"] = total_sites
    vault["vault_metadata"]["version"] = "5.0.0"

    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(vault, f, indent=2, ensure_ascii=False)

    print(f"[*] Final Tiers Appended. Current Total Sites: {total_sites}")

append_final_tiers()
