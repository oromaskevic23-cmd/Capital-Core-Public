"""Capital Core reference engine — architectural prototype, not a deployed brokerage.

Founding architect: Alexander Nikolaevich Romaskevich (RomaskevicH).
Original implementation contributions are recorded by Git history.
Third-party rights are retained where applicable.
"""
from .attribution import AcceptedContribution, AttributionLedger
from .reference import (
    Agent, City, CityNetwork, ContractTerms, FinanceLedger,
    GovernanceError, Mission, PaymentAttestation, RevenueGateError,
    sign_attestation,
)

__all__ = [
    "Agent", "City", "CityNetwork", "ContractTerms", "FinanceLedger",
    "GovernanceError", "Mission", "PaymentAttestation", "RevenueGateError",
    "sign_attestation", "AcceptedContribution", "AttributionLedger",
]
