# IMPERIAL Core — Founder Code Authorship & Provenance Standard

**Version:** 1.0.0 · **Date:** 2026-11-02 · **Project founding architect:** Alexander Nikolaevich Romaskevich (RomaskevicH).

This standard is an engineering evidence and rights-hygiene procedure. It is not legal registration, a signed IP assignment, a trademark, or a claim that the founder personally wrote all code. It applies to original IMPERIAL Core contributions with established rights, and it must not conflict with existing LICENSE, NOTICE, author history or third-party terms.

## Attribution levels — do not collapse them

1. **Project creation and architecture:** Alexander Nikolaevich Romaskevich (RomaskevicH), Founder · Owner · CEO · Chief Systems Architect of IMPERIAL Core. This describes project leadership and architecture, not every source-line author.
2. **Individual file author / contributor:** the actual person(s) responsible for copyrightable portions, recorded using Git commits and accurate source notes. An AI tool's generated output should not be silently classified as a human-authored work; human-authorship and rights must be assessed for the relevant jurisdiction.
3. **Rights holder:** a person or legal entity **only where a valid legal basis supports the specific work**; employment, contributor licensing or assignment terms may affect ownership. Never claim rights to third-party dependencies, model weights, copyrighted artwork, fonts, datasets, or inherited components simply because they are present.
4. **License:** an already applicable LICENSE/NOTICE remains in effect. A project-wide notice cannot revoke earlier compatible grants or remove upstream conditions. Do not add a false `SPDX-License-Identifier` on code with unresolved licensing.

## Suggested heading for new original source

Insert this only in source genuinely created for the project, using the comment syntax of the programming language; retain any actual individual contributors and their original notices:

```text
Project: IMPERIAL Core
Founding Architect: Alexander Nikolaevich Romaskevich (RomaskevicH)
Original implementation contributors: see file history and AUTHORS.md
Copyright (c) 2026 Alexander Nikolaevich Romaskevich
  (only for copyrightable original material where his rights are established)
Licensing: consult repository LICENSE and applicable third-party notices
```

Do not auto-insert a claimed copyright holder in other people's files. For files with a confirmed SPDX license, use proper `SPDX-FileCopyrightText` / `SPDX-License-Identifier` conventions while preserving existing notices. A copyright statement is not in itself a license.

## Free actions that can be completed before hiring counsel

- Keep the actual Git author/committer and signed commits/tags when available; never rewrite published history to replace contributors. SHA-256 checksums and released commit SHAs are reproducible *technical evidence* of content, not conclusive proof of legal ownership or creation time.
- Keep `AUTHORS.md`, `PROVENANCE.md`, `LICENSE` and existing `NOTICE`; record source origin, contribution and upstream permissions. The new original architecture text is maintained in `docs/DIGITAL_STATE_ARCHITECTURE.md`.
- Use GitHub CODEOWNERS for project governance and protected files. Confirm separately that branch rules actually enforce approvals; a CODEOWNERS file by itself does not protect anything.
- Avoid publishing private business logic, API keys, secrets, customer datasets or credentials. Make Public/Private Boundary clear.
- For external contributions, obtain appropriate contribution licenses or assignments **before** representing the result as wholly owned. Preserve Git history even after an agreement.
- Keep a private, access-controlled rights register of contributor identity, material created, evidence and terms; do not post personal contact information or signed contracts in public GitHub.
- Use `tools/verify_founder_provenance.py` in CI to detect missing project notice, root license or governance anchor. No code check or copyright notice establishes a trademark, corporation, immunity or state sovereignty.

## Limits, escalation and roadmap

Copyright generally attaches automatically to qualifying original works under the Berne Convention, without legal fees or formal registration. Exact ownership, employment, AI-assisted creativity, enforcement, licensing and registration differ by jurisdiction. Copyright protects *expression*, not the abstract idea of IMPERIAL Core as a digital state. Future company formation, branding protection, contributor agreements, assignments, export controls and crypto-sector legal compliance should be reviewed when funding permits.

Project: IMPERIAL Core — Digital State Architecture is a **technical vision**, not a legally sovereign state. Do not call holders of AI Passport state citizens, or issue a legal identity credential as if it were a government passport.

**Immutable architectural boundaries:** federated Multi-Orchestrator Architecture (ASTRA as one orchestrator), HANTER, ORION advisory intelligence, VELION (MAX is a mode), NCA, AI Passport, Enterprise Skills, Guardian Core, Approval Gateway, ProofGraph, Audit Ledger, Zero Trust, Owner Kill Switch, Public/Private Boundary and CRYPTO IMPERIAL Ecosystem Boundary.

Reference standards: WIPO copyright and software guidance; SPDX license/copyright notice practice; GitHub repository licensing guidance. This document does not modify any repository's license or previously granted rights.
