#!/usr/bin/env python3
"""
SpectraBinary Studio Local Server & Analysis API Gateway.
Zero-dependency HTTP server that serves the interactive web interface
and exposes a high-performance REST API for the 10-phase reverse engineering engine.
"""

import sys
import os
import json
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import Dict, Any

# Ensure project root in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.reverse_engineering_analyst import execute_10phase_re_pipeline, analyze_target_system

WEB_DIR = os.path.join(BASE_DIR, "web")

class StudioRequestHandler(SimpleHTTPRequestHandler):
    """Handles static web asset delivery and reverse engineering REST endpoints."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resp = {
                "status": "ONLINE",
                "engine": "SpectraBinary Core",
                "phases_supported": 10,
                "statutory_compliance": "DMCA 1201(f) & EU 2009/24/EC Art 6"
            }
            self.wfile.write(json.dumps(resp).encode("utf-8"))
            return

        # Serve static web interface
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/analyze":
            content_length = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_length)

            target_name = "UploadStream"
            intent = "Clean-room interoperability evaluation"
            binary_sample = post_body if post_body else None

            try:
                result = execute_10phase_re_pipeline(
                    target_name=target_name,
                    intent=intent,
                    binary_sample=binary_sample
                )
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(result, default=str).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

def run_server(port: int = 8899):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, StudioRequestHandler)
    print(f"\n=================================================================")
    print(f" 🛡️ SpectraBinary Studio Server Online: http://127.0.0.1:{port}")
    print(f" 📦 Web Dashboard Directory : {WEB_DIR}")
    print(f" ⚡ 10-Phase Engine Active  : REST /api/analyze & /api/health")
    print(f"=================================================================\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Studio Server shutting down cleanly.")
        httpd.server_close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SpectraBinary Studio Local Server")
    parser.add_argument("--port", type=int, default=8899, help="HTTP Port (default: 8899)")
    args = parser.parse_args()
    run_server(args.port)
