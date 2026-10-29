"""
Zobar Real-Time MCP (Model Context Protocol) Server
Production-Grade JSON-RPC 2.0 Live Server over stdio

Provides 19 live, fully-functional tools connected directly to Zobar Skill core engines:
1. semantic_cache_query         -> scripts.semantic_cache.SemanticCache (<0.05ms inverted index)
2. smart_route                  -> scripts.smart_model_router.SmartModelRouter
3. audit_supabase_sql           -> scripts.supabase_db_optimizer.SupabaseDBOptimizer
4. compress_context             -> scripts.context_compressor.ContextCompressor
5. recall_user_memory           -> scripts.continual_memory_engine.ContinualMemoryEngine
6. simulate_unit_economics      -> scripts.unit_economics_investor_simulator.UnitEconomicsSimulator
7. generate_image_prompt        -> scripts.image_prompt_synthesizer.ImagePromptSynthesizer
8. step_ecs_simulation          -> scripts.ecs_game_engine (ECSWorld + GameLoop)
9. search_asset_vault           -> scripts.query_asset_vault.AssetVaultQueryEngine
10. calculate_systems_math      -> scripts.systems_math_engine.SystemsMathEngine (Roofline, Queueing, Amdahl, Spring, Kelly)
11. get_design_style            -> scripts.design_system_generator.ModernDesignStylesEngine (Glassmorphism, Aurora, Bento)
12. analyze_reverse_engineering -> scripts.reverse_engineering_analyst (REA & Clean-Room Safe Harbors)
13. generate_game_mod_architecture -> scripts.game_modding_engine (Fabric/Harmony & Voxel/Minecraft Greedy Meshing)
14. deliberate_council          -> scripts.multi_agent_deliberation_council (Academic, Public, Workforce & Chief Engineer)
15. generate_evolutionary_design-> scripts.creative_evolutionary_designer (Novelty Divergence >= 0.75 & Genetic UI)
16. analyze_human_delight       -> scripts.human_delight_psychology_engine (Dopamine loops, viral K-factor, optimistic UI)
17. generate_client_agency_pitch-> scripts.freelance_agency_growth_engine (Cold audits, client ROI pitches, MRR retainer models)
18. manage_skills_and_mcp       -> scripts.skill_registry_and_installer_engine (Skill researcher & MCP terminal command runner)
19. get_free_component_snippet  -> scripts.modern_component_snippets (Ready-to-copy free modern UI snippets)
"""

import sys
import os
import json
import time
from typing import Dict, Any, List, Optional

# Ensure project root is in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.semantic_cache import SemanticCache
from scripts.smart_model_router import SmartModelRouter
from scripts.supabase_db_optimizer import SupabaseDBOptimizer
from scripts.context_compressor import ContextCompressor
from scripts.continual_memory_engine import ContinualMemoryEngine
from scripts.unit_economics_investor_simulator import UnitEconomicsSimulator
from scripts.image_prompt_synthesizer import ImagePromptSynthesizer
from scripts.ecs_game_engine import ECSWorld, DeterministicGameLoop
from scripts.query_asset_vault import AssetVaultQueryEngine
from scripts.systems_math_engine import SystemsMathEngine
from scripts.design_system_generator import ModernDesignStylesEngine
from scripts.reverse_engineering_analyst import analyze_target_system, execute_7phase_re_pipeline, execute_10phase_re_pipeline
from scripts.end_to_end_app_architect import synthesize_complete_application, evaluate_feature_internally, generate_concise_co_creation_dialogue
from scripts.autonomous_idea_factory import harvest_and_curate_ideas, inject_feature_into_file
from scripts.game_modding_engine import synthesize_minecraft_in_game_bridge, calculate_greedy_meshing_metrics, generate_mod_code_template
from scripts.multi_agent_deliberation_council import conduct_executive_board_deliberation
from scripts.creative_evolutionary_designer import generate_evolutionary_design
from scripts.human_delight_psychology_engine import analyze_user_psychology_and_delight, calculate_viral_k_factor
from scripts.freelance_agency_growth_engine import generate_cold_audit_proposal, calculate_agency_retainer_growth
from scripts.skill_registry_and_installer_engine import search_ecosystem_skills, synthesize_new_skill_scaffold, execute_terminal_mcp_command
from scripts.modern_component_snippets import ModernComponentsEngine
from scripts.security_permission_guard import SecurityPermissionGuard
from scripts.evidence_provenance_engine import EvidenceProvenanceGraph
from scripts.feedback_outcome_learning_engine import FeedbackOutcomeEngine
from scripts.unified_system_orchestrator import UnifiedSystemOrchestrator
from scripts.trend_trick_harvester_engine import TrendTrickHarvesterEngine


