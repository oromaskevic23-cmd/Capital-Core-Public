# Capital Core — Global City NCA Enterprise Architecture

**Status:** IMPLEMENTED AS A LOCAL REFERENCE CONTROL PLANE; all real-city deployments, brokerage authority, LLM workers, CRM integration, payment-provider integration and revenue collection are **NOT VERIFIED / NOT DEPLOYED** by this repository.

**Architecture authority:** Alexander Nikolaevich Romaskevich (RomaskevicH), Founder • Owner • CEO • Chief Systems Architect of IMPERIAL Core, final architectural decision authority.

**Date:** 2026-11-03 · **Language:** English (GitHub documentation standard).

## 1. Mission and non-negotiable boundaries

Design a multi-tenant, federated Capital Core network where each major metropolitan market can host **one or more Universal NCA real-estate specialists**, supervised professional teams and licensed local partners. Cities are **independent jurisdictional operating cells**. This is a scalable blueprint, not a claim of active agents in any city.

Universal NCA means an agent capable of switching among **approved Enterprise Skills** (research, listing quality review, lead triage, drafting, appointment preparation, market analysis). It **does not** mean unrestricted authority to broker property, negotiate legally binding agreements, act as a lawyer, receive customer escrow money, or perform licensed activity without an authorized licensed human/entity.

A city can have one anchor NCA and dynamically additional specialized NCA workers; capacity increases with verified workload and supervised quality, never merely with city population. No claim of 24/7 operation until server runtime and external evidence demonstrate it.

### Canonical authority chain

```text
Architect — Alexander Nikolaevich Romaskevich (final architectural authority)
  └── HANTER — AI Command Center (mission intake, priorities, evidence)
        └── Federated Capital Core domain / regional orchestrators
              ├── Frankfurt City Cell -> Universal NCA -> specialized NCA team
              ├── Dubai City Cell     -> Universal NCA -> specialized NCA team
              ├── London City Cell    -> Universal NCA -> specialized NCA team
              ├── New York City Cell  -> Universal NCA -> specialized NCA team
              └── N other independently governed city cells
                    -> Human licensed partner / broker where required
                    -> CRM-SOFFT (independent revenue and task workspaces)
                    -> Independent QA -> Approval Gateway -> Audit Ledger
```

**HANTER is not an all-powerful global worker orchestrator.** Each regional/domain orchestrator has bounded authority and a partitioned execution domain. Guardian Core, AI Passport, Enterprise Skills, Zero Trust, Public / Private Boundary, Approval Gateway, Owner Kill Switch, Audit Ledger and independent QA apply at city, agent, task, deal and finance layers.

ORION offers research inputs, VELION offers proposed model inference (MAX is a mode, not an alternate model name), CONSTRUCTOR AI builds verified tooling, and CYBER HAK supplies defensive assurance. None of these relationships imply production deployment. The CRYPTO IMPERIAL Ecosystem Boundary is separate; **IMPERIUM** is a long-term architectural digital currency envisioned for AI agents worldwide, not a current globally adopted or exchange-listed currency. **Capital Core must not route property-sale proceeds into crypto or tokens by default.**

## 2. Enterprise city cell data contracts

| Entity | Required fields | Governance |
|---|---|---|
| `CityCell` | stable city_id, city name, ISO country, jurisdiction profile, time zone, status | Human owner approves market before any real work |
| `CityLegalPolicy` | legal_review_ref, licensed_scope, broker identity, expiry/review date, advertising and data rules | Local counsel / qualified licensing reviewer required for controlled services |
| `CityPrivacyPolicy` | data residency, consent basis, retention, data subject controls, privacy_review_ref | Separate PII vault; no raw customer data in public Audit Ledger |
| `NcaPassport` | agent_id, city scope, skill allowlist, examiner evidence, permit expiry, supervisor | Identity is not authorization; short-lived, revocable permits |
| `AgentMission` | mission_id, source_ref, consent_ref, listing_rights_ref where needed, city, skill, idempotency key | Per-mission permission; no unsolicited outreach without an independently verified legal basis |
| `Contract` | party identifiers, scope, currency, agreed service fee terms, legal clearance, human approval | Contract approved before invoice and financial allocations |
| `RevenueEvidence` | external processor/bank receipt, verification ref, approved cost/tax/refund adjustments | External independent confirmation required; agents cannot self-attest cash |
| `AuditEvent` | event_id, actor, action, object_id, policy_version, evidence references, correlation id, integrity proof | Append-only durable chain in production; retention per jurisdiction |

