#!/usr/bin/env python3
"""
Unit Test Suite for Zobar Skill Stage 9 Frontier Expansion:
1. REA Reverse Engineering & Clean-Room Legal Safe Harbors (EU 2009/24/EC, DMCA 1201(f)).
2. Game Modding & Voxel / Minecraft Bridge Engine (Greedy Meshing & Mixin/Harmony hooks).
3. Multi-Agent Deliberation Council (Academic, Public, Workforce & Ratified Senate).
4. Non-Repetitive Creative Evolutionary Designer (Novelty Divergence >= 0.75 & Genetic UI).
"""

import unittest
import os
import json
import tempfile

from scripts.reverse_engineering_analyst import (
    detect_binary_format, extract_strings_and_symbols,
    evaluate_reverse_engineering_legality, generate_clean_room_specification,
    analyze_target_system
)
from scripts.game_modding_engine import (
    calculate_greedy_meshing_metrics, synthesize_minecraft_in_game_bridge,
    generate_mod_code_template, MODDING_TARGETS
)
from scripts.multi_agent_deliberation_council import (
    simulate_academic_council, simulate_public_assembly,
    simulate_workforce_council, simulate_systems_engineering_board,
    conduct_executive_board_deliberation
)
from scripts.creative_evolutionary_designer import (
    calculate_novelty_divergence, generate_evolutionary_design,
    MATERIALS, GEOMETRIES, LIGHTING_AND_CHROMA, KINETIC_PHYSICS
)
from scripts.zobar_mcp_server import ZobarMCPServer

class TestReverseEngineeringAnalyst(unittest.TestCase):
    def test_magic_binary_detection(self):
        elf_bytes = b"\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        res_elf = detect_binary_format(elf_bytes)
        self.assertTrue(res_elf["identified"])
        self.assertTrue(res_elf["executable"])
        self.assertIn("ELF", res_elf["format"])

        pe_bytes = b"MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00"
        res_pe = detect_binary_format(pe_bytes)
        self.assertTrue(res_pe["identified"])
        self.assertIn("PE/COFF", res_pe["format"])

        wasm_bytes = b"\x00asm\x01\x00\x00\x00"
        res_wasm = detect_binary_format(wasm_bytes)
        self.assertTrue(res_wasm["identified"])
        self.assertIn("WebAssembly", res_wasm["format"])

    def test_string_symbol_extraction(self):
        sample = b"junk\x00\x01\x02http://api.service.internal/v1/user\x00init_renderer\x00short\x00"
        symbols = extract_strings_and_symbols(sample, min_length=4)
        self.assertTrue(any("api.service.internal" in s for s in symbols))
        self.assertTrue(any("init_renderer" in s for s in symbols))

    def test_legal_safe_harbor_interoperability(self):
        legal = evaluate_reverse_engineering_legality(
            intent="Interoperability with our independent client adapter",
            target_name="LegacyServerProtocol"
        )
        self.assertIn("Yeşil", legal["risk_level"])
        self.assertTrue(legal["clean_room_mandate_required"])
        self.assertTrue(any("Sega Enterprises" in sh["precedent"] for sh in legal["recognized_safe_harbors"]))
        self.assertTrue(any("Directive 2009/24/EC" in sh["statute"] for sh in legal["recognized_safe_harbors"]))

    def test_legal_drm_circumvention_violation(self):
        illegal = evaluate_reverse_engineering_legality(
            intent="Crack and bypass license protection for cloning",
            target_name="CommercialProduct",
            has_circumvented_drm=True
        )
        self.assertIn("Kırmızı", illegal["risk_level"])
        self.assertTrue(len(illegal["statutory_violations_or_cautions"]) >= 1)

    def test_clean_room_specification_generation(self):
        interfaces = [
            {"name": "auth_handshake", "type": "Network Protocol", "behavior": "Exchanges public ECDSA keys."},
            {"name": "render_tick", "type": "Exported Symbol", "behavior": "Performs double-buffered draw call."}
        ]
        fsd = generate_clean_room_specification("TestEngine", interfaces)
        self.assertEqual(len(fsd["functional_specifications"]), 2)
        self.assertIn("Chinese Wall", fsd["protocol"])
        self.assertIn("Clean Room Affidavit", fsd["legal_defensibility"])

