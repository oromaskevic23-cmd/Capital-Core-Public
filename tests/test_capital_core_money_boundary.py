"""Synthetic, stdlib-only trust boundary and accounting evidence tests.

No real payments, bank confirmation, financial authority or funds are involved.
"""
import unittest
from dataclasses import replace

from capital_core.money_boundary import (
    ApprovedInvoice, MoneyBoundary, MoneyDenied, OwnerControl, OwnerPermit,
    ProviderReceipt, ProviderReversal, payment_intent_digest,
    reference_sign_owner, reference_sign_provider,
)

PROVIDER = b"synthetic-provider-credential-for-local-demo-2026"
OWNER = b"separate-synthetic-owner-credential-for-demo-2026"


def fixture():
    ledger = MoneyBoundary(tenant_id="imperial-fra", provider_verification_keys={"demo-bank": PROVIDER},
                           owner_verification_key=OWNER)
    invoice = ApprovedInvoice("invoice-001", "imperial-fra", "contract-001", "beneficiary-001",
                              "EUR", 12500, "signed-agreement", "legal-check", "independent-qa")
    proof = reference_sign_provider(ProviderReceipt(
        "demo-bank", "evt-001", "txn-001", "invoice-001", "imperial-fra", "beneficiary-001", "EUR", 12500,
    ), key=PROVIDER)
    permit = reference_sign_owner(OwnerPermit(payment_intent_digest(invoice, proof), 0, "permit-nonce-001"), key=OWNER)
    return ledger, invoice, proof, permit


