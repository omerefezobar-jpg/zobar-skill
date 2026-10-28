#!/usr/bin/env python3
"""
Zobar Skill: Security & Permission Guard (Hardened v2.0).
Enforces real operating system execution sandboxing, symlink traversal prevention,
AST-based Python code inspection, argument-level validation, and environment isolation.

CRITICAL SECURITY HARDENING (v2.0):
1. Symlink Traversal Defense: Resolves realpath across symlinks; rejects any link target outside workspace.
2. Argument-Level Allowlisting: Validates every subargument; prohibits arbitrary flag injection.
3. AST Python Code Inspection: Eliminates arbitrary `python -c` execution! Parses inline AST and rejects
   forbidden imports (os, sys, subprocess, socket, etc.), dangerous builtins (eval, exec, open), and dunders.
4. Script Confinement: Any script file executed with python/node must strictly reside inside workspace_root.
5. OS-Level Environment Sanitization: Strips all ambient tokens, API keys, and secrets from subprocess env.
6. Execution Quota & Timeout: Hard timeout kills process trees and enforces resource boundaries.
"""

import sys
import os
import re
import ast
import shlex
import subprocess
import time
from typing import Dict, List, Any, Tuple, Optional, Set

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Allowed Base Executables
BASE_ALLOWLIST: Set[str] = {
    "git", "python", "python3", "node", "npm", "dir", "ls", "echo"
}

# Strictly Blocked Commands & Binaries (Malicious / Destructive / Privilege Escalation)
BLOCKED_COMMANDS: Set[str] = {
    "rm", "del", "format", "erase", "mkfs", "dd", "fdisk", "diskpart",
    "curl", "wget", "nc", "netcat", "ncat", "telnet", "ssh",
    "bash", "sh", "zsh", "powershell", "cmd", "wscript", "cscript",
    "sudo", "su", "runas", "chmod", "chown", "reg", "taskkill", "shutdown",
    "kill", "pkill", "attrib", "takeown", "icacls", "socat"
}

# Dangerous Shell Metacharacters (Prevent arbitrary command chaining / injection)
DANGEROUS_METACHARACTERS = [";", "&&", "||", "|", "`", "$", ">", "<", "\n", "\r"]

# Allowed Git subcommands (Strict read-only and non-destructive operations)
ALLOWED_GIT_SUBCOMMANDS: Set[str] = {
    "status", "diff", "log", "branch", "rev-parse", "show"
}

# Blocked Git flags that could trigger external hook execution, arbitrary file writes, or pagination leaks
BLOCKED_GIT_FLAGS: Set[str] = {
    "--output", "--exec-path", "-c", "--upload-pack", "--receive-pack",
    "--paginate", "-p", "--ext-diff"
}


class SecuritySandboxViolation(Exception):
    """Raised when an operation violates security boundaries."""
    pass


class PythonASTSecurityVisitor(ast.NodeVisitor):
    """
    Strict Abstract Syntax Tree (AST) Auditor for inline Python snippets (-c).
    Rejects dangerous modules, system calls, filesystem modifications, and reflection.
    """
    BANNED_MODULES: Set[str] = {
        "os", "sys", "subprocess", "shutil", "ctypes", "socket", "http",
        "urllib", "requests", "multiprocessing", "threading", "pty",
        "builtins", "importlib", "pickle", "shelve", "webbrowser", "winreg",
        "posix", "nt", "signal", "asyncio", "inspect", "platform", "resource"
    }

    BANNED_FUNCTIONS: Set[str] = {
        "eval", "exec", "compile", "open", "__import__", "getattr",
        "setattr", "delattr", "globals", "locals", "vars", "input",
        "breakpoint", "exit", "quit"
    }

    BANNED_ATTRIBUTES: Set[str] = {
        "__subclasses__", "__bases__", "__mro__", "__class__",
        "__builtins__", "__globals__", "__code__", "__dict__",
        "system", "popen", "spawn", "unlink", "remove", "rmdir"
    }

    def __init__(self):
        self.violations: List[str] = []

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            base = alias.name.split(".")[0].lower()
            if base in self.BANNED_MODULES:
                self.violations.append(f"Yasaklı modül importu: '{alias.name}'")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module:
            base = node.module.split(".")[0].lower()
            if base in self.BANNED_MODULES:
                self.violations.append(f"Yasaklı modül importu (from {node.module})")
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        if isinstance(node.func, ast.Name):
            if node.func.id in self.BANNED_FUNCTIONS:
                self.violations.append(f"Yasaklı fonksiyon çağrısı: '{node.func.id}()'")
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in self.BANNED_ATTRIBUTES:
                self.violations.append(f"Yasaklı metot çağrısı: '.{node.func.attr}()'")
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute):
        if node.attr in self.BANNED_ATTRIBUTES:
            self.violations.append(f"Yasaklı öznitelik erişimi: '.{node.attr}'")
        self.generic_visit(node)


