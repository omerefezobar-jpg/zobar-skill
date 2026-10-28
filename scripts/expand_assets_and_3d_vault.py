#!/usr/bin/env python3
"""
Expands references/free_assets_and_3d_vault.json from 25 to 50+ curated,
100% free / CC0 / Open Source 3D assets, textures, animations, and shaders.
"""

import json
import os
import sys

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT_PATH = os.path.join(os.path.dirname(__file__), "..", "references", "free_assets_and_3d_vault.json")

NEW_ASSETS = {
    "3d_models_and_meshes": [
        {
            "name": "Sketchfab CC0 Showcase",
            "url": "https://sketchfab.com/features/free-3d-models",
            "license": "Creative Commons CC0 / CC-BY",
            "formats": ["GLTF", "USDZ", "OBJ"],
            "description": "Thousands of community 3D models with direct in-browser inspection and one-click GLTF download.",
            "best_for": "Web 3D showcases, photogrammetry, product visualizations",
            "integration_code": "// Download GLTF and load via Three.js GLTFLoader\nloader.load('sketchfab_model.gltf', (gltf) => scene.add(gltf.scene));"
        },
        {
            "name": "Mixamo by Adobe",
            "url": "https://www.mixamo.com",
            "license": "Free for Commercial and Personal Use (Royalty-Free with Adobe Account)",
            "formats": ["FBX", "Collada DAE"],
            "description": "Massive library of pre-rigged 3D humanoid characters and over 10,000 motion-capture animations (walk, run, combat, dance).",
            "best_for": "Character rigging, game prototypes, skeletal animations in Three.js / Unreal",
            "integration_code": "// Load FBX and bind AnimationMixer\nconst mixer = new THREE.AnimationMixer(fbx);\nmixer.clipAction(fbx.animations[0]).play();"
        },
        {
            "name": "NASA 3D Planetary & Spacecraft Resources",
            "url": "https://nasa3d.arc.nasa.gov",
            "license": "Public Domain (US Government Work)",
            "formats": ["OBJ", "GLTF", "STL", "3DS"],
            "description": "Official 3D models of Mars rovers (Perseverance, Curiosity), ISS Space Station, Apollo landers, and celestial terrain elevation maps.",
            "best_for": "Scientific simulations, educational space portals, aerospace telemetry HUDs",
            "integration_code": "// Real orbital asset models from NASA JPL directly usable in Three.js"
        },
        {
            "name": "Smithsonian 3D Digitization",
            "url": "https://3d.si.edu",
            "license": "Smithsonian Open Access (CC0 Public Domain)",
            "formats": ["GLTF", "OBJ"],
            "description": "Millions of historical artifacts, dinosaur skeletons, and Apollo 11 command module digitized in millimeter accuracy.",
            "best_for": "Museum digital twins, educational spatial web apps, high-fidelity geometry",
            "integration_code": "// Access open access historical 3D models with full PBR textures"
        },
        {
            "name": "CGTrader Free 3D Repository",
            "url": "https://www.cgtrader.com/free-3d-models",
            "license": "Royalty-Free / Editorial",
            "formats": ["FBX", "OBJ", "MAX", "BLEND"],
            "description": "Over 100,000 free 3D models across automotive, architecture, nature, and consumer electronics.",
            "best_for": "Blender modeling, Unity/Unreal game development, architectural renders",
            "integration_code": "// Export from Blender to GLTF/GLB with Draco compression for web delivery"
        }
    ],
    "pbr_textures_and_materials": [
        {
            "name": "AmbientCG (Formerly CC0 Textures)",
            "url": "https://ambientcg.com",
            "license": "CC0 1.0 Universal (Public Domain)",
            "formats": ["PNG", "JPG", "SBSAR"],
            "description": "Over 2,000 photorealistic PBR materials up to 8K resolution with complete normal, roughness, displacement, and ambient occlusion maps.",
            "best_for": "Blender, Three.js, Unreal Engine, Godot photorealistic rendering",
            "integration_code": "// Three.js PBR Material loading Color, Normal and Roughness maps\nconst mat = new THREE.MeshStandardMaterial({ map: colorMap, normalMap: normMap, roughnessMap: roughMap });"
        },
        {
            "name": "Poly Haven Materials & HDRIs",
            "url": "https://polyhaven.com",
            "license": "CC0 1.0 Universal (100% Free Public Domain)",
            "formats": ["EXR", "HDR", "PNG"],
            "description": "Industry gold standard for uncompressed 32-bit HDR environmental maps and calibrated physical PBR scans.",
            "best_for": "Realistic image-based lighting (IBL) in WebGL and architectural rendering",
            "integration_code": "// RGBELoader in Three.js\nnew RGBELoader().load('polyhaven.hdr', (texture) => { texture.mapping = THREE.EquirectangularReflectionMapping; scene.environment = texture; });"
        },
        {
            "name": "ShareTextures",
            "url": "https://www.sharetextures.com",
            "license": "CC0 Public Domain",
            "formats": ["JPG", "PNG"],
            "description": "Over 1,200 architectural building materials: weathered concrete, modern wood flooring, subway tiles, and asphalt.",
            "best_for": "Architectural visualizations, urban simulations, clean-room WebGL",
            "integration_code": "// Direct CC0 tileable textures with zero attribution requirements"
        }
    ],
    "ui_component_and_animation_libraries": [
        {
            "name": "Lucide React Icons",
            "url": "https://lucide.dev",
            "license": "ISC License (100% Free Open Source)",
            "formats": ["SVG", "React Component", "Vue", "Web Component"],
            "description": "Modern, crisp, lightweight icon set with 1,400+ vector icons. Official community successor to Feather Icons.",
            "best_for": "S-Tier clean dashboards, linear-style command palettes, SaaS navigation",
            "integration_code": "import { ShieldCheck, Cpu, ArrowUpRight } from 'lucide-react';\n<ShieldCheck className=\"w-5 h-5 text-emerald-400\" />"
        },
        {
            "name": "Tabler Icons",
            "url": "https://tabler.io/icons",
            "license": "MIT License",
            "formats": ["SVG", "React", "Vue", "Figma"],
            "description": "Over 5,200 pixel-perfect vector icons with stroke-width customization and zero runtime dependencies.",
            "best_for": "High-density enterprise software, SCADA HUDs, medical portals",
            "integration_code": "import { IconTerminal2, IconBinaryTree } from '@tabler/icons-react';"
        },
        {
            "name": "Aceternity UI",
            "url": "https://ui.aceternity.com",
            "license": "MIT Open Source",
            "formats": ["React", "Framer Motion", "Tailwind CSS v4"],
            "description": "Trending modern landing page components: Bento grids, 3D pin cards, tracing beams, glowing borders, and particle canvases.",
            "best_for": "High-conversion developer tools, modern AI startup landing pages",
            "integration_code": "// Copy-and-paste Tailwind and Framer Motion animated components"
        },
        {
            "name": "LottieFiles Free Open Animations",
            "url": "https://lottiefiles.com/free-animations",
            "license": "Lottie Simple License / Free Commercial",
            "formats": ["JSON", "dotLottie"],
            "description": "Ultra-lightweight vector JSON micro-animations for success checkmarks, loading rings, empty states, and celebrations.",
            "best_for": "Delightful UX micro-interactions, mobile app confirmation dialogs",
            "integration_code": "import Lottie from 'lottie-react';\n<Lottie animationData={checkmarkAnimation} loop={false} />"
        },
        {
            "name": "Phosphor Icons",
            "url": "https://phosphoricons.com",
            "license": "MIT License",
            "formats": ["SVG", "React", "Vue", "Figma"],
            "description": "Flexible icon family with 6 distinct weight styles: Thin, Light, Regular, Bold, Fill, and Duotone.",
            "best_for": "S-Tier luxury and editorial layouts requiring custom icon weight hierarchy",
            "integration_code": "import { Lightning, Code } from '@phosphor-icons/react';\n<Lightning weight=\"duotone\" className=\"text-sky-400\" />"
        }
    ],
    "audio_sfx_and_soundtracks": [
        {
            "name": "FreeSound.org Collaborative Audio Archive",
            "url": "https://freesound.org",
            "license": "Creative Commons 0 / CC-BY",
            "formats": ["WAV", "MP3", "FLAC", "OGG"],
            "description": "World's largest collaborative database of over 500,000 royalty-free audio samples, UI foley, mechanical clicks, and ambient pads.",
            "best_for": "Tactile micro-interaction audio feedback, button clicks, notification chimes",
            "integration_code": "const audio = new Audio('https://freesound.org/data/previews/...mp3');\naudio.volume = 0.25; audio.play();"
        },
        {
            "name": "Sonniss GDC Audio Archive",
            "url": "https://sonniss.com/gameaudiogdc",
            "license": "100% Royalty-Free Commercial License",
            "formats": ["WAV (24-bit 96kHz)"],
            "description": "Over 150 Gigabytes of uncompressed Hollywood-grade sound effects: sci-fi telemetry, UI beeps, drones, mechanical switches.",
            "best_for": "Game audio engines, AAA sound design, WebAudio sound synthesis",
            "integration_code": "// Commercial game-grade sound packs free for personal and commercial projects"
        },
        {
            "name": "Kenney Audio Sound Kits",
            "url": "https://kenney.nl/assets/series:Audio",
            "license": "CC0 1.0 Universal (Public Domain)",
            "formats": ["OGG", "WAV"],
            "description": "Curated retro and modern UI sound effects: Digital Audio Pack, Interface Sounds, Casino Audio, Sci-Fi Sound Pack.",
            "best_for": "Sub-millisecond UI button chimes and gaming sound effects with zero attribution",
            "integration_code": "// Play short UI chime on successful form submission or button click"
        }
    ],
    "webgl_shaders_and_spatial_tools": [
        {
            "name": "ShaderToy GLSL Community",
            "url": "https://www.shadertoy.com",
            "license": "Creative Commons / Open Source",
            "formats": ["GLSL", "Fragment Shader"],
            "description": "World's leading procedural pixel shader repository. Ray-marching, volumetric clouds, generative noise, and fluid dynamics.",
            "best_for": "Custom Three.js ShaderMaterial, hero background visual effects",
            "integration_code": "// Convert ShaderToy fragment shader into Three.js ShaderMaterial uniform iTime and iResolution"
        },
        {
            "name": "The Book of Shaders",
            "url": "https://thebookofshaders.com",
            "license": "Open Educational Resource",
            "formats": ["GLSL", "WebGL"],
            "description": "Step-by-step guide and mathematical formula repository for generative algorithmic graphics (fractal brownian motion, voronoi, cellular noise).",
            "best_for": "Algorithmic procedural texture generation without downloading bitmap assets",
            "integration_code": "// Algorithmic noise functions implemented in pure GLSL"
        },
        {
            "name": "PMNDRS Drei (React Three Fiber Helpers)",
            "url": "https://github.com/pmndrs/drei",
            "license": "MIT Open Source",
            "formats": ["npm package", "TypeScript"],
            "description": "Essential collection of ready-to-use Three.js components: OrbitControls, Float, Center, Text3D, Sparkles, MeshReflectorMaterial, Sky.",
            "best_for": "Rapid production 3D web application development in React and Next.js",
            "integration_code": "import { Sparkles, Float, MeshReflectorMaterial } from '@react-three/drei';"
        }
    ]
}

