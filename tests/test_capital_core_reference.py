"""Capital Core reference controls: deterministic regression suite.

Founding architect: Alexander Nikolaevich Romaskevich (RomaskevicH).
Implementation provenance: Git history. This is not production/financial attestation.
"""
from __future__ import annotations

from dataclasses import replace
import unittest

from capital_core.reference import (
    Agent, City, CityNetwork, ContractTerms, FinanceLedger,
    GovernanceError, Mission, PaymentAttestation, RevenueGateError,
    audit_chain_valid, sign_attestation,
)

KEY = b"only-for-unit-tests-no-production-key-0001"


def approved_network() -> CityNetwork:
    n = CityNetwork()
    n.register_city(City("de-fra", "Frankfurt", "DE"))
    n.approve_city("de-fra", legal_review_ref="legal-1",
                   privacy_review_ref="privacy-1",
                   licensed_partner_ref="licensed-human-1",
                   human_owner_ref="owner-approval-1")
    n.register_agent(Agent(
        "nca-fra-001", "de-fra",
        frozenset({"property_research", "marketing_draft", "lead_triage"}),
        "ai-passport-1", "independent-exam-1", "human-supervisor-1",
    ))
    n.approve_agent("nca-fra-001", owner_approval_ref="owner-cert-1")
    return n


def mission(mission_id: str = "m1", skill: str = "property_research") -> Mission:
    return Mission(mission_id, "de-fra", "nca-fra-001", skill,
                   "source-proof-1", "consent-evidence-1")


def terms() -> ContractTerms:
    return ContractTerms(
        "contract-1", "de-fra", "EUR", "software_subscription",
        "signed-agreement-1", "legal-clearance-1", "owner-approval-1",
        "licensed-partner-1", 2000, 7000, 1000,
    )


def receipt() -> PaymentAttestation:
    return PaymentAttestation(
        "payment-1", "contract-1", 12500, "EUR",
        "bank-transaction-ref-1", "trusted-adapter-ref-1",
        "delivered-qa-ref-1", "finance-owner-approval-1",
    )


class CityControlTests(unittest.TestCase):
    def test_unreviewed_city_cannot_certify_agent(self) -> None:
        n = CityNetwork()
        n.register_city(City("de-fra", "Frankfurt", "DE"))
        n.register_agent(Agent("nca", "de-fra", frozenset({"lead_triage"}),
                               "passport", "exam", "supervisor"))
        with self.assertRaises(GovernanceError):
            n.approve_agent("nca", owner_approval_ref="owner")

    def test_city_approval_requires_all_references(self) -> None:
        n = CityNetwork()
        n.register_city(City("de-fra", "Frankfurt", "DE"))
        with self.assertRaises(GovernanceError):
            n.approve_city("de-fra", legal_review_ref="legal",
                           privacy_review_ref="", licensed_partner_ref="partner",
                           human_owner_ref="owner")

    def test_approved_city_and_agent_reference_not_claimed_live(self) -> None:
        n = approved_network()
        self.assertEqual(n.cities["de-fra"].status, "PILOT_READY")
        self.assertEqual(n.agents["nca-fra-001"].status, "CERTIFIED_REFERENCE")
        self.assertTrue(audit_chain_valid(n.audit))

    def test_allowed_dispatch_and_independent_review_gate(self) -> None:
        n = approved_network()
        n.dispatch(mission())
        with self.assertRaises(GovernanceError):
            n.accept_mission("m1", qa_ref="", human_approval_ref="human")
        accepted = n.accept_mission("m1", qa_ref="independent-qa",
                                    human_approval_ref="human")
        self.assertEqual(accepted.status, "HUMAN_ACCEPTED")
        self.assertTrue(audit_chain_valid(n.audit))

    def test_unapproved_skill_and_missing_listing_rights_denied(self) -> None:
        n = approved_network()
        with self.assertRaises(GovernanceError):
            n.dispatch(mission(skill="contract_negotiation"))
        with self.assertRaises(GovernanceError):
            n.dispatch(mission(skill="marketing_draft"))
        n.dispatch(replace(mission(), skill="marketing_draft",
                           listing_authorization_ref="owner-listing-permission"))

    def test_duplicate_city_agent_and_mission_denied(self) -> None:
        n = approved_network()
        with self.assertRaises(GovernanceError):
            n.register_city(City("de-fra", "Frankfurt", "DE"))
        with self.assertRaises(GovernanceError):
            n.register_agent(n.agents["nca-fra-001"])
        n.dispatch(mission())
        with self.assertRaises(GovernanceError):
            n.dispatch(mission())

    def test_wrong_city_and_missing_consent_denied(self) -> None:
        n = approved_network()
        n.register_city(City("ae-dxb", "Dubai", "AE"))
        with self.assertRaises(GovernanceError):
            n.dispatch(replace(mission(), city_id="ae-dxb"))
        with self.assertRaises(GovernanceError):
            n.dispatch(replace(mission(), consent_ref=""))

    def test_owner_kill_switch_and_manual_disabling(self) -> None:
        n = approved_network()
        n.set_kill_switch(True, owner_approval_ref="owner")
        with self.assertRaises(GovernanceError):
            n.dispatch(mission())
        n.set_kill_switch(False, owner_approval_ref="owner")
        n.disable_agent("nca-fra-001", owner_approval_ref="owner")
        with self.assertRaises(GovernanceError):
            n.dispatch(mission())
        self.assertTrue(audit_chain_valid(n.audit))

    def test_city_disable_revokes_dispatch(self) -> None:
        n = approved_network()
        n.disable_city("de-fra", owner_approval_ref="owner")
        with self.assertRaises(GovernanceError):
            n.dispatch(mission())

    def test_tampering_breaks_local_audit_chain(self) -> None:
        n = approved_network()
        n.audit[0]["details"]["city"] = "other"
        self.assertFalse(audit_chain_valid(n.audit))


