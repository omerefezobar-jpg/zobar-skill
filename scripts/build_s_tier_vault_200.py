#!/usr/bin/env python3
"""
Builder script to expand S-Tier Design Vault to 200+ world-class digital products,
including heavy pro desktop powerhouses (Steam, Excel, Premiere Pro, Blender, VS Code, Ableton, UE5).
"""

import json
import os

VAULT_PATH = os.path.join(os.path.dirname(__file__), "..", "references", "s_tier_design_vault.json")

NEW_CATEGORIES = [
    {
        "category_name": "Heavy Pro Desktop & Creative Powerhouses",
        "design_paradigm": "Multi-Pane Workspace, Multi-Track Timelines, Virtualized Grids & GPU Shaders",
        "recommended_libraries": ["WebGPU / wgpu", "Canvas2D Virtualized Tiles", "Dockview / GoldenLayout", "Dear ImGui / Rust UI"],
        "sites": [
            {
                "name": "Steam (Valve)",
                "url": "https://store.steampowered.com",
                "hero_pattern": "Dynamic billboard trailer carousel with live community broadcast overlay and price discount badges",
                "component_features": "Collapsible game library tree, multi-pane download queue with disk/network charts, Steam Workshop mod browser, community review scorecards",
                "color_tokens": {"background": "#171A21", "accent": "#66C0F4", "text": "#C5C3C0"},
                "key_interactions": "Micro-hover video trailer scrubber, instant one-click install modal, friend activity toast animations"
            },
            {
                "name": "Microsoft Excel",
                "url": "https://www.microsoft.com/microsoft-365/excel",
                "hero_pattern": "Infinite 2D virtualized calculation grid with green ribbon header and live formula omnibar",
                "component_features": "Virtual tile renderer (1M+ rows), pivot table builder drawer, conditional formatting color scales, cell comment threads",
                "color_tokens": {"background": "#FFFFFF", "accent": "#107C41", "text": "#242424"},
                "key_interactions": "Cell marquee selection bounding box, drag-to-fill handle with autofill heuristics, formula autocomplete popover"
            },
            {
                "name": "Adobe Premiere Pro",
                "url": "https://www.adobe.com/products/premiere.html",
                "hero_pattern": "Multi-pane non-linear video editing workstation with audio VU meters and program monitor",
                "component_features": "Multi-track magnetic timeline, keyframe curve editor, Lumetri color grading wheel dials, effect controls inspector",
                "color_tokens": {"background": "#1E1E1E", "accent": "#9999FF", "text": "#D9D9D9"},
                "key_interactions": "Zero-latency timeline playhead scrubbing with J-K-L shuttle hotkeys, ripple edit drag"
            },
            {
                "name": "Blender",
                "url": "https://www.blender.org",
                "hero_pattern": "3D spatial viewport with real-time EEVEE/Cycles path-tracing and shader node editor",
                "component_features": "Outliner scene collection tree, nodal shader graph with spline connectors, timeline dopesheet, transform gizmo",
                "color_tokens": {"background": "#303030", "accent": "#E87D0D", "text": "#FFFFFF"},
                "key_interactions": "Interactive 3D transform gizmo (grab, rotate, scale) with numeric constraint hotkeys"
            },
            {
                "name": "DaVinci Resolve",
                "url": "https://www.blackmagicdesign.com/products/davinciresolve",
                "hero_pattern": "Hardware console color grading studio with dual monitors and waveform scopes",
                "component_features": "Node-based color grading graph, Fairlight audio mixer with 3D spatial panning, multi-source cut page",
                "color_tokens": {"background": "#181818", "accent": "#D8232A", "text": "#E0E0E0"},
                "key_interactions": "Color wheel vectorscope live feedback responding to mouse delta"
            },
            {
                "name": "Ableton Live",
                "url": "https://www.ableton.com/en/live/",
                "hero_pattern": "Dual-mode Session (Clip Launcher) and Arrangement (Timeline) digital audio workstation",
                "component_features": "Audio track vertical mixer channels, MIDI piano roll editor, effect chain device rack, clip slot launch matrix",
                "color_tokens": {"background": "#202020", "accent": "#FFDF34", "text": "#D5D5D5"},
                "key_interactions": "Quantized clip launching with synchronized tempo tap, automation lane curve pinching"
            },
            {
                "name": "Visual Studio Code (VS Code)",
                "url": "https://code.visualstudio.com",
                "hero_pattern": "Sleek developer code workspace with side-by-side editor groups and integrated terminal",
                "component_features": "Monaco editor with inline AST diagnostics, Git source control diff gutter, extension marketplace side panel",
                "color_tokens": {"background": "#1E1E1E", "accent": "#007ACC", "text": "#CCCCCC"},
                "key_interactions": "Multi-cursor editing (Alt+Click), quick open palette (Cmd+P), terminal split pane toggle"
            },
            {
                "name": "Unreal Engine 5",
                "url": "https://www.unrealengine.com",
                "hero_pattern": "Photorealistic 3D game engine editor with Nanite geometry and Lumen lighting viewports",
                "component_features": "Blueprint visual scripting node canvas, Content Drawer hotkey browser, World Outliner, Details panel",
                "color_tokens": {"background": "#121212", "accent": "#0E86D4", "text": "#FAFAFA"},
                "key_interactions": "Real-time game simulation possess mode (Play-in-Editor), Blueprint wire dragging with auto-cast"
            },
            {
                "name": "Adobe Photoshop",
                "url": "https://www.adobe.com/products/photoshop.html",
                "hero_pattern": "Raster graphics canvas with floating tool palette and layer blend mode controls",
                "component_features": "Layer hierarchy tree with masks and clipping groups, generative fill prompt bar, history state stack",
                "color_tokens": {"background": "#262626", "accent": "#31A8FF", "text": "#EBEBEB"},
                "key_interactions": "Pressure-sensitive brush dynamics on canvas, contextual task bar floating beneath selection"
            },
            {
                "name": "Final Cut Pro",
                "url": "https://www.apple.com/final-cut-pro/",
                "hero_pattern": "Magnetic Timeline video editor with Metal-optimized background rendering",
                "component_features": "Magnetic timeline preventing clip collision, skimming playhead with audio scrubbing, color inspector",
                "color_tokens": {"background": "#1C1C1E", "accent": "#0A84FF", "text": "#F2F2F7"},
                "key_interactions": "Magnetic clip snap automatically rippling adjacent b-roll tracks"
            },
            {
                "name": "AutoCAD",
                "url": "https://www.autodesk.com/products/autocad",
                "hero_pattern": "Precision 2D/3D CAD drafting canvas with crosshair cursor and command line prompt",
                "component_features": "Layer state manager, precision dimensioning tools, model/layout space tabs, block library palette",
                "color_tokens": {"background": "#212121", "accent": "#E51937", "text": "#FFFFFF"},
                "key_interactions": "Object snap (OSNAP) magnetic targeting to endpoints, midpoints, and tangents"
            },
            {
                "name": "Unity Editor",
                "url": "https://unity.com",
                "hero_pattern": "Cross-platform game creation suite with hierarchical scene tree and live game preview",
                "component_features": "Component-based GameObject inspector, Project asset browser, Animator state machine graph, profiler",
                "color_tokens": {"background": "#222222", "accent": "#000000", "text": "#C4C4C4"},
                "key_interactions": "Drag-and-drop C# scripts onto GameObjects, live tweaking parameters during Play mode"
            },
            {
                "name": "FL Studio",
                "url": "https://www.image-line.com/fl-studio/",
                "hero_pattern": "Pattern-based step sequencer with vector piano roll and multi-bus mixer",
                "component_features": "Step sequencer grid, advanced piano roll with slide notes, fruity wrapper plugin host, playlist arranger",
                "color_tokens": {"background": "#2D3238", "accent": "#F67A18", "text": "#E8E8E8"},
                "key_interactions": "Left-click to paint notes, right-click to slice/erase in piano roll"
            },
            {
                "name": "Cinema 4D",
                "url": "https://www.maxon.net/cinema-4d",
                "hero_pattern": "Motion graphics 3D studio with MoGraph procedural cloner and Redshift GPU renderer",
                "component_features": "Object manager hierarchy, MoGraph field effectors, nodal material system, attribute manager",
                "color_tokens": {"background": "#2E2E2E", "accent": "#0055FF", "text": "#EDEDED"},
                "key_interactions": "Procedural field visualizer displaying animated falloff in viewport"
            },
            {
                "name": "Substance 3D Painter",
                "url": "https://www.adobe.com/products/substance3d-painter.html",
                "hero_pattern": "3D PBR texture painting studio with multi-channel viewport (BaseColor, Metallic, Roughness, Normal)",
                "component_features": "Layer stack with smart materials, shelf asset browser with search, baker modal",
                "color_tokens": {"background": "#232323", "accent": "#FF4B4B", "text": "#DFDFDF"},
                "key_interactions": "Direct painting onto 3D mesh surface with real-time UV unwrapped projection"
            }
        ]
    },
    {
        "category_name": "Gaming, Esports & Game Launchers",
        "design_paradigm": "High-Contrast Gamer UI, Real-Time Stats & Interactive Tournaments",
        "recommended_libraries": ["Tailwind CSS v4", "Framer Motion", "Recharts", "Lucide React"],
        "sites": [
            {
                "name": "Epic Games Store",
                "url": "https://store.epicgames.com",
                "hero_pattern": "Weekly free game countdown billboard with full-bleed key art and instant claim button",
                "component_features": "Seasonal sale carousel, library download progress bar, developer publishing portal",
                "color_tokens": {"background": "#121212", "accent": "#0078F2", "text": "#F5F5F5"},
                "key_interactions": "Claim free game one-click overlay without opening payment modal"
            },
            {
                "name": "Riot Games (League Client)",
                "url": "https://www.riotgames.com",
                "hero_pattern": "Animated Hextech golden client border with champion lock-in cinematic",
                "component_features": "Champion select draft phase countdown, rune page builder, end-of-game damage graphs",
                "color_tokens": {"background": "#010A13", "accent": "#C8AA6E", "text": "#F0E6D2"},
                "key_interactions": "Hextech lock-in sound and particle flare animation on champion click"
            },
            {
                "name": "Battle.net",
                "url": "https://battle.net",
                "hero_pattern": "Franchise brand selector rail (Warcraft, Overwatch, Diablo, StarCraft) with live news feed",
                "component_features": "Game update scanner bar, cross-game friends list with status tags, patch note drawer",
                "color_tokens": {"background": "#141721", "accent": "#00AEFF", "text": "#D9E3ED"},
                "key_interactions": "Play button glowing state when game update download completes"
            },
            {
                "name": "itch.io",
                "url": "https://itch.io",
                "hero_pattern": "Indie game jam showcase with pixel-art badges and community creator cards",
                "component_features": "Game jam leaderboard, pay-what-you-want donation slider, in-browser HTML5 game runner",
                "color_tokens": {"background": "#FA5C5C", "accent": "#222222", "text": "#FFFFFF"},
                "key_interactions": "Instant in-browser WebGL game launch in sandboxed iframe"
            },
            {
                "name": "GOG Galaxy",
                "url": "https://www.gog.com/galaxy",
                "hero_pattern": "Universal game launcher uniting Steam, Epic, and console libraries under DRM-free philosophy",
                "component_features": "Multi-platform library consolidator, cross-platform playtime tracking, custom game tags",
                "color_tokens": {"background": "#1C142B", "accent": "#9F5EE7", "text": "#FFFFFF"},
                "key_interactions": "Filtering games across all platforms simultaneously with single click"
            },
            {
                "name": "Roblox Studio",
                "url": "https://create.roblox.com",
                "hero_pattern": "Experience creator portal with monetized game metrics and marketplace models",
                "component_features": "3D asset toolbox with instant preview, Lua scripting editor, live server analytics chart",
                "color_tokens": {"background": "#191B1D", "accent": "#00A2FF", "text": "#FFFFFF"},
                "key_interactions": "One-click experience publish pushing live build to millions of mobile/PC players"
            },
            {
                "name": "Liquipedia",
                "url": "https://liquipedia.net",
                "hero_pattern": "Esports tournament bracket tree with live match scores and hero pick/ban statistics",
                "component_features": "Interactive tournament double-elimination brackets, player transfer timeline, live match ticker",
                "color_tokens": {"background": "#121921", "accent": "#0084FF", "text": "#E1E1E1"},
                "key_interactions": "Hovering tournament match node highlights progression path through bracket"
            },
            {
                "name": "HLTV",
                "url": "https://www.hltv.org",
                "hero_pattern": "Counter-Strike live match scorecard with live round-by-round kill feed and player ratings",
                "component_features": "Player ADR/KAST radar charts, world ranking leaderboard, demo download links",
                "color_tokens": {"background": "#292E36", "accent": "#3E82B8", "text": "#FFFFFF"},
                "key_interactions": "Clicking match round reveals 2D map replay showing player movement"
            },
            {
                "name": "Speedrun.com",
                "url": "https://www.speedrun.com",
                "hero_pattern": "World record leaderboard with verified video proof links and milliseconds timing",
                "component_features": "Game subcategory tabs (Any%, 100%, Glitchless), submission verification queue, runner profiles",
                "color_tokens": {"background": "#1F232D", "accent": "#2EB574", "text": "#FFFFFF"},
                "key_interactions": "Hovering world record shows runner's split comparison against personal best"
            },
            {
                "name": "EA App",
                "url": "https://www.ea.com",
                "hero_pattern": "Modern dark gamer hub with EA Play subscription benefits and friend activity feed",
                "component_features": "Game library with playtime counter, automatic background game repairs, cloud save sync",
                "color_tokens": {"background": "#161616", "accent": "#FF4747", "text": "#FFFFFF"},
                "key_interactions": "Quick launch overlay popping up from Windows taskbar tray"
            },
            {
                "name": "Ubisoft Connect",
                "url": "https://ubisoftconnect.com",
                "hero_pattern": "Ubisoft club reward dashboard with badge unlock notifications and stats comparison",
                "component_features": "Cross-progression sync indicator, in-game overlay browser, units loyalty shop",
                "color_tokens": {"background": "#000B1A", "accent": "#0070FF", "text": "#FFFFFF"},
                "key_interactions": "Redeeming Ubisoft units for in-game skin directly from desktop launcher"
            }
        ]
    },
    {
        "category_name": "Enterprise Data, Analytics & BI",
        "design_paradigm": "High-Density Timeseries, SQL Workbenches & Interactive BI Visualizers",
        "recommended_libraries": ["Apache ECharts", "D3.js", "TanStack Table", "Monaco Editor"],
        "sites": [
            {
                "name": "Snowflake",
                "url": "https://www.snowflake.com",
                "hero_pattern": "Data Cloud telemetry overview with real-time compute credit warehouse consumption",
                "component_features": "Snowsight SQL worksheet with multi-query tabs, auto-generated data charts, data marketplace catalog",
                "color_tokens": {"background": "#FFFFFF", "accent": "#29B5E8", "text": "#1A2433"},
                "key_interactions": "Executing SQL query dynamically renders column distribution histogram in results drawer"
            },
            {
                "name": "Palantir Foundry",
                "url": "https://www.palantir.com",
                "hero_pattern": "Enterprise ontology management canvas linking business objects to data pipelines",
                "component_features": "Pipeline Builder visual DAG, Contour data exploration sheets, Workshop low-code app builder",
                "color_tokens": {"background": "#101214", "accent": "#1473E6", "text": "#F5F5F5"},
                "key_interactions": "Clicking an ontology object expands its entire upstream and downstream dependency graph"
            },
            {
                "name": "Tableau",
                "url": "https://www.tableau.com",
                "hero_pattern": "Drag-and-drop visual analytics canvas with dimensions and measures shelves",
                "component_features": "Show Me chart recommendation matrix, dashboard storyboard builder, geographic map visualizer",
                "color_tokens": {"background": "#FFFFFF", "accent": "#E97627", "text": "#2B2B2B"},
                "key_interactions": "Dragging a measure onto color shelf immediately updates all chart mark hues"
            },
            {
                "name": "Grafana Labs",
                "url": "https://grafana.com",
                "hero_pattern": "Real-time infrastructure observability dashboard with dark-mode time-series heatmaps",
                "component_features": "PromQL/LogQL query editor, synchronized crosshair across multi-panels, alert rule creator modal",
                "color_tokens": {"background": "#111217", "accent": "#F47A20", "text": "#CCCCDC"},
                "key_interactions": "Clicking and dragging on any chart zooms all dashboard panels to that identical time slice"
            },
            {
                "name": "Metabase",
                "url": "https://www.metabase.com",
                "hero_pattern": "User-friendly query builder allowing non-technical teams to ask questions about data",
                "component_features": "Visual notebook query builder, automated x-ray exploration charts, dashboard auto-refresh toggle",
                "color_tokens": {"background": "#FFFFFF", "accent": "#509EE3", "text": "#34495E"},
                "key_interactions": "Clicking any table cell opens instant drill-down menu (filter, break out, view details)"
            },
            {
                "name": "Looker (Google Cloud)",
                "url": "https://cloud.google.com/looker",
                "hero_pattern": "LookML governed data model modeling layer powering company-wide dashboards",
                "component_features": "Explore data builder, scheduled report email dispatcher, embedded analytics SDKs",
                "color_tokens": {"background": "#F8F9FA", "accent": "#4285F4", "text": "#202124"},
                "key_interactions": "Pivoting data dimensions in real-time with automatic table calculation generation"
            },
            {
                "name": "Mixpanel",
                "url": "https://mixpanel.com",
                "hero_pattern": "Product event funnel conversion analysis with drop-off percentage markers",
                "component_features": "Retention cohort heatmaps, user journey flow trees, event attribute breakdowns",
                "color_tokens": {"background": "#14151B", "accent": "#7856FF", "text": "#FFFFFF"},
                "key_interactions": "Clicking any funnel drop-off bar immediately filters to inspect those specific user profiles"
            },
            {
                "name": "PostHog",
                "url": "https://posthog.com",
                "hero_pattern": "Open-source all-in-one product analytics with retro-hedgehog illustrations and session replays",
                "component_features": "DOM session recording player with network/console logs, feature flag manager, A/B test calculator",
                "color_tokens": {"background": "#F3EFE0", "accent": "#F54E00", "text": "#1D1F25"},
                "key_interactions": "Watching user session replay with automatic skip of inactivity periods"
            },
            {
                "name": "Amplitude",
                "url": "https://amplitude.com",
                "hero_pattern": "Digital analytics platform measuring user behavioral cohorts and product growth loops",
                "component_features": "Pathfinder user flow graphs, Compass correlation calculator, synchronized data table",
                "color_tokens": {"background": "#0D1126", "accent": "#185BFF", "text": "#FFFFFF"},
                "key_interactions": "Cohort creation directly from anomalous datapoints in a chart"
            },
            {
                "name": "Dune Analytics",
                "url": "https://dune.com",
                "hero_pattern": "Community crypto analytics with shared SQL queries and live blockchain charts",
                "component_features": "SQL editor querying multi-chain schemas, dashboard fork button, embeddable iframe charts",
                "color_tokens": {"background": "#0F1114", "accent": "#FF6838", "text": "#FFFFFF"},
                "key_interactions": "One-click 'Fork Query' allowing instant editing and customizing of complex SQL visualizers"
            },
            {
                "name": "Hex",
                "url": "https://hex.tech",
                "hero_pattern": "Collaborative data science workspace combining Python, SQL, and interactive UI inputs",
                "component_features": "DAG notebook dependency graph, slider/dropdown input widgets, published app view",
                "color_tokens": {"background": "#0D0E11", "accent": "#A855F7", "text": "#F3F4F6"},
                "key_interactions": "Changing a UI slider immediately re-runs only the downstream dependent Python cells"
            },
            {
                "name": "Observable",
                "url": "https://observablehq.com",
                "hero_pattern": "Reactive JavaScript data visualization notebook canvas by Mike Bostock",
                "component_features": "D3.js visualization sandbox, reactive cell evaluation, SVG export controls",
                "color_tokens": {"background": "#FFFFFF", "accent": "#3B5FC0", "text": "#222222"},
                "key_interactions": "Real-time reactive D3 chart morphing as code parameters are edited"
            }
        ]
    },
    {
        "category_name": "Heavy Grid & Spreadsheet Operating Systems",
        "design_paradigm": "Relational Tables, Kanban Boards & Multi-View Database Canvases",
        "recommended_libraries": ["TanStack Table", "Gridstack.js", "Handsontable", "Radix Popover"],
        "sites": [
            {
                "name": "Airtable",
                "url": "https://www.airtable.com",
                "hero_pattern": "Colorful relational database spreadsheet with linked records and automated workflows",
                "component_features": "Multi-view switcher (Grid, Calendar, Kanban, Gallery, Gantt), linked record expansion modal, field type picker",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FCB400", "text": "#1A1A1A"},
                "key_interactions": "Clicking linked record pill opens full relational sub-table record drawer"
            },
            {
                "name": "Google Sheets",
                "url": "https://sheets.google.com",
                "hero_pattern": "Collaborative cloud spreadsheet with real-time multi-colored cell focus markers",
                "component_features": "Formula suggestion bar, explore panel with automatic pivot tables, revision history drawer",
                "color_tokens": {"background": "#FFFFFF", "accent": "#0F9D58", "text": "#202124"},
                "key_interactions": "Real-time co-author cursor presence displaying name tag above active cell"
            },
            {
                "name": "Coda",
                "url": "https://coda.io",
                "hero_pattern": "All-in-one doc combining documents, spreadsheets, and interactive action buttons",
                "component_features": "Interactive push buttons inside table rows, Pack integrations (Slack/GitHub/Figma), formulas in canvas",
                "color_tokens": {"background": "#FFFFFF", "accent": "#F85631", "text": "#222222"},
                "key_interactions": "Clicking an in-cell button executes live API webhook (e.g. sends Slack notification)"
            },
            {
                "name": "Rows",
                "url": "https://rows.com",
                "hero_pattern": "Modern spreadsheet with built-in integrations to social and finance APIs without code",
                "component_features": "Data enrichment actions inside cells, publishable interactive calculators, AI formula assistant",
                "color_tokens": {"background": "#FFFFFF", "accent": "#000000", "text": "#111111"},
                "key_interactions": "Instant conversion of table block into an embeddable customer-facing widget"
            },
            {
                "name": "Smartsheet",
                "url": "https://www.smartsheet.com",
                "hero_pattern": "Enterprise work management grid with critical path dependency arrows and Gantt schedules",
                "component_features": "Gantt timeline bar dragging, automated approval request workflows, resource utilization view",
                "color_tokens": {"background": "#002B49", "accent": "#0073EC", "text": "#FFFFFF"},
                "key_interactions": "Dragging Gantt dependency connector between tasks adjusts downstream deadlines"
            },
            {
                "name": "Equals",
                "url": "https://equals.com",
                "hero_pattern": "Next-generation spreadsheet connected directly to live SQL databases with automated versioning",
                "component_features": "SQL query block inside spreadsheet, automatic daily data snapshot history, formula autocomplete",
                "color_tokens": {"background": "#0A0B0E", "accent": "#38BDF8", "text": "#F8FAFC"},
                "key_interactions": "One-click refresh pulling live data from Snowflake/Postgres directly into formulas"
            },
            {
                "name": "Retool",
                "url": "https://retool.com",
                "hero_pattern": "Internal tool builder canvas with drag-and-drop table, form, and chart components",
                "component_features": "Component property inspector, JavaScript query transformer, database CRUD connectors",
                "color_tokens": {"background": "#FFFFFF", "accent": "#3C82F6", "text": "#1F2937"},
                "key_interactions": "Connecting an SQL query to a Table component with one-line `{{ query.data }}`"
            },
            {
                "name": "Monday.com",
                "url": "https://monday.com",
                "hero_pattern": "High-color work operating system board with pulse status columns and progress bars",
                "component_features": "Color-coded status dropdowns, workload capacity widgets, customizable dashboard boards",
                "color_tokens": {"background": "#FFFFFF", "accent": "#0073EA", "text": "#323338"},
                "key_interactions": "Status dropdown change triggering celebratory confetti and notifying board subscribers"
            },
            {
                "name": "ClickUp",
                "url": "https://clickup.com",
                "hero_pattern": "All-in-one productivity suite with Space/Folder/List hierarchy and custom fields",
                "component_features": "Everything view aggregating tasks across organization, Whiteboard canvas, mindmaps",
                "color_tokens": {"background": "#FFFFFF", "accent": "#7B68EE", "text": "#24223E"},
                "key_interactions": "Instant view toggle between List, Board, Box, Calendar, and Mind Map without re-querying"
            },
            {
                "name": "Basecamp",
                "url": "https://basecamp.com",
                "hero_pattern": "Calm project communication hub with Campfire chat, Message Board, and Hill Charts",
                "component_features": "Hill Charts visual progress tracking, To-do lists with assignees, automatic check-in questions",
                "color_tokens": {"background": "#FFFFFF", "accent": "#283C46", "text": "#222222"},
                "key_interactions": "Dragging progress dots up and over the 'Hill' to represent problem understanding vs execution"
            }
        ]
    },
    {
        "category_name": "Luxury, Architecture & Industrial Design",
        "design_paradigm": "Minimalist High-Contrast, Large Typography & Precision Detailing",
        "recommended_libraries": ["Lenis Smooth Scroll", "Split-Type", "Tailwind CSS v4", "Three.js"],
        "sites": [
            {
                "name": "Porsche",
                "url": "https://www.porsche.com",
                "hero_pattern": "3D interactive vehicle configurator with photorealistic lighting environments",
                "component_features": "Personalization engine (stitching, brake calipers, rims), engine sound acoustic simulator",
                "color_tokens": {"background": "#FFFFFF", "accent": "#D5001C", "text": "#000000"},
                "key_interactions": "Engine start button playing real recorded exhaust sound of selected 911 model"
            },
            {
                "name": "Rimowa",
                "url": "https://www.rimowa.com",
                "hero_pattern": "Grooved aluminum suitcase industrial showcase with tactile materials",
                "component_features": "Aluminum luggage customizer (wheels, handles, luggage tag), personalization monogrammer",
                "color_tokens": {"background": "#F6F6F6", "accent": "#000000", "text": "#111111"},
                "key_interactions": "360-degree smooth spin of metallic luggage reflecting studio light"
            },
            {
                "name": "Leica Camera",
                "url": "https://leica-camera.com",
                "hero_pattern": "Legendary red dot photography exhibition with ultra-high dynamic range gallery",
                "component_features": "Camera lens focal length comparison slider, optical schematic cross-sections, master photographer essays",
                "color_tokens": {"background": "#000000", "accent": "#E30613", "text": "#FFFFFF"},
                "key_interactions": "Interactive lens aperture simulator showing depth-of-field bokeh changes"
            },
            {
                "name": "Bang & Olufsen",
                "url": "https://www.bang-olufsen.com",
                "hero_pattern": "Acoustic craftsmanship showcase with tactile wood, aluminum, and fabric acoustic grilles",
                "component_features": "Room placement sound visualizer, modular speaker configuration builder, AR camera preview",
                "color_tokens": {"background": "#F5F5F3", "accent": "#000000", "text": "#1A1A1A"},
                "key_interactions": "Audio acoustic beam direction interactive visualization"
            },
            {
                "name": "Polestar",
                "url": "https://www.polestar.com",
                "hero_pattern": "Scandinavian minimalist electric vehicle design with clean typography and zero clutter",
                "component_features": "Carbon emissions lifecycle transparency meter, Google built-in infotainment simulator",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF7500", "text": "#000000"},
                "key_interactions": "Smooth camera track zooming into battery pack engineering architecture"
            },
            {
                "name": "Vitra",
                "url": "https://www.vitra.com",
                "hero_pattern": "Architectural furniture catalog featuring Eames and modern workspace classics",
                "component_features": "Material textile swatch selector, 3D AR room model viewer, designer biography links",
                "color_tokens": {"background": "#FFFFFF", "accent": "#E30613", "text": "#1D1D1B"},
                "key_interactions": "Texture zoom lens revealing grain of molded plywood and leather stitching"
            },
            {
                "name": "Herman Miller",
                "url": "https://www.hermanmiller.com",
                "hero_pattern": "Aeron ergonomic chair engineering breakdown showing PostureFit sacral support",
                "component_features": "Ergonomic chair sizing guide, adjustment video tutorials, office space planner 3D",
                "color_tokens": {"background": "#FFFFFF", "accent": "#ED1C24", "text": "#252525"},
                "key_interactions": "Interactive anatomy points highlighting spinal pressure relief"
            },
            {
                "name": "Arc'teryx",
                "url": "https://arcteryx.com",
                "hero_pattern": "Extreme alpine weather apparel showcase with waterproof membrane testing visuals",
                "component_features": "GORE-TEX layer visualizer, activity condition filter (Climbing, Skiing, Trail), size fit chart",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#E6E6E6"},
                "key_interactions": "Thermal layer cutaway animation showing stormproof seam construction"
            },
            {
                "name": "Moncler",
                "url": "https://www.moncler.com",
                "hero_pattern": "High-fashion puffer luxury runway showcase with bold editorial photography",
                "component_features": "Down density warmth gauge, Genius designer collaboration gallery, boutique appointment scheduler",
                "color_tokens": {"background": "#FFFFFF", "accent": "#001E62", "text": "#000000"},
                "key_interactions": "Full-screen video loop transitioning smoothly into product purchase drawer"
            },
            {
                "name": "Rolex",
                "url": "https://www.rolex.com",
                "hero_pattern": "Oyster Perpetual horology showcase with sweeping second-hand mechanical physics",
                "component_features": "Chronometer movement cutaway, gold alloy foundry specifications, dial configurator",
                "color_tokens": {"background": "#0C1B14", "accent": "#006039", "text": "#FFFFFF"},
                "key_interactions": "Continuous sweeping motion of watch second hand synced to user's real-time computer clock"
            }
        ]
    },
    {
        "category_name": "Developer Platforms, Cloud & Modern APIs",
        "design_paradigm": "Interactive API Explorers, Real-Time Request Logs & Key Management",
        "recommended_libraries": ["Shadcn/ui", "Lucide React", "PrismJS", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Postman",
                "url": "https://www.postman.com",
                "hero_pattern": "Collaborative API client with environment variable selector and HTTP verb dropdown",
                "component_features": "Request headers key-value table, response body JSON viewer with search, collection runner",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF6C37", "text": "#212121"},
                "key_interactions": "Send button triggering status code 200 badge and timing waterfall graph"
            },
            {
                "name": "Insomnia",
                "url": "https://insomnia.rest",
                "hero_pattern": "Streamlined GraphQL and REST client with lightweight dark theme",
                "component_features": "GraphQL schema documentation explorer, cookie jar manager, environment switcher",
                "color_tokens": {"background": "#2E1C44", "accent": "#5849BE", "text": "#FFFFFF"},
                "key_interactions": "Instant GraphQL auto-completion based on introspected schema"
            },
            {
                "name": "Docker",
                "url": "https://www.docker.com",
                "hero_pattern": "Containerization platform hero with interactive Dockerfile command visualizer",
                "component_features": "Docker Desktop container resource monitor (CPU/Memory gauges), image layer inspector",
                "color_tokens": {"background": "#FFFFFF", "accent": "#2496ED", "text": "#1D272B"},
                "key_interactions": "One-click container restart button with animated status ring"
            },
            {
                "name": "Kubernetes",
                "url": "https://kubernetes.io",
                "hero_pattern": "Container orchestration documentation portal with YAML declarative manifests",
                "component_features": "Interactive Pod/Service/Ingress architecture diagrams, cluster command reference cards",
                "color_tokens": {"background": "#326CE5", "accent": "#FFFFFF", "text": "#FFFFFF"},
                "key_interactions": "Copy kubectl command button with immediate shell syntax feedback"
            },
            {
                "name": "Neon",
                "url": "https://neon.tech",
                "hero_pattern": "Serverless Postgres with instant database branching and scale-to-zero compute",
                "component_features": "Visual Git-like database branch tree, point-in-time restore slider, connection string drawer",
                "color_tokens": {"background": "#00E599", "accent": "#000000", "text": "#000000"},
                "key_interactions": "Creating instant isolated child branch of production database in under 500ms"
            },
            {
                "name": "Turso (LibSQL)",
                "url": "https://turso.tech",
                "hero_pattern": "Edge SQLite database with microsecond read latency across 35 global locations",
                "component_features": "Global replication map, database shell CLI runner, usage analytics graph",
                "color_tokens": {"background": "#14151A", "accent": "#4FF8D2", "text": "#FFFFFF"},
                "key_interactions": "Real-time query execution in web shell displaying execution time in milliseconds"
            },
            {
                "name": "Upstash",
                "url": "https://upstash.com",
                "hero_pattern": "Serverless Redis and Kafka with per-request pricing and zero cold starts",
                "component_features": "REST API cURL generator, live memory usage gauge, rate-limiting rule builder",
                "color_tokens": {"background": "#000000", "accent": "#00E699", "text": "#FFFFFF"},
                "key_interactions": "Interactive Redis CLI widget executing PING and SET/GET commands"
            },
            {
                "name": "Resend",
                "url": "https://resend.com",
                "hero_pattern": "Modern email API for developers with React email previews and high deliverability",
                "component_features": "Live HTML/React email split-screen editor, delivery event webhook stream, domain DNS checklist",
                "color_tokens": {"background": "#000000", "accent": "#FFFFFF", "text": "#FFFFFF"},
                "key_interactions": "Toggling between Mobile and Desktop email preview with smooth frame resizing"
            },
            {
                "name": "Clerk",
                "url": "https://clerk.com",
                "hero_pattern": "Complete user authentication suite with drop-in React components and session management",
                "component_features": "User profile modal preview, multi-factor auth (MFA) setup flow, social login buttons",
                "color_tokens": {"background": "#131316", "accent": "#6C47FF", "text": "#FFFFFF"},
                "key_interactions": "Live theme customization preview updating sign-in modal in real-time"
            },
            {
                "name": "Auth0",
                "url": "https://auth0.com",
                "hero_pattern": "Enterprise identity platform with customizable login flows and universal directory",
                "component_features": "Single Sign-On (SSO) configuration wizard, attack protection anomaly meters, tenant switcher",
                "color_tokens": {"background": "#000000", "accent": "#EB5424", "text": "#FFFFFF"},
                "key_interactions": "Drag-and-drop Actions trigger flow for post-login scripts"
            },
            {
                "name": "Algolia",
                "url": "https://www.algolia.com",
                "hero_pattern": "Instant search-as-you-type search bar demonstrating sub-10ms response times",
                "component_features": "Search index configuration rules, synonym management modal, relevance score simulator",
                "color_tokens": {"background": "#FFFFFF", "accent": "#003DFF", "text": "#21243D"},
                "key_interactions": "Typing keystroke instantaneously highlighting matching query substrings in results"
            },
            {
                "name": "Sentry",
                "url": "https://sentry.io",
                "hero_pattern": "Application performance monitoring with actionable stack traces and issue grouping",
                "component_features": "Interactive stack trace with source map resolution, breadcrumb user event timeline, alert rule builder",
                "color_tokens": {"background": "#1E1A29", "accent": "#362D59", "text": "#FFFFFF"},
                "key_interactions": "Clicking an issue unfolds the exact code line, commit blame, and preceding user clicks"
            }
        ]
    },
    {
        "category_name": "Security, Identity & Cloud Operations",
        "design_paradigm": "Zero-Trust Dashboards, Credential Vaults & Audit Log Streams",
        "recommended_libraries": ["Shadcn/ui Data Table", "Radix Dialog", "Lucide React", "Recharts"],
        "sites": [
            {
                "name": "1Password",
                "url": "https://1password.com",
                "hero_pattern": "Encrypted digital vault showcasing password health score and Watchtower alerts",
                "component_features": "Biometric unlock simulation, compromised credential alert badge, one-time sharing link generator",
                "color_tokens": {"background": "#0B1A2C", "accent": "#0572EC", "text": "#FFFFFF"},
                "key_interactions": "Password generator slider dynamically evaluating entropy bits and estimated crack time"
            },
            {
                "name": "Bitwarden",
                "url": "https://bitwarden.com",
                "hero_pattern": "Open source password manager with transparent zero-knowledge encryption architecture",
                "component_features": "Item type switcher (Login, Card, Identity, Secure Note), organization collection tree",
                "color_tokens": {"background": "#FFFFFF", "accent": "#175DDC", "text": "#212529"},
                "key_interactions": "Instant copy password button with auto-clearing clipboard countdown"
            },
            {
                "name": "CrowdStrike",
                "url": "https://www.crowdstrike.com",
                "hero_pattern": "Falcon cyber threat intelligence graph with real-time adversary tracking and kill-chain analysis",
                "component_features": "Endpoint detection incident tree, automated quarantine action pill, threat actor dossiers",
                "color_tokens": {"background": "#141414", "accent": "#FC0000", "text": "#FFFFFF"},
                "key_interactions": "Interactive attack timeline showing process tree execution branch"
            },
            {
                "name": "Tailscale",
                "url": "https://tailscale.com",
                "hero_pattern": "Zero-config WireGuard mesh VPN connecting devices with simple IP addresses",
                "component_features": "Device list with MagicDNS names, ACL policy JSON editor, exit node toggle switches",
                "color_tokens": {"background": "#FFFFFF", "accent": "#2D3748", "text": "#1A202C"},
                "key_interactions": "Toggling an exit node instantly animates the mesh network routing topology"
            },
            {
                "name": "Wiz",
                "url": "https://www.wiz.io",
                "hero_pattern": "Cloud security risk graph connecting vulnerabilities, misconfigurations, and identity exposures",
                "component_features": "Toxic combination toxic risk badges, cloud asset inventory graph, compliance posture score",
                "color_tokens": {"background": "#000B26", "accent": "#0073FF", "text": "#FFFFFF"},
                "key_interactions": "Clicking a critical risk opens graph path showing internet-to-database attack route"
            },
            {
                "name": "WireGuard",
                "url": "https://www.wireguard.com",
                "hero_pattern": "Minimalist ultra-fast cryptographic network tunnel with C codebase simplicity",
                "component_features": "Cryptographic key exchange code snippet, benchmark performance comparison matrix",
                "color_tokens": {"background": "#FFFFFF", "accent": "#88171A", "text": "#000000"},
                "key_interactions": "Copy configuration file template button"
            },
            {
                "name": "Cloudflare Zero Trust",
                "url": "https://one.dash.cloudflare.com",
                "hero_pattern": "Secure access service edge (SASE) dashboard with real-time blocked threat analytics",
                "component_features": "Access application launcher, device posture verification rules, gateway DNS policy builder",
                "color_tokens": {"background": "#1F1F1F", "accent": "#F6821F", "text": "#FFFFFF"},
                "key_interactions": "Filter threat logs by geography with dynamic world map highlight"
            },
            {
                "name": "Palo Alto Networks",
                "url": "https://www.paloaltonetworks.com",
                "hero_pattern": "Next-generation firewall security operations center with AI-driven threat mitigation",
                "component_features": "Security policy rule table, network bandwidth utilization waterfall, SOC alert feed",
                "color_tokens": {"background": "#0A0B0D", "accent": "#FA582D", "text": "#FFFFFF"},
                "key_interactions": "Drill down from high-level enterprise risk gauge into individual packet sessions"
            },
            {
                "name": "Splunk",
                "url": "https://www.splunk.com",
                "hero_pattern": "Security Information and Event Management (SIEM) log search bar with SPL processing syntax",
                "component_features": "Search processing language (SPL) bar, log histogram timeline, event detail drawer",
                "color_tokens": {"background": "#000000", "accent": "#E82163", "text": "#FFFFFF"},
                "key_interactions": "Clicking a bar in log timeline restricts search time range and refreshes events"
            },
            {
                "name": "Elastic (ELK Stack)",
                "url": "https://www.elastic.co",
                "hero_pattern": "Elasticsearch distributed search and Kibana dashboard canvas",
                "component_features": "Kibana Lens drag-and-drop chart builder, index lifecycle management policies, vector search",
                "color_tokens": {"background": "#1D1E24", "accent": "#005571", "text": "#DFE5EF"},
                "key_interactions": "Dragging a data field onto Kibana canvas to automatically choose optimal visualization"
            }
        ]
    },
    {
        "category_name": "Education, EdTech & Interactive Learning",
        "design_paradigm": "Gamified Steppers, Interactive Sandboxes & Progress Streaks",
        "recommended_libraries": ["Framer Motion", "Canvas-Confetti", "Tailwind CSS v4", "Lucide React"],
        "sites": [
            {
                "name": "Duolingo",
                "url": "https://www.duolingo.com",
                "hero_pattern": "Gamified learning path tree with animated mascot Duo and streak flame counter",
                "component_features": "Daily streak flame badge, interactive quiz word bank bubble selector, heart health meter",
                "color_tokens": {"background": "#FFFFFF", "accent": "#58CC02", "text": "#4B4B4B"},
                "key_interactions": "Bouncy spring animation and triumphant audio ping when answering quiz correctly"
            },
            {
                "name": "Brilliant.org",
                "url": "https://brilliant.org",
                "hero_pattern": "Interactive STEM visual problem-solving canvas with tactile math sliders",
                "component_features": "Physics simulator widget, bite-sized daily puzzle card, progress learning roadmaps",
                "color_tokens": {"background": "#FFFFFF", "accent": "#1A1A1A", "text": "#1A1A1A"},
                "key_interactions": "Dragging interactive physics gear or geometric shapes directly inside lesson card"
            },
            {
                "name": "Khan Academy",
                "url": "https://www.khanacademy.org",
                "hero_pattern": "Mastery learning curriculum dashboard with personalized student recommendation cards",
                "component_features": "Video player synchronized with transcript notes, mastery points badge progress, hint drawer",
                "color_tokens": {"background": "#FFFFFF", "accent": "#14BF96", "text": "#21242C"},
                "key_interactions": "Step-by-step hint revealer unfolding calculations one line at a time"
            },
            {
                "name": "Coursera",
                "url": "https://www.coursera.org",
                "hero_pattern": "University accredited degree and professional certificate showcase with alumni career outcomes",
                "component_features": "Syllabus week-by-week timeline, peer graded assignment submission portal, verified certificate preview",
                "color_tokens": {"background": "#FFFFFF", "accent": "#0056D2", "text": "#1F1F1F"},
                "key_interactions": "Enrolling in course launches animated congratulations modal with calendar add options"
            },
            {
                "name": "edX",
                "url": "https://www.edx.org",
                "hero_pattern": "Harvard and MIT founded online campus with search filters across university faculties",
                "component_features": "Course card with estimated hours and prerequisites, discussion board threads, video notes",
                "color_tokens": {"background": "#FFFFFF", "accent": "#B22222", "text": "#222222"},
                "key_interactions": "Course progress bar updating immediately as student watches lecture modules"
            },
            {
                "name": "Codecademy",
                "url": "https://www.codecademy.com",
                "hero_pattern": "Three-pane interactive programming classroom (Instructions, Code Editor, Terminal Output)",
                "component_features": "In-browser code editor with automated unit test runner, syntax error tips, lesson step counter",
                "color_tokens": {"background": "#10162F", "accent": "#FFD300", "text": "#FFFFFF"},
                "key_interactions": "Clicking 'Run' tests student code against test suites and prints feedback in terminal"
            },
            {
                "name": "LeetCode",
                "url": "https://leetcode.com",
                "hero_pattern": "Technical interview coding problem workspace with runtime/memory percentile bell curves",
                "component_features": "Monaco code editor with language selector, test case input/output tab, execution timer",
                "color_tokens": {"background": "#1A1A1A", "accent": "#FFA116", "text": "#EFF0F6"},
                "key_interactions": "Submit button displaying 'Accepted' green badge and speed runtime distribution chart"
            },
            {
                "name": "Frontend Masters",
                "url": "https://frontendmasters.com",
                "hero_pattern": "Expert video learning courses taught by industry leaders with code repository attachments",
                "component_features": "Video chapter scrubber with time stamps, instructor profile card, related course pathways",
                "color_tokens": {"background": "#222222", "accent": "#C02D28", "text": "#FFFFFF"},
                "key_interactions": "Video playback speed controls (1x, 1.25x, 1.5x, 2x) with audio pitch correction"
            },
            {
                "name": "Kaggle",
                "url": "https://www.kaggle.com",
                "hero_pattern": "Machine learning competition leaderboard with prize money badges and live Jupyter notebooks",
                "component_features": "Leaderboard standings with up/down arrows, dataset explorer, GPU notebook kernel runner",
                "color_tokens": {"background": "#FFFFFF", "accent": "#20BEFF", "text": "#202124"},
                "key_interactions": "Clicking 'Copy & Edit Notebook' opens interactive GPU session in seconds"
            },
            {
                "name": "Wolfram Alpha",
                "url": "https://www.wolframalpha.com",
                "hero_pattern": "Computational intelligence engine omnibar accepting natural language and math formulas",
                "component_features": "Step-by-step math solution generator, dynamic 2D/3D function plot renderer, source data citations",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF5500", "text": "#222222"},
                "key_interactions": "Clicking 'Show Steps' reveals the intermediate derivative or integral transformations"
            }
        ]
    },
    {
        "category_name": "Modern Social, Creator Economy & Community",
        "design_paradigm": "Feed Virtualization, Creator Tipping & Rich Social Micro-Interactions",
        "recommended_libraries": ["Virtuoso / TanStack Virtual", "Framer Motion", "Tailwind CSS v4"],
        "sites": [
            {
                "name": "Threads (Meta)",
                "url": "https://www.threads.net",
                "hero_pattern": "Single vertical stream of clean typography conversations with subtle minimalist borders",
                "component_features": "Post composer dialog with image attachments, reply threading lines, heart counter",
                "color_tokens": {"background": "#101010", "accent": "#FFFFFF", "text": "#F3F5F7"},
                "key_interactions": "Smooth pull-to-refresh and optimistic heart button pulse animation"
            },
            {
                "name": "X (Twitter)",
                "url": "https://x.com",
                "hero_pattern": "High-velocity real-time chronological and algorithmic feed with media cards",
                "component_features": "Character countdown ring progress, Retweet/Quote sheet, trending topics sidebar",
                "color_tokens": {"background": "#000000", "accent": "#1D9BF0", "text": "#E7E9EA"},
                "key_interactions": "Instant bookmarking with slide-in bottom toast confirmation"
            },
            {
                "name": "Reddit",
                "url": "https://www.reddit.com",
                "hero_pattern": "Community subreddit forum feed with upvote/downvote scores and nested comments",
                "component_features": "Collapsible recursive comment trees, subreddit flairs, rich media gallery post embeds",
                "color_tokens": {"background": "#0E1113", "accent": "#FF4500", "text": "#D7DADC"},
                "key_interactions": "Clicking vertical comment thread line collapses entire sub-discussion tree"
            },
            {
                "name": "Patreon",
                "url": "https://www.patreon.com",
                "hero_pattern": "Creator membership tier comparison cards with exclusive patron-only post feeds",
                "component_features": "Tier benefit check-list, monthly pledge checkout drawer, patron community chat rooms",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FF424D", "text": "#241E12"},
                "key_interactions": "Selecting membership tier smoothly highlights unlocked patron benefits"
            },
            {
                "name": "Buy Me a Coffee",
                "url": "https://www.buymeacoffee.com",
                "hero_pattern": "Friendly creator support widget allowing fans to buy coffees or monthly memberships",
                "component_features": "Coffee quantity button selector (1, 3, 5 coffees), fan message text box, supporter wall",
                "color_tokens": {"background": "#FFFFFF", "accent": "#FFDD00", "text": "#000000"},
                "key_interactions": "Selecting coffee count dynamically updates total dollar amount with bouncing cup animation"
            },
            {
                "name": "Gumroad",
                "url": "https://gumroad.com",
                "hero_pattern": "Bold retro-brutalist digital creator store with neon color blocks and heavy black borders",
                "component_features": "Product preview carousel, pay-what-you-want price input, instant download receipt modal",
                "color_tokens": {"background": "#F4F4F0", "accent": "#FF90E8", "text": "#000000"},
                "key_interactions": "One-click Apple Pay / Credit Card checkout drawer without leaving store"
            },
            {
                "name": "Lemon Squeezy",
                "url": "https://www.lemonsqueezy.com",
                "hero_pattern": "Merchant of Record platform for software sales with global tax compliance",
                "component_features": "Sleek SaaS checkout overlay modal, customer license key generator, revenue dashboard",
                "color_tokens": {"background": "#0C0C0D", "accent": "#7047EB", "text": "#FFFFFF"},
                "key_interactions": "Interactive embeddable checkout drawer sliding over merchant website"
            },
            {
                "name": "Kickstarter",
                "url": "https://www.kickstarter.com",
                "hero_pattern": "Crowdfunding project campaign page with funding progress bar and backer count",
                "component_features": "Reward tier side column, campaign video player, community updates and comments tab",
                "color_tokens": {"background": "#FFFFFF", "accent": "#05CE78", "text": "#282828"},
                "key_interactions": "Pledge progress bar dynamically showing percentage funded with green fill"
            },
            {
                "name": "Product Hunt",
                "url": "https://www.producthunt.com",
                "hero_pattern": "Daily curated new tech products leaderboard with upvote counters and maker comments",
                "component_features": "Upvote button with live score increments, product media gallery, discussion thread",
                "color_tokens": {"background": "#FFFFFF", "accent": "#DA552F", "text": "#4B587C"},
                "key_interactions": "Clicking upvote triggers subtle scale pulse and updates daily ranking"
            },
            {
                "name": "Indiegogo",
                "url": "https://www.indiegogo.com",
                "hero_pattern": "Hardware and creative project crowdfunding with flexible or fixed goal trackers",
                "component_features": "Perk selection cards, shipping countdown timer, prototype readiness stage badge",
                "color_tokens": {"background": "#FFFFFF", "accent": "#EB1478", "text": "#2A2A2A"},
                "key_interactions": "Perk hover state showing estimated worldwide delivery month"
            }
        ]
    }
]

def expand_vault():
    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_categories = {c["category_name"] for c in data["categories"]}
    
    for new_cat in NEW_CATEGORIES:
        if new_cat["category_name"] not in existing_categories:
            data["categories"].append(new_cat)
            existing_categories.add(new_cat["category_name"])

    # Update metadata count
    total_sites = sum(len(c["sites"]) for c in data["categories"])
    data["vault_metadata"]["total_sites"] = total_sites
    data["vault_metadata"]["description"] = f"Curated collection of {total_sites}+ S-Tier digital products, heavy pro desktop apps, and web platforms for automated UI/UX component synthesis."

    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[+] S-Tier Design Vault expanded: {len(data['categories'])} categories | {total_sites} total sites.")

if __name__ == "__main__":
    expand_vault()
