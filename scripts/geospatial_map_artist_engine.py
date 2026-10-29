#!/usr/bin/env python3
"""
Geospatial Map Artist & 3D Google Earth Studio Automation Engine.
High-performance, zero-dependency cartographic synthesis and 3D camera trajectory generator:

Capabilities:
1. Google Earth 3D Cinematic Tour Generator (KML / gx:Tour format):
   - Computes smooth spherical camera orbits, flyovers, and pitch/heading transitions.
   - Exports valid Keyhole Markup Language (KML 2.2 + gx extensions) compatible with Google Earth Pro & Web.
2. Artistic Map Style Synthesizer (MapLibre / Leaflet / Deck.gl):
   - 5 S-Tier Artistic Style Presets:
     * Cyberpunk Midnight (Neon glowing vectors, deep obsidian backdrop)
     * Minimalist Monochrome (High-contrast Swiss architectural line art)
     * Vintage Topographic (Warm parchment, contour shading, serif typography)
     * Infrared Thermal Satellite (Multi-spectral false-color thermal gradient)
     * Swiss Alpine Clean (Crisp elevation relief, subtle glacier blue vectors)
   - Free, high-speed tile provider integration (OpenStreetMap, CartoDB Positron/DarkMatter, Stamen Toner/Terrain).
3. Spherical Geospatial Math Suite (Pure Standard Library):
   - Haversine distance, spherical bearing, Great Circle interpolation (Slerp), and bounding box derivation.
4. Generative UI Interactive 3D Globe Widget:
   - Standalone `<agent-embed>` HTML5 canvas 3D sphere with camera orbit animation conforming to Antigravity UI spec.
"""

import sys
import os
import json
import math
import time
import xml.etree.ElementTree as ET
from typing import Dict, List, Any, Optional, Tuple

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPTS_DIR, ".."))
REFERENCES_DIR = os.path.join(ROOT_DIR, "references")
AUDIT_LOG_FILE = os.path.join(REFERENCES_DIR, "session_telemetry_audit.log")

# Earth mean radius in meters
EARTH_RADIUS_METERS = 6371000.0

# Free, High-Speed Public Tile Providers (Zero API Key Required)
FREE_TILE_PROVIDERS = {
    "carto_dark_matter": {
        "name": "CartoDB Dark Matter",
        "url_template": "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
        "subdomains": ["a", "b", "c", "d"],
        "attribution": "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
        "max_zoom": 20,
        "aesthetic_vibe": "Deep dark aesthetic, ideal for neon trajectory overlays and high-contrast dashboards."
    },
    "carto_positron": {
        "name": "CartoDB Positron",
        "url_template": "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        "subdomains": ["a", "b", "c", "d"],
        "attribution": "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
        "max_zoom": 20,
        "aesthetic_vibe": "Ultra-clean minimalist paper light, ideal for corporate reports and print-quality cartography."
    },
    "carto_voyager": {
        "name": "CartoDB Voyager",
        "url_template": "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
        "subdomains": ["a", "b", "c", "d"],
        "attribution": "&copy; OpenStreetMap contributors &copy; CARTO",
        "max_zoom": 19,
        "aesthetic_vibe": "Modern pastel editorial cartography with subtle building outlines and clean typography."
    },
    "osm_standard": {
        "name": "OpenStreetMap Standard",
        "url_template": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        "subdomains": ["a", "b", "c"],
        "attribution": "&copy; OpenStreetMap contributors",
        "max_zoom": 19,
        "aesthetic_vibe": "Global crowdsourced standard reference tile layer."
    },
    "stamen_toner_mirror": {
        "name": "Stamen Toner (Stadia Mirror)",
        "url_template": "https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}.png",
        "attribution": "&copy; Stamen Design &copy; OpenStreetMap",
        "max_zoom": 20,
        "aesthetic_vibe": "Extreme black & white high-contrast bimodal vector aesthetic."
    }
}

