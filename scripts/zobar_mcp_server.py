"""
Zobar Real-Time MCP (Model Context Protocol) Server
Production-Grade JSON-RPC 2.0 Live Server over stdio

Provides 8 live, fully-functional tools connected directly to Zobar Skill core engines:
1. semantic_cache_query   -> scripts.semantic_cache.SemanticCache
2. smart_route            -> scripts.smart_model_router.SmartModelRouter
3. audit_supabase_sql     -> scripts.supabase_db_optimizer.SupabaseDBOptimizer
4. compress_context       -> scripts.context_compressor.ContextCompressor
5. recall_user_memory     -> scripts.continual_memory_engine.ContinualMemoryEngine
6. simulate_unit_economics-> scripts.unit_economics_investor_simulator.UnitEconomicsSimulator
7. generate_image_prompt  -> scripts.image_prompt_synthesizer.ImagePromptSynthesizer
8. step_ecs_simulation    -> scripts.ecs_game_engine (ECSWorld + GameLoop)
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


class ZobarMCPServer:
    def __init__(self):
        self.semantic_cache = SemanticCache()
        self.model_router = SmartModelRouter(semantic_cache=self.semantic_cache)
        self.context_compressor = ContextCompressor()
        self.memory_engine = ContinualMemoryEngine()
        self.image_synthesizer = ImagePromptSynthesizer()
        self.asset_vault = AssetVaultQueryEngine()

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