class TestGameModdingAndVoxelEngine(unittest.TestCase):
    def test_greedy_meshing_mathematics(self):
        metrics = calculate_greedy_meshing_metrics(chunk_dimensions=(16, 16, 256), fill_ratio=0.45)
        self.assertGreater(metrics["naive_mesh"]["triangles"], metrics["greedy_mesh"]["triangles"])
        self.assertGreater(metrics["optimization"]["triangle_reduction_percentage"], 80.0)
        self.assertGreater(metrics["greedy_mesh"]["draw_call_reduction_ratio"], 5.0)

    def test_minecraft_bridge_architecture(self):
        bridge_unity = synthesize_minecraft_in_game_bridge("Unity")
        self.assertIn("Job System", bridge_unity["core_architecture"]["mesh_pipeline"])
        self.assertTrue(len(bridge_unity["protocol_bridge_steps"]) >= 4)

        bridge_unreal = synthesize_minecraft_in_game_bridge("Unreal")
        self.assertIn("ProceduralMeshComponent", bridge_unreal["core_architecture"]["mesh_pipeline"])

    def test_mod_code_synthesis(self):
        fabric_mod = generate_mod_code_template("Minecraft", "Custom Player Speed Boost")
        self.assertIn("PlayerSpeedMixin.java", fabric_mod["source_filename"])
        self.assertIn("@Mixin(PlayerEntity.class)", fabric_mod["code_snippet"])
        self.assertIn("@Inject", fabric_mod["code_snippet"])

        unity_mod = generate_mod_code_template("Unity", "Physics Movement Detour")
        self.assertIn("PluginPatch.cs", unity_mod["source_filename"])
        self.assertIn("[HarmonyPatch", unity_mod["code_snippet"])
        self.assertIn("BaseUnityPlugin", unity_mod["code_snippet"])

class TestMultiAgentDeliberationCouncil(unittest.TestCase):
    def test_academic_council_scoring_and_citations(self):
        acad = simulate_academic_council("Distributed Voxel Engine with P2P Consensus")
        self.assertGreaterEqual(acad["score"], 70)
        self.assertEqual(acad["verdict"], "ONAY")
        self.assertTrue(any("Knuth" in c for c in acad["key_citations"]))

    def test_public_assembly_rejection_of_invasive_systems(self):
        pub_clean = simulate_public_assembly("Accessible Glassy Design Modding Sandbox")
        self.assertGreaterEqual(pub_clean["score"], 70)
        self.assertEqual(pub_clean["verdict"], "HALK DESTEĞİ")

        pub_invasive = simulate_public_assembly("Workplace Employee Biometric Emotion Tracking and Dismissal")
        self.assertLess(pub_invasive["score"], 50)
        self.assertEqual(pub_invasive["verdict"], "TOPLUMSAL VETO")

    def test_chief_engineering_board_audit_and_contributions(self):
        eng = simulate_systems_engineering_board("Zero-Copy Lock-Free RingBuffer Telemetry Pipeline")
        self.assertGreaterEqual(eng["score"], 80)
        self.assertEqual(eng["verdict"], "MÜHENDİSLİK MÜHRÜ HAZIR")
        self.assertTrue(len(eng["engineering_detail_audit"]) >= 3)
        self.assertTrue(len(eng["chief_engineer_contributions"]) >= 3)
        self.assertTrue(any("RingBuffer" in c for c in eng["chief_engineer_contributions"]))

    def test_executive_board_deliberation_consensus_and_chief_oversight(self):
        council = conduct_executive_board_deliberation("Zero-Copy Voxel Rendering Engine with Open Source Protocol")
        self.assertGreaterEqual(council["consensus_score"], 70.0)
        self.assertIn("ONAYLANDI", council["final_resolution"])
        self.assertEqual(len(council["debate_transcript"]), 3)
        self.assertIn("academic", council["council_scores"])
        self.assertIn("public", council["council_scores"])
        self.assertIn("workforce", council["council_scores"])
        self.assertIn("chief_engineering", council["council_scores"])

        gate = council["chief_engineer_final_oversight"]
        self.assertTrue(gate["seal_granted"])
        self.assertIn("Dr. Zobar", gate["lead_architect_signature"])
        self.assertTrue(len(gate["microscopic_flaw_summary"]) >= 3)
        self.assertTrue(len(gate["injected_architectural_contributions"]) >= 3)

    def test_chief_engineer_veto_or_conditional_oversight(self):
        fragile = conduct_executive_board_deliberation("Monolith with unbounded global lock polling sleep")
        gate = fragile["chief_engineer_final_oversight"]
        self.assertTrue("CHIEF ENGINEER" in gate["oversight_status"] or "VETO" in gate["oversight_status"])
        self.assertLess(fragile["council_scores"]["chief_engineering"]["score"], 60)