# 5 S-Tier Artistic Style Presets
ARTISTIC_STYLE_PRESETS: Dict[str, Dict[str, Any]] = {
    "cyberpunk_midnight": {
        "name": "Cyberpunk Midnight",
        "base_tile_provider": "carto_dark_matter",
        "background_color": "#0a0a0f",
        "primary_accent": "#00f0ff",
        "secondary_accent": "#ff0055",
        "trajectory_glow": "0 0 12px rgba(0, 240, 255, 0.75)",
        "font_family": "ui-monospace, SFMono-Regular, Menlo, monospace",
        "map_filter": "brightness(0.85) contrast(1.25) hue-rotate(180deg) invert(0.08)",
        "camera_profile": {
            "default_tilt": 65,
            "orbit_speed_multiplier": 1.2,
            "fov": 75
        }
    },
    "minimalist_monochrome": {
        "name": "Minimalist Monochrome",
        "base_tile_provider": "carto_positron",
        "background_color": "#f8f9fa",
        "primary_accent": "#111827",
        "secondary_accent": "#6b7280",
        "trajectory_glow": "none",
        "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        "map_filter": "grayscale(100%) contrast(1.15) brightness(0.98)",
        "camera_profile": {
            "default_tilt": 45,
            "orbit_speed_multiplier": 0.8,
            "fov": 60
        }
    },
    "vintage_topography": {
        "name": "Vintage Topography",
        "base_tile_provider": "carto_voyager",
        "background_color": "#f4ede1",
        "primary_accent": "#78350f",
        "secondary_accent": "#065f46",
        "trajectory_glow": "0 0 4px rgba(120, 53, 15, 0.4)",
        "font_family": "Georgia, Cambria, 'Times New Roman', serif",
        "map_filter": "sepia(0.35) contrast(1.05) saturate(0.85)",
        "camera_profile": {
            "default_tilt": 55,
            "orbit_speed_multiplier": 0.6,
            "fov": 55
        }
    },
    "infrared_thermal": {
        "name": "Infrared Thermal Satellite",
        "base_tile_provider": "carto_dark_matter",
        "background_color": "#030712",
        "primary_accent": "#f97316",
        "secondary_accent": "#ef4444",
        "trajectory_glow": "0 0 16px rgba(249, 115, 22, 0.8)",
        "font_family": "'SF Pro Display', -apple-system, sans-serif",
        "map_filter": "contrast(1.3) hue-rotate(290deg) saturate(1.8)",
        "camera_profile": {
            "default_tilt": 70,
            "orbit_speed_multiplier": 1.0,
            "fov": 68
        }
    },
    "swiss_alpine_clean": {
        "name": "Swiss Alpine Clean",
        "base_tile_provider": "carto_positron",
        "background_color": "#ffffff",
        "primary_accent": "#0284c7",
        "secondary_accent": "#0f172a",
        "trajectory_glow": "0 0 8px rgba(2, 132, 199, 0.4)",
        "font_family": "Helvetica, Arial, sans-serif",
        "map_filter": "contrast(1.1) brightness(1.02) saturate(0.95)",
        "camera_profile": {
            "default_tilt": 50,
            "orbit_speed_multiplier": 0.9,
            "fov": 62
        }
    }
}


