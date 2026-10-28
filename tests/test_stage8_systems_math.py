"""
Stage 8 Systems Engineering & Mathematical Modeling Tests
Unit tests for SystemsMathEngine and calculate_systems_math MCP integration.
"""

import unittest
from scripts.systems_math_engine import SystemsMathEngine
from scripts.zobar_mcp_server import ZobarMCPServer


class TestStage8SystemsMath(unittest.TestCase):
    def setUp(self):
        self.server = ZobarMCPServer()

    def test_roofline_memory_bound_detection(self):
        # 100 GFLOPs with 10 GB transferred = 10 FLOPs/Byte (Memory bound on A100)
        res = SystemsMathEngine.calculate_roofline_analysis(
            total_flops=1e11,
            total_bytes_transferred=1e10,
            hardware_target="nvidia_a100_80gb"
        )
        self.assertEqual(res["bottleneck_classification"], "MEMORY_BANDWIDTH_BOUND")
        self.assertEqual(res["arithmetic_intensity_flops_per_byte"], 10.0)
        self.assertIn("PagedAttention", res["optimization_recommendation"])

    def test_roofline_compute_bound_detection(self):
        # 100 TFLOPs with 100 MB transferred = 1,000,000 FLOPs/Byte (Compute bound)
        res = SystemsMathEngine.calculate_roofline_analysis(
            total_flops=1e14,
            total_bytes_transferred=1e8,
            hardware_target="nvidia_a100_80gb"
        )
        self.assertEqual(res["bottleneck_classification"], "COMPUTE_ALU_BOUND")
        self.assertEqual(res["attainable_tflops"], 312.0)

    def test_queueing_theory_stable_and_unstable(self):
        # Stable queue: lambda=400, mu=500 -> rho=0.8
        stable = SystemsMathEngine.calculate_queueing_latency(
            arrival_rate_lambda=400.0,
            service_rate_mu=500.0
        )
        self.assertEqual(stable["system_status"], "STABLE")
        self.assertEqual(stable["utilization_percent"], 80.0)
        self.assertEqual(stable["average_latency_ms"], 10.0)  # 1 / (500 - 400) = 0.01s = 10ms
        self.assertGreater(stable["p99_tail_latency_ms"], 40.0)

        # Unstable queue: lambda=600 > mu=500
        unstable = SystemsMathEngine.calculate_queueing_latency(
            arrival_rate_lambda=600.0,
            service_rate_mu=500.0
        )
        self.assertEqual(unstable["system_status"], "UNSTABLE_QUEUE_OVERFLOW")
        self.assertGreater(unstable["utilization_rho"], 1.0)

    def test_amdahl_speedup_scaling(self):
        # 90% parallel on 16 cores
        res = SystemsMathEngine.calculate_amdahl_speedup(parallel_fraction_p=0.90, processor_cores_s=16)
        self.assertEqual(res["achieved_speedup_multiplier"], 6.4)
        self.assertEqual(res["theoretical_infinite_core_limit"], 10.0)
        self.assertEqual(res["serial_bottleneck_percent"], 10.0)

    def test_spring_physics_critically_damped(self):
        # m=1, k=100 -> omega_0 = 10. For critical damping zeta=1: c = 2 * sqrt(100) = 20
        res = SystemsMathEngine.calculate_spring_physics(
            mass_m=1.0, stiffness_k=100.0, damping_c=20.0, initial_displacement=1.0
        )
        self.assertEqual(res["damping_ratio_zeta"], 1.0)
        self.assertIn("CRITICALLY_DAMPED", res["regime"])
        self.assertEqual(len(res["trajectory_sample"]), 5)

    def test_kelly_capital_allocation(self):
        # 50% win probability, 2:1 payoff multiple: f* = (0.5 * 3 - 1) / 2 = 0.25 (25% allocation)
        res = SystemsMathEngine.calculate_kelly_capital_allocation(
            win_probability_p=0.50, upside_downside_ratio_b=2.0, bankroll_or_time_budget_usd=10000.0
        )
        self.assertEqual(res["pure_kelly_fraction"], 0.25)
        self.assertEqual(res["conservative_half_kelly_allocation_percent"], 25.0)
        self.assertEqual(res["recommended_budget_allocation_usd"], 2500.0)
        self.assertIn("POZİTİF", res["risk_verdict"])

    def test_mcp_server_calculate_systems_math_tool(self):
        req_args = {
            "math_type": "roofline",
            "parameters": {
                "total_flops": 5e11,
                "total_bytes_transferred": 2e10,
                "hardware_target": "nvidia_rtx_4090"
            }
        }
        res = self.server.execute_tool("calculate_systems_math", req_args)
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertIn("bottleneck_classification", res["result"])
        self.assertLess(res["execution_latency_ms"], 10.0)


if __name__ == "__main__":
    unittest.main()