def main():
    if not os.path.exists(VAULT_PATH):
        print(f"Error: {VAULT_PATH} not found")
        sys.exit(1)

    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = data.get("categories", {})
    added_count = 0

    for cat_name, asset_list in NEW_ASSETS.items():
        if cat_name not in categories:
            categories[cat_name] = []
        existing_names = {a["name"] for a in categories[cat_name]}
        for item in asset_list:
            if item["name"] not in existing_names:
                categories[cat_name].append(item)
                existing_names.add(item["name"])
                added_count += 1

    total_resources = sum(len(v) for v in categories.values())
    data["categories"] = categories
    data["total_resources"] = total_resources
    data["version"] = "2.0.0"

    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=================================================================")
    print(" FREE ASSETS & 3D VAULT GENISLETILDI (50+ HEDEFI)")
    print("=================================================================")
    print(f"[*] Toplam Kaynak Sayisi   : {total_resources} (+{added_count} yeni)")
    print(f"[*] Toplam Kategori Sayisi : {len(categories)}")
    print(f"[*] Kaydedildi: {VAULT_PATH}")

if __name__ == "__main__":
    main()

EXTRA_10_ASSETS = {
    "3d_models_and_meshes": [
        {
            "name": "OpenGameArt 3D Portal",
            "url": "https://opengameart.org/art-search-advanced?keys=&field_art_type_tid%5B%5D=10",
            "license": "CC0 / Open Source",
            "formats": ["BLEND", "OBJ", "FBX"],
            "description": "Massive community-driven repository of free 3D models, characters, weapons, and environmental props.",
            "best_for": "Indie game prototyping, open-source games, Godot/Unity assets",
            "integration_code": "// Free community 3D models with open-source licensing"
        },
        {
            "name": "Clara.io Free 3D Cloud Archive",
            "url": "https://clara.io/library",
            "license": "Royalty-Free / Public Domain",
            "formats": ["OBJ", "FBX", "STL"],
            "description": "Over 100,000 user-submitted 3D models across automotive, aerospace, architecture, and electronics.",
            "best_for": "Broad 3D asset variety and rapid concept modeling",
            "integration_code": "// Import into Blender and export as optimized web glTF"
        }
    ],
    "pbr_textures_and_materials": [
        {
            "name": "3DAssets.one Meta-Search Engine",
            "url": "https://3dassets.one",
            "license": "CC0 / Free",
            "formats": ["PNG", "JPG", "EXR"],
            "description": "Aggregated search engine indexing over 15,000 free, CC0 PBR textures, HDRIs, and 3D models across 12 independent sites.",
            "best_for": "Fastest discovery of specific materials (e.g. Damascus steel, brushed copper)",
            "integration_code": "// Meta-search across AmbientCG, Poly Haven, ShareTextures in one query"
        },
        {
            "name": "TextureCan PBR Library",
            "url": "https://www.texturecan.com",
            "license": "100% Free for Commercial Use",
            "formats": ["PNG 4K/2K"],
            "description": "High-quality realistic tileable materials: marble floors, rustic bricks, woven fabrics, and carbon fiber.",
            "best_for": "WebGL e-commerce 3D product visualizers and floorings",
            "integration_code": "// Standard PBR map set: diffuse, normal, roughness, displacement"
        }
    ],
    "ui_component_and_animation_libraries": [
        {
            "name": "Motion One by Matt Perry",
            "url": "https://motion.dev",
            "license": "MIT Open Source",
            "formats": ["npm package", "JavaScript"],
            "description": "The smallest, fastest Web Animations API (WAAPI) library on the web (under 3.8kb), outperforming traditional JS animation loops.",
            "best_for": "Hardware-accelerated mobile animations, spring physics, zero bundle bloat",
            "integration_code": "import { animate, spring } from 'motion';\nanimate(element, { scale: [0.95, 1] }, { easing: spring() });"
        },
        {
            "name": "Embla Carousel",
            "url": "https://www.embla-carousel.com",
            "license": "MIT License",
            "formats": ["npm package", "React", "Vue", "Svelte"],
            "description": "Lightweight, bare-bones carousel library with fluid spring physics and zero forced layout shifts.",
            "best_for": "Streaming service rails, hero banners, testimonial sliders",
            "integration_code": "import useEmblaCarousel from 'embla-carousel-react';\nconst [emblaRef] = useEmblaCarousel({ loop: true });"
        },
        {
            "name": "Sonner Toast Notification System",
            "url": "https://sonner.emilkowal.ski",
            "license": "MIT License",
            "formats": ["React", "TypeScript"],
            "description": "The definitive, opinionated, beautiful toast component for React with stacking animations and keyboard navigation.",
            "best_for": "S-Tier enterprise dashboards, transaction alerts, copy-to-clipboard chimes",
            "integration_code": "import { Toaster, toast } from 'sonner';\ntoast.success('İşlem başarıyla mühürlendi');"
        },
        {
            "name": "CMDK Command Menu Primitives",
            "url": "https://cmdk.paco.me",
            "license": "MIT Open Source",
            "formats": ["React Component", "TypeScript"],
            "description": "Fast, unstyled command menu React component used by Linear, Vercel, and Raycast Web.",
            "best_for": "Power-user keyboard navigation, instant command palettes",
            "integration_code": "import { Command } from 'cmdk';\n<Command.Input placeholder=\"Komut arayın...\" />"
        }
    ],
    "audio_sfx_and_soundtracks": [
        {
            "name": "Mixkit Royalty-Free Sound Effects",
            "url": "https://mixkit.co/free-sound-effects/",
            "license": "Mixkit Stock Music Free License",
            "formats": ["WAV", "MP3"],
            "description": "High-impact modern sound effects: glitch risers, digital swooshes, mouse clicks, and ambient game pads.",
            "best_for": "Web micro-interactions, explainer videos, portfolio motion design",
            "integration_code": "// Direct MP3 embed with zero attribution for commercial apps"
        },
        {
            "name": "BBC Sound Effects Archive",
            "url": "https://sound-effects.bbcrewind.co.uk",
            "license": "Personal, Educational & Research Free License",
            "formats": ["WAV", "FLAC"],
            "description": "Over 16,000 historical and modern sound recordings spanning a century of global broadcasting.",
            "best_for": "Atmospheric audio design, industrial ambient background tracks",
            "integration_code": "// Authentic acoustic soundscapes for immersive spatial simulations"
        }
    ]
}

def append_extra_10():
    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = data.get("categories", {})
    added = 0
    for cat_name, items in EXTRA_10_ASSETS.items():
        if cat_name not in categories:
            categories[cat_name] = []
        names = {x["name"] for x in categories[cat_name]}
        for it in items:
            if it["name"] not in names:
                categories[cat_name].append(it)
                names.add(it["name"])
                added += 1

    total = sum(len(v) for v in categories.values())
    data["categories"] = categories
    data["total_resources"] = total
    data["version"] = "2.2.0"

    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[*] Extra 10 Assets Appended. Total Vault Resources: {total}")

append_extra_10()