class GeospatialMapArtistEngine:
    """
    Core Cartography and 3D Google Earth Cinematic Synthesis Suite.
    Operates using pure Python standard library for ultra-fast, zero-dependency execution.
    """

    def __init__(self):
        os.makedirs(REFERENCES_DIR, exist_ok=True)
        self.presets = ARTISTIC_STYLE_PRESETS
        self.providers = FREE_TILE_PROVIDERS

    # --- 1. SPHERICAL GEOSPATIAL CALCULATIONS ---

    @staticmethod
    def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Computes great-circle distance between two GPS coordinates in meters.
        """
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * (math.sin(delta_lambda / 2.0) ** 2)
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(max(0.0, 1.0 - a)))
        return round(EARTH_RADIUS_METERS * c, 2)

    @staticmethod
    def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Computes the initial compass bearing (heading in degrees: 0-360) from point 1 to point 2.
        """
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_lambda = math.radians(lon2 - lon1)

        y = math.sin(delta_lambda) * math.cos(phi2)
        x = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(delta_lambda)
        theta = math.atan2(y, x)
        bearing = (math.degrees(theta) + 360.0) % 360.0
        return round(bearing, 2)

    @staticmethod
    def interpolate_great_circle(
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float,
        fraction: float
    ) -> Tuple[float, float]:
        """
        Spherical linear interpolation (Slerp) along the great circle arc between two points.
        fraction: 0.0 (start) to 1.0 (destination).
        """
        if fraction <= 0.0:
            return (lat1, lon1)
        if fraction >= 1.0:
            return (lat2, lon2)

        phi1 = math.radians(lat1)
        lam1 = math.radians(lon1)
        phi2 = math.radians(lat2)
        lam2 = math.radians(lon2)

        d = 2.0 * math.asin(
            math.sqrt(
                math.sin((phi2 - phi1) / 2.0) ** 2 +
                math.cos(phi1) * math.cos(phi2) * (math.sin((lam2 - lam1) / 2.0) ** 2)
            )
        )

        if d < 1e-9:
            return (lat1, lon1)

        a = math.sin((1.0 - fraction) * d) / math.sin(d)
        b = math.sin(fraction * d) / math.sin(d)

        x = a * math.cos(phi1) * math.cos(lam1) + b * math.cos(phi2) * math.cos(lam2)
        y = a * math.cos(phi1) * math.sin(lam1) + b * math.cos(phi2) * math.sin(lam2)
        z = a * math.sin(phi1) + b * math.sin(phi2)

        phi = math.atan2(z, math.sqrt(x * x + y * y))
        lam = math.atan2(y, x)

        return (round(math.degrees(phi), 6), round(math.degrees(lam), 6))

    # --- 2. 3D CAMERA TRAJECTORY & ORBIT GENERATOR ---

    def generate_orbit_trajectory(
        self,
        center_lat: float,
        center_lon: float,
        radius_meters: float = 1200.0,
        altitude_meters: float = 850.0,
        tilt_degrees: float = 65.0,
        points_count: int = 36,
        duration_seconds: float = 24.0
    ) -> List[Dict[str, Any]]:
        """
        Computes a 360-degree smooth circular camera orbit around a center focal point.
        Each keyframe includes latitude, longitude, altitude, heading, tilt, and duration.
        """
        keyframes = []
        step_deg = 360.0 / max(4, points_count)
        step_duration = round(duration_seconds / max(4, points_count), 2)

        angular_distance = radius_meters / EARTH_RADIUS_METERS
        center_phi = math.radians(center_lat)
        center_lam = math.radians(center_lon)

        for i in range(points_count):
            bearing_deg = (i * step_deg) % 360.0
            bearing_rad = math.radians(bearing_deg)

            # Destination point formula given distance and bearing from center
            point_phi = math.asin(
                math.sin(center_phi) * math.cos(angular_distance) +
                math.cos(center_phi) * math.sin(angular_distance) * math.cos(bearing_rad)
            )
            point_lam = center_lam + math.atan2(
                math.sin(bearing_rad) * math.sin(angular_distance) * math.cos(center_phi),
                math.cos(angular_distance) - math.sin(center_phi) * math.sin(point_phi)
            )

            lat = round(math.degrees(point_phi), 6)
            lon = round(math.degrees(point_lam), 6)

            # Camera heading faces inward toward the center
            camera_heading = (bearing_deg + 180.0) % 360.0

            keyframes.append({
                "index": i,
                "latitude": lat,
                "longitude": lon,
                "altitude": altitude_meters,
                "heading": round(camera_heading, 2),
                "tilt": tilt_degrees,
                "duration": step_duration
            })

        return keyframes

    def calculate_flyover_trajectory(
        self,
        waypoints: List[Dict[str, float]],
        steps_between: int = 10,
        start_altitude: float = 1500.0,
        end_altitude: float = 400.0,
        tilt: float = 60.0
    ) -> List[Dict[str, Any]]:
        """
        Generates a cinematic multi-waypoint flyover path interpolating along great-circle arcs.
        Smoothly modulates altitude and heading toward forward travel direction.
        """
        if len(waypoints) < 2:
            raise ValueError("Flyover requires at least 2 waypoints.")

        trajectory = []
        total_segments = len(waypoints) - 1
        total_steps = total_segments * steps_between

        step_idx = 0
        for seg_idx in range(total_segments):
            p1 = waypoints[seg_idx]
            p2 = waypoints[seg_idx + 1]

            for s in range(steps_between):
                fraction = s / float(steps_between)
                overall_fraction = step_idx / float(max(1, total_steps))

                lat, lon = self.interpolate_great_circle(
                    p1["latitude"], p1["longitude"],
                    p2["latitude"], p2["longitude"],
                    fraction
                )

                # Smoothly interpolate altitude
                current_alt = start_altitude + (end_altitude - start_altitude) * overall_fraction

                # Heading points forward to next target
                heading = self.calculate_bearing(lat, lon, p2["latitude"], p2["longitude"])

                trajectory.append({
                    "step": step_idx,
                    "latitude": lat,
                    "longitude": lon,
                    "altitude": round(current_alt, 2),
                    "heading": heading,
                    "tilt": tilt,
                    "duration": 1.5
                })
                step_idx += 1

        # Append final destination point
        dest = waypoints[-1]
        trajectory.append({
            "step": step_idx,
            "latitude": dest["latitude"],
            "longitude": dest["longitude"],
            "altitude": end_altitude,
            "heading": trajectory[-1]["heading"] if trajectory else 0.0,
            "tilt": tilt,
            "duration": 2.0
        })

        return trajectory

    # --- 3. GOOGLE EARTH KML 3D TOUR EXPORTER ---

    def export_google_earth_kml_tour(
        self,
        tour_name: str,
        keyframes: List[Dict[str, Any]],
        description: str = "Cinematic 3D Camera Tour for Google Earth Studio"
    ) -> str:
        """
        Serializes camera keyframes into standard Google Earth KML 2.2 format
        with Google extension (<gx:Tour>, <gx:FlyTo>, <LookAt> or <Camera>).
        Compatible directly with Google Earth Pro desktop, Earth Web, and Earth Studio import.
        """
        kml_ns = "http://www.opengis.net/kml/2.2"
        gx_ns = "http://www.google.com/kml/ext/2.2"

        kml = ET.Element("kml", {
            "xmlns": kml_ns,
            "xmlns:gx": gx_ns
        })
        doc = ET.SubElement(kml, "Document")
        
        name_el = ET.SubElement(doc, "name")
        name_el.text = tour_name
        
        desc_el = ET.SubElement(doc, "description")
        desc_el.text = description

        # Build gx:Tour
        tour = ET.SubElement(doc, "{http://www.google.com/kml/ext/2.2}Tour")
        tour_name_el = ET.SubElement(tour, "name")
        tour_name_el.text = tour_name
        
        playlist = ET.SubElement(tour, "{http://www.google.com/kml/ext/2.2}Playlist")

        for kf in keyframes:
            flyto = ET.SubElement(playlist, "{http://www.google.com/kml/ext/2.2}FlyTo")
            dur = ET.SubElement(flyto, "{http://www.google.com/kml/ext/2.2}duration")
            dur.text = str(kf.get("duration", 2.0))
            
            mode = ET.SubElement(flyto, "{http://www.google.com/kml/ext/2.2}flyToMode")
            mode.text = "smooth"

            camera = ET.SubElement(flyto, "Camera")
            
            lon_el = ET.SubElement(camera, "longitude")
            lon_el.text = str(kf["longitude"])
            
            lat_el = ET.SubElement(camera, "latitude")
            lat_el.text = str(kf["latitude"])
            
            alt_el = ET.SubElement(camera, "altitude")
            alt_el.text = str(kf.get("altitude", 500.0))
            
            heading_el = ET.SubElement(camera, "heading")
            heading_el.text = str(kf.get("heading", 0.0))
            
            tilt_el = ET.SubElement(camera, "tilt")
            tilt_el.text = str(kf.get("tilt", 60.0))
            
            roll_el = ET.SubElement(camera, "roll")
            roll_el.text = "0.0"
            
            alt_mode = ET.SubElement(camera, "altitudeMode")
            alt_mode.text = "relativeToGround"

        xml_str = ET.tostring(kml, encoding="utf-8").decode("utf-8")
        formatted_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_str}'

        self._log_audit(f"EXPORT_KML_TOUR | name={tour_name} | keyframes={len(keyframes)}")
        return formatted_xml

    # --- 4. ARTISTIC MAP STYLE SYNTHESIZER ---

    def synthesize_artistic_map_style(
        self,
        style_preset_key: str = "cyberpunk_midnight",
        custom_accent: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Synthesizes a complete web cartography specification including tile endpoints,
        CSS color tokens, hardware-accelerated CSS filters, and MapLibre/Leaflet code snippets.
        """
        preset = self.presets.get(style_preset_key, self.presets["cyberpunk_midnight"])
        provider = self.providers.get(preset["base_tile_provider"], self.providers["carto_dark_matter"])

        primary_accent = custom_accent or preset["primary_accent"]

        # Synthesize Leaflet / MapLibre Configuration
        map_config = {
            "style_name": preset["name"],
            "tile_provider": provider["name"],
            "tile_url_template": provider["url_template"],
            "subdomains": provider.get("subdomains", []),
            "attribution": provider["attribution"],
            "max_zoom": provider["max_zoom"],
            "theme_tokens": {
                "background_color": preset["background_color"],
                "primary_accent": primary_accent,
                "secondary_accent": preset["secondary_accent"],
                "trajectory_glow": preset["trajectory_glow"],
                "font_family": preset["font_family"],
                "css_filter": preset["map_filter"]
            },
            "camera_profile": preset["camera_profile"]
        }

        # Ready-to-paste Leaflet Quick-Start Snippet
        subdomain_str = json.dumps(provider.get("subdomains", []))
        leaflet_code = (
            f"// {preset['name']} - S-Tier Free Cartography Setup\n"
            f"const map = L.map('map-container', {{\n"
            f"  center: [41.0082, 28.9784],\n"
            f"  zoom: 13,\n"
            f"  zoomControl: false\n"
            f"}});\n\n"
            f"L.tileLayer('{provider['url_template']}', {{\n"
            f"  subdomains: {subdomain_str},\n"
            f"  attribution: '{provider['attribution']}',\n"
            f"  maxZoom: {provider['max_zoom']},\n"
            f"  className: 'artistic-map-tiles'\n"
            f"}}).addTo(map);\n\n"
            f"/* Apply Hardware-Accelerated CSS Tone Filter */\n"
            f".artistic-map-tiles {{\n"
            f"  filter: {preset['map_filter']};\n"
            f"}}"
        )
        map_config["leaflet_integration_snippet"] = leaflet_code

        return map_config

    # --- 5. GENERATIVE UI INTERACTIVE 3D GLOBE WIDGET ---

    def render_artistic_globe_widget(
        self,
        center_label: str = "Global Operations Terminal",
        locations: Optional[List[Dict[str, Any]]] = None,
        theme: str = "cyberpunk_midnight"
    ) -> str:
        """
        Generates an inline HTML5/Canvas 3D wireframe globe widget with interactive rotation,
        conforming to Google Antigravity generative_ui <agent-embed> specifications.
        """
        locs = locations or [
            {"name": "Silicon Valley", "lat": 37.7749, "lon": -122.4194, "metric": "99.98% Uptime"},
            {"name": "Zurich", "lat": 47.3769, "lon": 8.5417, "metric": "0.4ms Latency"},
            {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503, "metric": "HFT Node Active"},
            {"name": "Istanbul", "lat": 41.0082, "lon": 28.9784, "metric": "Gateway Synced"}
        ]
        locs_json = json.dumps(locs)
        preset = self.presets.get(theme, self.presets["cyberpunk_midnight"])
        accent = preset["primary_accent"]
        bg = preset["background_color"]

        widget_html = f"""<div style="background:{bg}; color:#f1f5f9; border-radius:12px; border:1px solid rgba(255,255,255,0.1); padding:20px; font-family:-apple-system,BlinkMacSystemFont,sans-serif; max-width:680px; margin:auto; box-shadow:0 20px 40px rgba(0,0,0,0.5);">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:8px;">
    <div>
      <span style="font-size:11px; text-transform:uppercase; letter-spacing:1px; color:{accent}; font-weight:700;">Cartographic 3D Terminal</span>
      <h3 style="margin:2px 0 0 0; font-size:16px; font-weight:600;">{center_label}</h3>
    </div>
    <span style="font-size:11px; background:rgba(0,240,255,0.1); color:{accent}; padding:3px 8px; border-radius:20px; border:1px solid rgba(0,240,255,0.25);">60 FPS Canvas</span>
  </div>
  
  <div style="position:relative; width:100%; height:260px; display:flex; justify-content:center; align-items:center;">
    <canvas id="globe-canvas-widget" width="500" height="260" style="max-width:100%; height:260px; cursor:grab;"></canvas>
  </div>

  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:8px; margin-top:12px;">
    {"".join(f'<div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06); border-radius:8px; padding:8px 10px;"><div style="font-size:11px; color:#94a3b8;">{l["name"]}</div><div style="font-size:12px; font-weight:700; color:{accent}; margin-top:2px;">{l["metric"]}</div></div>' for l in locs)}
  </div>

  <script>
    (function() {{
      const canvas = document.getElementById('globe-canvas-widget');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let angle = 0;
      const radius = 95;
      const nodes = {locs_json};

      function draw() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;

        // Draw atmospheric glow
        const grad = ctx.createRadialGradient(cx, cy, radius * 0.7, cx, cy, radius * 1.3);
        grad.addColorStop(0, 'rgba(0, 240, 255, 0.08)');
        grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(cx, cy, radius * 1.3, 0, Math.PI * 2);
        ctx.fill();

        // Draw sphere border
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(cx, cy, radius, 0, Math.PI * 2);
        ctx.stroke();

        // Draw latitude rings
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
        for (let lat = -60; lat <= 60; lat += 30) {{
          const r = radius * Math.cos(lat * Math.PI / 180);
          const y = cy + radius * Math.sin(lat * Math.PI / 180) * 0.4;
          ctx.beginPath();
          ctx.ellipse(cx, y, r, r * 0.25, 0, 0, Math.PI * 2);
          ctx.stroke();
        }}

        // Draw rotating longitude meridian arcs
        for (let lon = 0; lon < 360; lon += 45) {{
          const rad = (lon + angle) * Math.PI / 180;
          const xOffset = Math.sin(rad) * radius;
          if (Math.cos(rad) > 0) {{
            ctx.beginPath();
            ctx.ellipse(cx, cy, Math.abs(xOffset), radius, 0, 0, Math.PI * 2);
            ctx.strokeStyle = 'rgba(0, 240, 255, 0.12)';
            ctx.stroke();
          }}
        }}

        // Plot nodes
        nodes.forEach(node => {{
          const nLon = (node.lon + angle) * Math.PI / 180;
          const nLat = node.lat * Math.PI / 180;
          const z = Math.cos(nLat) * Math.cos(nLon);
          if (z > 0) {{
            const px = cx + radius * Math.cos(nLat) * Math.sin(nLon);
            const py = cy - radius * Math.sin(nLat) * 0.7;
            ctx.fillStyle = '{accent}';
            ctx.beginPath();
            ctx.arc(px, py, 3.5, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 8;
            ctx.shadowColor = '{accent}';
            ctx.fill();
            ctx.shadowBlur = 0;
          }}
        }});

        angle += 0.45;
        requestAnimationFrame(draw);
      }}
      draw();
    }})();
  </script>
