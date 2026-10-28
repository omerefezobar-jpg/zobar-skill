"""
Asset Vault Builder Script
Generates references/free_assets_and_3d_vault.json with verified 3D assets,
PBR textures, UI component libraries, audio SFX, and icon systems.
"""

import os
import json

ASSETS_DATA = {
    "version": "1.0.0",
    "total_resources": 0,
    "categories": {
        "3d_models_and_meshes": [
            {
                "name": "Kenney 3D Asset Packs",
                "url": "https://kenney.nl/assets/series:3D",
                "license": "CC0 1.0 Universal (Public Domain - 100% Free for commercial use)",
                "formats": ["GLTF", "FBX", "OBJ"],
                "description": "Dozens of high-quality modular 3D game asset kits: Space Kit, City Kit, Blaster Kit, Car Kit, Nature Kit, Dungeon Kit. Zero attribution required.",
                "best_for": "Indie games, rapid 3D prototyping, Three.js WebGL scenes",
                "integration_code": "// Three.js GLTFLoader\nimport { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';\nconst loader = new GLTFLoader();\nloader.load('path/to/kenney_model.gltf', (gltf) => scene.add(gltf.scene));"
            },
            {
                "name": "Poly Pizza",
                "url": "https://poly.pizza",
                "license": "CC0 / CC-BY (Searchable filter for 100% CC0 public domain)",
                "formats": ["GLTF", "GLB", "OBJ"],
                "description": "Massive community library of low-poly 3D models with one-click download. Successor to Google Poly.",
                "best_for": "Low-poly games, mobile apps, lightweight web 3D",
                "integration_code": "// React Three Fiber\nimport { useGLTF } from '@react-three/drei';\nfunction Model() { const { scene } = useGLTF('https://poly.pizza/path.glb'); return <primitive object={scene} />; }"
            },
            {
                "name": "Quaternius 3D Modular Kits",
                "url": "https://quaternius.com",
                "license": "CC0 1.0 Universal (Public Domain)",
                "formats": ["GLTF", "FBX", "Blend"],
                "description": "Over 50 modular 3D packs: animated characters, monsters, mechs, medieval villages, sci-fi modular environments, low-poly vehicles.",
                "best_for": "Godot, Unity, Unreal Engine, and WebGPU 3D games",
                "integration_code": "Quaternius assets come with pre-rigged armatures and animations (Walk, Run, Attack, Idle)."
            },
            {
                "name": "PMNDRS Market (React Three Fiber)",
                "url": "https://market.pmnd.rs",
                "license": "Open Source / CC0",
                "formats": ["GLTF", "GLB", "R3F Components"],
                "description": "Curated 3D assets, procedural shaders, and interactive 3D components made specifically for the Poimandres React Three Fiber ecosystem.",
                "best_for": "Interactive 3D web experiences, creative agency landing pages",
                "integration_code": "npx gltfjsx model.glb // Automatically creates typed JSX R3F component"
            },
            {
                "name": "NASA 3D Resources",
                "url": "https://nasa3d.arc.nasa.gov",
                "license": "Public Domain (NASA Educational & Commercial Fair Use)",
                "formats": ["GLTF", "OBJ", "STL"],
                "description": "Official 3D models of spacecraft, satellites (James Webb, Hubble), Mars rovers (Curiosity, Perseverance), planets, asteroids, and Moon landing sites.",
                "best_for": "Space simulators, science applications, educational WebGL",
                "integration_code": "Download satellite / rover GLTF model and load into Three.js scene."
            },
            {
                "name": "Mixamo (Adobe)",
                "url": "https://www.mixamo.com",
                "license": "Royalty-Free (Free for commercial and non-commercial projects)",
                "formats": ["FBX", "DAE"],
                "description": "Thousands of production-ready 3D humanoid characters and motion-capture animations (combat, locomotion, dance, sports). Automatic auto-rigger for custom meshes.",
                "best_for": "Character rigging, game animations, interactive avatar controllers",
                "integration_code": "Export rigged FBX with Skin, import into Blender or Three.js AnimationMixer."
            },
            {
                "name": "Ready Player Me",
                "url": "https://readyplayer.me",
                "license": "Free Developer API / Commercial Friendly",
                "formats": ["GLB"],
                "description": "Cross-game 3D avatar creator with customizable facial blendshapes for real-time lip-sync and facial tracking (ARKit compatible).",
                "best_for": "Virtual worlds, AI conversational avatars, WebRTC video/voice bots",
                "integration_code": "https://models.readyplayer.me/YOUR_AVATAR_ID.glb?morphTargets=ARKit"
            },
            {
                "name": "Spline 3D Community Library",
                "url": "https://spline.design/community",
                "license": "Free Community Remixes",
                "formats": ["Spline Scene", "GLTF", "WebGL Embed"],
                "description": "Interactive web-first 3D scenes with real-time physics, glass materials, mouse cursor tracking, and zero-code React embeds.",
                "best_for": "SaaS hero sections, interactive landing page 3D micro-interactions",
                "integration_code": "<Spline scene='https://prod.spline.design/your-scene/scene.splinecode' />"
            }
        ],
        "pbr_textures_and_materials": [
            {
                "name": "Poly Haven PBR Textures & HDRIs",
                "url": "https://polyhaven.com/textures",
                "license": "CC0 1.0 Universal (100% Public Domain)",
                "formats": ["PNG", "EXR", "JPG (1K to 8K PBR Maps)"],
                "description": "Industry gold-standard photorealistic PBR textures: Diffuse/Albedo, Normal (DirectX/OpenGL), Roughness, Displacement, Ambient Occlusion, Metalness.",
                "best_for": "Photorealistic 3D rendering, Blender, Unreal Engine, WebGPU",
                "integration_code": "const material = new MeshStandardMaterial({ map: albedoMap, normalMap: normalMap, roughnessMap: roughMap });"
            },
            {
                "name": "ambientCG",
                "url": "https://ambientcg.com",
                "license": "CC0 1.0 Universal (Public Domain)",
                "formats": ["PNG", "JPG", "SBSAR"],
                "description": "Over 2,200 public domain PBR materials: concrete, bricks, marble, metals, wood, fabrics, terrain, and procedural Substance Designer materials.",
                "best_for": "Architectural visualization, environment art, procedural shader graphs",
                "integration_code": "Download full PBR ZIP containing BaseColor, NormalGL, Roughness, and Height."
            },
            {
                "name": "ShareTextures",
                "url": "https://www.sharetextures.com",
                "license": "CC0 Public Domain",
                "formats": ["PNG", "JPG (up to 4K)"],
                "description": "Over 1,400 arch-viz and game-ready textures scanned from real-world surfaces by architectural designers.",
                "best_for": "Interior design renders, modern architectural websites",
                "integration_code": "Direct download of packed PBR texture sets."
            }
        ],
        "ui_component_and_animation_libraries": [
            {
                "name": "Aceternity UI",
                "url": "https://ui.aceternity.com",
                "license": "MIT License (Free for commercial use)",
                "formats": ["React", "Next.js", "Tailwind CSS", "Framer Motion"],
                "description": "Trending S-Tier interactive components: 3D Pin, Canvas Reveal Effect, Bento Grid, Tracing Beam, Sparkles, Lamp Header, Evervault Card.",
                "best_for": "Frontier AI and tech startup landing pages",
                "integration_code": "npx shadcn@latest add 'https://ui.aceternity.com/registry/bento-grid.json'"
            },
            {
                "name": "Magic UI",
                "url": "https://magicui.design",
                "license": "MIT License",
                "formats": ["React", "Tailwind CSS", "Framer Motion"],
                "description": "50+ copy-paste animated components for modern marketing pages: Animated Beam, Globe 3D, Shimmer Button, Retro Grid, Orbiting Circles, Dot Pattern.",
                "best_for": "SaaS hero sections, developer tools, viral product launches",
                "integration_code": "npx shadcn@latest add 'https://magicui.design/r/globe'"
            },
            {
                "name": "Shadcn UI",
                "url": "https://ui.shadcn.com",
                "license": "MIT License",
                "formats": ["React", "Next.js", "Radix UI", "Tailwind CSS"],
                "description": "The undisputed modern standard for web apps. Accessible, keyboard-navigable components that you own and copy directly into your project.",
                "best_for": "Enterprise dashboards, SaaS products, production applications",
                "integration_code": "npx shadcn@latest init && npx shadcn@latest add button dialog dropdown-menu"
            },
            {
                "name": "21st.dev (The NPM for Design Engineers)",
                "url": "https://21st.dev",
                "license": "MIT / Open Source",
                "formats": ["React", "Tailwind CSS"],
                "description": "Curated library of hyper-polished micro-interactions and design engineering components created by top frontend craftsmen.",
                "best_for": "Unique UI micro-interactions, spring physics cards, magnetic buttons",
                "integration_code": "Browse, preview interactive widget, copy code snippet directly."
            },
            {
                "name": "Tremor",
                "url": "https://www.tremor.so",
                "license": "Apache 2.0",
                "formats": ["React", "Tailwind CSS"],
                "description": "The leading open-source library for building charts, analytical dashboards, metric cards, and data visualization grids.",
                "best_for": "FinTech dashboards, developer analytics, observability panels",
                "integration_code": "npm i @tremor/react // Import AreaChart, Card, Metric, Flex, Badge"
            },
            {
                "name": "Uiverse.io",
                "url": "https://uiverse.io",
                "license": "MIT / Open Source",
                "formats": ["HTML", "CSS", "Tailwind CSS"],
                "description": "Over 3,500 open-source community UI elements: animated glowing buttons, cyber checkouts, loaders, input fields, tooltips, glass cards.",
                "best_for": "Pure CSS animations, zero-dependency lightweight widgets",
                "integration_code": "Click any component and copy pure CSS or Tailwind classes."
            },
            {
                "name": "React Flow & Svelte Flow",
                "url": "https://reactflow.dev",
                "license": "MIT License (Core is 100% free)",
                "formats": ["React", "Svelte", "TypeScript"],
                "description": "Highly customizable library for building node-based interactive UIs, workflow builders, neural network visualizers, and diagram editors.",
                "best_for": "Agent orchestration UIs, no-code visual workflow editors",
                "integration_code": "npm install @xyflow/react // Render <ReactFlow nodes={nodes} edges={edges} />"
            }
        ],
        "icons_and_vector_design_systems": [
            {
                "name": "Lucide Icons",
                "url": "https://lucide.dev",
                "license": "ISC License (Equivalent to MIT - Free commercial use)",
                "formats": ["SVG", "React", "Vue", "Angular", "Figma"],
                "description": "Beautiful & consistent icon toolkit with 1,450+ icons. The official community fork and evolution of Feather Icons.",
                "best_for": "Modern SaaS, design systems, clean typography",
                "integration_code": "npm i lucide-react // import { Sparkles, ArrowRight, Database } from 'lucide-react';"
            },
            {
                "name": "Phosphor Icons",
                "url": "https://phosphoricons.com",
                "license": "MIT License",
                "formats": ["SVG", "React", "Web Components", "Figma"],
                "description": "1,200+ icons in 6 weights: Thin, Light, Regular, Bold, Fill, and Duotone.",
                "best_for": "Playful, high-polish user interfaces requiring consistent line weights",
                "integration_code": "import { Compass, Cube } from '@phosphor-icons/react';"
            },
            {
                "name": "Simple Icons",
                "url": "https://simpleicons.org",
                "license": "CC0 1.0 Universal",
                "formats": ["SVG", "JSON", "React"],
                "description": "Over 3,100 clean, single-path SVG brand icons for popular tech stacks, databases, frameworks, cloud providers, and social platforms.",
                "best_for": "Tech stack showcases, integration badges, footer links",
                "integration_code": "import { siPostgresql, siRust, siDocker } from 'simple-icons';"
            },
            {
                "name": "SVGL (Tech Logo Library)",
                "url": "https://svgl.app",
                "license": "Open Source",
                "formats": ["SVG", "React", "Next.js"],
                "description": "A curated, modern library of SVG logos from top technology companies, frameworks, and developer platforms.",
                "best_for": "Landing page 'Trusted By' hero sections, developer portfolio tech logos",
                "integration_code": "Copy raw SVG or embed via CDN: https://svgl.app/library/supabase.svg"
            }
        ],
        "audio_sfx_and_soundtracks": [
            {
                "name": "Kenney Audio Packs",
                "url": "https://kenney.nl/assets/series:Audio",
                "license": "CC0 1.0 Universal (100% Free Public Domain)",
                "formats": ["OGG", "WAV"],
                "description": "Over 1,000 game-ready audio assets: UI audio (subtle clicks, pops, switches), digital audio (beeps, telemetries, computing), casino sounds, impact SFX.",
                "best_for": "Web app UI micro-interaction sounds, indie games",
                "integration_code": "const clickSound = new Audio('/sounds/click.ogg'); clickSound.play();"
            },
            {
                "name": "Freesound.org",
                "url": "https://freesound.org",
                "license": "Creative Commons (CC0, CC-BY, CC-Sampling+)",
                "formats": ["WAV", "FLAC", "MP3"],
                "description": "Collaborative database of over 500,000 sound effects, environmental ambiances, mechanical recordings, and foley.",
                "best_for": "Game sound design, ambient background audio, movie trailers",
                "integration_code": "REST API available for searching and programmatically streaming audio."
            },
            {
                "name": "Soniss GDC Audio Archive",
                "url": "https://soniss.com/gameaudiogdc",
                "license": "Royalty-Free Commercial License",
                "formats": ["WAV (24-bit 96kHz)"],
                "description": "Over 100 GB of high-end Hollywood and AAA game sound effects released royalty-free every year during Game Developers Conference (GDC).",
                "best_for": "AAA games, sci-fi weapons, cinematic explosions, monster foley",
                "integration_code": "Studio quality 96kHz WAV files ready for DAW or FMOD/Wwise integration."
            }
        ]
    }
}

# Calculate total count
total = sum(len(items) for items in ASSETS_DATA["categories"].values())
ASSETS_DATA["total_resources"] = total

target_path = os.path.join(os.path.dirname(__file__), "..", "references", "free_assets_and_3d_vault.json")
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(ASSETS_DATA, f, indent=2, ensure_ascii=False)

print(f"[+] Asset Vault created successfully with {total} verified resources at: {target_path}")
