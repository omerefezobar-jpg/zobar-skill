"""
Stage 4 Voice, Hardware Acceleration, and Unit Economics Tests
Unit tests for DiscordSFURouter, ElevenLabsStreamingTTS, PagedAttentionManager,
SpeculativeDecodingSimulator, ModelQuantizationBenchmark, and UnitEconomicsSimulator.
"""

import unittest
from scripts.realtime_audio_voice_engine import DiscordSFURouter, ElevenLabsStreamingTTS
from scripts.llm_hardware_accelerator import (
    PagedAttentionManager,
    SpeculativeDecodingSimulator,
    ModelQuantizationBenchmark,
)
from scripts.unit_economics_investor_simulator import UnitEconomicsSimulator


class TestStage4VoiceHardwareInvestor(unittest.TestCase):
    def test_discord_sfu_router(self):
        sfu = DiscordSFURouter(room_id="voice-room-42")
        sfu.join_room("alice")
        sfu.join_room("bob")
        sfu.join_room("charlie")

        self.assertEqual(len(sfu.participants), 3)

        # Alice speaks -> should be routed to Bob and Charlie
        routes = sfu.route_audio_packet("alice", b"\x01\x02\x03\x04", is_speaking=True)
        self.assertEqual(len(routes), 2)
        recipients = [r[0] for r in routes]
        self.assertIn("bob", recipients)
        self.assertIn("charlie", recipients)
        self.assertNotIn("alice", recipients)
        self.assertEqual(routes[0][1].payload_bytes, b"\x01\x02\x03\x04")

        # Alice stops speaking (VAD silent) -> zero packets forwarded
        silent_routes = sfu.route_audio_packet("alice", b"", is_speaking=False)
        self.assertEqual(len(silent_routes), 0)

        # Charlie leaves
        sfu.leave_room("charlie")
        self.assertEqual(len(sfu.participants), 2)

    def test_elevenlabs_streaming_tts(self):
        tts = ElevenLabsStreamingTTS(voice_id="narrator_tr")
        tts.set_speaker_embedding({"pitch_norm": 1.15, "cadence": 1.0})
        self.assertEqual(tts.speaker_embedding["pitch_norm"], 1.15)

        sample_text = "Gelişmiş sesli modeller, gerçek zamanlı konuşmaları milisaniyeler içinde dönüştürür."
        frames = tts.stream_synthesize(sample_text)

        self.assertGreater(len(frames), 1)
        # First chunk simulates sub-180ms TTFB
        self.assertLess(frames[0]["simulated_generation_latency_ms"], 180.0)
        self.assertEqual(frames[0]["voice_id"], "narrator_tr")

    def test_paged_attention_vram_savings(self):
        paged = PagedAttentionManager(page_size=16, bytes_per_token_kv=128)
        res = paged.calculate_savings(num_concurrent_requests=32, max_seq_len=4096, avg_seq_len=1024)

        self.assertGreater(res["vram_savings_percent"], 50.0)
        self.assertGreater(res["vram_saved_mb"], 10.0)
        self.assertGreater(res["throughput_multiplier"], 2.0)

    def test_speculative_decoding_speedup(self):
        spec = SpeculativeDecodingSimulator(draft_model_cost_ratio=0.06)
        res = spec.simulate(k_speculative_tokens=4, acceptance_rate=0.80)

        self.assertGreater(res["theoretical_speedup_factor"], 2.0)
        self.assertGreater(res["target_model_forward_passes_saved_percent"], 50.0)

    def test_model_quantization_profile(self):
        profile = ModelQuantizationBenchmark.profile(param_count_billions=70.0)
        self.assertEqual(profile["fp16_vram_gb"], 140.0)
        self.assertLess(profile["int4_awq_vram_gb"], 45.0)
        self.assertGreater(profile["awq_vram_compression_ratio"], 3.0)

    def test_unit_economics_and_investor_grade(self):
        sim = UnitEconomicsSimulator(
            arpu_monthly_usd=49.0,
            monthly_churn_rate=0.03,  # 3% monthly churn
            gross_margin=0.85,
            cac_usd=100.0,
        )
        metrics = sim.calculate_metrics()

        self.assertGreater(metrics["ltv_cac_ratio"], 10.0)
        self.assertLess(metrics["payback_period_months"], 3.0)
        self.assertTrue(metrics["is_tier1_investor_grade"])

        # Asymmetric compounding test
        comp = sim.simulate_asymmetric_payoff(months=12, initial_customers=10, monthly_growth_rate=0.15)
        self.assertGreater(comp["final_paying_users"], 10)
        self.assertGreater(comp["ending_arr_usd"], 5000.0)
        self.assertIn("0$", comp["downside_risk"])


if __name__ == "__main__":
    unittest.main()
