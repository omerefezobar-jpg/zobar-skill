#!/usr/bin/env python3
"""
Unit and Integration Tests for Geospatial Map Artist & 3D Google Earth Engine & MCP Tooling.
Verifies spherical geodesy, 3D camera orbit generation, KML gx:Tour XML generation,
artistic map styling synthesis, interactive 3D globe widget, and MCP server execution.
"""

import unittest
import os
import sys

# Ensure scripts dir in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from geospatial_map_artist_engine import (
    GeospatialMapArtistEngine,
    FREE_TILE_PROVIDERS,
    ARTISTIC_STYLE_PRESETS
)
from zobar_mcp_server import ZobarMCPServer


class TestGeospatialMapArtistEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GeospatialMapArtistEngine()

    def test_spherical_math_haversine_and_bearing(self):
        """Must accurately compute Great Circle distance and compass bearing."""
        # Istanbul (41.0082, 28.9784) to Ankara (39.9334, 32.8597) ~350km
        dist = self.engine.haversine_distance(41.0082, 28.9784, 39.9334, 32.8597)
        self.assertTrue(340000 < dist < 360000)

        # Bearing roughly southeast (100-130 degrees)
        bearing = self.engine.calculate_bearing(41.0082, 28.9784, 39.9334, 32.8597)
        self.assertTrue(90 < bearing < 150)

    def test_interpolate_great_circle(self):
        """Must correctly interpolate along the great circle arc."""
        start = (41.0082, 28.9784)
        end = (48.8566, 2.3522) # Paris

        p0 = self.engine.interpolate_great_circle(start[0], start[1], end[0], end[1], 0.0)
        self.assertAlmostEqual(p0[0], start[0], places=3)
        self.assertAlmostEqual(p0[1], start[1], places=3)

        p1 = self.engine.interpolate_great_circle(start[0], start[1], end[0], end[1], 1.0)
        self.assertAlmostEqual(p1[0], end[0], places=3)
        self.assertAlmostEqual(p1[1], end[1], places=3)

        pmid = self.engine.interpolate_great_circle(start[0], start[1], end[0], end[1], 0.5)
        self.assertTrue(start[0] < pmid[0] < end[0])

    def test_generate_orbit_trajectory(self):
        """Must generate a smooth 360-degree camera orbit around the target coordinate."""
        orbit = self.engine.generate_orbit_trajectory(
            center_lat=41.0082, center_lon=28.9784,
            radius_meters=1000.0, altitude_meters=600.0,
            tilt_degrees=60.0, points_count=16, duration_seconds=16.0
        )
        self.assertEqual(len(orbit), 16)
        self.assertEqual(orbit[0]["altitude"], 600.0)
        self.assertEqual(orbit[0]["tilt"], 60.0)
        self.assertAlmostEqual(orbit[0]["duration"], 1.0)

        # Check that headings vary across full 360 degrees
        headings = [kf["heading"] for kf in orbit]
        self.assertGreater(max(headings) - min(headings), 180.0)

    def test_calculate_flyover_trajectory(self):
        """Must calculate multi-waypoint path with altitude progression."""
        waypoints = [
            {"latitude": 41.0082, "longitude": 28.9784},
            {"latitude": 41.0369, "longitude": 28.9858},
            {"latitude": 41.0500, "longitude": 29.0000}
        ]
        flyover = self.engine.calculate_flyover_trajectory(
            waypoints=waypoints,
            steps_between=5,
            start_altitude=1200.0,
            end_altitude=300.0
        )
        self.assertEqual(len(flyover), 11)
        self.assertEqual(flyover[0]["altitude"], 1200.0)
        self.assertEqual(flyover[-1]["altitude"], 300.0)

    def test_export_google_earth_kml_tour(self):
        """Must produce valid KML 2.2 XML with gx:Tour and gx:FlyTo elements."""
        orbit = self.engine.generate_orbit_trajectory(
            center_lat=37.7749, center_lon=-122.4194,
            points_count=8
        )
        kml_xml = self.engine.export_google_earth_kml_tour(
            tour_name="San Francisco Cinematic Orbit",
            keyframes=orbit
        )
        self.assertIn("<?xml version=\"1.0\" encoding=\"UTF-8\"?>", kml_xml)
        self.assertIn("<kml", kml_xml)
        self.assertIn("San Francisco Cinematic Orbit", kml_xml)
        self.assertIn("Tour", kml_xml)
        self.assertIn("FlyTo", kml_xml)
        self.assertIn("Camera", kml_xml)

    def test_synthesize_artistic_map_style(self):
        """Must synthesize full cartographic spec for all 5 style presets."""
        for preset_key in ARTISTIC_STYLE_PRESETS:
            spec = self.engine.synthesize_artistic_map_style(preset_key)
            self.assertIn("style_name", spec)
            self.assertIn("tile_url_template", spec)
            self.assertIn("theme_tokens", spec)
            self.assertIn("leaflet_integration_snippet", spec)
            self.assertIn("filter:", spec["leaflet_integration_snippet"])

    def test_render_artistic_globe_widget(self):
        """Must render a valid HTML5 Canvas 60fps widget."""
        widget = self.engine.render_artistic_globe_widget(
            center_label="Global Operations",
            theme="cyberpunk_midnight"
        )
        self.assertIn("<canvas id=\"globe-canvas-widget\"", widget)
        self.assertIn("requestAnimationFrame(draw)", widget)
        self.assertIn("Global Operations", widget)

    def test_mcp_server_geospatial_tools(self):
        """Must execute all 3 geospatial tools via MCP JSON-RPC router."""
        server = ZobarMCPServer()

        # Tool 1: generate_google_earth_cinematic_tour
        res1 = server.execute_tool("generate_google_earth_cinematic_tour", {
            "center_lat": 41.0082,
            "center_lon": 28.9784,
            "tour_name": "Bosphorus Cinematic Flyover",
            "points_count": 8
        })
        self.assertEqual(res1["tool_status"], "SUCCESS")
        self.assertIn("kml_xml", res1["result"])
        self.assertIn("Bosphorus Cinematic Flyover", res1["result"]["kml_xml"])

        # Tool 2: synthesize_artistic_map_specification
        res2 = server.execute_tool("synthesize_artistic_map_specification", {
            "style_preset": "cyberpunk_midnight"
        })
        self.assertEqual(res2["tool_status"], "SUCCESS")
        self.assertIn("tile_url_template", res2["result"])

        # Tool 3: render_interactive_3d_globe_widget
        res3 = server.execute_tool("render_interactive_3d_globe_widget", {
            "center_label": "High Frequency Trading Nodes",
            "theme": "cyberpunk_midnight"
        })
        self.assertEqual(res3["tool_status"], "SUCCESS")
        self.assertIn("widget_html", res3["result"])
        self.assertIn("globe-canvas-widget", res3["result"]["widget_html"])


if __name__ == "__main__":
    unittest.main()
