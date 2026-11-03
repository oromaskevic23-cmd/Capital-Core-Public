# Public architecture

**Status: SPECIFIED.** This page describes architectural intent. See [public evidence](docs/EVIDENCE.md) for implemented and tested scopes.

## Authority and federation

Alexander Romaskevich — RomaskevicH — is Founder • Owner • CEO of IMPERIAL Core, and Architect / Final Architectural Decision Authority. HANTER is the AI Command Center / Chief Systems component under that architectural authority.

IMPERIAL Core uses a **Federated Multi-Orchestrator Architecture**. Domain and functional orchestrators have separate responsibilities, permissions and runtime boundaries. Multiple organizational structures and professional teams can allocate a dynamic number of Nano Core Agents. There is no single unrestricted global orchestrator.

## Component responsibilities

| Component | Architectural responsibility |
|---|---|
| HANTER | Architect interface and governed mission coordination |
| VELION | Intelligence architecture and bounded model proposals |
| CONSTRUCTOR AI | Software construction and verification |
| LEGION / Nano Core Agents | Professional teams and bounded agent work |
| CYBER HAK | Defensive security and digital immune-system architecture |
| ORION | Collective reasoning research |
| CRYPTO IMPERIAL Ecosystem | Separate blockchain-development and economic boundary |
| Capital Core | Distinct capital-domain architectural responsibility |

## Governance requirements

AI Passport identifies the agent; Enterprise Skills define intended capabilities; Guardian Core evaluates policy; Approval Gateway mediates required authorizations; Audit Ledger records evidence. Identity is not authority, and capability is not approval. These component names are requirements, not a claim that every control is deployed.

Zero Trust, Deny by Default and Fail Closed apply across boundaries. Public documentation excludes private control internals, credentials, infrastructure addresses and proprietary skill bodies. The Public / Private Boundary and CRYPTO IMPERIAL Ecosystem Boundary remain explicit.

## Capital Core — federated city operating model (reference implemented)

Each major city is a separate legal/privacy jurisdiction and agent-execution boundary with an optional anchor Universal NCA plus dynamic specialist workers. City agent identity (AI Passport), capability (Enterprise Skills), independent QA, regional approval and lawful licensed human supervision are different gates. No agent may authorize itself or make automatic brokerage or finance decisions.

- [City NCA Enterprise blueprint](docs/CAPITAL_CORE_GLOBAL_CITY_ENTERPRISE.md)
- [Revenue engine & verification contract](docs/CAPITAL_CORE_REVENUE_ENGINE.md)
- [Per-agent earnings attribution](docs/CAPITAL_CORE_AGENT_EARNINGS.md)
- [Stdlib Python control-plane reference](capital_core/reference.py) and [non-cash attribution](capital_core/attribution.py)

Implemented here: **local in-memory reference** for city registration, agent certification, bounded mission dispatch, explicit reviewer identity, owner stop, hash-linked demonstration events, signed adapter test receipts and non-cash internal attribution. This does **not** verify legality, qualified partners, live LLM workers, durable audit, CRM-SOFFT database, real bank transfers or running city operations. Production controls require independently verified integrations and privileges.

## Observed reference technologies

Node.js 22 / JavaScript, the Node built-in test runner and GitHub Actions are evidenced in public reference projects. CONSTRUCTOR AI's reference UI uses HTML/CSS and browser localStorage. Python standard-library tooling validates public documentation. Runtime capabilities remain scoped to the linked revisions.

## Continuity

[Earlier architecture notes](https://github.com/oromaskevic23-cmd/IMPERIAL-Core-Public/blob/6f52f3b0371b618529fe5bc3c857700ffc6802d1/README.md) remain in Git history. The [current founder identity](docs/FOUNDER_IDENTITY.md) governs current role wording. Repository names and existing ownership/license terms are preserved.
