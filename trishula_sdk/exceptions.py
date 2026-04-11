"""
TRISHULA VETO-GATE EXCEPTIONS
Deterministic Fault Definitions.
"""

class TrishulaSDKException(Exception):
    """Base exception for all Trishula SDK faults."""
    pass

class TrishulaVetoTriggered(TrishulaSDKException):
    """Raised when 3-Factor parity check fails to reach 100% agreement."""
    pass

class DataDissonanceError(TrishulaSDKException):
    """Raised when underlying data integrity is compromised."""
    pass

class KineticFrictionExceeded(TrishulaSDKException):
    """Raised when execution parameters exceed determined safety limits."""
    pass
