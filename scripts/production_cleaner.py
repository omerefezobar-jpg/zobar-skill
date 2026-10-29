#!/usr/bin/env python3
"""
Production Output Sanitizer & Clean Enterprise Formatter.
Eliminates internal bot signatures, self-referential meta-branding ('zobar', 'zobar mühendislik', etc.)
and formats generated applications, UIs, and source code into pristine, real-world enterprise standards.
"""

import sys
import re
import argparse
from typing import Dict, List, Any, Optional

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Patterns to sanitize and replace with clean production enterprise equivalents
BRANDING_PATTERNS = [
    (r"(?i)\bzobar\s+mühendislik\b", "Enterprise Engineering"),
    (r"(?i)\bzobar\s+skill\b", "Core Architecture"),
    (r"(?i)\bzobar\s+s-tier\b", "Enterprise S-Tier"),
    (r"(?i)\bzobar\s+mimari\b", "System Architecture"),
    (r"(?i)\bzobar\b", "ApexCore"),
    (r"(?i)\[zobar\]", "[Core]"),
    (r"(?i)⚡\s*zobar\b", "⚡ Enterprise System"),
    (r"(?i)zobar_skill", "enterprise_core"),
    (r"(?i)zobar_mcp", "core_mcp"),
]

def sanitize_production_output(text: str, custom_project_name: str = "Enterprise System") -> str:
    """
    Sanitizes raw generated text, UI code, HTML, or python source.
    Replaces internal self-referential labels with clean, professional enterprise terminology.
    """
    if not text:
        return ""

    sanitized = text
    for pattern, replacement in BRANDING_PATTERNS:
        # If user supplied a custom project name and pattern is pure 'zobar', use custom name
        if "ApexCore" in replacement and custom_project_name != "Enterprise System":
            sanitized = re.sub(pattern, custom_project_name, sanitized)
        else:
            sanitized = re.sub(pattern, replacement, sanitized)

    # Clean up multi-line internal meta comments
    sanitized = re.sub(r"#\s*⚡\s*ZOBAR.*?\n", "", sanitized)
    sanitized = re.sub(r"<!--\s*⚡\s*ZOBAR.*?-->", "", sanitized)

    return sanitized

def inspect_cleanliness(text: str) -> Dict[str, Any]:
    """Audits text to verify if any internal branding or meta-slogans remain."""
    flagged = []
    lower_text = text.lower()
    for keyword in ["zobar", "zobar mühendislik", "zobar skill"]:
        matches = [m.start() for m in re.finditer(re.escape(keyword), lower_text)]
        if matches:
            flagged.append({"keyword": keyword, "count": len(matches), "offsets": matches[:5]})

    is_clean = len(flagged) == 0
    return {
        "is_production_clean": is_clean,
        "cleanliness_score": 100.0 if is_clean else max(0.0, 100.0 - (len(flagged) * 25.0)),
        "flagged_keywords": flagged,
        "recommendation": "Ready for client delivery without internal meta chatter." if is_clean else "Sanitize output before production deployment."
    }

def main():
    parser = argparse.ArgumentParser(description="Production Output Sanitizer & Clean Enterprise Formatter.")
    parser.add_argument("--file", help="Path to file to sanitize in-place")
    parser.add_argument("--project-name", default="ApexCore", help="Enterprise brand name to replace internal tags")
    parser.add_argument("--check-only", action="store_true", help="Audit without modifying")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        audit = inspect_cleanliness(content)
        if args.check_only:
            print(f"Cleanliness Audit: {audit['cleanliness_score']}% (Clean: {audit['is_production_clean']})")
            sys.exit(0 if audit["is_production_clean"] else 1)

        cleaned = sanitize_production_output(content, custom_project_name=args.project_name)
        with open(args.file, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"File sanitized successfully: {args.file}")
    else:
        sample = "Zobar Mühendislik standardı ile üretilen Zobar Skill modülü."
        print("Original :", sample)
        print("Sanitized:", sanitize_production_output(sample))

if __name__ == "__main__":
    main()
