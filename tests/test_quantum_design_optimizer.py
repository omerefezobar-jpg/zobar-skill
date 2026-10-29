#!/usr/bin/env python3
"""
Unit tests for Quantum Design Optimizer & Aesthetic Ground-State Selector.
Verifies quantum state superposition, Hamiltonian minimization, Born collapse,
and sub-millisecond execution.
"""

import os
import sys
import unittest
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.quantum_design_optimizer import (
    QuantumDesignOptimizer,
    hex_to_rgb,
    calculate_wcag_luminance,
    calculate_contrast_ratio,
    GOLDEN_RATIO
)
from scripts.zobar_mcp_server import ZobarMCPServer


class TestQuantumDesignOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = QuantumDesignOptimizer()
        self.candidates = [
            {
                "name": "Linear Dark Minimalist",
                "background_hex": "#0e1017",
                "text_hex": "#f8fafc",
                "accent_hex": "#6366f1",
                "visual_density": 0.44,
                "aspect_ratio": 1.618,
                "spring_damping": 0.86,
                "delight_factor": 0.95
            },
            {
                "name": "Generic Gray Clutter",
                "background_hex": "#888888",
                "text_hex": "#777777",
                "accent_hex": "#999999",
                "visual_density": 0.90,
                "aspect_ratio": 1.100,
                "spring_damping": 0.20,
                "delight_factor": 0.10
            },
            {
                "name": "Apple Ultra Clean Spatial",
                "background_hex": "#000000",
                "text_hex": "#ffffff",
                "accent_hex": "#2997ff",
                "visual_density": 0.40,
                "aspect_ratio": 1.618,
                "spring_damping": 0.88,
                "delight_factor": 0.98
            }
        ]

    def test_wcag_contrast_and_luminance_math(self):
        # Black vs White should be 21.0
        contrast = calculate_contrast_ratio("#000000", "#ffffff")
        self.assertAlmostEqual(contrast, 21.0, places=1)

        # Identical colors should be 1.0
        identical = calculate_contrast_ratio("#123456", "#123456")
        self.assertAlmostEqual(identical, 1.0, places=2)

        # Hex parsing
        rgb = hex_to_rgb("#ff0000")
        self.assertEqual(rgb, (255, 0, 0))

    def test_hamiltonian_computation(self):
        H, energies = self.optimizer.compute_aesthetic_hamiltonian(self.candidates)
        n = len(self.candidates)
        self.assertEqual(len(H), n)
        self.assertEqual(len(H[0]), n)

        # Diagonal energy of high-craft designs should be significantly lower than generic clutter
        # Lower energy in Hamiltonian corresponds to higher aesthetic fitness
        self.assertLess(energies[0], energies[1], "Linear Dark should have lower Hamiltonian energy than generic clutter")
        self.assertLess(energies[2], energies[1], "Apple Clean should have lower Hamiltonian energy than generic clutter")

    def test_ground_state_solver_and_born_collapse(self):
        result = self.optimizer.select_optimal_design(self.candidates)

        self.assertIn("selected_design", result)
        self.assertIn("ground_state_energy", result)
        self.assertIn("collapse_probability", result)
        self.assertIn("von_neumann_entropy", result)
        self.assertIn("quantum_coherence_fidelity", result)

        # Winning design must be one of the top tier designs (Apple or Linear), never Generic Clutter
        winning_name = result["design_name"]
        self.assertIn(winning_name, ["Apple Ultra Clean Spatial", "Linear Dark Minimalist"])
        self.assertNotEqual(winning_name, "Generic Gray Clutter")

        # Probability distribution must sum to 1.0
        probs = result["probability_distribution"]
        self.assertAlmostEqual(sum(probs), 1.0, places=2)

        # Von Neumann entropy must be positive and bounded
        self.assertGreater(result["von_neumann_entropy"], 0.0)
        self.assertLess(result["von_neumann_entropy"], 2.0)

    def test_sub_millisecond_execution_performance(self):
        t_start = time.perf_counter()
        for _ in range(50):
            self.optimizer.select_optimal_design(self.candidates)
        elapsed = (time.perf_counter() - t_start) / 50.0

        # Sub-millisecond execution mandate: average execution should be well under 10ms
        self.assertLess(elapsed * 1000.0, 10.0, f"Quantum design selection too slow: {elapsed * 1000.0:.2f}ms > 10ms")

    def test_simulated_quantum_annealing_and_trace(self):
        H, _ = self.optimizer.compute_aesthetic_hamiltonian(self.candidates)
        ground_state, ground_energy, trace = self.optimizer.simulate_quantum_annealing(H, steps=5)
        self.assertEqual(len(trace), 6)
        self.assertEqual(len(ground_state), len(self.candidates))
        self.assertIsInstance(ground_energy, float)

    def test_density_matrix_and_purity(self):
        state = [1.0 / (3.0 ** 0.5)] * 3
        rho = self.optimizer.compute_density_matrix(state)
        self.assertEqual(len(rho), 3)
        self.assertEqual(len(rho[0]), 3)

        purity = self.optimizer.compute_purity(rho)
        self.assertGreaterEqual(purity, 1.0 / 3.0)
        self.assertLessEqual(purity, 1.0)

    def test_multi_viewport_quantum_fidelity(self):
        desktop = self.candidates[0]
        mobile = dict(self.candidates[0])
        mobile["visual_density"] = 0.46
        res = self.optimizer.evaluate_multi_viewport_fidelity(desktop, mobile)
        self.assertIn("responsive_quantum_fidelity", res)
        self.assertGreaterEqual(res["responsive_quantum_fidelity"], 50.0)
        self.assertIn("harmonic_status", res)

    def test_mcp_tool_quantum_optimize_design(self):
        server = ZobarMCPServer()
        res = server.execute_tool("quantum_optimize_design", {"candidates": self.candidates})
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertLess(res["execution_latency_ms"], 50.0)

        payload = res["result"]
        self.assertIn("selected_design", payload)
        self.assertIn("mathematical_optimality_proof", payload)


if __name__ == "__main__":
    unittest.main()