class TestCreativeEvolutionaryDesigner(unittest.TestCase):
    def test_novelty_divergence_calculation(self):
        history = [
            {"material_name": "Bioluminescent Organic Glass", "geometry_name": "Asymmetric Bento with Variable Aspect Ratios", "palette_name": "Emerald Bio-Grid", "physics_type": "Apple 2nd-Order Spring"}
        ]
        # Candidate with exact identical chromosomes
        candidate_identical = {
            "material": {"name": "Bioluminescent Organic Glass"},
            "geometry": {"name": "Asymmetric Bento with Variable Aspect Ratios"},
            "chroma": {"palette": "Emerald Bio-Grid"},
            "physics": {"type": "Apple 2nd-Order Spring"}
        }
        dist_zero = calculate_novelty_divergence(candidate_identical, history)
        self.assertEqual(dist_zero, 0.0)

        # Candidate with all distinct chromosomes
        candidate_distinct = {
            "material": {"name": "Kinetic Neo-Brutalist Concrete"},
            "geometry": {"name": "Monospaced Swiss Data Grid"},
            "chroma": {"palette": "Monochrome Acid Lime"},
            "physics": {"type": "High-Tension Snap"}
        }
        dist_full = calculate_novelty_divergence(candidate_distinct, history)
        self.assertEqual(dist_full, 1.0)

    def test_evolutionary_design_generation(self):
        res = generate_evolutionary_design("Autonomous Quantum Operating System", seed=42)
        self.assertIn("EVO-", res["design_id"])
        self.assertGreaterEqual(res["novelty_divergence_score"], 0.70)
        self.assertIn("Standart Bootstrap/Shadcn", res["cliche_avoidance_gate"])
        self.assertIn("export const EvolvedNovelCard", res["react_component_code"])
        self.assertIn("framer-motion", res["react_component_code"])

class TestMCPStage9ToolsIntegration(unittest.TestCase):
    def setUp(self):
        self.server = ZobarMCPServer()

    def test_mcp_manifest_contains_15_tools(self):
        tools = self.server.get_tools_manifest()
        self.assertEqual(len(tools), 15)
        names = [t["name"] for t in tools]
        self.assertIn("analyze_reverse_engineering", names)
        self.assertIn("generate_game_mod_architecture", names)
        self.assertIn("deliberate_council", names)
        self.assertIn("generate_evolutionary_design", names)

    def test_mcp_execute_reverse_engineering(self):
        res = self.server.execute_tool("analyze_reverse_engineering", {
            "target_name": "DiscordVoiceGateway",
            "intent": "Interoperability with custom Linux bot client"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertIn("ELF", res["result"]["binary_analysis"]["format"])
        self.assertIn("Yeşil", res["result"]["legal_safe_harbor_audit"]["risk_level"])

    def test_mcp_execute_game_mod(self):
        res = self.server.execute_tool("generate_game_mod_architecture", {
            "target_game": "Minecraft",
            "mod_feature": "Low-Latency Voxel Packet Synchronizer"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertIn("greedy_meshing_optimization", res["result"])
        self.assertGreater(res["result"]["greedy_meshing_optimization"]["optimization"]["triangle_reduction_percentage"], 80.0)

    def test_mcp_execute_deliberate_council(self):
        res = self.server.execute_tool("deliberate_council", {
            "topic": "Deterministic Pure-Python Voxel Subsystem"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertIn("consensus_score", res["result"])
        self.assertIn("final_resolution", res["result"])

    def test_mcp_execute_evolutionary_design(self):
        res = self.server.execute_tool("generate_evolutionary_design", {
            "domain_context": "Deep Space Telemetry Dashboard"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertIn("EVO-", res["result"]["design_id"])
        self.assertGreaterEqual(res["result"]["novelty_divergence_score"], 0.70)

if __name__ == "__main__":
    unittest.main()