Recommended durable implementation: PostgreSQL with separate organizations, city units, agents, tasks, contracts, invoices, receipts, payouts and audit events; row-level security enforced by real tenant/city membership, unique external receipt IDs, transactional outbox, retry queue and operator incident procedures. Supabase may be evaluated as a backend, but **this repository has not deployed or configured those tables**.

### City admission state machine

```text
CANDIDATE
   -> LEGAL_AND_PRIVACY_REVIEW
   -> LICENSED_PARTNER_VERIFIED
   -> OWNER_APPROVED
   -> PILOT_READY
   -> INDEPENDENT_QA_ACCEPTED
   -> PRODUCTION_ENABLED  (requires separate deployment evidence)
   -> SUSPENDED / REVOKED (Owner Kill Switch)
```

The provided Python reference engine implements only CANDIDATE -> PILOT_READY and revocation. Reference status **CERTIFIED_REFERENCE** is not a professional qualification or government-issued licence.

## 3. City NCA operating teams

One anchor Universal NCA per city is the preferred presentation identity. Assign zero or more bounded specialist agents when needed:

| Function | Agent work allowed in approved sandbox | Required human boundary |
|---|---|---|
| Property Intelligence | Market comparisons, property research, source citations | Licensed specialist checks pricing/claims |
| Lead Operations | Consent-aware intake, deduplication, classification, preparation | Human decides lead acceptance and outreach legality |
| Listing Quality | Draft descriptions, image/metadata QA, rights checking | Owner/broker authorizes publication |
| Buyer/Tenant Experience | Scheduling proposals, informative FAQs, document preparation | Human specialist handles regulated advice and negotiations |
| Commercial Real Estate | Office/retail/industrial analysis, tenant market research | Licensed local agent and counsel where required |
| Risk & Cyber | PII classification, fraud flags, CYBER HAK rules | Security owner reviews incidents |
| Finance Attribution | Invoice assistance, evidence reconciliation, integer-precision allocations | Finance owner authorizes payments; no NCA escrow control |

Agent avatars represent **digital agents**, not licensed human brokers. Display AI disclosure and make transfer to an accountable human possible. Identity-locked imagery may vary clothes/background/market, but do not alter an approved agent face or the canonical corporate symbol; changes require Architect approval.

## 4. Workflow contract — demand to income

1. **Demand discovery** — legitimate permissioned sources, verified property rights, provenance evidence. No scraping that violates terms or privacy rules.
2. **Lead qualification** — CRM-SOFFT `DEMAND_FOUND -> QUALIFIED`; dedupe, consent, locale, service classification.
3. **Federated routing** — HANTER selects a city cell; city orchestrator assigns an NCA with valid AI Passport, skills, supervised scope and issued permit.
4. **Professional work** — NCA produces research, drafts or bounded service artifacts with input/output evidence; external marketing requires approval.
5. **Independent QA** — separate reviewer checks accuracy, rights, performance and customer deliverable.
6. **Local commercial approval** — authorized broker/legal professional completes regulated stages. Contract scope and agreed fee captured.
7. **Invoice and confirmation** — external billing records are reconciled; signed test attestations are **not** proof a bank paid.
8. **Allocation and payout gate** — deterministically calculate internal shares only from approved and independently verified receipts; human finance approval; no auto-transfer by NCA.
9. **Audit and learning** — event trace, dispute/chargeback handling, agent performance measured from independently accepted work.

