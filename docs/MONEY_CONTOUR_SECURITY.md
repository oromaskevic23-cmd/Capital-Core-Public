# IMPERIAL Core — Money Contour: Financial Evidence Boundary v0.1

**Founder / Final Architectural Authority:** Alexander Nikolaevich Romaskevich (RomaskevicH).
**Date:** 2026-11-23.
**Status:** ARCHITECTURE + SYNTHETIC LOCAL REFERENCE. No production settlement, bank connection, token market activity, wallet operations, revenue or autonomous transfers are verified.

## Purpose

Protect the economic pathway from approved service delivery to truthful revenue reporting. An agent's claim of a sale is not a customer payment. An HMAC-attested synthetic event is not bank confirmation. A token balance multiplied by a target or hypothetical market price is not realized USD revenue, accessible cash or corporate valuation.

The new reference is in [money_boundary.py](../capital_core/money_boundary.py) and [its adversarial tests](../tests/test_capital_core_money_boundary.py). It is intentionally separate from the existing [revenue model](CAPITAL_CORE_REVENUE_ENGINE.md), [reference allocation engine](../capital_core/reference.py) and [agent attribution](../capital_core/attribution.py). **No real runtime integration is claimed.**

## Authority and domains

- **Architect:** final authority for financial changes, policy, custody and real transfers. Separate independent Owner Authority and protected execution sink are required in production.
- **HANTER — AI Command Center:** coordinates approved missions, receives status and risk reports, but never controls unrestricted treasury keys or executes direct bank and wallet actions. HANTER is not a single unrestricted global orchestrator.
- **Capital Core:** treasury policy, professional financial review, invoices, reconciliation, budget proposals, risk and accounting. Federated Multi-Orchestrator Architecture supports multiple organizations, teams and dynamic NCA populations.
- **CRYPTO IMPERIAL Ecosystem Boundary:** digital assets are separately governed, including AGY mission/evidence architecture and distinct token projects. **IMPERIUM is a long-term architectural digital currency envisioned for AI agents worldwide**, not a current worldwide accepted currency.
- **Nano Core Agents:** may perform Enterprise Skills such as invoice preparation, research, quality assessment and reconciliation *proposals*. An AI Passport proves identity, not spending authority. NCA may not hold live payment/withdrawal/trading/custody permissions.
- **Guardian Core / Approval Gateway / Audit Ledger:** independent policy evaluation, exact approval, evidence provenance and audit. Maintain Zero Trust, Deny by Default, Fail Closed and a strict Public/Private Boundary.

Capital Core can send HANTER **reports**, not unrestricted financial execution commands. Financial communication across Capital Core and CRYPTO IMPERIAL Ecosystem must use explicitly approved contracts, correlation IDs, trust validation and audit.

## Target finance state machine

~~~text
SERVICE_DELIVERED + INDEPENDENT_QA
    -> CONTRACT_APPROVED + LEGAL_CLEARANCE
    -> INVOICE_ISSUED (tenant / beneficiary / amount / currency)
    -> EXTERNAL_PROVIDER_EVIDENCE_OBSERVED
    -> INDEPENDENT_SETTLEMENT_RECONCILIATION
    -> OWNER_APPROVAL (exact intent + epoch + replay-resistant nonce)
    -> ACCOUNTING_REVIEW
    -> INTERNAL_ALLOCATION_PROPOSED
    -> PAYOUT_REQUESTED
    -> SEPARATE OWNER / HUMAN APPROVAL
    -> PROTECTED SINK SETTLEMENT
    -> FINAL PROVIDER RECONCILIATION
~~~

**The reference module implements only a local synthetic evidence and reversal model.** It never sets PAYMENT_CONFIRMED and never invokes a bank, PSP, blockchain RPC, exchange, wallet, payout or invoice issuance API. Receipt status is \`REFERENCE_EVIDENCE_ONLY_NOT_BANK_SETTLED\`; transfer total stays \`cash_disbursed_minor = 0\`.

## Implemented local controls

1. Domain-separated HMAC fixtures for synthetic provider evidence and synthetic Owner permits, requiring distinct 32-byte-or-longer test keys. **Production signing must be performed by isolated external providers/Owner Authority with public-key verification**, not the demo signer.
2. Exact signed approval intent binds invoice ID, contract, tenant, beneficiary, currency, amount, agreement evidence, legal review, independent QA and provider event.
3. Provider allowlist and in-memory replay rejection by invoice ID, provider event ID, provider transaction ID and Owner nonce.
4. Signed \`STOP\` and \`RESUME\` simulation with strictly increasing authority epochs. Recovery needs a recovery reference and independent-review reference. A pre-STOP permit is invalid after recovery.
5. Provider-attested synthetic REFUND and CHARGEBACK records. Reversal events are accepted during STOP to avoid hiding adverse evidence, but they freeze internal allocations. Over-reversal, forged signatures and cross-tenant events are rejected.
6. Positive integer minor-units, no floating-point accounting, defensive result copies and locally hash-linked event logs.

**Known limitations:** No independent external provider verification, durable storage, database uniqueness/transactions, permit expiration, HSM, signed public-key verification, real owner identity, actual billing, KYC/AML, sanctions screening, tax accounting, external audit custody, multi-process STOP, production retries, race-safe idempotency, or deployed authorization. Local hash chaining can be rewritten by a party controlling all memory. **Do not deploy this class as a payment gateway.**

## Production hardening gates (not completed)

1. Define private isolated identities for independent Owner Authority, provider adapter, reconciler and Protected Financial Execution Sink. Split keys, permissions and networks; the LLM must not sign its own approvals.
2. Persist provider events via transactional inbox/outbox; make \`(provider_id, event_id)\` and \`(provider_id, transaction_id)\` unique with actual DB constraints. Isolate tenant data with explicit authorization and tenant-aware RLS.
3. Validate beneficiary and invoice against independently sourced, authorized records; reconcile settlement, partial payment, reversals, refunds and chargebacks via trusted provider/bank records.
4. Implement signed permits with expiry, revocation, monotonic epoch and independent protected sink-side enforcement even if the model, HANTER, AGY or primary DB is unavailable. Owner STOP must fail closed; recovery needs independent evidence.
5. Implement accountant-reviewed books distinguishing gross invoiced, collected funds, available funds, refunds, liabilities, profits, estimates and token market prices. Preserve exact integer units and currency policies.
6. Run independent security and fault tests including cross-tenant races, compromised provider adapter, changed beneficiary, concurrent duplicate events, post-settlement reversal, database loss, unavailable owner authority and prompt injection. **Do not mark production PASS without actual evidence.**
7. Obtain explicit transaction-specific Architect approval before real transfers, wallet approvals, token distributions, market trades, liquidity, subscriptions, paid integrations or custody. **FREE_ONLY / $0** remains the default.

## Reproduce

~~~sh
python3 -m unittest discover -s tests -p 'test_capital_core_money_boundary.py' -v
python3 -m unittest discover -s tests -p 'test_capital_core_*.py' -v
~~~

The isolated module had **14/14 local synthetic tests PASS** on 2026-11-23. The second command is an intended integration check; the full repository suite, GitHub Actions, independent reviewer acceptance and live execution are **not** claimed verified by that local result.

**Principle:** Architecture → Implementation → Evidence. Payment intent ≠ payment. Claim ≠ evidence. Evidence ≠ independent verification.