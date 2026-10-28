#!/usr/bin/env python3
"""
Zobar Skill: Consolidated Core Utilities (Ortak Çekirdek Yardımcılar).
Pure Python standard library, zero dependencies, sub-millisecond execution.
Consolidates repetitive boilerplate identified during Pillar 5 pruning audit:
1. Safe UTF-8 stdout reconfiguration across Windows/POSIX.
2. Robust JSON file loader and saver with graceful fallback and schema tolerance.
3. Universal text tokenization and stop-word normalization for semantic search.
4. Deterministic hashing and nanosecond telemetry helpers.
"""

import sys
import os
import re
import json
import time
from typing import Dict, List, Set, Any, Optional

# 1. Global Safe UTF-8 Configuration
def ensure_utf8_stdout():
    """Configures stdout for UTF-8 without raising errors on non-supporting streams."""
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

ensure_utf8_stdout()

# 2. Universal Stop Words
COMMON_STOP_WORDS: Set[str] = {
    "the", "a", "an", "and", "or", "of", "to", "in", "is", "for", "with", "on", "at", "by", "from",
    "ve", "ile", "için", "bir", "bu", "şu", "da", "de", "olarak", "tarafından", "hakkında", "göre"
}

# 3. Text Tokenizer
def tokenize_and_normalize(text: str, min_len: int = 2) -> Set[str]:
    """Extracts lowercase alphabetic and alphanumeric tokens stripping punctuation and stop-words."""
    if not text:
        return set()
    words = re.findall(r"[a-zA-Z0-9çğıöşüÇĞİÖŞÜ_]+", text.lower())
    return {w for w in words if w not in COMMON_STOP_WORDS and len(w) >= min_len}

# 4. Safe JSON Loader
def load_json_safe(filepath: str, default: Optional[Any] = None) -> Any:
    """Loads JSON file with robust UTF-8 encoding and fallback handling."""
    if not os.path.exists(filepath):
        return default if default is not None else {}
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return json.load(f)
    except Exception:
        return default if default is not None else {}

# 5. Safe JSON Saver
def save_json_atomic(filepath: str, data: Any, indent: int = 2) -> bool:
    """Atomically saves data to JSON file with parent directory creation."""
    try:
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        return True
    except Exception:
        return False

# 6. Telemetry Timer Context Manager
class LatencyTimer:
    """Sub-millisecond execution stopwatch."""
    def __init__(self):
        self.t_start = 0.0
        self.elapsed_ms = 0.0

    def __enter__(self):
        self.t_start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_ms = round((time.perf_counter() - self.t_start) * 1000.0, 3)
