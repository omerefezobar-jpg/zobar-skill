#!/usr/bin/env python3
"""
Automated Tech Stack & Component Architecture Synthesizer for Frontier Innovator (Phase 5).
Evaluates system latency, concurrency, memory safety, and UI ergonomics, generating
a concrete, justified technology stack and component specification.
"""

import sys
import argparse

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def synthesize_tech_stack(domain: str):
    """
    Selects optimal languages, frameworks, and UI components based on domain constraints.
    """
    lowered = domain.lower()
    
    # 1. Core Engine Language Selection
    if any(k in lowered for k in ["compiler", "ast", "parser", "realtime", "high performance", "system", "embedded", "crypto"]):
        core_lang = "Rust"
        core_reason = "Bellek güvenliği (ownership & borrow checker), sıfır maliyetli soyutlama (zero-cost abstractions) ve nanosaniye seviyesinde Tree-sitter AST analizi."
        core_libs = ["tree-sitter", "tokio", "rayon", "serde", "wasmtime"]
    elif any(k in lowered for k in ["distributed", "network", "microservice", "gateway", "orchestrat"]):
        core_lang = "Go"
        core_reason = "Hafif goroutine'ler, yerleşik concurrency mimarisi ve mikro-servisler arası düşük gecikmeli RPC haberleşmesi."
        core_libs = ["gRPC", "chi", "protobuf", "zap", "temporal-sdk-go"]
    else:
        core_lang = "TypeScript / Rust (Hibrit Mimari)"
        core_reason = "Uç nokta hızını Rust ile garantiye alırken, geliştirici ergonomisi ve modülerliği TypeScript/Node.js ile sağlama."
        core_libs = ["tokio", "zod", "trpc", "neon-bindings"]

    # 2. Data & State Storage Layer
    if "vector" in lowered or "agent" in lowered or "ai" in lowered:
        data_layer = "Embedded Vector DB (LanceDB / Qdrant Embedded) + SQLite / LibSQL"
        data_reason = "Harici veritabanı sunucusu bağımlılığını sıfıra indiren yerel, disk dostu ve sıfır-konfigürasyon gömülü mimari."
    else:
        data_layer = "PostgreSQL + Redis (Dağıtık) veya Embedded SQLite (Masaüstü/CLI)"
        data_reason = "ACID güvencesi, WAL modu ile yüksek okuma/yazma throughput'u."

    # 3. UI/UX Component Architecture
    ui_stack = {
        "runtime": "Tauri v2 + React 19 (Desktop/Web Native)",
        "design_system": "Tailwind CSS v4 + Radix UI Primitives (Erişilebilir, Bilişsel Yükü Düşük)",
        "specialized_components": [
            "Shadcn/ui Data Table (Sanal scroll ile 100k+ satır akıcı render)",
            "Monaco Editor / Canvas Diff Viewer (Kod ve şema görselleştirme)",
            "Mermaid.js / React Flow (Dinamik mimari akış görselleştirici)"
        ],
        "ergonomic_rule": "Bilişsel Kalkan (Zero-Noise UX): Kullanıcıya sadece onay gerektiren yüksek değerli aksiyonları göster; arka plan loglarını katlanabilir tut."
    }

    return {
        "domain": domain,
        "core_language": core_lang,
        "language_justification": core_reason,
        "recommended_libraries": core_libs,
        "data_layer": data_layer,
        "data_justification": data_reason,
        "ui_architecture": ui_stack
    }

def main():
    parser = argparse.ArgumentParser(description="Phase 5 Architectural Synthesizer.")
    parser.add_argument("domain", help="Target domain for architectural synthesis")
    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f" 🛠️ OTOMATİK MİMARİ & BİLEŞEN SENTEZİ: '{args.domain}'")
    print(f"=======================================================\n")

    arch = synthesize_tech_stack(args.domain)
    print(f"🖥️ Çekirdek Dil      : {arch['core_language']}")
    print(f"   Seçim Gerekçesi   : {arch['language_justification']}")
    print(f"   Temel Kütüphaneler: {', '.join(arch['recommended_libraries'])}\n")
    print(f"💾 Veri Katmanı      : {arch['data_layer']}")
    print(f"   Veri Gerekçesi    : {arch['data_justification']}\n")
    print(f"🎨 Arayüz Mimarisi   : {arch['ui_architecture']['runtime']}")
    print(f"   Tasarım Sistemi   : {arch['ui_architecture']['design_system']}")
    print(f"   Kural             : {arch['ui_architecture']['ergonomic_rule']}")

if __name__ == "__main__":
    main()
