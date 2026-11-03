"""Evidence-gated per-agent attribution of non-cash, internal NCA reserves.

Founding architect: Alexander Nikolaevich Romaskevich (RomaskevicH).
Implementation contributors: see Git history. Reference accounting only:
no legal payroll, commission award, bank receipt verification or payout.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

from .reference import (
    CityNetwork, GovernanceError, _audit_append, _require_ref,
)


@dataclass(frozen=True)
class AcceptedContribution:
    agent_id: str
    mission_id: str
    city_id: str
    weight_units: int
    qa_ref: str
    qa_reviewer_id: str
    acceptance_ref: str


class AttributionLedger:
    """Distribute a single internal agent reserve over independently accepted work.

    Production requires a durable unique constraint for both receipt and
    contributing mission IDs, finance settlement checks, legal review and
    beneficiary controls before any real-world compensation.
    """

    def __init__(self) -> None:
        self.allocations: dict[str, dict[str, Any]] = {}
        self.used_mission_ids: set[str] = set()
        self.audit: list[dict[str, Any]] = []
        self.owner_kill_switch = False

    def stop(self, *, owner_approval_ref: str) -> None:
        _require_ref(owner_approval_ref, "owner_approval_ref")
        self.owner_kill_switch = True
        _audit_append(self.audit, "ATTRIBUTION_STOPPED", {"approval": owner_approval_ref})

    def allocate(
        self,
        *,
        network: CityNetwork,
        city_id: str,
        receipt: dict[str, Any],
        contributions: Sequence[AcceptedContribution],
        owner_approval_ref: str,
    ) -> dict[str, Any]:
        if self.owner_kill_switch or network.owner_kill_switch:
            raise GovernanceError("agent attribution blocked by Owner Kill Switch")
        _require_ref(city_id, "city_id")
        _require_ref(owner_approval_ref, "owner_approval_ref")
        if city_id not in network.cities or network.cities[city_id].status != "PILOT_READY":
            raise GovernanceError("city attribution requires approved pilot city")
        if not isinstance(receipt, dict):
            raise GovernanceError("receipt must be the immutable result of the finance gate")
        receipt_id = receipt.get("payment_id")
        _require_ref(receipt_id, "payment_id")
        if receipt_id in self.allocations:
            raise GovernanceError("duplicate receipt attribution")
        if receipt.get("status") != "REFERENCE_ATTESTED_NOT_SETTLED":
            raise GovernanceError("an attested reference receipt is required")
        reserve = receipt.get("nca_internal_reserve_minor")
        if type(reserve) is not int or reserve < 0:
            raise GovernanceError("invalid internal reserve amount")
        if not contributions:
            raise GovernanceError("there is no independently accepted work")
        mission_ids: set[str] = set()
        weights: dict[str, int] = {}
        for contribution in contributions:
            if not isinstance(contribution, AcceptedContribution):
                raise GovernanceError("invalid contribution record")
            if contribution.mission_id in mission_ids or contribution.mission_id in self.used_mission_ids:
                raise GovernanceError("duplicate or previously rewarded mission")
            mission_ids.add(contribution.mission_id)
            if contribution.city_id != city_id:
                raise GovernanceError("cross-city compensation is forbidden")
            if type(contribution.weight_units) is not int or not 1 <= contribution.weight_units <= 100:
                raise GovernanceError("reviewed work weight must be integer from 1 to 100")
            mission = network.missions.get(contribution.mission_id)
            agent = network.agents.get(contribution.agent_id)
            if not mission or mission.status != "HUMAN_ACCEPTED":
                raise GovernanceError("mission lacks independent QA acceptance")
            if not agent or agent.status != "CERTIFIED_REFERENCE":
                raise GovernanceError("agent identity is not certified")
            if mission.city_id != city_id or mission.agent_id != contribution.agent_id:
                raise GovernanceError("mission and city identity mismatch")
            if (contribution.qa_ref != mission.qa_ref or
                contribution.qa_reviewer_id != mission.qa_reviewer_id or
                contribution.acceptance_ref != mission.human_approval_ref or
                contribution.qa_reviewer_id == contribution.agent_id):
                raise GovernanceError("independent QA and human approval evidence mismatch")
            weights[contribution.agent_id] = weights.get(contribution.agent_id, 0) + contribution.weight_units

        all_weights = sum(weights.values())
        names = sorted(weights)
        cents = {name: reserve * weights[name] // all_weights for name in names}
        remainder = reserve - sum(cents.values())
        # Deterministic largest-remainder apportionment; ties by agent ID.
        rank = sorted(names, key=lambda name: (
            -(reserve * weights[name] % all_weights), name
        ))
        for name in rank[:remainder]:
            cents[name] += 1
        if sum(cents.values()) != reserve:
            raise GovernanceError("non-conserving allocation")

        result: dict[str, Any] = {
            "status": "NON_CASH_INTERNAL_ATTRIBUTION_ONLY",
            "payment_id": receipt_id,
            "city_id": city_id,
            "reserve_minor": reserve,
            "agent_credits_minor": cents,
            "cash_disbursed_minor": 0,
            "owner_approval_ref": owner_approval_ref,
        }
        self.allocations[receipt_id] = result.copy()
        self.used_mission_ids.update(mission_ids)
        _audit_append(self.audit, "REFERENCE_AGENT_CREDIT", {
            "payment": receipt_id, "city": city_id,
            "agents": names, "total_minor": reserve,
        })
        return result.copy()
