#!/usr/bin/env python3
"""
Enterprise Security, Red Teaming & Regulatory Fortification Engine.
Enforces multi-layered security, intellectual property clean-room isolation,
prompt-injection defenses, and compliance with the EU AI Act & GDPR/KVKK.

Modules:
1. Jailbreak & Prompt Injection Red Teaming (Indirect injection, delimiter spoofing, roleplay escapes).
2. Clean-Room IP Shield (Separation of Dirty Analysis & Clean Reproduction, clean functional specs).
3. Regulatory Audit (EU AI Act High-Risk Category Classifier, Art. 5 Prohibited AI, GDPR Art. 17/22).
4. Automated Penetration & Hardening Gatekeeper (Score in [0 - 100], Zero-Tolerance Policy).
"""

import sys
import os
import re
import json
import time
import argparse
from typing import Dict, List, Any, Optional, Tuple

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


# Common and sophisticated prompt injection / jailbreak attack vectors
RED_TEAM_ATTACK_PATTERNS = [
    {
        "vector_id": "VEC-DELIM-SPOOF",
        "name": "Delimiter & System Tag Spoofing",
        "pattern": r"(?:<SYSTEM_MESSAGE>|<\|im_start\|>|<\|im_end\|>|\[SYSTEM\]|system:|<identity>|Human:|Assistant:)",
        "severity": "CRITICAL",
        "description": "Attempts to inject artificial system tags or turn boundaries to hijack system prompt."
    },
    {
        "vector_id": "VEC-INDIRECT-INJECT",
        "name": "Indirect Instruction Overriding",
        "pattern": r"(?:ignore\s+(?:all\s+)?previous\s+instructions|disregard\s+(?:the\s+)?rules|forget\s+all\s+guidelines)",
        "severity": "HIGH",
        "description": "Direct adversarial instruction reset commands attempting to wipe behavioral guardrails."
    },
    {
        "vector_id": "VEC-PRIV-ESC",
        "name": "Root & Shell Command Injection",
        "pattern": r"(?:;\s*rm\s+-rf|powershell\s+-enc|cmd\.exe\s+/c|wget\s+http|curl\s+-s\s+http|eval\s*\(|exec\s*\()",
        "severity": "CRITICAL",
        "description": "Attempts to chain unauthorized shell payloads or execute unconstrained code."
    },
    {
        "vector_id": "VEC-IP-POACH",
        "name": "Proprietary Code / Secret Extraction",
        "pattern": r"(?:print\s+(?:the\s+)?system\s+prompt|reveal\s+(?:your\s+|internal\s+)?system\s+prompt|reveal\s+(?:your\s+)?internal\s+instructions|dump\s+(?:api\s+keys?|environment\s+variables?))",
        "severity": "HIGH",
        "description": "Extraction of confidential internal prompts, credentials, or proprietary intellectual property."
    },
    {
        "vector_id": "VEC-ROLEPLAY-ESCAPE",
        "name": "Adversarial Persona / DAN Roleplay Escape",
        "pattern": r"(?:you\s+are\s+now\s+DAN|do\s+anything\s+now|unfiltered\s+mode|developer\s+mode\s+enabled)",
        "severity": "HIGH",
        "description": "Adversarial roleplay frames designed to bypass safety filters and legal compliance."
    }
]


