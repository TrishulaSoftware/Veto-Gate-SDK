"""
TRISHULA VETO-GATE SDK v1.0 — CORE
Hybrid Sync/Async Decorator & Audit Nexus.
"""

import functools
import asyncio
import logging
import datetime
from typing import Callable, Any, Union, Optional
from trishula_sdk.exceptions import TrishulaVetoTriggered

# Default Audit Logger
log_format = "%(asctime)s [TRISHULA-AUDIT] %(levelname)s — %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)
audit_logger = logging.getLogger("trishula_audit")

class VetoAuditLogger:
    """Built-in hook for recording deterministic veto events."""
    @staticmethod
    def log_veto(function_name: str, factors: dict):
        failed_factors = [k for k, v in factors.items() if not v]
        timestamp = datetime.datetime.now().isoformat()
        audit_logger.warning(
            f"VETO TRIGGERED | FN: {function_name} | FAILED: {failed_factors} | TS: {timestamp}"
        )

def trishula_veto_gate(
    get_structure: Callable[[], bool],
    get_liquidity: Callable[[], bool],
    get_sentiment: Callable[[], bool]
):
    """
    Sovereign 3-Factor Veto Gate.
    Intercepts execution unless Structure, Liquidity, and Sentiment are 100% aligned.
    Supports both synchronous and asynchronous decorated functions.
    """
    def decorator(func: Callable[..., Any]):
        
        async def async_resolver(caller: Callable):
            """Resolves callable regardless of sync/async state."""
            if asyncio.iscoroutinefunction(caller):
                return await caller()
            return caller()

        def sync_resolver(caller: Callable):
            """Standard synchronous resolver."""
            return caller()

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            factors = {
                "structure": await async_resolver(get_structure),
                "liquidity": await async_resolver(get_liquidity),
                "sentiment": await async_resolver(get_sentiment)
            }
            
            if not all(factors.values()):
                VetoAuditLogger.log_veto(func.__name__, factors)
                raise TrishulaVetoTriggered(f"Veto gate triggered. Factors: {factors}")
            
            return await func(*args, **kwargs)

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            factors = {
                "structure": sync_resolver(get_structure),
                "liquidity": sync_resolver(get_liquidity),
                "sentiment": sync_resolver(get_sentiment)
            }
            
            if not all(factors.values()):
                VetoAuditLogger.log_veto(func.__name__, factors)
                raise TrishulaVetoTriggered(f"Veto gate triggered. Factors: {factors}")
            
            return func(*args, **kwargs)

        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper

    return decorator
