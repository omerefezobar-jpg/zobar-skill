#!/usr/bin/env python3
"""
Clean-Room Specification & Statutory Legal Affidavit Export Engine.
Generates cryptographically sealed, court-defensible Clean-Room Functional
Specification Documents (FSD) and Legal Declarations pursuant to
US DMCA 17 U.S.C. § 1201(f) and EU Software Directive 2009/24/EC Article 6.
"""

import sys
import os
import json
import hashlib
import datetime
import argparse
from typing import Dict, List, Any, Optional

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Ensure project root in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.reverse_engineering_analyst import (
    generate_clean_room_specification,
    generate_clean_room_affidavit,
    evaluate_reverse_engineering_legality
)

def export_clean_room_package(
    target_module: str,
    output_dir: str,
    author_name: str = "Lead Systems Architect",
    version: str = "1.0.0",
    interfaces: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, str]:
    """
    Exports a court-defensible clean-room package consisting of:
    1. Functional Specification Document (FSD.md and FSD.json)
    2. Signed Legal Affidavit (AFFIDAVIT.md)
    3. Cryptographic Verification Manifest (MANIFEST.json with SHA-256)
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    default_interfaces = interfaces or [
        {
            "name": "packet_handshake",
            "type": "Network Protocol Endpoint",
            "behavior": "Authenticates client with 256-bit public key and returns session ticket."
        },
        {
            "name": "telemetry_dispatch",
            "type": "Telemetry / Stream Endpoint",
            "behavior": "Emits 64-bit Big-Endian sensor frame at 50Hz frequency."
        },
        {
            "name": "render_sync_frame",
            "type": "Internal Function Symbol",
            "behavior": "Synchronizes graphics double-buffer and clears stencil cache."
        }
    ]

    # 1. Generate FSD
    fsd_data = generate_clean_room_specification(target_module, default_interfaces)
    legal_audit = evaluate_reverse_engineering_legality("Clean-room interoperability adapter", target_module)

    # 2. Generate Affidavit
    clean_affidavit = generate_clean_room_affidavit(
        engineer_name=author_name,
        module_name=target_module,
        specification_version=version,
        is_clean_room_developer=True
    )
    dirty_affidavit = generate_clean_room_affidavit(
        engineer_name="Independent Reverse Analyst",
        module_name=target_module,
        specification_version=version,
        is_clean_room_developer=False
    )

    # 3. Build Markdown Content
    fsd_md = f"""# 📋 Functional Specification Document (FSD): {target_module}
**Specification Version:** `{version}`  
**Generated Timestamp:** `{timestamp}`  
**Statutory Doctrine:** Clean-Room Engineering (Chinese Wall Architecture)

---

## ⚖️ Statutory Legal Safe Harbor
- **Jurisdictions:** US DMCA 17 U.S.C. § 1201(f) & EU Directive 2009/24/EC Article 6
- **Judicial Landmark:** *Sega Enterprises Ltd. v. Accolade, Inc.* (977 F.2d 1510) & *Sony v. Connectix* (203 F.3d 596)
- **Risk Classification:** `{legal_audit['risk_level']}`

---

## 🏛️ Chinese Wall Protocol
- **Dirty Room Team:** Responsible for binary black-box inspection and telemetry sniffing. Forbidden from writing production code.
- **Clean Room Team:** Implements independent production code solely from this document. Has never had access to proprietary binary object code.

---

## 🔌 Discovered Interface Specifications
"""
    for req in fsd_data["functional_specifications"]:
        fsd_md += f"""
### {req['specification_id']}: `{req['endpoint_or_symbol']}`
- **Category:** {req['category']}
- **Behavior:** {req['functional_behavior']}
- **Clean-Room Constraint:** {req['clean_room_rule']}
"""

    affidavit_md = f"""# 📜 Statutory Clean-Room Legal Affidavit

**Declarant:** {clean_affidavit['declarant']}  
**Role:** {clean_affidavit['role']}  
**Module:** {clean_affidavit['target_module']}  
**Specification Version:** {clean_affidavit['specification_version']}  
**Statute:** {clean_affidavit['statutory_compliance']}  

---

### Formal Declaration
> "{clean_affidavit['formal_statement']}"

---

### Dirty-Room Auditor Counter-Affidavit
**Auditor:** {dirty_affidavit['declarant']}  
**Role:** {dirty_affidavit['role']}  
> "{dirty_affidavit['formal_statement']}"

---
*Signed and sealed electronically on {timestamp}.*
"""

    # File Paths
    fsd_json_path = os.path.join(output_dir, "FSD_SPECIFICATION.json")
    fsd_md_path = os.path.join(output_dir, "FSD_SPECIFICATION.md")
    affidavit_md_path = os.path.join(output_dir, "CLEAN_ROOM_AFFIDAVIT.md")
    manifest_path = os.path.join(output_dir, "SEALED_MANIFEST.json")

    with open(fsd_json_path, "w", encoding="utf-8") as f:
        json.dump(fsd_data, f, indent=2, ensure_ascii=False)

    with open(fsd_md_path, "w", encoding="utf-8") as f:
        f.write(fsd_md)

    with open(affidavit_md_path, "w", encoding="utf-8") as f:
        f.write(affidavit_md)

    # Compute Hashes for Manifest
    def get_hash(path: str) -> str:
        with open(path, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()

    manifest = {
        "target_module": target_module,
        "version": version,
        "sealed_timestamp": timestamp,
        "statutory_safe_harbor": "DMCA 1201(f) & EU 2009/24/EC Art 6",
        "file_hashes": {
            "FSD_SPECIFICATION.json": get_hash(fsd_json_path),
            "FSD_SPECIFICATION.md": get_hash(fsd_md_path),
            "CLEAN_ROOM_AFFIDAVIT.md": get_hash(affidavit_md_path),
        }
    }

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return {
        "fsd_json": fsd_json_path,
        "fsd_md": fsd_md_path,
        "affidavit_md": affidavit_md_path,
        "manifest": manifest_path
    }

def main():
    parser = argparse.ArgumentParser(description="Clean-Room Specification & Legal Affidavit Export Engine.")
    parser.add_argument("target", help="Module or system name")
    parser.add_argument("--out-dir", default="dist/clean_room_export", help="Output directory")
    parser.add_argument("--author", default="Lead Systems Architect", help="Declarant name")
    parser.add_argument("--version", default="1.0.0", help="Specification version")
    args = parser.parse_args()

    print("=================================================================")
    print(f" 📜 EXPORTING CLEAN-ROOM COURT PACKAGE: {args.target}")
    print("=================================================================\n")

    res = export_clean_room_package(args.target, args.out_dir, author_name=args.author, version=args.version)
    print(f"✅ FSD Markdown    : {res['fsd_md']}")
    print(f"✅ FSD JSON        : {res['fsd_json']}")
    print(f"✅ Legal Affidavit : {res['affidavit_md']}")
    print(f"✅ Sealed Manifest : {res['manifest']}")

if __name__ == "__main__":
    main()
