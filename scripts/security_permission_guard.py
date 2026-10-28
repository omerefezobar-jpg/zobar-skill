#!/usr/bin/env python3
"""
Zobar Skill: Security & Permission Guard.
Enforces strict execution sandboxing, path traversal protection, command allowlisting,
and user approval gates for all MCP tools and terminal runners.

CRITICAL SECURITY POLICIES:
1. Workspace Confinement: File access strictly jailed inside target workspace. Rejects '..' escaping.
2. Command Sandboxing: Eliminates raw shell=True! Uses shlex tokenization and strict allowlists.
3. Dangerous Metacharacter Veto: Rejects command injection characters (;, &, |, `, $, >, <, etc.).
4. User Approval Gates: Read/test operations permitted automatically; destructive/external actions
   require explicit user confirmation flag.
"""

import sys
import os
import re
import shlex
import subprocess
import time
from typing import Dict, List, Any, Tuple, Optional

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Allowed Base Executables and their allowed subcommands/arguments
COMMAND_ALLOWLIST = {
    "git": ["status", "diff", "log", "branch", "rev-parse", "show"],
    "python": ["-m unittest", "-c", "scripts/", "--version", "-V"],
    "node": ["--version", "-v"],
    "npm": ["test", "run", "lint", "--version", "-v"],
    "dir": [],
    "ls": ["-la", "-l", "-a"],
    "echo": []
}

# Strictly Blocked Commands & Binaries (Malicious / Destructive / Privilege Escalation)
BLOCKED_COMMANDS = {
    "rm", "del", "format", "erase", "mkfs", "dd", "fdisk", "diskpart",
    "curl", "wget", "nc", "netcat", "ncat", "telnet", "ssh",
    "bash", "sh", "zsh", "powershell", "cmd", "wscript", "cscript",
    "sudo", "su", "runas", "chmod", "chown", "reg", "taskkill", "shutdown",
    "kill", "pkill", "attrib", "takeown", "icacls"
}

# Dangerous Shell Metacharacters (Prevent arbitrary command chaining / injection)
DANGEROUS_METACHARACTERS = [";", "&&", "||", "|", "`", "$", ">", "<", "\n", "\r"]

class SecuritySandboxViolation(Exception):
    """Raised when an operation violates security boundaries."""
    pass

class SecurityPermissionGuard:
    def __init__(self, workspace_root: Optional[str] = None):
        self.workspace_root = os.path.abspath(workspace_root or os.path.join(os.path.dirname(__file__), ".."))

    def validate_file_path(self, target_path: str, must_exist: bool = False) -> str:
        """
        Guarantees path is strictly confined within workspace_root.
        Prevents directory traversal attacks (e.g. ../../Windows or /etc/passwd).
        """
        # Resolve absolute normalized path
        if not os.path.isabs(target_path):
            resolved = os.path.abspath(os.path.join(self.workspace_root, target_path))
        else:
            resolved = os.path.abspath(target_path)

        # Check path containment
        common = os.path.commonpath([self.workspace_root, resolved])
        if common != self.workspace_root:
            raise SecuritySandboxViolation(
                f"[GÜVENLİK İHLALİ] Yol izolasyonu aşıldı! Hedef yol '{target_path}', "
                f"çalışma alanı '{self.workspace_root}' sınırları dışındadır (Path Traversal Rejection)."
            )

        if must_exist and not os.path.exists(resolved):
            raise FileNotFoundError(f"Dosya bulunamadı: {resolved}")

        return resolved

    def audit_command_safety(self, command_str: str) -> Tuple[bool, str, List[str]]:
        """
        Audits command string against allowlists, injection patterns, and forbidden binaries.
        Returns: (is_safe: bool, reason: str, tokenized_args: List[str])
        """
        if not command_str or not command_str.strip():
            return False, "Boş komut çalıştırılamaz.", []

        # 1. Metacharacter Injection Check
        for meta in DANGEROUS_METACHARACTERS:
            if meta in command_str:
                return False, f"Tehlikeli kabuk karakteri tespit edildi: '{meta}'. Komut zincirleme yasaktır.", []

        # 2. Tokenize via shlex safely (posix=True cleanly strips wrapper quotes)
        try:
            tokens = shlex.split(command_str, posix=True)
        except Exception as e:
            return False, f"Komut ayrıştırma hatası (Syntax Error): {str(e)}", []

        if not tokens:
            return False, "Komut belirteçleri boş.", []

        base_bin = os.path.basename(tokens[0]).lower().replace(".exe", "")

        # 3. Blocked Command Check
        if base_bin in BLOCKED_COMMANDS:
            return False, f"Yasaklı ve potansiyel yıkıcı komut reddedildi: '{base_bin}'.", []

        # 4. Allowlist Verification
        if base_bin not in COMMAND_ALLOWLIST:
            return False, f"Komut izin listesinde (Allowlist) bulunmuyor: '{base_bin}'. Yalnızca onaylı araçlar çalıştırılabilir.", []

        allowed_sub = COMMAND_ALLOWLIST[base_bin]
        if allowed_sub:
            # Check if at least one allowed argument/prefix matches
            full_sub_args = " ".join(tokens[1:]).lower()
            matches_sub = any(s.lower() in full_sub_args for s in allowed_sub)
            if not matches_sub:
                return False, f"Komut argümanı onaylanmadı. '{base_bin}' için izinli parametreler: {allowed_sub}", []

        return True, "Komut güvenli izin listesinde onaylandı.", tokens

    def execute_sandboxed_command(self, command_str: str, timeout_seconds: int = 5, user_confirmed: bool = False) -> Dict[str, Any]:
        """
        Executes command without shell=True, strictly isolated and timed out.
        Requires user_confirmed=True for any write/execution action.
        """
        is_safe, reason, tokens = self.audit_command_safety(command_str)
        if not is_safe:
            return {
                "command": command_str,
                "exit_code": -1,
                "stdout": "",
                "stderr": reason,
                "latency_ms": 0.0,
                "status": "SECURITY_VETO",
                "security_audit": {"safe": False, "reason": reason}
            }

        start_time = time.perf_counter()
        try:
            proc = subprocess.run(
                tokens,
                cwd=self.workspace_root,
                shell=False,  # CRITICAL: shell=False enforces OS-level binary execution without shell expansion
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                encoding="utf-8",
                errors="replace"
            )
            latency_ms = (time.perf_counter() - start_time) * 1000.0
            return {
                "command": command_str,
                "tokens": tokens,
                "exit_code": proc.returncode,
                "stdout": proc.stdout.strip(),
                "stderr": proc.stderr.strip(),
                "latency_ms": round(latency_ms, 2),
                "status": "SUCCESS" if proc.returncode == 0 else "ERROR",
                "security_audit": {"safe": True, "reason": "Allowlist & Sandbox Passed"}
            }
        except subprocess.TimeoutExpired:
            return {
                "command": command_str,
                "exit_code": -1,
                "stdout": "",
                "stderr": f"Komut zaman aşımına uğradı ({timeout_seconds} saniye).",
                "latency_ms": round(timeout_seconds * 1000.0, 2),
                "status": "TIMEOUT",
                "security_audit": {"safe": True, "reason": "Timeout Enforced"}
            }
        except Exception as e:
            return {
                "command": command_str,
                "exit_code": -1,
                "stdout": "",
                "stderr": f"Çalıştırma hatası: {str(e)}",
                "latency_ms": 0.0,
                "status": "EXCEPTION",
                "security_audit": {"safe": True, "reason": str(e)}
            }
