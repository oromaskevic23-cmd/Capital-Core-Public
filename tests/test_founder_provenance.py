"""Regression tests for project provenance safeguards; no external dependencies."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from tools.verify_founder_provenance import (
    FOUNDER, ProvenanceViolation, verify_repository,
)


def fixture(root: Path) -> None:
    files = {
        "AUTHORS.md": "Founder Alexander Romaskevich / RomaskevicH; third-party contributions preserved.",
        "LICENSE": "Copyright (c) 2026 Alexander Nikolaevich Romaskevich; third-party rights preserved.",
        "PROVENANCE.md": "Original Git history, original contributors, AI-assisted drafting disclosed.",
        "docs/DIGITAL_STATE_ARCHITECTURE.md": (
            "Digital State Architecture - not a sovereign state. "
            + FOUNDER + " founded the Federated Multi-Orchestrator "
            + "platform. CRYPTO IMPERIAL Ecosystem Boundary."
        ),
        "governance/FOUNDER_CODE_AUTHORSHIP_STANDARD.md": (
            FOUNDER + " keeps actual Git history and third-party rights."
        ),
    }
    for relative, content in files.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


class FounderProvenanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        fixture(self.root)

    def test_valid_founder_provenance_is_not_ip_registration(self):
        result = verify_repository(self.root)
        self.assertEqual(len(result["checked_paths"]), 5)
        self.assertFalse(result["proof_of_legal_ownership"])
        self.assertFalse(result["external_attestation"])
        self.assertEqual(result["project_founder"], FOUNDER)
        self.assertTrue(result["third_party_rights_unaltered_by_this_check"])

    def test_missing_license_denied(self):
        (self.root / "LICENSE").unlink()
        with self.assertRaises(ProvenanceViolation):
            verify_repository(self.root)

    def test_removed_founder_or_third_party_notice_denied(self):
        (self.root / "AUTHORS.md").write_text("Anonymous only", encoding="utf-8")
        with self.assertRaises(ProvenanceViolation):
            verify_repository(self.root)

    def test_stripped_architecture_or_false_sovereignty_claim_denied(self):
        p = self.root / "docs/DIGITAL_STATE_ARCHITECTURE.md"
        p.write_text("A real sovereign state.", encoding="utf-8")
        with self.assertRaises(ProvenanceViolation):
            verify_repository(self.root)

    def test_missing_private_provenance_history_denied(self):
        (self.root / "PROVENANCE.md").unlink()
        with self.assertRaises(ProvenanceViolation):
            verify_repository(self.root)

    def test_new_original_code_requires_founder_project_credit_not_all_lines(self):
        path = self.root / "imperial_core/new_module.py"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("print('hello')", encoding="utf-8")
        with self.assertRaises(ProvenanceViolation):
            verify_repository(self.root, ["imperial_core/new_module.py"])
        path.write_text("# Founding Architect: " + FOUNDER + "\n"
                        "# Original implementation contributors: see Git commits\n", encoding="utf-8")
        self.assertEqual(len(verify_repository(
            self.root, ["imperial_core/new_module.py"])["checked_paths"]), 6)

    def test_out_of_scope_third_party_code_not_relicensed(self):
        p = self.root / "third_party/upstream.py"
        p.parent.mkdir(parents=True)
        p.write_text("# Copyright Third Party\n", encoding="utf-8")
        self.assertEqual(len(verify_repository(
            self.root, ["third_party/upstream.py"])["checked_paths"]), 5)

    def test_no_arbitrary_absolute_paths(self):
        with self.assertRaises(ProvenanceViolation):
            verify_repository(self.root, ["imperial_core/../../etc/passwd"])


if __name__ == "__main__":
    unittest.main()
