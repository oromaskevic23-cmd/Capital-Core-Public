"""IMPERIAL Core / Capital Core: isolated financial evidence boundary reference.

Founder and final architectural authority: Alexander Nikolaevich Romaskevich.
DEMONSTRATION ONLY: local HMAC fixtures cannot establish bank settlement,
owner identity, independent approval, custody, payment or production safety.
No bank, wallet, network, payment-provider or payout operations exist here.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
import hmac
import json
import re
from typing import Any, Mapping


class MoneyDenied(ValueError):
    """A monetary trust boundary failed closed."""


_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}\Z")
_DOMAIN = b"IMPERIAL-CAPITAL-MONEY-REFERENCE-v1|"


def _identifier(value: str, field: str) -> None:
    if not isinstance(value, str) or not _ID.fullmatch(value):
        raise MoneyDenied(f"{field} must be a bounded, nonempty reference identifier")


def _minor(value: int, field: str, *, positive: bool = True) -> None:
    if type(value) is not int or value < (1 if positive else 0):
        raise MoneyDenied(f"{field} must be an integer minor-unit amount")


def _currency(value: str) -> None:
    if not isinstance(value, str) or len(value) != 3 or not value.isascii() or not value.isupper() or not value.isalpha():
        raise MoneyDenied("currency requires a three-letter ISO-style uppercase code")


def _message(kind: str, fields: Mapping[str, Any]) -> bytes:
    return _DOMAIN + kind.encode("ascii") + b"|" + json.dumps(
        fields, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    ).encode("ascii")


def _sign(key: bytes, kind: str, fields: Mapping[str, Any]) -> str:
    if not isinstance(key, bytes) or len(key) < 32:
        raise MoneyDenied("reference verification keys must be at least 32 bytes")
    return hmac.new(key, _message(kind, fields), sha256).hexdigest()


def _verify(key: bytes, kind: str, fields: Mapping[str, Any], signature: str) -> None:
    if not isinstance(signature, str) or not hmac.compare_digest(_sign(key, kind, fields), signature):
        raise MoneyDenied(f"{kind} signature rejected")


def _sha_fields(kind: str, fields: Mapping[str, Any]) -> str:
    return sha256(_message(kind, fields)).hexdigest()


@dataclass(frozen=True)
class ApprovedInvoice:
    invoice_id: str
    tenant_id: str
    contract_id: str
    beneficiary_ref: str
    currency: str
    gross_minor: int
    agreement_ref: str
    legal_clearance_ref: str
    independent_qa_ref: str

    def validate(self) -> None:
        for name in ("invoice_id", "tenant_id", "contract_id", "beneficiary_ref",
                     "agreement_ref", "legal_clearance_ref", "independent_qa_ref"):
            _identifier(getattr(self, name), name)
        _currency(self.currency)
        _minor(self.gross_minor, "gross_minor")

    def fields(self) -> dict[str, Any]:
        return {k: getattr(self, k) for k in self.__dataclass_fields__}


@dataclass(frozen=True)
class ProviderReceipt:
    provider_id: str
    provider_event_id: str
    external_transaction_id: str
    invoice_id: str
    tenant_id: str
    beneficiary_ref: str
    currency: str
    amount_minor: int
    provider_claim: str = "SETTLED"
    signature_hex: str = ""

    def fields(self) -> dict[str, Any]:
        return {k: getattr(self, k) for k in self.__dataclass_fields__ if k != "signature_hex"}


@dataclass(frozen=True)
class OwnerPermit:
    intent_digest: str
    epoch: int
    nonce: str
    signature_hex: str = ""

    def fields(self) -> dict[str, Any]:
        return {"intent_digest": self.intent_digest, "epoch": self.epoch, "nonce": self.nonce}


@dataclass(frozen=True)
class OwnerControl:
    action: str
    epoch: int
    nonce: str
    recovery_ref: str = ""
    independent_review_ref: str = ""
    signature_hex: str = ""

    def fields(self) -> dict[str, Any]:
        return {k: getattr(self, k) for k in self.__dataclass_fields__ if k != "signature_hex"}


@dataclass(frozen=True)
class ProviderReversal:
    provider_id: str
    provider_event_id: str
    external_transaction_id: str
    invoice_id: str
    tenant_id: str
    currency: str
    amount_minor: int
    kind: str
    signature_hex: str = ""

    def fields(self) -> dict[str, Any]:
        return {k: getattr(self, k) for k in self.__dataclass_fields__ if k != "signature_hex"}


def reference_sign_provider(evidence: ProviderReceipt | ProviderReversal, *, key: bytes):
    """Local test-fixture signer; MUST NOT be used to sign real payment events."""
    kind = "provider-receipt" if isinstance(evidence, ProviderReceipt) else "provider-reversal"
    return replace(evidence, signature_hex=_sign(key, kind, evidence.fields()))


def reference_sign_owner(action: OwnerPermit | OwnerControl, *, key: bytes):
    """Local test-fixture signer; NOT an independent Owner Authority."""
    kind = "owner-permit" if isinstance(action, OwnerPermit) else "owner-control"
    return replace(action, signature_hex=_sign(key, kind, action.fields()))


def payment_intent_digest(invoice: ApprovedInvoice, receipt: ProviderReceipt) -> str:
    """Binds every invoice field and claimed provider receipt to one approval intent."""
    invoice.validate()
    return _sha_fields("record-receipt-intent", {"invoice": invoice.fields(), "receipt": receipt.fields()})


class MoneyBoundary:
    """In-memory simulation. No provider access, no settlement, no payouts.

    Production needs independently operated external verifier and owner authority,
    a transactional durable database, revocation checks and trusted audit anchoring.
    """

    def __init__(self, *, tenant_id: str, provider_verification_keys: Mapping[str, bytes],
                 owner_verification_key: bytes) -> None:
        _identifier(tenant_id, "tenant_id")
        _sign(owner_verification_key, "key-validation", {})
        if not provider_verification_keys:
            raise MoneyDenied("at least one explicit provider allowlist entry is required")
        for provider, key in provider_verification_keys.items():
            _identifier(provider, "provider_id")
            _sign(key, "key-validation", {})
        self.tenant_id = tenant_id
        self._provider_keys = dict(provider_verification_keys)
        self._owner_key = owner_verification_key
        self._epoch = 0
        self.stopped = False
        self._used_owner_nonces: set[str] = set()
        self._provider_events: set[tuple[str, str]] = set()
        self._transactions: set[tuple[str, str]] = set()
        self._receipts: dict[str, dict[str, Any]] = {}
        self._audit: list[dict[str, Any]] = []

    def _audit_event(self, kind: str, fields: dict[str, Any]) -> None:
        previous = self._audit[-1]["digest"] if self._audit else "0" * 64
        payload = {"sequence": len(self._audit) + 1, "previous": previous,
                   "kind": kind, "details": fields}
        digest = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        self._audit.append({**payload, "digest": digest})

    def audit_valid(self) -> bool:
        previous = "0" * 64
        for number, event in enumerate(self._audit, 1):
            payload = {k: event.get(k) for k in ("sequence", "previous", "kind", "details")}
            if payload["sequence"] != number or payload["previous"] != previous:
                return False
            digest = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            if not hmac.compare_digest(digest, str(event.get("digest", ""))):
                return False
            previous = digest
        return True

    def _provider_key(self, provider_id: str) -> bytes:
        _identifier(provider_id, "provider_id")
        if provider_id not in self._provider_keys:
            raise MoneyDenied("unrecognized provider")
        return self._provider_keys[provider_id]

    def _owner_nonce(self, nonce: str) -> None:
        _identifier(nonce, "owner nonce")
        if nonce in self._used_owner_nonces:
            raise MoneyDenied("owner nonce replay")

    def owner_control(self, control: OwnerControl) -> None:
        if control.action not in ("STOP", "RESUME"):
            raise MoneyDenied("unsupported owner control action")
        if type(control.epoch) is not int or control.epoch <= self._epoch:
            raise MoneyDenied("owner control epoch must advance monotonically")
        self._owner_nonce(control.nonce)
        if control.action == "RESUME":
            if not self.stopped:
                raise MoneyDenied("cannot resume an active boundary")
            _identifier(control.recovery_ref, "recovery_ref")
            _identifier(control.independent_review_ref, "independent_review_ref")
        elif not self.stopped and control.action != "STOP":
            raise MoneyDenied("invalid control")
        _verify(self._owner_key, "owner-control", control.fields(), control.signature_hex)
        self.stopped = control.action == "STOP"
        self._epoch = control.epoch
        self._used_owner_nonces.add(control.nonce)
        self._audit_event("OWNER_STOP" if self.stopped else "OWNER_RECOVERY_REFERENCE", {"epoch": self._epoch})

    def record_reference_receipt(self, invoice: ApprovedInvoice, receipt: ProviderReceipt,
                                 permit: OwnerPermit) -> dict[str, Any]:
        if self.stopped:
            raise MoneyDenied("Owner STOP: reject new receipts")
        invoice.validate()
        if invoice.tenant_id != self.tenant_id:
            raise MoneyDenied("invoice tenant mismatch")
        for field in ("provider_event_id", "external_transaction_id", "invoice_id", "tenant_id", "beneficiary_ref"):
            _identifier(getattr(receipt, field), field)
        _currency(receipt.currency)
        _minor(receipt.amount_minor, "amount_minor")
        if receipt.provider_claim != "SETTLED":
            raise MoneyDenied("provider claim is not settled")
        if (invoice.invoice_id != receipt.invoice_id or invoice.tenant_id != receipt.tenant_id or
            invoice.beneficiary_ref != receipt.beneficiary_ref or invoice.currency != receipt.currency or
            invoice.gross_minor != receipt.amount_minor):
            raise MoneyDenied("invoice / tenant / beneficiary / currency / amount mismatch")
        event_key = (receipt.provider_id, receipt.provider_event_id)
        tx_key = (receipt.provider_id, receipt.external_transaction_id)
        if (invoice.invoice_id in self._receipts or event_key in self._provider_events or
            tx_key in self._transactions):
            raise MoneyDenied("duplicate invoice, provider event or external transaction")
        _verify(self._provider_key(receipt.provider_id), "provider-receipt", receipt.fields(), receipt.signature_hex)
        if type(permit.epoch) is not int or permit.epoch != self._epoch:
            raise MoneyDenied("owner permit bound to stale or future authority epoch")
        self._owner_nonce(permit.nonce)
        digest = payment_intent_digest(invoice, receipt)
        if permit.intent_digest != digest:
            raise MoneyDenied("owner permit not bound to this exact invoice and receipt")
        _verify(self._owner_key, "owner-permit", permit.fields(), permit.signature_hex)
        result = {
            "status": "REFERENCE_EVIDENCE_ONLY_NOT_BANK_SETTLED",
            "invoice_id": invoice.invoice_id,
            "tenant_id": self.tenant_id,
            "contract_id": invoice.contract_id,
            "currency": invoice.currency,
            "gross_minor": invoice.gross_minor,
            "reversed_minor": 0,
            "net_reference_minor": invoice.gross_minor,
            "provider_id": receipt.provider_id,
            "external_transaction_id": receipt.external_transaction_id,
            "allocation_frozen": False,
            "cash_disbursed_minor": 0,
        }
        self._receipts[invoice.invoice_id] = result
        self._provider_events.add(event_key)
        self._transactions.add(tx_key)
        self._used_owner_nonces.add(permit.nonce)
        self._audit_event("REFERENCE_RECEIPT_RECORDED", {
            "invoice_id": invoice.invoice_id, "provider": receipt.provider_id,
            "authority_epoch": self._epoch, "evidence_digest": digest,
        })
        return result.copy()

    def record_reference_reversal(self, reversal: ProviderReversal) -> dict[str, Any]:
        """Accept independently attested reversal even when owner has stopped new work."""
        for field in ("provider_event_id", "external_transaction_id", "invoice_id", "tenant_id"):
            _identifier(getattr(reversal, field), field)
        _currency(reversal.currency)
        _minor(reversal.amount_minor, "amount_minor")
        if reversal.kind not in ("REFUND", "CHARGEBACK"):
            raise MoneyDenied("unsupported reversal type")
        row = self._receipts.get(reversal.invoice_id)
        if (not row or reversal.tenant_id != self.tenant_id or
            row["provider_id"] != reversal.provider_id or
            row["external_transaction_id"] != reversal.external_transaction_id or
            row["currency"] != reversal.currency):
            raise MoneyDenied("unmatched reversal / tenant / transaction")
        event_key = (reversal.provider_id, reversal.provider_event_id)
        if event_key in self._provider_events:
            raise MoneyDenied("duplicate provider reversal event")
        if reversal.amount_minor > row["net_reference_minor"]:
            raise MoneyDenied("reversal exceeds unreversed amount")
        _verify(self._provider_key(reversal.provider_id), "provider-reversal", reversal.fields(), reversal.signature_hex)
        updated = dict(row)
        updated["reversed_minor"] += reversal.amount_minor
        updated["net_reference_minor"] -= reversal.amount_minor
        updated["allocation_frozen"] = True
        updated["status"] = "REFERENCE_REVERSED_OR_DISPUTED_NO_SETTLEMENT_CLAIM"
        self._receipts[reversal.invoice_id] = updated
        self._provider_events.add(event_key)
        self._audit_event("REFERENCE_REVERSAL_RECORDED", {
            "invoice_id": reversal.invoice_id, "kind": reversal.kind,
            "amount_minor": reversal.amount_minor, "event_id": reversal.provider_event_id,
        })
        return updated.copy()

    def view(self, invoice_id: str) -> dict[str, Any]:
        _identifier(invoice_id, "invoice_id")
        if invoice_id not in self._receipts:
            raise MoneyDenied("unknown invoice")
        return self._receipts[invoice_id].copy()

    def audit_snapshot(self) -> list[dict[str, Any]]:
        return json.loads(json.dumps(self._audit))
