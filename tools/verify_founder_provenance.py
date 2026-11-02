"""IMPERIAL Core original-source governance checker (offline, no dependencies).
Project Founding Architect: Alexander Nikolaevich Romaskevich (RomaskevicH).
Original implementation: IMPERIAL Core project contributors; preserve Git history.
Copyright (c) 2026 Alexander Nikolaevich Romaskevich only for original
copyrightable material where ownership is established.
Existing third-party copyrights and software licenses remain unaffected.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

FOUNDER = "Alexander Nikolaevich Romaskevich"
SIGNATURE = "RomaskevicH"
REQUIRED = {
    "AUTHORS.md": ("Alexander", "RomaskevicH", "third-party"),
    "LICENSE": ("Alexander Nikolaevich Romaskevich", "third-party"),
    "docs/DIGITAL_STATE_ARCHITECTURE.md": (
        "Digital State Architecture", FOUNDER, "not a sovereign state",
        "Federated Multi-Orchestrator", "CRYPTO IMPERIAL Ecosystem Boundary"),
    "governance/FOUNDER_CODE_AUTHORSHIP_STANDARD.md": (
        FOUNDER, "actual", "third-party", "Git history"),
}
ANCHORS = frozenset({"AUTHORS.md", "LICENSE", "PROVENANCE.md"})
MAX_DOC_BYTES = 512 * 1024
SCOPED_ORIGINAL_MODULES = ("imperial_core/",)
PROGRAM_EXTENSIONS = frozenset({".py", ".js", ".ts", ".tsx", ".go", ".rs", ".java"})
FORBIDDEN_GUARANTEES = (
    "all repository code is personally written by",
    "exclusive ownership of all third-party material",
)


class ProvenanceViolation(ValueError):
    pass


def _tracked(root: Path, relative: str) -> bytes:
    """Never follow symlinks outside the repository."""
    if not relative or "\\" in relative or relative.startswith("/") or ".." in Path(relative).parts:
        raise ProvenanceViolation("INVALID_RELATIVE_PATH")
    base = root.resolve(strict=True)
    target = root / relative
    if target.is_symlink() or not target.is_file():
        raise ProvenanceViolation("REQUIRED_FILE_MISSING_OR_LINK: " + relative)
    target_real = target.resolve(strict=True)
    if not target_real.is_relative_to(base) or target.stat().st_size > MAX_DOC_BYTES:
        raise ProvenanceViolation("UNSAFE_FILE: " + relative)
    return target.read_bytes()


def verify_repository(root: Path, added_code_paths: list[str] | None = None) -> dict:
    if root.is_symlink() or not root.is_dir():
        raise ProvenanceViolation("REPOSITORY_ROOT_INVALID")
    digests = {}
    for path, fragments in REQUIRED.items():
        raw = _tracked(root, path)
        try:
            content = raw.decode("utf-8")
        except UnicodeError as exc:
            raise ProvenanceViolation("NON_UTF8_GOVERNANCE_FILE: " + path) from exc
        for fragment in fragments:
            if fragment.casefold() not in content.casefold():
                raise ProvenanceViolation("MISSING_CANONICAL_EVIDENCE: " + path + ": " + fragment)
        if any(phrase in content.casefold() for phrase in FORBIDDEN_GUARANTEES):
            raise ProvenanceViolation("UNSUBSTANTIATED_AUTHORSHIP_CLAIM: " + path)
        digests[path] = hashlib.sha256(raw).hexdigest()
    # This project already has a source provenance record. Never silently lose it.
    for path in sorted(ANCHORS - REQUIRED.keys()):
        digests[path] = hashlib.sha256(_tracked(root, path)).hexdigest()
    for path in (added_code_paths or []):
        if (type(path) is not str or not path or path.startswith("/")
                or "\\" in path or ".." in Path(path).parts):
            raise ProvenanceViolation("INVALID_NEW_SOURCE_PATH")
        if not path.startswith(SCOPED_ORIGINAL_MODULES) or Path(path).suffix not in PROGRAM_EXTENSIONS:
            continue  # Third-party or unscoped files are not automatically relicensed.
        raw = _tracked(root, path)
        head = raw[:4096].decode("utf-8", errors="replace")
        if FOUNDER not in head or "contributor" not in head.casefold():
            raise ProvenanceViolation("NEW_ORIGINAL_SOURCE_NEEDS_PROVENANCE: " + path)
        if "SPDX-License-Identifier:" in head and "License" not in head:
            raise ProvenanceViolation("SPDX_LICENSE_NOT_VERIFIED: " + path)
        digests[path] = hashlib.sha256(raw).hexdigest()
    return {
        "schema": "imperial.core.provenance-check.v1",
        "project_founder": FOUNDER, "founder_signature": SIGNATURE,
        "checked_paths": sorted(digests), "sha256": dict(sorted(digests.items())),
        "third_party_rights_unaltered_by_this_check": True,
        "proof_of_legal_ownership": False,
        "external_attestation": False, "production_authorized": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify explicit project provenance anchors only")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--new-original-source", action="append", default=[])
    args = parser.parse_args(argv)
    try:
        report = verify_repository(args.root, args.new_original_source)
    except (ProvenanceViolation, OSError, ValueError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps(report, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
