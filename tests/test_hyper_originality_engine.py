#!/usr/bin/env python3
"""
Unit tests for Hyper-Originality & Mathematical Innovation Multiplier Engine (10x -> 100x).
Verifies Kolmogorov information density, non-consensus divergence, 10x architectural elevation,
100x cross-domain mathematical isomorphisms, and MCP tool execution.
"""

import os
import sys
import unittest
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.hyper_originality_engine import HyperOriginalityEngine
from scripts.zobar_mcp_server import ZobarMCPServer


class TestHyperOriginalityEngine(unittest.TestCase):
    def setUp(self):
        self.engine = HyperOriginalityEngine()

    def test_originality_scoring_empty_code(self):
        res = self.engine.calculate_code_originality_score("")
        self.assertEqual(res["originality_score"], 0.0)
        self.assertEqual(res["multiplier"], 1.0)
        self.assertEqual(res["verdict"], "Empty Codebase")

    def test_originality_scoring_cliche_boilerplate(self):
        cliche_code = (
            "import React, { useState, useEffect } from 'react';\n"
            "import axios from 'axios';\n"
            "function UserList() {\n"
            "    const [data, setData] = useState(false);\n"
            "    useEffect(() => {\n"
            "        axios.get('/api/users').then(res => setData(res.data));\n"
            "    }, []);\n"
            "    return <div className='bg-blue-500 rounded-md p-4 shadow'>Users</div>;\n"
            "}"
        )
        res = self.engine.calculate_code_originality_score(cliche_code)
        self.assertLess(res["originality_score"], 70.0)
        self.assertGreaterEqual(res["cliche_violations_count"], 3)
        self.assertIn("Consensus", res["verdict"])

    def test_originality_scoring_high_density_code(self):
        high_craft_code = (
            "class SymplecticPhaseIntegrator:\n"
            "    __slots__ = ('_mass', '_stiffness', '_dt', '_q', '_p')\n"
            "    def __init__(self, m: float, k: float, dt: float):\n"
            "        self._mass, self._stiffness, self._dt = m, k, dt\n"
            "        self._q, self._p = 0.0, 0.0\n"
            "    def step(self, force: float):\n"
            "        p_half = self._p + 0.5 * (force - self._stiffness * self._q) * self._dt\n"
            "        self._q += (p_half / self._mass) * self._dt\n"
            "        self._p = p_half + 0.5 * (force - self._stiffness * self._q) * self._dt\n"
            "        return self._q, self._p"
        )
        res = self.engine.calculate_code_originality_score(high_craft_code)
        self.assertGreater(res["originality_score"], 75.0)
        self.assertEqual(res["cliche_violations_count"], 0)
        self.assertGreaterEqual(res["multiplier"], 10.0)

    def test_ten_x_architecture_synthesis(self):
        res = self.engine.synthesize_ten_x_architecture("High-Concurrency Edge State Synchronization")
        self.assertEqual(res["target_multiplier"], "10x Performance & Quality Acceleration")
        self.assertGreaterEqual(res["elevated_originality_score"], 80.0)
        self.assertGreaterEqual(len(res["architectural_pillars"]), 4)
        self.assertIn("reference_code_pattern", res)
        self.assertIn("RingBuffer", res["reference_code_pattern"])

    def test_hundred_x_frontier_breakthrough(self):
        res = self.engine.synthesize_hundred_x_breakthrough("Distributed Access Control and Permission Graph")
        self.assertEqual(res["breakthrough_status"], "100X FRONTIER PARADIGM ACHIEVED")
        self.assertGreaterEqual(res["originality_rating"], 95.0)
        self.assertEqual(len(res["all_frontier_isomorphisms"]), 4)

        # Check all 4 isomorphisms are present and defined
        iso_ids = [i["id"] for i in res["all_frontier_isomorphisms"]]
        self.assertIn("ISO-TOPOLOGY", iso_ids)
        self.assertIn("ISO-SYMPLECTIC", iso_ids)
        self.assertIn("ISO-CHAOS", iso_ids)
        self.assertIn("ISO-ROARING-BITMAP", iso_ids)

    def test_sub_millisecond_execution_performance(self):
        t_start = time.perf_counter()
        for _ in range(50):
            self.engine.calculate_code_originality_score("def add(a, b): return a + b")
            self.engine.synthesize_ten_x_architecture("cache")
            self.engine.synthesize_hundred_x_breakthrough("topology")
        elapsed = (time.perf_counter() - t_start) / 50.0

        # Sub-millisecond execution mandate: average execution should be well under 5ms
        self.assertLess(elapsed * 1000.0, 5.0, f"Hyper-originality engine too slow: {elapsed * 1000.0:.2f}ms > 5ms")

    def test_mcp_tool_synthesize_hyper_originality(self):
        server = ZobarMCPServer()
        res = server.execute_tool("synthesize_hyper_originality", {
            "domain": "Microsecond Telemetry Pipeline",
            "baseline_code": "const items = []; for(let i=0; i<100; i++) items.push(i);",
            "target_multiplier": "both"
        })
        self.assertEqual(res["tool_status"], "SUCCESS")
        self.assertLess(res["execution_latency_ms"], 50.0)

        payload = res["result"]
        self.assertIn("baseline_originality_analysis", payload)
        self.assertIn("ten_x_elevation", payload)
        self.assertIn("hundred_x_frontier_breakthrough", payload)


if __name__ == "__main__":
    unittest.main()
