# Capital Core — Universal NCA Agent Earnings & City P&L Contract

**Status:** SPECIFIED + PYTHON REFERENCE ATTRIBUTION. No AI agent or human has been paid from these reference calculations.

**Architectural authority:** Alexander Nikolaevich Romaskevich (RomaskevicH), Founder • Owner • CEO • Chief Systems Architect.

## Principle

A Universal NCA works for a permitted **City Cell**, executes **approved Enterprise Skills** under a federated Capital Core orchestrator, and receives **internal performance credits for independently accepted work**. A digitally represented NCA does not automatically become a legal person, licensed realtor, employee, payment account holder or commission beneficiary. All real compensation to human/service providers must follow lawful agreements and human financial approval.

An illustrative digital-agent identity (such as Sophia Bennett — Frankfurt Commercial Properties) is a consistent presentation identity, **not evidence of licensed brokerage or an active branch**.

## Two distinct ledgers

1. **Finance / city P&L ledger**: contracted and externally confirmed revenue, customer invoice, currency, taxes/refunds, costs, gross margin, receivables, local partner settlement, disputes, cash balances and legal payees.
2. **NCA contribution ledger**: independently accepted missions, evidence, reviewer identity, role scope, quality weighting, city, and **non-cash internal allocation** from a pre-approved `nca_internal_reserve_minor` pool. The NCA ledger never disburses actual money.

No real payment may be reclassified as confirmed merely because an NCA wrote `PAID` or produced an HMAC test signature. Real bank/processor reconciliation must be separately connected and verified. Any successful cloud compilation or unit test is not earnings proof.

## Reference attribution policy

```text
City + AI Passport + Certified Enterprise Skill
  -> source provenance and consent
  -> lawful supervised service deliverable
  -> independent QA (reviewer != agent)
  -> explicit human acceptance
  -> distinct, ledger-attested receipt (internal test scope)
  -> owner approval
  -> allocation from contracted NCA internal reserve
  -> zero automatic payout
```

`AcceptedContribution` fields: agent_id, mission_id, city_id, weight_units (1–100), qa_ref, qa_reviewer_id, acceptance_ref. These are pointers to independently retained evidence, not a real skills-exam or invoice.

`AttributionLedger.allocate` validates that each mission has a matching, accepted QA record, city/agent match, no duplicate contribution, allowed weight, finance receipt exists in the reference ledger, and no owner/finance emergency stop is active. Repeated allocation for the same receipt fails closed. A mission cannot be rewarded twice within the same in-memory ledger.

**Allocation formula:**

```text
agent_weight = sum(independently accepted mission weight_units)
reserve = receipt.nca_internal_reserve_minor
agent_credit = floor(reserve * agent_weight / sum(all_agent_weights))
rounding_remainder -> largest fractional remainders; tie break by agent_id
sum(agent_credit) == reserve
cash_disbursed == 0
```

Weights are not hard-coded pay rates. Quality and weighting policy should be contractually approved and non-discriminatory; no agent should set its own quality score. The example code does **not** enforce actual contract fairness or legal employment rules: these are separate human/legal gates.

## City revenue organization (commercial target)

| Layer | Responsibilities | Financial reporting |
|---|---|---|
| Global IMPERIAL Core | Platform, security, tooling, audit standard, founder governance | Corporate revenue/cost centre |
| Capital Core regional orchestrators | Route market tasks, enforce country boundary and escalation | Regional aggregation, no unrestricted money authority |
| City Cell | Lead intake, partner onboarding, listing quality, local language, QA | Separate city_id and currency P&L |
| Licensed local partner / qualified human | Regulated negotiation, contracts, client representation where permitted | Contractually due lawful revenue and payments |
| Universal NCA + specialists | Evidence-backed permitted digital work, source-based research, supervised client support | **Non-cash, internally attributed contribution reserve** |

Major-city expansion requires market viability, provider terms, housing-advertising rights, a real licensed partner as needed, and privacy/counsel review. No metropolitan market is active by default.

## Measurement

Measure **quality before volume**: independently QA-accepted deliverables, verified lead source rights, privacy incidents, denied actions, average time to accepted work, legitimate conversion, external invoice collection, refunds, legal disputes, support costs, and retained customers. Do not award credits for fake leads, bulk unconsented messages, self-reviewed work or superficial task count. The city P&L must make costs and chargebacks visible.

## Production blockers

- Current reference ledgers are in-memory and can be replaced/mutated by the test process. A production system needs private durable, transactionally unique storage with access control, immutable audit exports, signer isolation, independent external payment verification, revocation and replay defence across process restarts.
- Contract and reviewer refs are **not independently verified** by the Python demo. Production must bind them to licensed, authenticated human actors and real documents.
- No external CRM-SOFFT, Supabase, agent runtime, payout processor, employee payroll, licensing verifier or partner portal is connected here.
- A real chargeback/credit note reverses or adjusts allocations with explicit accounting records; the reference engine does not implement this yet.
- Any payouts, commission splitting and lead referral terms require case-by-case legal/tax/compliance approval for each country/state. Do not generalize a global split percentage.

**Next objective:** one city pilot, one scoped digital agent, a verified local partner, an approved service, independent QA, actual signed customer contract, real invoice and separately proven external collection. Scale only after this evidence.

[City architecture](CAPITAL_CORE_GLOBAL_CITY_ENTERPRISE.md) · [Revenue design](CAPITAL_CORE_REVENUE_ENGINE.md) · [Attribution code](../capital_core/attribution.py) · [Attribution tests](../tests/test_capital_core_attribution.py).