</div>"""
        return widget_html

    def _log_audit(self, message: str) -> None:
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            with open(AUDIT_LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message}\n")
        except Exception:
            pass


# Standalone CLI Verification
if __name__ == "__main__":
    engine = GeospatialMapArtistEngine()
    print("=== Geospatial Map Artist & 3D Google Earth Engine Initialized ===")

    # 1. Test Orbit Generation
    orbit = engine.generate_orbit_trajectory(
        center_lat=41.0082, center_lon=28.9784,
        radius_meters=1500.0, altitude_meters=700.0,
        points_count=12
    )
    print(f"Generated Circular Camera Orbit: {len(orbit)} keyframes.")
    print(f"Sample Orbit Keyframe 0: {orbit[0]}")

    # 2. Test KML 3D Tour Export
    kml_str = engine.export_google_earth_kml_tour(
        tour_name="Bosphorus Cinematic Orbit",
        keyframes=orbit
    )
    print(f"Exported Google Earth KML Tour: {len(kml_str)} bytes XML.")

    # 3. Test Artistic Map Style Synthesizer
    style = engine.synthesize_artistic_map_style("cyberpunk_midnight")
    print(f"Synthesized Map Style: {style['style_name']} | Tile: {style['tile_provider']}")

    # 4. Test Haversine Distance
    dist = engine.haversine_distance(41.0082, 28.9784, 40.9900, 29.0200)
    print(f"Haversine Great Circle Distance: {dist} meters.")
