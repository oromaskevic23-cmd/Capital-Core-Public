# Engineering roadmap

This is a plan with evidence gates, not a delivery guarantee.

| Priority | Next deliverable | Acceptance evidence |
|---|---|---|
| P0 | Founder profile activated | Public username repository, matching root README and observed rendered profile |
| P0 | Canonical public identity | Account fields and public introductions use the approved role and location |
| P0 | Publication-boundary remediation | Owner classification review of inconsistent public/private material; separate history review |
| P1 | Reference PR integration | Reviewed immutable heads, passing required checks and explicit merge records |
| P1 | Real model inference | Authorized free provider/model, real input/output and retained verification evidence |
| P1 | Verified application lifecycle | Isolated build, meaningful tests, failure handling and independent acceptance |
| P2 | Deployment and operations | Identified deployed version, live checks, rollback and bounded operational authority |
| P2 | Customer validation | Accepted pilot work and separately evidenced commercial outcomes |

## Capital Core — Enterprise City NCA rollout (2026-11-03)

| Priority | Evidence-gated deliverable | Release criterion |
|---|---|---|
| P0 | City registry + bounded NCA skills + duplicate-resistant local reference | [Reference tests](tests/test_capital_core_reference.py), green CI on exact commit |
| P0 | City-specific legal, privacy, licensed-partner and consent review | Review by competent human decision-makers; independently verifiable records |
| P0 | NCA earnings attribution separated from bank/payment ledger | [Agent earnings contract](docs/CAPITAL_CORE_AGENT_EARNINGS.md) and reference tests; no automatic payouts |
| P1 | One live city-cell worker with AI Passport, Guardian Core, Approval Gateway, Owner Kill Switch and independent QA | Signed identity, actual isolated LLM work, operator stop and rollback demonstrations |
| P1 | Private CRM-SOFFT integration for real property/customer tasks | Scoped tenant RLS, idempotent outbox, contract and source evidence |
| P1 | Local authorized real-estate partner and one signed, accepted service deliverable | City-specific legal proof, real consent, human acceptance |
| P1 | Independent payment processor reconciliation and city P&L | Actual financial evidence before `PAYMENT_CONFIRMED`, no agent-key access to cash |
| P2 | Scale to next cities after pilot succeeds | Separate city admission evidence, quality, privacy, load tests, recovery and measurable unit economics |

**This repository has no verified live city, broker, server worker, private CRM integration, bank settlement or commercial profit.** The new control-plane, revenue and attribution code is a testable **reference**, not a revenue-producing deployment.

FREE_ONLY remains in force. Architecture, tests, deployment and commercial outcomes have separate evidence requirements. The founder remains final architectural decision authority.