class ZobarMCPServer:
    def __init__(self):
        self.semantic_cache = SemanticCache()
        self.model_router = SmartModelRouter(semantic_cache=self.semantic_cache)
        self.context_compressor = ContextCompressor()
        self.memory_engine = ContinualMemoryEngine()
        self.image_synthesizer = ImagePromptSynthesizer()
        self.asset_vault = AssetVaultQueryEngine()
        self.design_styles = ModernDesignStylesEngine()
        self.components_engine = ModernComponentsEngine()
        self.security_guard = SecurityPermissionGuard()
        self.provenance_graph = EvidenceProvenanceGraph()
        self.learning_engine = FeedbackOutcomeEngine()
        self.unified_orchestrator = UnifiedSystemOrchestrator()
        self.trend_harvester = TrendTrickHarvesterEngine()

    def get_tools_manifest(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "semantic_cache_query",
                "description": "Performs sub-millisecond semantic cache lookup for a query to save LLM API costs.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "The user query or prompt"}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "smart_route",
                "description": "Analyzes prompt complexity and routes to Tier 0 (Cache), Tier 1 (Lightweight), or Tier 2 (Frontier).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "prompt": {"type": "string", "description": "The prompt to route"}
                    },
                    "required": ["prompt"]
                }
            },
            {
                "name": "audit_supabase_sql",
                "description": "Performs static security, RLS, and pgvector HNSW index audit on SQL content.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "sql_content": {"type": "string", "description": "SQL schema code to audit"}
                    },
                    "required": ["sql_content"]
                }
            },
            {
                "name": "compress_context",
                "description": "Compresses conversation dialogue using sliding-window state extraction and semantic token pruning.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "messages": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "role": {"type": "string"},
                                    "content": {"type": "string"}
                                },
                                "required": ["role", "content"]
                            },
                            "description": "List of message objects"
                        }
                    },
                    "required": ["messages"]
                }
            },
            {
                "name": "recall_user_memory",
                "description": "Recalls relevant knowledge graph triples and preferences based on query keywords.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query for memory recall"}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "simulate_unit_economics",
                "description": "Calculates LTV, CAC, payback period, and validates Tier-1 investor criteria.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "arpu": {"type": "number", "description": "Monthly average revenue per user"},
                        "churn": {"type": "number", "description": "Monthly churn rate (e.g. 0.04)"},
                        "cac": {"type": "number", "description": "Customer acquisition cost"}
                    },
                    "required": ["arpu", "churn", "cac"]
                }
            },
            {
                "name": "generate_image_prompt",
                "description": "Synthesizes hyper-realistic prompts for Midjourney v6.1 and FLUX.1 with optics and lighting.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string", "description": "Subject of the visual"},
                        "style": {"type": "string", "description": "Style preset (photorealistic_cinematic, modern_ui_product_mockup, cyberpunk_scifi)"},
                        "engine": {"type": "string", "description": "Target engine (midjourney, flux, dalle3)"}
                    },
                    "required": ["subject"]
                }
            },
            {
                "name": "step_ecs_simulation",
                "description": "Spawns 2D entities and executes deterministic 60 FPS ECS physics and spatial quadtree ticks.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ticks": {"type": "integer", "description": "Number of simulation ticks to execute"},
                        "entity_count": {"type": "integer", "description": "Number of active physics entities to spawn"}
                    },
                    "required": ["ticks"]
                }
            },
            {
                "name": "search_asset_vault",
                "description": "Searches verified 3D models (glTF/GLB), PBR textures, UI component libraries, icons, and audio SFX.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search term (e.g. 3d, gltf, bento, pbr, sound, character)"},
                        "category": {"type": "string", "description": "Optional category filter (3d_models_and_meshes, pbr_textures_and_materials, ui_component_and_animation_libraries, icons_and_vector_design_systems, audio_sfx_and_soundtracks)"},
                        "preferred_format": {"type": "string", "description": "Optional file format (GLTF, FBX, React, PNG, WAV)"}
                    }
                }
            },
            {
                "name": "calculate_systems_math",
                "description": "Computes rigorous mathematical models: Berkeley Roofline (memory vs compute bound), Queueing Theory (M/M/1 Little's law tail latency), Amdahl speedup, Spring physics ODE, and Kelly Criterion.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "math_type": {
                            "type": "string",
                            "enum": ["roofline", "queueing", "amdahl", "spring_physics", "kelly"],
                            "description": "The mathematical model to compute"
                        },
                        "parameters": {
                            "type": "object",
                            "description": "Parameters for the chosen calculation"
                        }
                    },
                    "required": ["math_type"]
                }
            },
            {
                "name": "get_design_style",
                "description": "Provides production-ready CSS, Tailwind classes, and React component code for S-Tier design paradigms: glassmorphism (frosted glass), aurora_mesh_gradient, neo_brutalism, cyberpunk_hud, dark_mode_bento, claymorphism.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "style_name": {
                            "type": "string",
                            "description": "Design style key (glassmorphism, aurora_mesh_gradient, neo_brutalism, cyberpunk_hud, dark_mode_bento, claymorphism)"
                        }
                    },
                    "required": ["style_name"]
                }
            },
            {
                "name": "analyze_reverse_engineering",
                "description": "REA-inspired reverse engineering analyst and statutory safe-harbor legal auditor. Inspects binary format headers, Shannon entropy, ISA CFG, printable symbols, safe-harbor legality (EU Directive 2009/24/EC Art 6 & US DMCA 1201(f) Interoperability), and generates Clean-Room Functional Specifications (FSD) with 7-phase analysis.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target_name": {"type": "string", "description": "Target binary or protocol name"},
                        "intent": {"type": "string", "description": "Goal of reverse engineering (e.g. Interoperability, Security Audit, Protocol Integration)"},
                        "full_7_phases": {"type": "boolean", "description": "Execute comprehensive 7-phase reverse engineering pipeline"},
                        "full_10_phases": {"type": "boolean", "description": "Execute complete 10-phase reverse engineering & systems architecture pipeline"}
                    },
                    "required": ["target_name"]
                }
            },
            {
                "name": "generate_game_mod_architecture",
                "description": "Synthesizes production-grade game modding architectures across Minecraft (Fabric Mixin / NeoForge) and Unity (BepInEx Harmony). Computes Greedy Meshing voxel geometry optimizations (90% draw call reduction) and cross-game Minecraft embedding bridges.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target_game": {"type": "string", "description": "Target game (e.g. Minecraft, Unity, Unreal)"},
                        "mod_feature": {"type": "string", "description": "Desired mod feature or integration mechanic"}
                    },
                    "required": ["target_game"]
                }
            },
            {
                "name": "deliberate_council",
                "description": "Multi-agent deliberation council and senatorial consensus engine. Simulates an intense 3-way adversarial debate between Academic Council (algorithms, safety), Public Assembly (UX, privacy, voting), and Workforce Council (toil, maintainability), yielding a binding ratified consensus score and dissenting opinion log.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "description": "Architecture proposal or feature under deliberation"}
                    },
                    "required": ["topic"]
                }
            },
            {
                "name": "generate_evolutionary_design",
                "description": "Evolves non-repetitive, novel, and self-strengthening UI/UX design architectures. Enforces high novelty divergence (D_novelty >= 0.75), rejects cliché bootstrap/shadcn presets, updates persistent aesthetic memory, and produces executable Tailwind v4 classes and React spring-physics components.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "domain_context": {"type": "string", "description": "Product or application domain"}
                    },
                    "required": ["domain_context"]
                }
            },
            {
                "name": "analyze_human_delight",
                "description": "Evaluates user psychology, cognitive friction, dopamine micro-interactions (optimistic UI, shimmer skeletons, spring physics), and calculates viral loop K-factor (K = i * c).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "feature_or_page": {"type": "string", "description": "Feature, funnel, or UI component to evaluate"},
                        "invites_per_user": {"type": "number", "description": "Average invites per user (default 2.5)"},
                        "invitee_conversion_rate": {"type": "number", "description": "Conversion rate of invited users (default 0.35)"}
                    },
                    "required": ["feature_or_page"]
                }
            },
            {
                "name": "generate_client_agency_pitch",
                "description": "Freelance, agency & indie-developer growth engine. Generates high-margin niche business ideas, cold audit outreach proposals that quantify lost revenue/ROI, and monthly recurring maintenance retainers (MRR).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target_business": {"type": "string", "description": "Target client business name (e.g. Apex Dental)"},
                        "niche": {"type": "string", "description": "Niche category (clinic, contractor, hotel, restaurant)"},
                        "client_website": {"type": "string", "description": "Existing client website domain (optional)"}
                    },
                    "required": ["target_business"]
                }
            },
            {
                "name": "manage_skills_and_mcp",
                "description": "Skill Researcher & MCP Terminal Engineer role. Discovers ecosystem skills, scaffolds compliant SKILL.md packages, and executes terminal MCP subshell commands with latency and exit code capture.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["search", "scaffold", "execute_command"], "description": "Action to perform"},
                        "query": {"type": "string", "description": "Skill search keyword, new skill name, or terminal command string"}
                    },
                    "required": ["action", "query"]
                }
            },
            {
                "name": "get_free_component_snippet",
                "description": "Retrieves ready-to-copy, zero-cost, modern S-Tier React and Tailwind CSS v4 component snippets (e.g. Shimmer Skeleton Card, Bento Metric Card, Mobile Sticky WhatsApp Conversion Bar, Interactive Client ROI Slider).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Component search term or keyword (e.g. skeleton, bento, whatsapp, roi)"},
                        "component_id": {"type": "string", "description": "Optional direct component ID (e.g. COMP-01, COMP-03)"}
                    }
                }
            },
            {
                "name": "run_unified_orchestration",
                "description": "Executes the autonomous 9-phase end-to-end product engineering pipeline: Research -> Sentiment -> Competitors -> Legal Compliance -> Architecture -> Code Prototype -> Sandbox & AST Validation -> Provenance -> Senate Ratification.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "vision": {"type": "string", "description": "Product idea, system vision, or architecture proposal"},
                        "sector": {"type": "string", "description": "Industry sector (default: High-Performance Systems)"}
                    },
                    "required": ["vision"]
                }
            },
            {
                "name": "audit_security_sandbox",
                "description": "Strict security audit: verifies workspace path containment (path traversal block), validates shell metacharacters and blocked binaries, and executes safe sandboxed commands with shell=False.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["audit_command", "validate_path", "execute_command"], "description": "Security action to perform"},
                        "target": {"type": "string", "description": "Command string to audit/execute or file path to validate"},
                        "timeout_seconds": {"type": "integer", "description": "Execution timeout limit (default: 5)"},
                        "user_confirmed": {"type": "boolean", "description": "User confirmation gate for execution (default: false)"}
                    },
                    "required": ["action", "target"]
                }
            },
            {
                "name": "query_evidence_provenance",
                "description": "Tracks evidence provenance, confidence tiers (Statutory, Peer-Reviewed, Telemetry, Heuristic, Hypothesis), causal decision links, and flags stale data.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["integrity_audit", "get_node"], "description": "Action to run on provenance graph"},
                        "evidence_id": {"type": "string", "description": "Optional evidence ID to inspect"}
                    },
                    "required": ["action"]
                }
            },
            {
                "name": "query_learning_registry",
                "description": "Queries empirical Bayesian Beta-Binomial learning registry to retrieve calibrated pattern win-rates and empirical trial history.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "pattern_name": {"type": "string", "description": "Architecture pattern key to query (e.g. lock_free_ringbuffer, rust_tauri_core)"}
                    },
                    "required": ["pattern_name"]
                }
            },
            {
                "name": "harvest_trending_tricks",
                "description": "Continuous Real-Time Trend & Trick Harvester. Monitors viral tech Reels & YouTube Shorts, trending GitHub breakout repos, and global tech news wires. Auto-assimilates fresh developer tricks into continual memory and active sessions.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["sync_session", "search_tricks", "get_daily_brief", "harvest_source"], "description": "Action to run"},
                        "source": {"type": "string", "enum": ["reels_shorts", "github_trending", "global_news", "all"], "description": "Target source if harvest_source chosen"},
                        "keyword": {"type": "string", "description": "Search keyword or topic (default: all)"},
                        "max_items": {"type": "integer", "description": "Maximum tricks to retrieve (default: 4)"}
                    },
                    "required": ["action"]
                }
            },
            {
                "name": "audit_module_maturity",
                "description": "Audits, benchmarks, and categorizes system modules into Capability Maturity Levels: Level 3 (Production Proven - Live API/Sandbox/Statute), Level 2 (Heuristic Hybrid - Rules/AST/Templates), and Level 1 (Experimental Prototype - Simulation).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get_summary", "get_module", "generate_report"], "description": "Audit action to run"},
                        "module_name": {"type": "string", "description": "Optional module script name to inspect (e.g. security_permission_guard.py)"}
                    },
                    "required": ["action"]
                }
            },
            {
                "name": "synthesize_cinematic_art_direction",
                "description": "Synthesizes world-class cinematic visual grammar (Kubrick, Deakins, Wong Kar-wai, Wes Anderson, Miyazaki), Aristotelian Poetics UX arc, and Calvino Six Memos interface tokens.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "product_vision": {"type": "string", "description": "The software or product vision to critique and stylize"},
                        "target_mood": {"type": "string", "enum": ["kubrickian_symmetry", "deakins_chiaroscuro", "wong_kar_wai_neon_melancholy", "wes_anderson_diegetic_whimsy", "miyazaki_ma_contemplation"], "description": "Optional specific cinematic director mood"}
                    },
                    "required": ["product_vision"]
                }
            },
            {
                "name": "synthesize_complete_application",
                "description": "Synthesizes an end-to-end complete, non-generic application spanning Core Dashboard, Product Catalog, User Profile, Workspace Settings, and working Command Palette (Cmd+K) with zero dead buttons.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "app_name": {"type": "string", "description": "Brand name of the application (e.g. Apex Studio)"},
                        "domain_type": {"type": "string", "description": "Application industry domain"},
                        "custom_inventions": {"type": "array", "items": {"type": "string"}, "description": "Optional domain inventions to embed"}
                    },
                    "required": ["app_name"]
                }
            },
            {
                "name": "evaluate_feature_co_creation",
                "description": "Autonomous internal pre-evaluation of a proposed feature followed by ultra-concise, high-signal conversational co-creation options for the user.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "feature_name": {"type": "string", "description": "Proposed feature name or micro-mechanic"},
                        "domain_context": {"type": "string", "description": "Target domain or application context"}
                    },
                    "required": ["feature_name"]
                }
            },
            {
                "name": "harvest_ideas_and_co_create",
                "description": "Autonomous Idea Factory: monitors real-world breakout trends, runs internal pre-evaluation, and formulates crisp 1-line decision options for the user.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "domain": {"type": "string", "description": "Domain sector (e.g. saas, ecommerce, medtech, creative_agency)"}
                    }
                }
            },
            {
                "name": "inject_live_app_feature",
                "description": "Live Application Injector: automatically injects working HTML markup, styling, and JS handlers for a selected feature into a live HTML file.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target_file": {"type": "string", "description": "Relative or absolute path to the target HTML file"},
                        "feature_id": {"type": "string", "description": "Selected feature ID (e.g. FEAT-SPLIT-FILTER, FEAT-OFFLINE-QUEUE, FEAT-DARK-ACCENT-TOGGLE)"}
                    },
                    "required": ["target_file", "feature_id"]
                }
            },
            {
                "name": "blend_proven_ui_components",
                "description": "Proven Pattern Synthesis Mandate: Never write inferior generic UI. Extracts and blends battle-tested UI components and design tokens from world-class benchmark sites (Linear, Stripe, Apple, Vercel) stored in the S-Tier Design Vault.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Domain or UI need (e.g. saas, dashboard, luxury ecommerce, medtech telemetry, 3d canvas)"},
                        "component_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of specific component IDs from vault (e.g. ['COMP-02', 'COMP-08'])"
                        },
                        "inject_target_file": {
                            "type": "string",
                            "description": "Optional HTML file path to automatically inject blended components into"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "quantum_optimize_design",
                "description": "Quantum Design Optimizer: Evaluates candidate UI designs using quantum state superposition, Hamiltonian energy minimization, and Von Neumann entropy to mathematically select the best-looking, most harmonic, and lowest-friction design.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "candidates": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "List of design options with color tokens, aspect ratio, visual density, etc."
                        }
                    },
                    "required": ["candidates"]
                }
            },
            {
                "name": "synthesize_full_stack_triad",
                "description": "Full-Stack Triad Architecture Engine: Unites Deep Analysis, Quantum-Optimized Frontend Design, and Sub-Millisecond Backend REST/SQL Architecture into a single cohesive production package.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "vision": {"type": "string", "description": "The product or software system vision"},
                        "sector": {"type": "string", "description": "Target industry sector (e.g. Enterprise SaaS, FinTech, MedTech, Luxury E-Commerce)"},
                        "brand_name": {"type": "string", "description": "Optional brand or product title"},
                        "output_dir": {"type": "string", "description": "Optional directory to output full-stack deliverables (HTML, Python server, SQL)"}
                    },
                    "required": ["vision"]
                }
            },
            {
                "name": "ground_academic_foundations",
                "description": "Grounds architectural, algorithmic, and UX designs in top university curricula (MIT, Stanford, ETH Zürich, Oxford), seminal textbooks (Knuth, Lamport, Sutton & Barto, Kleppmann), and mathematical theorems (Little's Law, Roofline, PACELC, Von Neumann Entropy).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "domain": {"type": "string", "description": "The problem domain or software category"},
                        "problem_statement": {"type": "string", "description": "Specific engineering problem or design challenge"}
                    },
                    "required": ["domain"]
                }
            },
            {
                "name": "synthesize_master_logo_and_icons",
                "description": "Synthesizes world-class brandmarks, icons, and anti-cliché visual prompts grounded in Paul Rand's 7-Step Logo Test, Josef Müller-Brockmann grid systems, Dieter Rams functionalism, and Gestalt negative space closure.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "concept": {"type": "string", "description": "Brand or iconography concept to design"},
                        "archetype": {
                            "type": "string",
                            "enum": ["negative_space_monolith", "swiss_ribbon", "golden_spiral_vortex", "brutalist_monogram", "precision_reticle"],
                            "description": "Graphic design archetype"
                        },
                        "medium": {
                            "type": "string",
                            "enum": ["vector_silkscreen", "titanium_etched", "letterpress_stamp"],
                            "description": "Material execution medium"
                        },
                        "engine": {
                            "type": "string",
                            "enum": ["midjourney", "flux", "dalle3"],
                            "description": "Target generative AI engine"
                        }
                    },
                    "required": ["concept"]
                }
            },
            {
                "name": "synthesize_hyper_originality",
                "description": "Calculates Kolmogorov-Chaitin information density and elevates software architectures by 10x and 100x using cross-domain mathematical isomorphisms (Algebraic Topology, Symplectic Integrators, Non-Linear Chaos Attractors, and Bit-Parallel SIMD).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "domain": {"type": "string", "description": "Problem domain or system architecture"},
                        "baseline_code": {"type": "string", "description": "Optional baseline code snippet to evaluate and elevate"},
                        "target_multiplier": {
                            "type": "string",
                            "enum": ["10x", "100x", "both"],
                            "description": "Target innovation multiplier"
                        }
                    },
                    "required": ["domain"]
                }
            },
            {
                "name": "benchmark_and_close_skill_gaps",
                "description": "Performs exhaustive competitive benchmark against top agent ecosystems (Google Antigravity, Devin/SWE-bench, DSPy, Reflexion), detects operational blind spots, and executes remediation.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "execute_self_healing_verification",
                "description": "SWE-bench/Devin standard self-healing loop: Runs tests in an isolated sandbox, captures exact stack traces, diagnoses root causes, generates targeted AST patches, and iterates until 100% green.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "test_command": {"type": "string", "description": "Verification test command to execute"},
                        "max_attempts": {"type": "integer", "description": "Maximum self-healing attempts (default: 3)"}
                    }
                }
            },
            {
                "name": "amplify_model_test_time_compute",
                "description": "DSPy / Reflexion / o1-o3 standard: Multiplies base AI reasoning by exploring Best-of-N branches, scoring via Process Reward Model (PRM), and executing verbal Reflexion self-critique.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "problem": {"type": "string", "description": "Complex engineering problem or architecture to solve"},
                        "domain": {"type": "string", "description": "Target technical domain"}
                    },
                    "required": ["problem"]
                }
            },
            {
                "name": "synthesize_generative_ui_widget",
                "description": "Google Antigravity Generative UI standard: Synthesizes self-contained interactive chat widgets using allowlisted gstatic Tailwind CDN and host semantic design-system tokens.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "widget_type": {
                            "type": "string",
                            "enum": ["telemetry_pulse", "interactive_calculator"],
                            "description": "Type of interactive widget"
                        },
                        "title": {"type": "string", "description": "Widget header title"}
                    }
                }
            }
        ]

    def execute_tool(self, name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        start_time = time.perf_counter()

        if name == "semantic_cache_query":
            query = args.get("query", "")
            res = self.semantic_cache.get(query)
            payload = res if res else {"matched": False, "message": "Cache miss. No similar query found."}

        elif name == "smart_route":
            prompt = args.get("prompt", "")
            payload = self.model_router.route(prompt)

        elif name == "audit_supabase_sql":
            sql_content = args.get("sql_content", "")
            import tempfile
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".sql") as tmp:
                tmp.write(sql_content)
                tmp_path = tmp.name
            try:
                optimizer = SupabaseDBOptimizer(tmp_path)
                payload = optimizer.audit()
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

        elif name == "compress_context":
            messages = args.get("messages", [])
            payload = self.context_compressor.compress_conversation(messages)

        elif name == "recall_user_memory":
            query = args.get("query", "")
            payload = {
                "recalled_memories": self.memory_engine.recall_relevant_memories(query),
                "active_profile": self.memory_engine.user_profile,
            }

        elif name == "simulate_unit_economics":
            sim = UnitEconomicsSimulator(
                arpu_monthly_usd=float(args.get("arpu", 49.0)),
                monthly_churn_rate=float(args.get("churn", 0.04)),
                gross_margin=float(args.get("gross_margin", 0.85)),
                cac_usd=float(args.get("cac", 100.0)),
            )
            payload = sim.calculate_metrics()

        elif name == "generate_image_prompt":
            subject = args.get("subject", "")
            style = args.get("style", "photorealistic_cinematic")
            engine = args.get("engine", "midjourney")
            payload = self.image_synthesizer.synthesize(subject=subject, style=style, engine=engine)

        elif name == "step_ecs_simulation":
            ticks = int(args.get("ticks", 60))
            count = int(args.get("entity_count", 20))
            world = ECSWorld()
            for i in range(count):
                e = world.create_entity()
                world.add_transform(e, x=(i * 20.0) % 400, y=(i * 15.0) % 400)
                world.add_velocity(e, vx=15.0, vy=-10.0)
                world.add_collider(e, width=10.0, height=10.0)
            loop = DeterministicGameLoop(world)
            payload = loop.step_fixed_ticks(ticks)

        elif name == "search_asset_vault":
            query = args.get("query", "")
            category = args.get("category")
            fmt = args.get("preferred_format")
            matches = self.asset_vault.search(query=query, category=category, preferred_format=fmt)
            payload = {
                "query": query,
                "matches_found": len(matches),
                "results": matches,
            }

        elif name == "calculate_systems_math":
            mtype = args.get("math_type", "roofline")
            p = args.get("parameters", {})
            if mtype == "roofline":
                payload = SystemsMathEngine.calculate_roofline_analysis(
                    total_flops=float(p.get("total_flops", 1e12)),
                    total_bytes_transferred=float(p.get("total_bytes_transferred", 5e10)),
                    hardware_target=p.get("hardware_target", "nvidia_a100_80gb")
                )
            elif mtype == "queueing":
                payload = SystemsMathEngine.calculate_queueing_latency(
                    arrival_rate_lambda=float(p.get("arrival_rate_lambda", 400.0)),
                    service_rate_mu=float(p.get("service_rate_mu", 500.0)),
                    concurrency_channels_c=int(p.get("concurrency_channels_c", 1))
                )
            elif mtype == "amdahl":
                payload = SystemsMathEngine.calculate_amdahl_speedup(
                    parallel_fraction_p=float(p.get("parallel_fraction_p", 0.90)),
                    processor_cores_s=int(p.get("processor_cores_s", 16))
                )
            elif mtype == "spring_physics":
                payload = SystemsMathEngine.calculate_spring_physics(
                    mass_m=float(p.get("mass_m", 1.0)),
                    stiffness_k=float(p.get("stiffness_k", 180.0)),
                    damping_c=float(p.get("damping_c", 12.0)),
                    initial_displacement=float(p.get("initial_displacement", 1.0))
                )
            elif mtype == "kelly":
                payload = SystemsMathEngine.calculate_kelly_capital_allocation(
                    win_probability_p=float(p.get("win_probability_p", 0.40)),
                    upside_downside_ratio_b=float(p.get("upside_downside_ratio_b", 4.0)),
                    bankroll_or_time_budget_usd=float(p.get("bankroll_or_time_budget_usd", 10000.0))
                )
            else:
                raise ValueError(f"Unknown math_type: {mtype}")

        elif name == "get_design_style":
            style_name = args.get("style_name", "glassmorphism")
            style_data = self.design_styles.get_style(style_name)
            if not style_data:
                payload = {
                    "error": f"Style '{style_name}' not found.",
                    "available_styles": [s["key"] for s in self.design_styles.list_styles()]
                }
            else:
                payload = {
                    "style_name": style_name,
                    "tokens": style_data,
                }

        elif name == "analyze_reverse_engineering":
            target_name = args.get("target_name", "UnknownBinary")
            intent = args.get("intent", "Interoperability with third-party software")
            full_10_phases = args.get("full_10_phases", False)
            full_7_phases = args.get("full_7_phases", False)
            if full_10_phases:
                payload = execute_10phase_re_pipeline(target_name=target_name, intent=intent)
            elif full_7_phases:
                payload = execute_7phase_re_pipeline(target_name=target_name, intent=intent)
            else:
                payload = analyze_target_system(target_name=target_name, intent=intent)

        elif name == "generate_game_mod_architecture":
            target_game = args.get("target_game", "Minecraft")
            mod_feature = args.get("mod_feature", "Custom Voxel Mechanics")
            greedy = calculate_greedy_meshing_metrics()
            bridge = synthesize_minecraft_in_game_bridge(target_game)
            mod_code = generate_mod_code_template(target_game, mod_feature)
            payload = {
                "greedy_meshing_optimization": greedy,
                "minecraft_in_game_bridge": bridge,
                "mod_code_template": mod_code
            }

        elif name == "deliberate_council":
            topic = args.get("topic", "General Architecture Proposal")
            payload = conduct_executive_board_deliberation(topic=topic)

        elif name == "generate_evolutionary_design":
            domain_context = args.get("domain_context", "Modern Enterprise Application")
            payload = generate_evolutionary_design(domain_context=domain_context)

        elif name == "analyze_human_delight":
            feat = args.get("feature_or_page", "Main Landing Page Funnel")
            invites = float(args.get("invites_per_user", 2.5))
            conv = float(args.get("invitee_conversion_rate", 0.35))
            psych = analyze_user_psychology_and_delight(feat)
            viral = calculate_viral_k_factor(invites, conv)
            payload = {
                "psychology_analysis": psych,
                "viral_k_factor": viral
            }

        elif name == "generate_client_agency_pitch":
            biz = args.get("target_business", "Prospective Client")
            niche = args.get("niche", "clinic")
            web = args.get("client_website", "example.com")
            proposal = generate_cold_audit_proposal(biz, niche_key=niche, client_website=web)
            monthly_fee = float(proposal["niche_data"]["monthly_retainer_usd"])
            growth = calculate_agency_retainer_growth(client_count=10, avg_monthly_fee=monthly_fee)
            payload = {
                "client_proposal": proposal,
                "agency_10_client_growth_model": growth
            }

        elif name == "manage_skills_and_mcp":
            action = args.get("action", "search")
            query = args.get("query", "browser")
            if action == "search":
                payload = {"matched_skills": search_ecosystem_skills(query)}
            elif action == "scaffold":
                payload = synthesize_new_skill_scaffold(skill_name=query, skill_description=f"Automated skill for {query}")
            elif action == "execute_command":
                payload = execute_terminal_mcp_command(command=query)
            else:
                raise ValueError(f"Unknown action: {action}")

        elif name == "get_free_component_snippet":
            comp_id = args.get("component_id")
            query = args.get("query", "")
            if comp_id:
                comp = self.components_engine.get_component_by_id(comp_id)
                payload = {"component": comp} if comp else {"error": f"Component ID '{comp_id}' not found."}
            else:
                matches = self.components_engine.search_components(query)
                payload = {"query": query, "count": len(matches), "components": matches}

        elif name == "run_unified_orchestration":
            vision = args.get("vision", "")
            sector = args.get("sector", "High-Performance Systems")
            payload = self.unified_orchestrator.orchestrate_product_lifecycle(vision, target_sector=sector)

        elif name == "audit_security_sandbox":
            action = args.get("action", "audit_command")
            target = args.get("target", "")
            timeout = args.get("timeout_seconds", 5)
            user_confirmed = args.get("user_confirmed", False)
            if action == "audit_command":
                safe, reason, tokens = self.security_guard.audit_command_safety(target)
                payload = {"is_safe": safe, "reason": reason, "tokenized_args": tokens}
            elif action == "validate_path":
                try:
                    resolved = self.security_guard.validate_file_path(target)
                    payload = {"is_valid": True, "resolved_path": resolved}
                except Exception as e:
                    payload = {"is_valid": False, "error": str(e)}
            elif action == "execute_command":
                payload = self.security_guard.execute_sandboxed_command(target, timeout_seconds=timeout, user_confirmed=user_confirmed)
            else:
                raise ValueError(f"Unknown security action: {action}")

        elif name == "query_evidence_provenance":
            action = args.get("action", "integrity_audit")
            if action == "integrity_audit":
                payload = self.provenance_graph.audit_evidence_integrity()
            elif action == "get_node":
                ev_id = args.get("evidence_id", "")
                payload = self.provenance_graph.evidence_nodes.get(ev_id, {"error": "Node not found"})
            else:
                raise ValueError(f"Unknown provenance action: {action}")

        elif name == "query_learning_registry":
            pattern_name = args.get("pattern_name", "")
            payload = self.learning_engine.get_pattern_reputation(pattern_name)

        elif name == "harvest_trending_tricks":
            action = args.get("action", "sync_session")
            keyword = args.get("keyword", "")
            source = args.get("source", "all")
            max_items = args.get("max_items", 4)

            if action == "sync_session":
                payload = self.trend_harvester.sync_active_session()
            elif action == "get_daily_brief":
                payload = {"brief_markdown": self.trend_harvester.generate_daily_trick_brief()}
            elif action == "search_tricks":
                platform = None if source == "all" else source
                payload = {
                    "keyword": keyword,
                    "matches": self.trend_harvester.search_tricks(keyword=keyword, platform=platform)
                }
            elif action == "harvest_source":
                if source == "reels_shorts":
                    items = self.trend_harvester.harvest_youtube_instagram_reels(topic=keyword or "coding tricks", max_items=max_items)
                elif source == "github_trending":
                    items = self.trend_harvester.harvest_github_trending_repos(query=keyword or "ai-agent", max_items=max_items)
                elif source == "global_news":
                    items = self.trend_harvester.harvest_global_tech_news(category=keyword or "ai", max_items=max_items)
                else:
                    items = (
                        self.trend_harvester.harvest_youtube_instagram_reels(max_items=2) +
                        self.trend_harvester.harvest_github_trending_repos(max_items=2) +
                        self.trend_harvester.harvest_global_tech_news(max_items=2)
                    )
                payload = {"source": source, "count": len(items), "tricks": items}
            else:
                raise ValueError(f"Unknown trend harvest action: {action}")

        elif name == "audit_module_maturity":
            from scripts.module_maturity_auditor import ModuleMaturityAuditor
            auditor = ModuleMaturityAuditor()
            action = args.get("action", "get_summary")
            if action == "generate_report":
                json_path, md_path = auditor.persist_reports()
                payload = {"status": "SUCCESS", "json_path": json_path, "md_report_path": md_path}
            elif action == "get_module":
                mod_name = args.get("module_name", "")
                data = auditor.audit_all_modules()
                mod_info = data["modules"].get(mod_name)
                payload = mod_info if mod_info else {"error": f"Module '{mod_name}' not found in catalog."}
            else:
                data = auditor.audit_all_modules()
                payload = {
                    "system_maturity_index": data["system_maturity_index"],
                    "average_score": data["average_module_score"],
                    "tier_distribution": data["tier_distribution"],
                    "total_audited": data["total_modules_audited"]
                }

        elif name == "synthesize_cinematic_art_direction":
            from scripts.cinematic_literary_criticism_engine import CinematicLiteraryCriticismEngine
            vision = args.get("product_vision", "")
            mood = args.get("target_mood")
            payload = CinematicLiteraryCriticismEngine.critique_and_synthesize_art_direction(vision, target_mood=mood)

        elif name == "synthesize_complete_application":
            app_name = args.get("app_name", "Enterprise Platform")
            domain_type = args.get("domain_type", "High-Performance SaaS")
            custom_inventions = args.get("custom_inventions")
            payload = synthesize_complete_application(app_name=app_name, domain_type=domain_type, custom_inventions=custom_inventions)

        elif name == "evaluate_feature_co_creation":
            feature_name = args.get("feature_name", "Interactive Filter")
            domain_context = args.get("domain_context", "Enterprise SaaS")
            critique = evaluate_feature_internally(feature_name=feature_name, domain_context=domain_context)
            dialogue = generate_concise_co_creation_dialogue([critique])
            payload = {
                "internal_evaluation": critique,
                "concise_co_creation_dialogue": dialogue
            }

        elif name == "harvest_ideas_and_co_create":
            domain = args.get("domain", "saas")
            payload = harvest_and_curate_ideas(domain_context=domain)

        elif name == "inject_live_app_feature":
            target_file = args.get("target_file", "web/apex_app.html")
            feature_id = args.get("feature_id", "FEAT-SPLIT-FILTER")
            payload = inject_feature_into_file(target_file_path=target_file, feature_id=feature_id)

        elif name == "blend_proven_ui_components":
            query = args.get("query", "saas")
            comp_ids = args.get("component_ids", None)
            inject_target = args.get("inject_target_file", None)
            from scripts.proven_component_harmonizer import ProvenComponentHarmonizer
            harmonizer = ProvenComponentHarmonizer()
            if inject_target:
                payload = harmonizer.inject_harmonized_components_into_file(inject_target, query, comp_ids)
            else:
                payload = harmonizer.harmonize_ui_components(query, comp_ids)

        elif name == "quantum_optimize_design":
            candidates = args.get("candidates", [])
            from scripts.quantum_design_optimizer import QuantumDesignOptimizer
            optimizer = QuantumDesignOptimizer()
            payload = optimizer.select_optimal_design(candidates)

        elif name == "synthesize_full_stack_triad":
            vision = args.get("vision", "High-Performance Cloud Core")
            sector = args.get("sector", "Enterprise SaaS")
            brand = args.get("brand_name", None)
            output_dir = args.get("output_dir", None)
            from scripts.full_stack_triad_engine import FullStackTriadEngine
            engine = FullStackTriadEngine()
            result = engine.synthesize_full_stack_triad(vision, sector, brand)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
                    f.write(result["pillars"]["pillar_2_frontend_design"]["generated_html_code"])
                with open(os.path.join(output_dir, "server.py"), "w", encoding="utf-8") as f:
                    f.write(result["pillars"]["pillar_3_backend_systems"]["edge_service_python"])
                with open(os.path.join(output_dir, "schema.sql"), "w", encoding="utf-8") as f:
                    f.write(result["pillars"]["pillar_3_backend_systems"]["database_sql_schema"])
                result["written_output_dir"] = os.path.abspath(output_dir)
            payload = result

        elif name == "ground_academic_foundations":
            domain = args.get("domain", "systems architecture")
            problem = args.get("problem_statement", "")
            from scripts.academic_foundations_engine import AcademicFoundationsEngine
            engine = AcademicFoundationsEngine()
            payload = engine.ground_domain(domain, problem)

        elif name == "synthesize_master_logo_and_icons":
            concept = args.get("concept", "Apex System")
            archetype = args.get("archetype", "negative_space_monolith")
            medium = args.get("medium", "vector_silkscreen")
            engine_name = args.get("engine", "midjourney")
            from scripts.graphic_design_mastery_engine import GraphicDesignMasteryEngine
            gd_engine = GraphicDesignMasteryEngine()
            eval_res = gd_engine.evaluate_paul_rand_test(concept, f"Master brandmark for {concept}", archetype)
            prompt_res = gd_engine.synthesize_master_prompt(concept, archetype, medium, engine_name)
            svg_res = gd_engine.generate_parametric_svg(concept, archetype)
            payload = {
                "concept": concept,
                "archetype": archetype,
                "paul_rand_evaluation": eval_res,
                "master_prompts": prompt_res,
                "parametric_svg": svg_res
            }

        elif name == "synthesize_hyper_originality":
            domain = args.get("domain", "systems architecture")
            baseline_code = args.get("baseline_code", "")
            target_mult = args.get("target_multiplier", "both")
            from scripts.hyper_originality_engine import HyperOriginalityEngine
            ho_engine = HyperOriginalityEngine()
            score = ho_engine.calculate_code_originality_score(baseline_code) if baseline_code else None
            ten_x = ho_engine.synthesize_ten_x_architecture(domain, baseline_code) if target_mult in ("10x", "both") else None
            hundred_x = ho_engine.synthesize_hundred_x_breakthrough(domain) if target_mult in ("100x", "both") else None
            payload = {
                "domain": domain,
                "baseline_originality_analysis": score,
                "ten_x_elevation": ten_x,
                "hundred_x_frontier_breakthrough": hundred_x
            }

        elif name == "benchmark_and_close_skill_gaps":
            from scripts.skill_benchmark_and_gap_closer import SkillBenchmarkAndGapCloser
            engine = SkillBenchmarkAndGapCloser()
            payload = engine.execute_competitive_teardown()

        elif name == "execute_self_healing_verification":
            cmd = args.get("test_command", "python -m unittest discover tests")
            attempts = int(args.get("max_attempts", 3))
            from scripts.self_healing_code_engine import SelfHealingCodeEngine
            engine = SelfHealingCodeEngine()
            payload = engine.execute_self_healing_loop(cmd, attempts)

        elif name == "amplify_model_test_time_compute":
            problem = args.get("problem", "High-concurrency state synchronization")
            domain = args.get("domain", "Distributed Systems")
            from scripts.test_time_compute_engine import TestTimeComputeEngine
            engine = TestTimeComputeEngine()
            payload = engine.amplify_model_reasoning(problem, domain)

        elif name == "synthesize_generative_ui_widget":
            wtype = args.get("widget_type", "telemetry_pulse")
            title = args.get("title", "Live Telemetry Pulse")
            from scripts.generative_ui_widget_synthesizer import GenerativeUIWidgetSynthesizer
            engine = GenerativeUIWidgetSynthesizer()
            if wtype == "interactive_calculator":
                payload = engine.synthesize_slider_calculator_widget(title=title)
            else:
                payload = engine.synthesize_telemetry_widget(title=title)

        else:
            raise ValueError(f"Unknown tool name: {name}")

        latency_ms = (time.perf_counter() - start_time) * 1000.0

        return {
            "result": payload,
            "execution_latency_ms": round(latency_ms, 3),
            "tool_status": "SUCCESS",
        }

    def handle_request(self, req_json_str: str) -> str:
        try:
            req = json.loads(req_json_str)
        except Exception as e:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {str(e)}"}
            })

        req_id = req.get("id")
        method = req.get("method")

        if method == "initialize":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}, "resources": {}},
                    "serverInfo": {
                        "name": "zobar-mcp-engine",
                        "version": "2.0.0",
                        "description": "Live production-grade MCP server for Zobar Skill"
                    }
                }
            })

        elif method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"tools": self.get_tools_manifest()}
            })

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})
            try:
                tool_output = self.execute_tool(name, args)
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(tool_output, ensure_ascii=False)}],
                        "isError": False
                    }
                }, ensure_ascii=False)
            except Exception as e:
                return json.dumps({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": f"Tool execution failed: {str(e)}"}],
                        "isError": True
                    }
                })

        return json.dumps({
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method '{method}' not found"}
        })


def run_stdio_server():
    if sys.platform == "win32":
        try:
            sys.stdin.reconfigure(encoding="utf-8")
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    server = ZobarMCPServer()
    for line in sys.stdin:
        line_clean = line.strip()
        if line_clean:
            response = server.handle_request(line_clean)
            sys.stdout.write(response + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    run_stdio_server()
