"""Governed multi-city NCA and revenue reference engine (stdlib-only).

Founding architect: Alexander Nikolaevich Romaskevich (RomaskevicH).
Original implementation contributors: see repository Git history.
No real brokerage authority, payments, licensing verification, or external dispatch.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
import hmac
import json
from typing import Any


class GovernanceError(ValueError):
    """A missing human, permission or provenance gate denied an operation."""


class RevenueGateError(ValueError):
    """The reference finance controls rejected an untrusted operation."""


ALLOWED_SKILLS = frozenset({
    "property_research", "listing_quality_review", "lead_triage",
    "marketing_draft", "appointment_preparation", "market_analysis",
})
ALLOWED_SERVICES = frozenset({
    "software_subscription", "delivered_marketing_services",
    "partner_supervised_support",
})


def _require_ref(value: str, name: str, exc: type[Exception] = GovernanceError) -> None:
    if not isinstance(value, str) or not value.strip():
        raise exc(f"{name} requires a non-empty evidence reference")


def _audit_append(events: list[dict[str, Any]], kind: str, details: dict[str, Any]) -> None:
    sequence = len(events) + 1
    previous = events[-1]["digest"] if events else "0" * 64
    payload = {"sequence": sequence, "previous": previous, "kind": kind, "details": details}
    digest = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    events.append({**payload, "digest": digest})


def audit_chain_valid(events: list[dict[str, Any]]) -> bool:
    previous = "0" * 64
    for i, event in enumerate(events, start=1):
        payload = {k: event.get(k) for k in ("sequence", "previous", "kind", "details")}
        if payload["sequence"] != i or payload["previous"] != previous:
            return False
        digest = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if not hmac.compare_digest(digest, str(event.get("digest", ""))):
            return False
        previous = digest
    return True


@dataclass(frozen=True)
class City:
    city_id: str
    name: str
    country_code: str
    status: str = "CANDIDATE"
    legal_review_ref: str = ""
    privacy_review_ref: str = ""
    licensed_partner_ref: str = ""
    human_owner_ref: str = ""


@dataclass(frozen=True)
class Agent:
    agent_id: str
    city_id: str
    skills: frozenset[str]
    passport_ref: str
    independent_exam_ref: str
    human_supervisor_ref: str
    status: str = "CANDIDATE"


@dataclass(frozen=True)
class Mission:
    mission_id: str
    city_id: str
    agent_id: str
    skill: str
    source_ref: str
    consent_ref: str
    listing_authorization_ref: str = ""
    status: str = "DISPATCHED"
    qa_ref: str = ""
    human_approval_ref: str = ""


class CityNetwork:
    """In-memory control-plane demo. Persistence and authorization remain external."""

    def __init__(self) -> None:
        self.cities: dict[str, City] = {}
        self.agents: dict[str, Agent] = {}
        self.missions: dict[str, Mission] = {}
        self.audit: list[dict[str, Any]] = []
        self.owner_kill_switch = False

    def register_city(self, city: City) -> None:
        for k, value in (("city_id", city.city_id), ("name", city.name),
                         ("country_code", city.country_code)):
            _require_ref(value, k)
        if city.status != "CANDIDATE" or city.city_id in self.cities:
            raise GovernanceError("new cities must be unique CANDIDATE records")
        self.cities[city.city_id] = city
        _audit_append(self.audit, "CITY_CANDIDATE", {"city": city.city_id})

    def approve_city(self, city_id: str, *, legal_review_ref: str, privacy_review_ref: str,
                     licensed_partner_ref: str, human_owner_ref: str) -> City:
        if self.owner_kill_switch or city_id not in self.cities:
            raise GovernanceError("city approval denied")
        for k, value in locals().copy().items():
            if k.endswith("_ref"):
                _require_ref(value, k)
        city = self.cities[city_id]
        if city.status != "CANDIDATE":
            raise GovernanceError("city already approved or disabled")
        approved = replace(city, status="PILOT_READY", legal_review_ref=legal_review_ref,
                           privacy_review_ref=privacy_review_ref,
                           licensed_partner_ref=licensed_partner_ref,
                           human_owner_ref=human_owner_ref)
        self.cities[city_id] = approved
        _audit_append(self.audit, "CITY_GATE_APPROVED", {"city": city_id, "owner": human_owner_ref})
        return approved

    def register_agent(self, agent: Agent) -> None:
        if agent.agent_id in self.agents or agent.city_id not in self.cities:
            raise GovernanceError("duplicate agent or unknown city")
        if agent.status != "CANDIDATE" or not agent.skills or not agent.skills <= ALLOWED_SKILLS:
            raise GovernanceError("only bounded candidate skills are accepted")
        for k in ("agent_id", "passport_ref", "independent_exam_ref", "human_supervisor_ref"):
            _require_ref(getattr(agent, k), k)
        self.agents[agent.agent_id] = agent
        _audit_append(self.audit, "AGENT_CANDIDATE", {"agent": agent.agent_id, "city": agent.city_id})

    def approve_agent(self, agent_id: str, *, owner_approval_ref: str) -> Agent:
        _require_ref(owner_approval_ref, "owner_approval_ref")
        agent = self.agents.get(agent_id)
        if self.owner_kill_switch or not agent or agent.status != "CANDIDATE":
            raise GovernanceError("agent approval denied")
        city = self.cities[agent.city_id]
        if city.status != "PILOT_READY":
            raise GovernanceError("city has not passed required gates")
        approved = replace(agent, status="CERTIFIED_REFERENCE")
        self.agents[agent_id] = approved
        _audit_append(self.audit, "AGENT_REFERENCE_CERTIFIED", {"agent": agent_id, "approval": owner_approval_ref})
        return approved

    def dispatch(self, mission: Mission) -> Mission:
        if self.owner_kill_switch:
            raise GovernanceError("Owner Kill Switch is active")
        if mission.mission_id in self.missions or mission.status != "DISPATCHED":
            raise GovernanceError("duplicate or invalid mission")
        city = self.cities.get(mission.city_id)
        agent = self.agents.get(mission.agent_id)
        if not city or city.status != "PILOT_READY":
            raise GovernanceError("city is not approved")
        if not agent or agent.city_id != mission.city_id or agent.status != "CERTIFIED_REFERENCE":
            raise GovernanceError("agent is not certified for this city")
        if mission.skill not in ALLOWED_SKILLS or mission.skill not in agent.skills:
            raise GovernanceError("unapproved Enterprise Skill")
        for k in ("mission_id", "source_ref", "consent_ref"):
            _require_ref(getattr(mission, k), k)
        if mission.skill in {"listing_quality_review", "marketing_draft"}:
            _require_ref(mission.listing_authorization_ref, "listing_authorization_ref")
        self.missions[mission.mission_id] = mission
        _audit_append(self.audit, "REFERENCE_MISSION_DISPATCH", {
            "mission": mission.mission_id, "agent": mission.agent_id, "city": mission.city_id
        })
        return mission

    def accept_mission(self, mission_id: str, *, qa_ref: str, human_approval_ref: str) -> Mission:
        if self.owner_kill_switch:
            raise GovernanceError("Owner Kill Switch is active")
        _require_ref(qa_ref, "qa_ref")
        _require_ref(human_approval_ref, "human_approval_ref")
        mission = self.missions.get(mission_id)
        if not mission or mission.status != "DISPATCHED":
            raise GovernanceError("mission not found or already reviewed")
        if self.agents[mission.agent_id].status != "CERTIFIED_REFERENCE":
            raise GovernanceError("disabled agent cannot complete a mission")
        if self.cities[mission.city_id].status != "PILOT_READY":
            raise GovernanceError("disabled city cannot complete a mission")
        accepted = replace(mission, status="HUMAN_ACCEPTED", qa_ref=qa_ref,
                           human_approval_ref=human_approval_ref)
        self.missions[mission_id] = accepted
        _audit_append(self.audit, "REFERENCE_MISSION_ACCEPTED", {"mission": mission_id, "qa": qa_ref})
        return accepted

    def disable_agent(self, agent_id: str, *, owner_approval_ref: str) -> None:
        _require_ref(owner_approval_ref, "owner_approval_ref")
        if agent_id not in self.agents:
            raise GovernanceError("unknown agent")
        self.agents[agent_id] = replace(self.agents[agent_id], status="DISABLED")
        _audit_append(self.audit, "AGENT_DISABLED", {"agent": agent_id})

    def disable_city(self, city_id: str, *, owner_approval_ref: str) -> None:
        _require_ref(owner_approval_ref, "owner_approval_ref")
        if city_id not in self.cities:
            raise GovernanceError("unknown city")
        self.cities[city_id] = replace(self.cities[city_id], status="DISABLED")
        _audit_append(self.audit, "CITY_DISABLED", {"city": city_id})

    def set_kill_switch(self, enabled: bool, *, owner_approval_ref: str) -> None:
        _require_ref(owner_approval_ref, "owner_approval_ref")
        if not isinstance(enabled, bool):
            raise GovernanceError("kill switch value must be a boolean")
        self.owner_kill_switch = enabled
        _audit_append(self.audit, "OWNER_KILL_SWITCH", {"enabled": enabled, "approval": owner_approval_ref})


@dataclass(frozen=True)
class ContractTerms:
    contract_id: str
    city_id: str
    currency: str
    service_kind: str
    agreement_ref: str
    legal_clearance_ref: str
    owner_approval_ref: str
    local_partner_ref: str
    platform_bps: int
    local_partner_bps: int
    nca_internal_reserve_bps: int

    def validate(self) -> None:
        for k in ("contract_id", "city_id", "agreement_ref", "legal_clearance_ref",
                  "owner_approval_ref", "local_partner_ref"):
            _require_ref(getattr(self, k), k, RevenueGateError)
        if self.service_kind not in ALLOWED_SERVICES:
            raise RevenueGateError("unapproved service category: no referral bounty or unsupported commission")
        if not (isinstance(self.currency, str) and len(self.currency) == 3 and
                self.currency.isascii() and self.currency.isalpha() and self.currency.isupper()):
            raise RevenueGateError("currency must be a three-letter uppercase ISO-style code")
        shares = (self.platform_bps, self.local_partner_bps, self.nca_internal_reserve_bps)
        if any(type(x) is not int or not 0 <= x <= 10_000 for x in shares) or sum(shares) != 10_000:
            raise RevenueGateError("explicit, whole-number contractual basis points must total 10000")


@dataclass(frozen=True)
class PaymentAttestation:
    payment_id: str
    contract_id: str
    amount_minor: int
    currency: str
    external_receipt_ref: str
    external_verifier_ref: str
    service_qa_ref: str
    finance_approval_ref: str
    signature_hex: str = ""

    def canonical_message(self) -> bytes:
        fields = {k: getattr(self, k) for k in (
            "payment_id", "contract_id", "amount_minor", "currency",
            "external_receipt_ref", "external_verifier_ref",
            "service_qa_ref", "finance_approval_ref",
        )}
        return json.dumps(fields, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


def sign_attestation(attestation: PaymentAttestation, *, trusted_adapter_key: bytes) -> PaymentAttestation:
    """Test adapter only. Production signing keys must never reach NCA/clients."""
    if not isinstance(trusted_adapter_key, bytes) or len(trusted_adapter_key) < 32:
        raise RevenueGateError("a 32-byte-or-longer trusted adapter key is required")
    signature = hmac.new(trusted_adapter_key, attestation.canonical_message(), "sha256").hexdigest()
    return replace(attestation, signature_hex=signature)


class FinanceLedger:
    """Internal allocation demonstration. No funds are transferred or verified here."""

    def __init__(self, *, trusted_adapter_key: bytes) -> None:
        if not isinstance(trusted_adapter_key, bytes) or len(trusted_adapter_key) < 32:
            raise RevenueGateError("verifier key must be at least 32 bytes")
        self._key = trusted_adapter_key
        self.receipts: dict[str, dict[str, Any]] = {}
        self.audit: list[dict[str, Any]] = []
        self.owner_kill_switch = False

    def set_kill_switch(self, enabled: bool, *, owner_approval_ref: str) -> None:
        _require_ref(owner_approval_ref, "owner_approval_ref", RevenueGateError)
        if not isinstance(enabled, bool):
            raise RevenueGateError("boolean required")
        self.owner_kill_switch = enabled
        _audit_append(self.audit, "FINANCE_KILL_SWITCH", {"enabled": enabled})

    def post_attested_receipt(self, terms: ContractTerms, attestation: PaymentAttestation,
                              *, tax_hold_minor: int = 0, refund_minor: int = 0,
                              direct_cost_minor: int = 0) -> dict[str, Any]:
        if self.owner_kill_switch:
            raise RevenueGateError("finance stopped by Owner Kill Switch")
        terms.validate()
        for k in ("payment_id", "contract_id", "external_receipt_ref",
                  "external_verifier_ref", "service_qa_ref", "finance_approval_ref"):
            _require_ref(getattr(attestation, k), k, RevenueGateError)
        if attestation.payment_id in self.receipts:
            raise RevenueGateError("duplicate payment evidence (idempotency)")
        if terms.contract_id != attestation.contract_id or terms.currency != attestation.currency:
            raise RevenueGateError("contract and currency mismatch")
        if type(attestation.amount_minor) is not int or attestation.amount_minor <= 0:
            raise RevenueGateError("positive integer minor-unit amount required")
        holds = (tax_hold_minor, refund_minor, direct_cost_minor)
        if any(type(x) is not int or x < 0 for x in holds):
            raise RevenueGateError("holds must be nonnegative integer minor units")
        if sum(holds) > attestation.amount_minor:
            raise RevenueGateError("holds cannot exceed receipt amount")
        expected = hmac.new(self._key, attestation.canonical_message(), "sha256").hexdigest()
        if not hmac.compare_digest(expected, attestation.signature_hex):
            raise RevenueGateError("trusted-adapter attestation failed (fail closed)")
        distributable = attestation.amount_minor - sum(holds)
        local = distributable * terms.local_partner_bps // 10_000
        nca_reserve = distributable * terms.nca_internal_reserve_bps // 10_000
        platform = distributable - local - nca_reserve
        result = {
            "status": "REFERENCE_ATTESTED_NOT_SETTLED",
            "payment_id": attestation.payment_id,
            "contract_id": terms.contract_id,
            "currency": terms.currency,
            "gross_minor": attestation.amount_minor,
            "tax_hold_minor": tax_hold_minor,
            "refund_minor": refund_minor,
            "direct_cost_minor": direct_cost_minor,
            "distributable_minor": distributable,
            "platform_allocation_minor": platform,
            "local_partner_allocation_minor": local,
            "nca_internal_reserve_minor": nca_reserve,
            "cash_disbursed_minor": 0,
        }
        self.receipts[attestation.payment_id] = result.copy()
        _audit_append(self.audit, "REFERENCE_RECEIPT_ALLOCATED", {
            "payment": attestation.payment_id, "contract": terms.contract_id,
            "distributable_minor": distributable,
        })
        return result.copy()
