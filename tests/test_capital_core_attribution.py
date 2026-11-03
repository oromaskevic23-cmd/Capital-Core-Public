"""Attribution gates for city-scoped NCA contributions (reference-only).

Founder: Alexander Nikolaevich Romaskevich (RomaskevicH).
No real money is disbursed or employment commission promised.
"""
from __future__ import annotations

from dataclasses import replace
import unittest

from capital_core.attribution import AcceptedContribution, AttributionLedger
from capital_core.reference import (
    Agent, City, CityNetwork, ContractTerms, FinanceLedger,
    GovernanceError, Mission, PaymentAttestation, sign_attestation,
    audit_chain_valid,
)

KEY = b"reference-attribution-test-adapter-key-001"


def fixtures(amount: int = 101):
    network = CityNetwork()
    network.register_city(City("de-fra", "Frankfurt", "DE"))
    network.approve_city(
        "de-fra", legal_review_ref="counsel-review", privacy_review_ref="privacy",
        licensed_partner_ref="licensed-local-partner", human_owner_ref="owner",
    )
    contributions = []
    for agent_id, suffix in (("nca-001", "1"), ("nca-002", "2")):
        network.register_agent(Agent(
            agent_id, "de-fra", frozenset({"market_analysis"}),
            "passport-" + suffix, "exam-" + suffix, "supervisor-" + suffix,
        ))
        network.approve_agent(agent_id, owner_approval_ref="cert-" + suffix)
        mission = Mission("mission-" + suffix, "de-fra", agent_id, "market_analysis",
                          "source-" + suffix, "consent-" + suffix)
        network.dispatch(mission)
        network.accept_mission(mission.mission_id, qa_ref="qa-" + suffix,
                               reviewer_id="independent-human-" + suffix,
                               human_approval_ref="accept-" + suffix)
        contributions.append(AcceptedContribution(
            agent_id, mission.mission_id, "de-fra", 1, "qa-" + suffix,
            "independent-human-" + suffix, "accept-" + suffix,
        ))
    finance = FinanceLedger(trusted_adapter_key=KEY)
    terms = ContractTerms(
        "contract-1", "de-fra", "EUR", "software_subscription", "contract",
        "legal-clearance", "owner-approval", "partner", 2000, 7000, 1000,
    )
    evidence = PaymentAttestation(
        "payment-1", "contract-1", amount, "EUR", "external-ref",
        "test-adapter", "quality-reviewed", "finance-owner",
    )
    finance.post_attested_receipt(
        terms, sign_attestation(evidence, trusted_adapter_key=KEY)
    )
    return network, finance, contributions


class AttributionTests(unittest.TestCase):
    def test_deterministic_tie_rounding_and_conservation(self):
        network, finance, contributions = fixtures(amount=11)
        ledger = AttributionLedger()
        result = ledger.allocate(
            network=network, finance=finance, city_id="de-fra",
            receipt_id="payment-1", contributions=contributions,
            owner_approval_ref="owner-finance-approval",
        )
        self.assertEqual(result["reserve_minor"], 1)
        self.assertEqual(result["agent_credits_minor"], {"nca-001": 1, "nca-002": 0})
        self.assertEqual(result["cash_disbursed_minor"], 0)
        self.assertEqual(result["status"], "NON_CASH_INTERNAL_ATTRIBUTION_ONLY")
        self.assertTrue(audit_chain_valid(ledger.audit))

    def test_no_fake_financial_record_allowed(self):
        network, finance, contributions = fixtures()
        with self.assertRaises(GovernanceError):
            AttributionLedger().allocate(
                network=network, finance=finance, city_id="de-fra",
                receipt_id="invented-paid-case", contributions=contributions,
                owner_approval_ref="owner",
            )

    def test_cannot_reward_same_mission_twice(self):
        network, finance, contributions = fixtures()
        ledger = AttributionLedger()
        args = dict(network=network, finance=finance, city_id="de-fra",
                    receipt_id="payment-1", contributions=contributions,
                    owner_approval_ref="owner")
        ledger.allocate(**args)
        with self.assertRaises(GovernanceError):
            ledger.allocate(**args)

    def test_mission_qa_reference_must_match_original_review(self):
        network, finance, contributions = fixtures()
        forged = [replace(contributions[0], qa_ref="self-asserted"), contributions[1]]
        with self.assertRaises(GovernanceError):
            AttributionLedger().allocate(
                network=network, finance=finance, city_id="de-fra",
                receipt_id="payment-1", contributions=forged,
                owner_approval_ref="owner",
            )

    def test_cross_city_and_duplicate_missions_denied(self):
        network, finance, contributions = fixtures()
        with self.assertRaises(GovernanceError):
            AttributionLedger().allocate(
                network=network, finance=finance, city_id="de-fra",
                receipt_id="payment-1",
                contributions=[replace(contributions[0], city_id="ae-dxb")],
                owner_approval_ref="owner",
            )
        with self.assertRaises(GovernanceError):
            AttributionLedger().allocate(
                network=network, finance=finance, city_id="de-fra",
                receipt_id="payment-1", contributions=[contributions[0], contributions[0]],
                owner_approval_ref="owner",
            )

    def test_negative_and_unbounded_weights_denied(self):
        network, finance, contributions = fixtures()
        for weight in (-1, 0, 101, True):
            with self.subTest(weight=weight), self.assertRaises(GovernanceError):
                AttributionLedger().allocate(
                    network=network, finance=finance, city_id="de-fra",
                    receipt_id="payment-1",
                    contributions=[replace(contributions[0], weight_units=weight)],
                    owner_approval_ref="owner",
                )

    def test_owner_and_finance_kill_switches_fail_closed(self):
        network, finance, contributions = fixtures()
        ledger = AttributionLedger()
        ledger.stop(owner_approval_ref="owner")
        with self.assertRaises(GovernanceError):
            ledger.allocate(
                network=network, finance=finance, city_id="de-fra",
                receipt_id="payment-1", contributions=contributions,
                owner_approval_ref="owner",
            )
        ledger = AttributionLedger()
        finance.set_kill_switch(True, owner_approval_ref="owner")
        with self.assertRaises(GovernanceError):
            ledger.allocate(
                network=network, finance=finance, city_id="de-fra",
                receipt_id="payment-1", contributions=contributions,
                owner_approval_ref="owner",
            )


if __name__ == "__main__":
    unittest.main()
