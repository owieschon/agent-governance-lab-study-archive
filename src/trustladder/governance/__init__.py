"""Deterministic governance treatment used by the public lab smoke."""

from trustladder.governance.gate import (
    ARMS,
    GateDecision,
    VerificationEvidence,
    decide,
    tree_hash,
)

__all__ = ['ARMS', 'GateDecision', 'VerificationEvidence', 'decide', 'tree_hash']