**Suggested CRM-SOFFT statuses:** DEMAND_FOUND -> QUALIFIED -> ROUTED -> WORK_IN_PROGRESS -> QA_ACCEPTED -> CONTRACT_APPROVED -> INVOICED -> PAYMENT_CONFIRMED -> ALLOCATION_APPROVED -> REPEAT. These are integration contracts, **not present live schema migrations**. `PAYMENT_CONFIRMED` must only be set after independent real provider evidence, never merely by a proposed receipt or model output.

## 5. Security and reliability gates

- AI Passport + Enterprise Skills: agent_id is scoped to city/organization, skill and execution time. Rotate/revoke; reject unauthorized destinations. No master NCA credentials.
- Guardian Core: deny-by-default outbound tools, PII actions, real-estate-advertising actions, and financial actions; explicit exceptions are human-authorized.
- Approval Gateway: separate Approve/Reject for published listing, binding commercial step, invoice and any payout. Four-eyes for sensitive operations; no AI self-approval.
- Audit Ledger: persist signed/immutable event history and retention policy. The local SHA-256 audit chain in this repo is **tamper-evident only within the currently held in-memory object**, not a production ledger.
- Owner Kill Switch: stop new dispatch, active worker lease renewal and finance authorization at orchestration and runtime levels; include independent emergency channel and post-stop audit.
- Idempotency: unique mission IDs, invoice IDs, processor transaction IDs; exactly-once **effects** using transactional persistence plus dedupe; queues may deliver at least once.
- Monetary precision: integer minor currency units; explicit validated contract basis points (10,000 = 100%); deterministic remainder, no floating point, no invented default commission rates.
- Operations: separate development/staging/production, sandbox evaluation, canary/rollback, cryptographic release provenance, audit retention, backup/restore drills, DLQ, SLOs and independent QA.
- Privacy: consent records, minimization, subject requests, encryption, data-region controls; no passwords, private buyer/seller records or private deal data in this public repository.

## 6. Initial city *candidates* (not operating claims)

| Candidate | Intended specialization | Admission evidence status |
|---|---|---|
| Frankfurt, DE | Commercial and corporate properties | NOT SUBMITTED / CANDIDATE |
| Dubai, AE | Luxury and international properties | NOT SUBMITTED / CANDIDATE |
| London, GB | Residential and leasing support | NOT SUBMITTED / CANDIDATE |
| New York, US | Urban residential, condos and commercial research | NOT SUBMITTED / CANDIDATE |
| Miami, US | Luxury villas, vacation and waterfront market research | NOT SUBMITTED / CANDIDATE |

Each US state and country requires **its own policy review**, even when another city's technical model is identical. Scaling to 100, 1,000 or more cities is an architecture objective, not a measured production achievement.

## 7. Independent release gates

| Gate | Required independently verifiable evidence |
|---|---|
| E0 — SPECIFIED | City policy model, threat model, data classification, source/provenance |
| E1 — REFERENCE TESTED | Reproducible unit tests on exact immutable commit |
| E2 — INTEGRATED | Real identity/Approval Gateway, CRM-SOFFT integration, scoped database RLS, signed evidence |
| E3 — SANDBOX E2E | Worker dispatch, actual LLM call, adverse tests, rollback and stop, independent QA |
| E4 — AUTHORIZED CITY PILOT | Local human/partner verification, jurisdiction approval, real customer consent and accepted service |
| E5 — REVENUE VERIFIED | External bank/payment proof, approved invoice, cost/tax accounting and reconciliation |
| E6 — EXPANSION PROVEN | Multi-region tenant isolation, load/security DR tests, support, regulatory monitoring, renewal revenue |

No "Enterprise-ready", "licensed broker", "active city office" or revenue claim is valid before its respective evidence gate.

**Related:** [Revenue Engine](CAPITAL_CORE_REVENUE_ENGINE.md) · [reference module](../capital_core/reference.py) · [tests](../tests/test_capital_core_reference.py).
