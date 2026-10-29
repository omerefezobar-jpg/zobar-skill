#!/usr/bin/env python3
"""
Unit tests for Advanced Reverse Engineering (7-Phase Pipeline) & Safe Harbors.
Verifies binary parsing (PE/ELF), Shannon entropy, ISA CFG reconstruction,
McCabe cyclomatic complexity, TLV protocol dissection, CAN-Bus decoding,
and clean-room affidavit generation.
"""

import unittest
import struct
import json
from scripts.reverse_engineering_analyst import (
    calculate_shannon_entropy,
    parse_executable_headers,
    reconstruct_basic_cfg,
    dissect_binary_protocol,
    decode_can_bus_frame,
    generate_clean_room_affidavit,
    execute_7phase_re_pipeline,
    detect_binary_format,
    analyze_target_system
)
from scripts.zobar_mcp_server import ZobarMCPServer

class TestAdvancedReverseEngineering(unittest.TestCase):
    def test_shannon_entropy_calculation(self):
        # Empty data
        res_empty = calculate_shannon_entropy(b"")
        self.assertEqual(res_empty["entropy"], 0.0)
        self.assertFalse(res_empty["is_packed_or_encrypted"])

        # Low/Normal entropy plain ASCII text
        res_plain = calculate_shannon_entropy(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * 10)
        self.assertLess(res_plain["entropy"], 6.0)
        self.assertFalse(res_plain["is_packed_or_encrypted"])

        # High entropy pseudorandom data (simulating packed executable)
        high_entropy_bytes = bytes(range(256)) * 4
        res_packed = calculate_shannon_entropy(high_entropy_bytes)
        self.assertGreater(res_packed["entropy"], 7.5)
        self.assertTrue(res_packed["is_packed_or_encrypted"])

    def test_pe_coff_header_parsing(self):
        # Construct synthetic PE binary
        pe = bytearray(256)
        pe[0:2] = b"MZ"
        pe[0x3C:0x40] = struct.pack("<I", 0x80) # e_lfanew
        pe[0x80:0x84] = b"PE\x00\x00"
        pe[0x84:0x86] = struct.pack("<H", 0x8664) # AMD64 / x86_64
        pe[0x86:0x88] = struct.pack("<H", 6)      # 6 sections
        pe[0x88:0x8C] = struct.pack("<I", 1700000000)

        parsed = parse_executable_headers(bytes(pe))
        self.assertEqual(parsed["format"], "Windows PE/COFF")
        self.assertIn("x86_64", parsed["machine_architecture"])
        self.assertEqual(parsed["number_of_sections"], 6)

    def test_elf_header_parsing(self):
        # Construct synthetic ELF64 Little-Endian binary
        elf = bytearray(64)
        elf[0:4] = b"\x7fELF"
        elf[4] = 2 # 64-bit
        elf[5] = 1 # Little endian
        elf[16:18] = struct.pack("<H", 2)    # EXEC
        elf[18:20] = struct.pack("<H", 0x3E) # AMD64 / x86_64
        elf[24:32] = struct.pack("<Q", 0x401000) # Entry point

        parsed = parse_executable_headers(bytes(elf))
        self.assertEqual(parsed["format"], "ELF")
        self.assertEqual(parsed["bitness"], 64)
        self.assertIn("Little Endian", parsed["endianness"])
        self.assertIn("AMD64", parsed["machine_architecture"])
        self.assertEqual(parsed["entry_point"], "0x401000")

    def test_cfg_reconstruction_and_cyclomatic_complexity(self):
        # Sequence: NOP (90), JZ +4 (74 04), NOP NOP (90 90), JMP +2 (EB 02), NOP (90), RET (C3)
        code = b"\x90\x74\x04\x90\x90\xEB\x02\x90\xC3"
        cfg = reconstruct_basic_cfg(code, base_address=0x1000)
        
        self.assertGreaterEqual(cfg["basic_blocks_count"], 2)
        self.assertGreaterEqual(cfg["edges_count"], 1)
        self.assertGreaterEqual(cfg["cyclomatic_complexity"], 1)
        self.assertTrue(any(e["type"] == "true_branch" for e in cfg["edges"]))

    def test_binary_protocol_dissection(self):
        # TLV packets: Tag 0x01, Len 4, "TEST" + Tag 0x02, Len 5, "HELLO"
        pkt = b"\x01\x04TEST\x02\x05HELLO"
        dissected = dissect_binary_protocol(pkt)
        
        self.assertEqual(dissected["framing_type"], "TLV (Type-Length-Value)")
        self.assertEqual(len(dissected["tlv_records_detected"]), 2)
        self.assertEqual(dissected["tlv_records_detected"][0]["value_ascii"], "TEST")
        self.assertIn("crc32", dissected["checksum_signatures"])

    def test_can_bus_frame_decoding(self):
        # CAN frame with 8-byte payload
        payload = struct.pack("<H", 1250) + struct.pack(">H", 3400) + b"\x00\x00\x00\x00"
        can_res = decode_can_bus_frame(can_id=0x18FEE000, payload=payload)
        
        self.assertEqual(can_res["frame_type"], "Extended CAN 2.0B (29-bit)")
        self.assertEqual(can_res["extracted_signals"]["word0_intel_le"], 1250)
        self.assertEqual(can_res["extracted_signals"]["word0_motorola_be"], struct.unpack(">H", payload[:2])[0])

    def test_clean_room_affidavit_generation(self):
        affidavit_clean = generate_clean_room_affidavit(
            engineer_name="Ada Lovelace",
            module_name="CleanClientEngine",
            specification_version="2.1.0",
            is_clean_room_developer=True
        )
        self.assertIn("Clean Room Developer", affidavit_clean["role"])
        self.assertIn("solely and exclusively from the functional interface specification", affidavit_clean["formal_statement"])
        self.assertIn("DMCA", affidavit_clean["statutory_compliance"])

        affidavit_dirty = generate_clean_room_affidavit(
            engineer_name="Alan Turing",
            module_name="CleanClientEngine",
            specification_version="2.1.0",
            is_clean_room_developer=False
        )
        self.assertIn("Dirty Room Analyst", affidavit_dirty["role"])

    def test_full_7phase_pipeline_execution(self):
        sample = b"\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00>\x00\x01\x00\x00\x00\x90\xC3\x00http://api.service.internal/v1\x00"
        pipeline = execute_7phase_re_pipeline(
            target_name="AutonomousVehicleTelemetry",
            intent="Clean-room interoperability adapter",
            binary_sample=sample
        )
        self.assertIn("phase1_static_triage", pipeline)
        self.assertIn("phase2_isa_cfg", pipeline)
        self.assertIn("phase3_ir_ast", pipeline)
        self.assertIn("phase4_protocol_dissection", pipeline)
        self.assertIn("phase5_hardware_bus", pipeline)
        self.assertIn("phase6_clean_room_legal", pipeline)
        self.assertIn("phase7_differential_verification", pipeline)

    def test_mcp_execute_reverse_engineering_7phase(self):
        server = ZobarMCPServer()
        res = server.execute_tool("analyze_reverse_engineering", {
            "target_name": "ProprietarySmartMeter",
            "intent": "Interoperability interface extraction",
            "full_7_phases": True
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        payload = res["result"]
        self.assertIn("phase1_static_triage", payload)
        self.assertIn("phase6_clean_room_legal", payload)

    def test_phase8_anti_analysis_and_obfuscation(self):
        from scripts.reverse_engineering_analyst import detect_anti_analysis_and_obfuscation
        code_with_rdtsc_and_peb = b"\x90\x0f\x31\x64\xa1\x30\x00\x00\x00\xcc\xc3"
        analysis = detect_anti_analysis_and_obfuscation(code_with_rdtsc_and_peb)
        self.assertTrue(analysis["anti_analysis_detected"])
        self.assertTrue(any("RDTSC" in p["signature"] for p in analysis["obfuscation_patterns"]))
        self.assertTrue(any("PEB" in p["type"] for p in analysis["obfuscation_patterns"]))

    def test_phase9_firmware_mmio_and_fuzzing(self):
        from scripts.reverse_engineering_analyst import simulate_firmware_mmio_and_fuzz
        sample_fw = b"\x00\x20\x00\x20\x09\x00\x00\x08"
        fuzz_sim = simulate_firmware_mmio_and_fuzz(sample_fw)
        self.assertIn("UART0_DATA_REGISTER", fuzz_sim["peripheral_memory_map"])
        self.assertIn("12,500 executions/second", fuzz_sim["in_memory_snapshot_fuzzing"]["snapshot_reset_throughput_target"])
        self.assertIn("Heap-buffer-overflow (CWE-122)", fuzz_sim["in_memory_snapshot_fuzzing"]["asan_fault_triage"])

    def test_phase10_binary_diffing_and_shims(self):
        from scripts.reverse_engineering_analyst import diff_binary_graphs
        cfg_v1 = {"basic_blocks_count": 10, "cyclomatic_complexity": 5}
        cfg_v2 = {"basic_blocks_count": 13, "cyclomatic_complexity": 7}
        diff = diff_binary_graphs(base_cfg=cfg_v1, target_cfg=cfg_v2)
        self.assertEqual(diff["diff_metrics"]["block_delta"], 3)
        self.assertEqual(diff["diff_metrics"]["cyclomatic_delta"], 2)
        self.assertIn("Patch / Security Fix", diff["mutation_classification"])
        self.assertIn("class InteroperabilityShim", diff["resilient_interoperability_shim"])

    def test_execute_10phase_re_pipeline_and_mcp(self):
        from scripts.reverse_engineering_analyst import execute_10phase_re_pipeline
        pipeline = execute_10phase_re_pipeline("NextGenTelemetryUnit", intent="Independent Adapter")
        self.assertTrue(pipeline["ten_phase_certified"])
        self.assertIn("phase8_anti_analysis_deobfuscation", pipeline)
        self.assertIn("phase9_firmware_mmio_fuzzing", pipeline)
        self.assertIn("phase10_binary_diffing_shims", pipeline)

        server = ZobarMCPServer()
        res = server.execute_tool("analyze_reverse_engineering", {
            "target_name": "NextGenTelemetryUnit",
            "intent": "Independent Adapter",
            "full_10_phases": True
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertTrue(res["result"]["ten_phase_certified"])

    def test_production_cleaner_sanitization(self):
        from scripts.production_cleaner import sanitize_production_output, inspect_cleanliness
        dirty_input = "Bu proje Zobar Mühendislik standardı ve Zobar Skill mimarisi ile inşa edilmiştir."
        cleaned = sanitize_production_output(dirty_input, custom_project_name="NexusEnterprise")
        self.assertNotIn("Zobar Mühendislik", cleaned)
        self.assertNotIn("Zobar Skill", cleaned)
        self.assertIn("Enterprise Engineering", cleaned)
        audit = inspect_cleanliness(cleaned)
        self.assertTrue(audit["is_production_clean"])
        self.assertEqual(audit["cleanliness_score"], 100.0)

    def test_reverse_engineering_studio_server_endpoints(self):
        import urllib.request
        import threading
        import time
        from http.server import HTTPServer
        from scripts.reverse_engineering_server import StudioRequestHandler

        test_port = 8993
        server = HTTPServer(('127.0.0.1', test_port), StudioRequestHandler)
        t = threading.Thread(target=server.serve_forever, daemon=True)
        t.start()
        time.sleep(0.1)

        try:
            # 1. Health endpoint test
            with urllib.request.urlopen(f'http://127.0.0.1:{test_port}/api/health') as resp:
                self.assertEqual(resp.status, 200)
                data = json.loads(resp.read().decode('utf-8'))
                self.assertEqual(data["status"], "ONLINE")
                self.assertEqual(data["phases_supported"], 10)

            # 2. Analyze POST endpoint test
            sample_payload = b"\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00>\x00\x01\x00\x00\x00"
            req = urllib.request.Request(
                f'http://127.0.0.1:{test_port}/api/analyze',
                data=sample_payload,
                headers={'Content-Type': 'application/octet-stream'}
            )
            with urllib.request.urlopen(req) as resp:
                self.assertEqual(resp.status, 200)
                analysis = json.loads(resp.read().decode('utf-8'))
                self.assertTrue(analysis["ten_phase_certified"])
                self.assertIn("phase1_static_triage", analysis)
        finally:
            server.shutdown()
            server.server_close()

if __name__ == "__main__":
    unittest.main()