class SecurityAndRegulatoryEngine:
    """
    Comprehensive gatekeeper for prompt injection defense,
    Clean-Room IP provenance, and EU AI Act / GDPR compliance.
    """

    def __init__(self):
        self.attack_patterns = RED_TEAM_ATTACK_PATTERNS

    # =========================================================================
    # 1. RED TEAMING & PROMPT INJECTION SCANNER
    # =========================================================================
    def scan_prompt_injection(self, text_input: str) -> Dict[str, Any]:
        """
        Scans incoming instructions or external text inputs for red team adversarial vectors.
        """
        if not text_input:
            return {"is_safe": True, "violations": [], "threat_score": 0.0}

        violations = []
        threat_score = 0.0

        for vec in self.attack_patterns:
            matches = re.findall(vec["pattern"], text_input, flags=re.IGNORECASE)
            if matches:
                weight = 40.0 if vec["severity"] == "CRITICAL" else 25.0
                threat_score += weight * len(matches)
                violations.append({
                    "vector_id": vec["vector_id"],
                    "vector_name": vec["name"],
                    "severity": vec["severity"],
                    "matched_substrings": matches[:3],
                    "mitigation": "Sanitize and neutralize adversarial delimiters; preserve system prompt boundary."
                })

        threat_score = min(100.0, threat_score)
        is_safe = len(violations) == 0

        return {
            "is_safe": is_safe,
            "threat_score": round(threat_score, 1),
            "safety_verdict": "SECURE" if is_safe else "ADVERSARIAL_INJECTION_DETECTED",
            "violations_count": len(violations),
            "violations": violations
        }

    # =========================================================================
    # 2. CLEAN-ROOM INTELLECTUAL PROPERTY SHIELD
    # =========================================================================
    def audit_clean_room_provenance(
        self,
        analysis_dirty_room_notes: str,
        clean_room_implementation_code: str
    ) -> Dict[str, Any]:
        """
        Enforces Clean-Room Reverse Engineering & Legal IP Provenance:
        1. Analyzes whether proprietary strings, exact copyrighted variable names, or decompiled byte patterns leaked into clean code.
        2. Ensures clean implementation relies only on functional specifications (inputs, outputs, mathematical state transitions).
        """
        # Extract potential proprietary tokens from dirty room notes
        dirty_tokens = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]{5,}\b", analysis_dirty_room_notes))
        clean_tokens = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]{5,}\b", clean_room_implementation_code))

        # Check for direct suspicious verbatim overlap of specialized identifiers
        common_identifiers = dirty_tokens.intersection(clean_tokens)
        
        # Whitelisted standard terms
        safe_words = {"function", "return", "status", "result", "payload", "system", "timestamp", "import", "class"}
        suspicious_leakages = [t for t in common_identifiers if t.lower() not in safe_words]

        is_clean = len(suspicious_leakages) == 0
        clean_score = 100.0 if is_clean else max(0.0, 100.0 - (len(suspicious_leakages) * 15.0))

        return {
            "clean_room_status": "CERTIFIED_CLEAN_ROOM" if is_clean else "DIRTY_ROOM_CONTAMINATION_RISK",
            "clean_score": clean_score,
            "suspicious_leaked_identifiers": suspicious_leakages,
            "legal_protection_standard": (
                "Complies with Sony Computer Entertainment v. Connectix Corp (9th Cir. 2000) "
                "and NEC v. Intel clean-room functional specification precedents."
            )
        }

    # =========================================================================
    # 3. REGULATORY COMPLIANCE AUDIT (EU AI ACT & GDPR)
    # =========================================================================
    def audit_regulatory_compliance(self, domain_or_product_spec: str) -> Dict[str, Any]:
        """
        Audits product specification against EU AI Act (2024/1689), GDPR (2016/679), and KVKK.
        Classifies risk tiers:
        - Unacceptable Risk (Prohibited under Art. 5: Social scoring, subliminal manipulation, real-time biometric mass surveillance)
        - High Risk (Annex III: Critical infrastructure, medical diagnostics, credit scoring, autonomous vehicles)
        - Specific Transparency Risk (Art. 50: Synthetic audio/video/text disclosure)
        - Minimal / No Risk (Standard SaaS, developer tooling, e-commerce)
        """
        spec_lower = domain_or_product_spec.lower()

        # 1. Prohibited Check (Art. 5)
        prohibited_matches = []
        if any(k in spec_lower for k in ["social scoring", "subliminal manipulation", "biometric mass surveillance", "emotion recognition in workplace"]):
            prohibited_matches.append("Article 5 EU AI Act: Prohibited AI Practice.")

        # 2. High Risk Check (Annex III)
        is_high_risk = False
        high_risk_reasons = []
        if any(k in spec_lower for k in ["medical diagnosis", "clinical patient triage", "clinical telemetry", "autonomous vehicle", "critical infrastructure power grid"]):
            is_high_risk = True
            high_risk_reasons.append("Annex III (Health/Safety): High-Risk Medical/Infrastructure AI System requiring Conformity Assessment.")
        if any(k in spec_lower for k in ["creditworthiness", "credit scoring", "loan underwriting", "automated hiring screening"]):
            is_high_risk = True
            high_risk_reasons.append("Annex III (Fundamental Rights): High-Risk Financial/Employment AI.")

        # 3. GDPR Automated Decision-Making (Art. 22)
        gdpr_triggers = []
        if "automated decision" in spec_lower or "profiling" in spec_lower:
            gdpr_triggers.append("GDPR Article 22: Mandates human-in-the-loop oversight and right to contest automated decisions.")
        if "user data" in spec_lower or "personal data" in spec_lower:
            gdpr_triggers.append("GDPR Article 17: Right to Erasure ('Right to be Forgotten') and data portability.")

        if prohibited_matches:
            risk_tier = "UNACCEPTABLE_RISK_PROHIBITED"
            action = "HALT DEPLOYMENT: Violates Article 5 EU AI Act."
        elif is_high_risk:
            risk_tier = "HIGH_RISK_ANNEX_III"
            action = "MANDATORY: Execute Fundamental Rights Impact Assessment (FRIA), human oversight, and quality management."
        else:
            risk_tier = "MINIMAL_RISK_STANDARD"
            action = "STANDARD COMPLIANCE: Adhere to standard transparency disclosures (Article 50) and GDPR privacy by design."

        return {
            "product_scope": domain_or_product_spec,
            "eu_ai_act_risk_tier": risk_tier,
            "prohibited_violations": prohibited_matches,
            "high_risk_triggers": high_risk_reasons,
            "gdpr_compliance_mandates": gdpr_triggers,
            "recommended_legal_action": action,
            "legal_gate_verdict": "PASSED" if not prohibited_matches else "BLOCKED"
        }

    # =========================================================================
    # 4. COMPOSITE SECURITY GATEKEEPER
    # =========================================================================
    def execute_full_security_audit(
        self,
        text_input: str,
        dirty_notes: str = "",
        clean_code: str = ""
    ) -> Dict[str, Any]:
        """
        Executes unified security, red teaming, clean-room, and regulatory gate check.
        """
        injection_report = self.scan_prompt_injection(text_input)
        clean_room_report = self.audit_clean_room_provenance(dirty_notes, clean_code) if clean_code else {"clean_score": 100.0, "clean_room_status": "SKIPPED_NO_CODE"}
        reg_report = self.audit_regulatory_compliance(text_input)

        overall_passed = injection_report["is_safe"] and reg_report["legal_gate_verdict"] == "PASSED" and clean_room_report["clean_score"] >= 80.0

        return {
            "overall_passed": overall_passed,
            "composite_security_rating": round((
                (100.0 - injection_report["threat_score"]) * 0.4
                + clean_room_report["clean_score"] * 0.3
                + (100.0 if reg_report["legal_gate_verdict"] == "PASSED" else 0.0) * 0.3
            ), 1),
            "prompt_injection_guard": injection_report,
            "clean_room_guard": clean_room_report,
            "regulatory_guard": reg_report
        }


def main():
    parser = argparse.ArgumentParser(description="Enterprise Security & Regulatory Fortification Engine.")
    parser.add_argument("--input", type=str, default="Medical clinical diagnosis platform with automated decision making", help="System prompt or task description")
    args = parser.parse_args()

    engine = SecurityAndRegulatoryEngine()
    res = engine.execute_full_security_audit(args.input)

    print("\n=================================================================")
    print(" 🛡️ ENTERPRISE SECURITY, RED TEAMING & LEGAL AUDIT GATE")
    print("=================================================================")
    print(f"📊 Overall Passed       : {res['overall_passed']}")
    print(f"💎 Security Rating      : {res['composite_security_rating']}/100")
    print(f"🛡️ Injection Status     : {res['prompt_injection_guard']['safety_verdict']}")
    print(f"🏛️ EU AI Act Tier       : {res['regulatory_guard']['eu_ai_act_risk_tier']}")
    print(f"⚖️ Recommended Action   : {res['regulatory_guard']['recommended_legal_action']}\n")


if __name__ == "__main__":
    main()