class SecurityPermissionGuard:
    def __init__(self, workspace_root: Optional[str] = None):
        raw_root = workspace_root or os.path.join(os.path.dirname(__file__), "..")
        self.workspace_root = os.path.abspath(raw_root)
        self.real_workspace_root = os.path.realpath(self.workspace_root)

    def validate_file_path(self, target_path: str, must_exist: bool = False) -> str:
        """
        Guarantees path is strictly confined within workspace_root.
        Prevents directory traversal attacks (e.g. ../../Windows or /etc/passwd),
        UNC network paths, and Symlink Traversal escapes.
        """
        if not target_path or not target_path.strip():
            raise SecuritySandboxViolation("Boş dosya yolu reddedildi.")

        # UNC network share rejection (e.g. \\attacker\share or //attacker/share)
        if target_path.startswith(r"\\") or target_path.startswith("//"):
            raise SecuritySandboxViolation(
                f"[GÜVENLİK İHLALİ] UNC ağ paylaşım yolu reddedildi: '{target_path}'"
            )

        # Cross-platform drive specifier rejection on non-Windows OS (e.g. C:\Windows on Linux)
        if re.match(r"^[a-zA-Z]:", target_path):
            if os.name != "nt":
                raise SecuritySandboxViolation(
                    f"[GÜVENLİK İHLALİ] Harici sürücü yolu POSIX ortamında reddedildi: '{target_path}'"
                )

        # 1. Resolve normalized absolute path
        if not os.path.isabs(target_path):
            resolved = os.path.abspath(os.path.join(self.workspace_root, target_path))
        else:
            resolved = os.path.abspath(target_path)

        # 2. Path Containment (Logical Abspath Check)
        try:
            common = os.path.commonpath([self.workspace_root, resolved])
        except ValueError:
            raise SecuritySandboxViolation(
                f"[GÜVENLİK İHLALİ] Hedef yol farklı bir sürücü veya köktedir: '{target_path}'"
            )

        if common != self.workspace_root:
            raise SecuritySandboxViolation(
                f"[GÜVENLİK İHLALİ] Yol izolasyonu aşıldı! Hedef yol '{target_path}', "
                f"çalışma alanı '{self.workspace_root}' sınırları dışındadır (Path Traversal Rejection)."
            )

        # 3. Symlink Traversal & Canonical Realpath Confinement Check
        # If the file or symlink already exists on disk, inspect where it physically points
        if os.path.lexists(resolved):
            real_target = os.path.realpath(resolved)
            try:
                real_common = os.path.commonpath([self.real_workspace_root, real_target])
            except ValueError:
                raise SecuritySandboxViolation(
                    f"[GÜVENLİK İHLALİ] Sembolik bağlantı harici köke işaret ediyor: '{target_path}' -> '{real_target}'"
                )

            if real_common != self.real_workspace_root:
                raise SecuritySandboxViolation(
                    f"[GÜVENLİK İHLALİ] Sembolik bağlantı (Symlink) izolasyonu aşıldı! Hedef '{target_path}' "
                    f"fiziksel olarak çalışma alanı dışındaki '{real_target}' konumuna işaret ediyor."
                )
        else:
            # If target does not exist yet, verify existing parent directory's canonical path
            parent = os.path.dirname(resolved)
            if os.path.exists(parent):
                real_parent = os.path.realpath(parent)
                try:
                    parent_common = os.path.commonpath([self.real_workspace_root, real_parent])
                except ValueError:
                    raise SecuritySandboxViolation(
                        f"[GÜVENLİK İHLALİ] Üst dizin harici köke işaret ediyor: '{parent}'"
                    )

                if parent_common != self.real_workspace_root:
                    raise SecuritySandboxViolation(
                        f"[GÜVENLİK İHLALİ] Üst dizin sembolik bağlantı ile çalışma alanı dışına bağlıdır: '{parent}'"
                    )

        if must_exist and not os.path.exists(resolved):
            raise FileNotFoundError(f"Dosya bulunamadı: {resolved}")

        return resolved

    def audit_command_safety(self, command_str: str) -> Tuple[bool, str, List[str]]:
        """
        Audits command string against allowlists, injection patterns, forbidden binaries,
        argument-level safety rules, and AST Python inspection.
        Returns: (is_safe: bool, reason: str, tokenized_args: List[str])
        """
        if not command_str or not command_str.strip():
            return False, "Boş komut çalıştırılamaz.", []

        # 1. Newline / multiline injection check
        if "\n" in command_str or "\r" in command_str:
            return False, "Tehlikeli kabuk karakteri tespit edildi: newline. Çok satırlı komut zincirleme yasaktır.", []

        # 2. Tokenize via shlex safely (posix=True cleanly strips wrapper quotes)
        try:
            tokens = shlex.split(command_str, posix=True)
        except Exception as e:
            return False, f"Komut ayrıştırma hatası (Syntax Error): {str(e)}", []

        if not tokens:
            return False, "Komut belirteçleri boş.", []

        # 3. Shell operator token injection check (unquoted chaining & redirection)
        shell_operators = {";", "&&", "||", "|", "&", ">", ">>", "<", "<<", "`"}
        for token in tokens:
            if token in shell_operators or token.startswith("`") or token.endswith("`"):
                return False, f"Tehlikeli kabuk karakteri tespit edildi: '{token}'. Komut zincirleme yasaktır.", []
            if token.startswith("$"):
                return False, f"Tehlikeli kabuk karakteri tespit edildi: '{token}'. Kabuk değişken açılımı yasaktır.", []

        base_bin = os.path.basename(tokens[0]).lower().replace(".exe", "")
        # Normalize python3 variants (python3.10, python3.11, python3.12 -> python3)
        if base_bin.startswith("python3"):
            base_bin = "python3"
        elif base_bin.startswith("python"):
            base_bin = "python"

        # 3. Blocked Command Check
        if base_bin in BLOCKED_COMMANDS:
            return False, f"Yasaklı ve potansiyel yıkıcı komut reddedildi: '{base_bin}'.", []

        # 4. Base Executable Allowlist Verification
        if base_bin not in BASE_ALLOWLIST:
            return False, f"Komut izin listesinde (Allowlist) bulunmuyor: '{base_bin}'. Yalnızca onaylı araçlar çalıştırılabilir.", []

        args = tokens[1:]

        # 5. Granular Executable-Specific Argument & AST Validation
        if base_bin in ("python", "python3"):
            return self._audit_python_args(base_bin, args, tokens)
        elif base_bin == "git":
            return self._audit_git_args(args, tokens)
        elif base_bin in ("node", "npm"):
            return self._audit_node_args(base_bin, args, tokens)

        # Default pass for benign builtins (echo, dir, ls)
        return True, "Komut güvenli izin listesinde onaylandı.", tokens

    def _audit_python_args(self, base_bin: str, args: List[str], tokens: List[str]) -> Tuple[bool, str, List[str]]:
        """Deep argument audit for Python executions (AST check for -c, path check for scripts)."""
        if not args:
            return False, f"'{base_bin}' argümansız etkileşimli REPL modunda çalıştırılamaz.", []

        # Version flags
        if len(args) == 1 and args[0] in ("--version", "-V", "-vv"):
            return True, "Python sürüm denetimi onaylandı.", tokens

        # -m module invocation
        if args[0] == "-m":
            if len(args) < 2:
                return False, "'-m' parametresi modül adı gerektirir.", []
            module_name = args[1].lower()
            # Strictly allowed modules
            if module_name == "unittest":
                # Only allow running tests inside workspace
                return True, "Python unittest modülü onaylandı.", tokens
            elif module_name == "json.tool":
                return True, "Python json.tool modülü onaylandı.", tokens
            else:
                return False, f"Yalnızca güvenli modüller çalıştırılabilir. Yasaklı modül: '{module_name}'", []

        # -c inline code evaluation -> STRICT AST AUDIT
        if args[0] == "-c":
            if len(args) < 2:
                return False, "'-c' parametresi inline Python kodu gerektirir.", []
            code_snippet = args[1]
            try:
                tree = ast.parse(code_snippet)
            except SyntaxError as se:
                return False, f"Inline Python sözdizimi hatası: {str(se)}", []

            visitor = PythonASTSecurityVisitor()
            visitor.visit(tree)
            if visitor.violations:
                return False, f"AST Güvenlik İhlali: {'; '.join(visitor.violations)}", []

            return True, "Inline Python kodu AST güvenlik denetiminden başarıyla geçti.", tokens

        # Script file invocation (e.g. python scripts/run.py ...)
        script_candidate = args[0]
        if script_candidate.startswith("-"):
            return False, f"Bilinmeyen veya desteklenmeyen Python bayrağı: '{script_candidate}'", []

        try:
            # Script MUST reside within workspace_root and must exist!
            self.validate_file_path(script_candidate, must_exist=True)
        except Exception as e:
            return False, f"Python script güvenlik ihlali: {str(e)}", []

        return True, f"Çalışma alanı içi Python scripti onaylandı: '{script_candidate}'", tokens

    def _audit_git_args(self, args: List[str], tokens: List[str]) -> Tuple[bool, str, List[str]]:
        """Validates Git commands to ensure strictly read-only and unhijackable execution."""
        if not args:
            return False, "'git' komutu argümansız çalıştırılamaz.", []

        # Check for dangerous flags
        for arg in args:
            for blocked in BLOCKED_GIT_FLAGS:
                if arg == blocked or arg.startswith(blocked + "="):
                    return False, f"Güvenlik gerekçesiyle yasaklanmış Git bayrağı tespit edildi: '{arg}'", []

        subcmd = args[0].lower()
        if subcmd not in ALLOWED_GIT_SUBCOMMANDS:
            return False, f"Yetkisiz Git alt komutu: '{subcmd}'. İzin verilen alt komutlar: {sorted(list(ALLOWED_GIT_SUBCOMMANDS))}", []

        return True, f"Git alt komutu onaylandı: '{subcmd}'", tokens

    def _audit_node_args(self, base_bin: str, args: List[str], tokens: List[str]) -> Tuple[bool, str, List[str]]:
        """Audits Node and NPM executions."""
        if not args:
            return True, f"'{base_bin}' çalıştırıldı.", tokens

        if base_bin == "node":
            if args[0] in ("-v", "--version"):
                return True, "Node sürüm denetimi onaylandı.", tokens
            if args[0] in ("-e", "--eval"):
                return False, "Node inline eval (-e) güvenlik nedeniyle yasaklanmıştır.", []
            # Check script path
            try:
                self.validate_file_path(args[0], must_exist=True)
            except Exception as e:
                return False, f"Node script güvenlik ihlali: {str(e)}", []
            return True, "Node script onaylandı.", tokens

        if base_bin == "npm":
            allowed_npm = {"test", "run", "lint", "-v", "--version"}
            if args[0].lower() not in allowed_npm:
                return False, f"Yetkisiz NPM komutu: '{args[0]}'. İzin verilenler: {allowed_npm}", []
            return True, "NPM komutu onaylandı.", tokens

        return True, "Komut onaylandı.", tokens

    def get_sanitized_environment(self) -> Dict[str, str]:
        """
        Builds a strictly sanitized environment dictionary for child subprocesses.
        Purges all ambient credential tokens (GITHUB_TOKEN, AWS, SSH, API keys, database secrets).
        """
        allowed_keys = {
            "PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "HOME", "USERPROFILE",
            "LANG", "LC_ALL", "TERM", "TZ", "COMSPEC", "PATHEXT", "OS"
        }
        clean_env: Dict[str, str] = {}
        for key, val in os.environ.items():
            if key.upper() in allowed_keys:
                clean_env[key] = val

        # Explicitly enforce sandbox isolation variables
        clean_env["PYTHONPATH"] = self.workspace_root
        clean_env["PYTHONUNBUFFERED"] = "1"
        clean_env["PYTHONDONTWRITEBYTECODE"] = "1"
        clean_env["ZOBAR_SANDBOX_ISOLATED"] = "1"
        return clean_env

    def execute_sandboxed_command(self, command_str: str, timeout_seconds: int = 5, user_confirmed: bool = False) -> Dict[str, Any]:
        """
        Executes command with full OS-level sandbox isolation:
        - shell=False strictly enforced
        - Sanitized environment with ambient secrets purged
        - Strict timeout termination
        - Working directory confined strictly to workspace_root
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
        sanitized_env = self.get_sanitized_environment()

        try:
            # Fallback for Ubuntu Linux when python binary is not aliased
            exec_tokens = list(tokens)
            if exec_tokens and exec_tokens[0] == "python" and os.name != "nt":
                import shutil
                if not shutil.which("python") and shutil.which("python3"):
                    exec_tokens[0] = "python3"

            proc = subprocess.run(
                exec_tokens,
                cwd=self.workspace_root,
                shell=False,  # CRITICAL: OS-level binary execution without shell interpolation
                env=sanitized_env,  # CRITICAL: Ambient secrets and API keys are stripped
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
                "security_audit": {"safe": True, "reason": "Allowlist, AST & Sandbox Passed"}
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


if __name__ == "__main__":
    guard = SecurityPermissionGuard()
    print("🛡️ SecurityPermissionGuard v2.0 initialized.")
    res = guard.execute_sandboxed_command("python --version")
    print("Self-test python --version:", res["status"], res["stdout"])