class MoneyBoundaryTests(unittest.TestCase):
    def test_reference_record_never_disburses_cash(self):
        ledger, invoice, proof, permit = fixture()
        row = ledger.record_reference_receipt(invoice, proof, permit)
        self.assertEqual(row["cash_disbursed_minor"], 0)
        self.assertEqual(row["gross_minor"], 12500)
        self.assertIn("NOT_BANK_SETTLED", row["status"])
        self.assertTrue(ledger.audit_valid())

    def test_unsigned_provider_or_owner_denied(self):
        ledger, invoice, proof, permit = fixture()
        for change in (replace(proof, signature_hex=""), replace(proof, signature_hex="0" * 64)):
            with self.assertRaises(MoneyDenied):
                ledger.record_reference_receipt(invoice, change, permit)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_receipt(invoice, proof, replace(permit, signature_hex=""))

    def test_beneficiary_tenant_currency_amount_binding(self):
        for mutation in (
            {"beneficiary_ref": "wrong-payee"}, {"tenant_id": "other-tenant"},
            {"currency": "USD"}, {"gross_minor": 12501}, {"invoice_id": "invoice-other"},
            {"contract_id": "contract-other"}, {"independent_qa_ref": "other-qa"},
        ):
            with self.subTest(mutation=mutation):
                ledger, invoice, proof, permit = fixture()
                with self.assertRaises(MoneyDenied):
                    ledger.record_reference_receipt(replace(invoice, **mutation), proof, permit)

    def test_replay_protection_invoice_event_transaction_nonce(self):
        ledger, invoice, proof, permit = fixture()
        ledger.record_reference_receipt(invoice, proof, permit)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_receipt(invoice, proof, permit)
        second_invoice = replace(invoice, invoice_id="invoice-002")
        new_event_same_tx = reference_sign_provider(replace(proof, provider_event_id="evt-002", invoice_id="invoice-002", signature_hex=""), key=PROVIDER)
        permit2 = reference_sign_owner(OwnerPermit(payment_intent_digest(second_invoice, new_event_same_tx), 0, "nonce-002"), key=OWNER)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_receipt(second_invoice, new_event_same_tx, permit2)

    def test_claim_not_settled_denied(self):
        ledger, invoice, proof, permit = fixture()
        changed = reference_sign_provider(replace(proof, provider_claim="PENDING", signature_hex=""), key=PROVIDER)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_receipt(invoice, changed, permit)

    def test_owner_epoch_stop_and_signed_independent_recovery(self):
        ledger, invoice, proof, permit = fixture()
        stop = reference_sign_owner(OwnerControl("STOP", 1, "stop-nonce-001"), key=OWNER)
        ledger.owner_control(stop)
        self.assertTrue(ledger.stopped)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_receipt(invoice, proof, permit)
        with self.assertRaises(MoneyDenied):
            ledger.owner_control(stop)
        with self.assertRaises(MoneyDenied):
            ledger.owner_control(reference_sign_owner(OwnerControl("RESUME", 2, "resume-nonce"), key=OWNER))
        with self.assertRaises(MoneyDenied):
            ledger.owner_control(replace(OwnerControl("RESUME", 2, "resume-nonce", "recovery-proof", "review-proof"), signature_hex="bad"))
        resume = reference_sign_owner(OwnerControl("RESUME", 2, "resume-nonce", "recovery-proof", "review-proof"), key=OWNER)
        ledger.owner_control(resume)
        self.assertFalse(ledger.stopped)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_receipt(invoice, proof, permit)  # stale permit from epoch 0
        fresh = reference_sign_owner(OwnerPermit(payment_intent_digest(invoice, proof), 2, "nonce-epoch-2"), key=OWNER)
        ledger.record_reference_receipt(invoice, proof, fresh)
        self.assertTrue(ledger.audit_valid())

    def test_stop_requires_owner_signature(self):
        ledger, *_ = fixture()
        with self.assertRaises(MoneyDenied):
            ledger.owner_control(OwnerControl("STOP", 1, "stop-without-owner-sig"))
        self.assertFalse(ledger.stopped)

    def test_refund_reverses_net_not_disbursed(self):
        ledger, invoice, proof, permit = fixture()
        ledger.record_reference_receipt(invoice, proof, permit)
        reversal = reference_sign_provider(ProviderReversal(
            "demo-bank", "refund-event", "txn-001", "invoice-001", "imperial-fra", "EUR", 2000, "REFUND",
        ), key=PROVIDER)
        row = ledger.record_reference_reversal(reversal)
        self.assertEqual(row["reversed_minor"], 2000)
        self.assertEqual(row["net_reference_minor"], 10500)
        self.assertTrue(row["allocation_frozen"])
        self.assertEqual(row["cash_disbursed_minor"], 0)
        self.assertTrue(ledger.audit_valid())

    def test_reversal_allowed_during_stop(self):
        ledger, invoice, proof, permit = fixture()
        ledger.record_reference_receipt(invoice, proof, permit)
        ledger.owner_control(reference_sign_owner(OwnerControl("STOP", 1, "stop-nonce"), key=OWNER))
        reversal = reference_sign_provider(ProviderReversal(
            "demo-bank", "chargeback-event", "txn-001", "invoice-001", "imperial-fra", "EUR", 12500, "CHARGEBACK",
        ), key=PROVIDER)
        result = ledger.record_reference_reversal(reversal)
        self.assertEqual(result["net_reference_minor"], 0)
        self.assertTrue(ledger.stopped)

    def test_reversal_replay_overrefund_forgery_and_cross_tenant(self):
        ledger, invoice, proof, permit = fixture()
        ledger.record_reference_receipt(invoice, proof, permit)
        orig = ProviderReversal("demo-bank", "event-r", "txn-001", "invoice-001", "imperial-fra", "EUR", 9000, "REFUND")
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_reversal(orig)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_reversal(reference_sign_provider(replace(orig, tenant_id="other"), key=PROVIDER))
        good = reference_sign_provider(orig, key=PROVIDER)
        ledger.record_reference_reversal(good)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_reversal(good)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_reversal(reference_sign_provider(replace(orig, provider_event_id="event-r2", amount_minor=9000), key=PROVIDER))

    def test_reversal_does_not_precede_recorded_receipt(self):
        ledger, *_ = fixture()
        bad = reference_sign_provider(ProviderReversal("demo-bank", "reversal-before", "txn-001", "invoice-001", "imperial-fra", "EUR", 1, "REFUND"), key=PROVIDER)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_reversal(bad)

    def test_boolean_and_invalid_financial_units_denied(self):
        for amount in (True, 0, -1, 125.0):
            ledger, invoice, proof, permit = fixture()
            with self.assertRaises(MoneyDenied):
                ledger.record_reference_receipt(replace(invoice, gross_minor=amount), proof, permit)

    def test_untrusted_provider_denied_even_with_synthetic_signature(self):
        ledger, invoice, proof, permit = fixture()
        other = reference_sign_provider(replace(proof, provider_id="untrusted-bank", signature_hex=""), key=PROVIDER)
        with self.assertRaises(MoneyDenied):
            ledger.record_reference_receipt(invoice, other, permit)

    def test_returned_rows_and_audit_are_copies(self):
        ledger, invoice, proof, permit = fixture()
        row = ledger.record_reference_receipt(invoice, proof, permit)
        row["net_reference_minor"] = 99
        self.assertEqual(ledger.view(invoice.invoice_id)["net_reference_minor"], 12500)
        audit = ledger.audit_snapshot()
        audit[0]["details"]["invoice_id"] = "tampered"
        self.assertTrue(ledger.audit_valid())


if __name__ == "__main__":
    unittest.main()