class FinanceTests(unittest.TestCase):
    def test_valid_contract_terms(self) -> None:
        terms().validate()
        with self.assertRaises(RevenueGateError):
            replace(terms(), platform_bps=2001).validate()
        with self.assertRaises(RevenueGateError):
            replace(terms(), platform_bps=True).validate()
        with self.assertRaises(RevenueGateError):
            replace(terms(), service_kind="unlicensed_referral_bounty").validate()

    def test_attestation_required_not_just_claimed_paid(self) -> None:
        ledger = FinanceLedger(trusted_adapter_key=KEY)
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(terms(), receipt())
        self.assertEqual(ledger.receipts, {})

    def test_internal_split_and_rounding_are_exact(self) -> None:
        ledger = FinanceLedger(trusted_adapter_key=KEY)
        signed = sign_attestation(receipt(), trusted_adapter_key=KEY)
        result = ledger.post_attested_receipt(
            terms(), signed, tax_hold_minor=400, refund_minor=100,
            direct_cost_minor=1500,
        )
        self.assertEqual(result["distributable_minor"], 10500)
        self.assertEqual(result["local_partner_allocation_minor"], 7350)
        self.assertEqual(result["nca_internal_reserve_minor"], 1050)
        self.assertEqual(result["platform_allocation_minor"], 2100)
        self.assertEqual(result["cash_disbursed_minor"], 0)
        self.assertEqual(result["status"], "REFERENCE_ATTESTED_NOT_SETTLED")
        self.assertTrue(audit_chain_valid(ledger.audit))

    def test_tampered_signed_receipt_is_rejected(self) -> None:
        ledger = FinanceLedger(trusted_adapter_key=KEY)
        signed = sign_attestation(receipt(), trusted_adapter_key=KEY)
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(terms(), replace(signed, amount_minor=999999))
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(terms(), replace(signed, external_receipt_ref="fake"))

    def test_wrong_currency_and_contract_denied(self) -> None:
        ledger = FinanceLedger(trusted_adapter_key=KEY)
        signed = sign_attestation(receipt(), trusted_adapter_key=KEY)
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(replace(terms(), currency="USD"), signed)
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(replace(terms(), contract_id="other"), signed)

    def test_duplicate_payment_and_negative_holds_denied(self) -> None:
        ledger = FinanceLedger(trusted_adapter_key=KEY)
        signed = sign_attestation(receipt(), trusted_adapter_key=KEY)
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(terms(), signed, tax_hold_minor=-1)
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(terms(), signed, tax_hold_minor=12501)
        ledger.post_attested_receipt(terms(), signed)
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(terms(), signed)

    def test_owner_stop_prevents_new_financial_allocation(self) -> None:
        ledger = FinanceLedger(trusted_adapter_key=KEY)
        ledger.set_kill_switch(True, owner_approval_ref="owner")
        with self.assertRaises(RevenueGateError):
            ledger.post_attested_receipt(
                terms(), sign_attestation(receipt(), trusted_adapter_key=KEY)
            )


if __name__ == "__main__":
    unittest.main()
