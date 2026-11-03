# Capital Core — Enterprise Earnings Model & Revenue Evidence Contract

**Date:** 2026-11-03 · **Status:** DESIGNED + TESTABLE PURE-PYTHON REFERENCE. No live customer, invoice, bank transfer, commission or profit verified.

**Architect / Founder:** Alexander Nikolaevich Romaskevich (RomaskevicH).

## 1. How each city can earn money

Revenue must come from **real contracted services** and **actually collected payment**, not from simulated leads, invented commissions, unverified token values or self-approved accounting.

| Model | Customer | Billable deliverable | NCA role | Legal and human gate |
|---|---|---|---|---|
| A. B2B SaaS subscription | Local licensed agency / property firm | CRM seats, AI-assisted listing QA, analytics, workflow automation | Support, onboarding and analysis | Software agreement, invoicing, privacy and any relevant local rules |
| B. Marketing/creative services | Licensed property company or owner with rights | Actually delivered listing packages, copy, media, campaign analytics | Drafts, quality checks, reporting | Rights proof; local advertising review; do not disguise an unlawful referral fee |
| C. Broker-supervised support | Licensed local property partner | Contracted research, admin and transaction support | Document preparation, comparisons, schedules | Qualified local broker signs off regulated work; compensation structure pre-approved by counsel |
| D. Enterprise research | Owner, developer, investor, institution | Lawfully sourced market reports and insights | Research and independent-data cross checks | Data licences, confidentiality, legal/privacy and commercial review |

**NCA is not an independent licensed broker or bank beneficiary by virtue of its AI Passport.** Internal agent allocation is a management/quality attribution reserve, not an NCA personal salary or a promise of automatic legal compensation.

**Forbidden without specific validated authorization:** paying for prohibited settlement-service referrals, unlicensed broker commissions, escrow custody, automatic legal advice, buyer/seller money handling, and promotional claims of guaranteed ROI.

## 2. Contracted allocation model — no invented default commission

There is **no universal percentage**. Every deal must specify signed terms with named contracting parties and legal clearance. A reference contract supplies:

- `contract_id`, `city_id`, `currency`, `service_kind`;
- `agreement_ref`, `legal_clearance_ref`, `owner_approval_ref`, `local_partner_ref`;
- `platform_bps`, `local_partner_bps`, `nca_internal_reserve_bps` totaling 10,000 basis points.

The share of the licensed local partner is **only an approved contractual allocation**, not evidence any specific jurisdiction allows an agent commission. An enterprise subscription may use a different partner and reserve arrangement from a broker-supported service. Cash disbursement requires a separate lawful payout workflow absent from this repository.

### Deterministic allocation math

Use whole-number **minor currency units**, never floats.

```text
GROSS_COLLECTED = externally verified receipt amount (minor units)
DISTRIBUTABLE = GROSS_COLLECTED
              - assessed tax hold
              - approved refunds
              - approved direct service costs

LOCAL_PARTNER = floor(DISTRIBUTABLE × contract.local_partner_bps / 10000)
NCA_INTERNAL_RESERVE = floor(DISTRIBUTABLE × contract.nca_internal_reserve_bps / 10000)
PLATFORM_ALLOCATION = DISTRIBUTABLE - LOCAL_PARTNER - NCA_INTERNAL_RESERVE

Invariant:
PLATFORM + LOCAL_PARTNER + NCA_INTERNAL_RESERVE = DISTRIBUTABLE
```

**Illustrative unit-test scenario only — NOT a recommended global tariff, not forecast revenue:** EUR 125.00 receipt, EUR 4.00 tax hold, EUR 1.00 refund, EUR 15.00 direct cost → EUR 105.00 distributable. Hypothetical, expressly signed contract terms of 20% platform / 70% local partner / 10% internal NCA reserve yield EUR 21.00 / EUR 73.50 / EUR 10.50. This is only arithmetic; tax amounts and shares must come from actual evidence and contracts.

**Profit is separate** from revenue allocation: compute actual corporate net profit from booked transactions after all operating expenses, applicable taxes and accounting adjustments, using an accountant-approved ledger. `nca_internal_reserve` is NOT spendable agent cash, and its naming must not obscure employment, consumer or financial law.

## 3. Trust chain for finance

```text
Delivered service + independent QA evidence
  -> signed client contract & legal clearance
  -> valid invoice from authorized party
  -> bank/payment processor proof (independent reconciler)
  -> owner Finance Approval Gateway
  -> deduplicated receipt in durable ledger
  -> deterministic internal allocation proposal
  -> legally authorized human payout
  -> chargeback / dispute reconciliation
```

The reference `FinanceLedger` accepts a test HMAC-SHA256 adapter attestation; it checks integrity and stores an internal allocation with status **REFERENCE_ATTESTED_NOT_SETTLED** and `cash_disbursed_minor: 0`. The signature proves only that a holder of that test adapter key signed a payload. **It cannot prove that any external bank received or cleared money.** Production must receive attested evidence from a trusted external provider with an independently implemented validator, appropriate signing/key isolation, durable uniqueness constraints and settlement reconciliation.

An agent must never hold the verification key; the real provider adapter and its approval chain run in a private trust domain. Test fixtures contain fake evidence references. This repo stores **no real payment credentials or live customer information**.

## 4. Jurisdiction boundaries (official source anchors; further counsel review required)

- **Germany:** §34c Gewerbeordnung includes real-estate mediation among regulated trades: https://www.gesetze-im-internet.de/gewo/__34c.html
- **Dubai:** Dubai Land Department's official FAQs address required broker registration and practice cards: https://dubailand.gov.ae/en/frequently-asked-questions
- **United Kingdom:** government guidance describes approved property-agent redress scheme obligations: https://www.gov.uk/redress-scheme-estate-agencies
- **United States:** CFPB explains RESPA Section 8 limits on mortgage-settlement referrals and unearned fees, with exceptions determined by applicable law: https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/real-estate-settlement-procedures-act/real-estate-settlement-procedures-act-faqs/

This section provides **architecture risk flags, not legal advice or clearance**. Rules vary by property type, country, state, municipality, consumer type and payment model. Local regulatory reviews must be refreshed before enabling each city.

## 5. Required CRM-SOFFT finance workspace integrations

| Event | Preconditions | Evidence |
|---|---|---|
| `SERVICE_DELIVERED` | Skill scope, rights/consent, independent QA | Work product and reviewer |
| `CONTRACT_APPROVED` | Authorized entity, pricing terms, legality review | Signed contract |
| `INVOICE_ISSUED` | Scope and payee verified | Invoice ID, amount, currency |
| `BANK_RECEIPT_VERIFIED` | Independent provider validation | Unique external transaction ref |
| `PAYMENT_CONFIRMED` | Finance owner accepts external proof | Approved immutable evidence |
| `ALLOCATION_PROPOSED` | No duplicates or negative/overallocated money | Integer share breakdown |
| `PAYOUT_APPROVED` | Beneficiary/AML/KYC and jurisdictional checks | Human finance authorization |
| `PAYOUT_SETTLED` | Actual external transfer confirmed | Transfer statement/ref |

These are **integration target contracts**, not statements that CRM-SOFFT or a payment provider is currently connected here.

## 6. Controls and SLO proposals

- Prevent false `PAYMENT_CONFIRMED` claims with external-provider-only transitions.
- Reject replays by `(provider_id, external_transaction_id)` unique keys, transactional database constraints and idempotency tokens; the current in-memory demo only guards `payment_id` within one process.
- Require signed approval and reviewer independence for service settlement; use audit log, data retention and complaint workflow.
- Detect refunds, duplicates, currency mismatch, commission cap violations and retroactive contract changes.
- Per-city KPIs: approved active partner count, independently accepted deliverables, legitimate qualified leads, realized collected revenue, refund rate, customer satisfaction, QA rejection rate, gross margin and payment reconciliation gap. Never convert forecasts to realized amounts.
- Stop/revoke authority through Owner Kill Switch independent of vendor models and financial adapters; zero funds automatically paid in this prototype.

## 7. Next real-world proof

**One city, one authorized contract, one supervised NCA mission, one independently accepted deliverable, and one externally reconciled paid invoice.** Complete and audit that loop before expanding to other cities or presenting commercial returns as achieved.

Source and tests: [reference engine](../capital_core/reference.py) · [regression tests](../tests/test_capital_core_reference.py).
