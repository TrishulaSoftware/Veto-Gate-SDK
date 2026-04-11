"""
TRISHULA VETO-GATE SDK — HYBRID DEMO
Hardening a Probabilistic Bot with Deterministic Sovereignty.
"""

import asyncio
import random
from trishula_sdk.core import trishula_veto_gate
from trishula_sdk.exceptions import TrishulaVetoTriggered

# --- 1. MOCK DATA STREAMS (THE 3 FACTORS) ---

def check_structure():
    """Mock Starfall Structural analysis."""
    val = random.choice([True, True, True, False]) # 75% bias for demo
    print(f"[AUDIT] Structure: {val}")
    return val

async def check_liquidity():
    """Mock Options Flow Liquidity analysis (Async Example)."""
    await asyncio.sleep(0.1) # Simulate network IO
    val = random.choice([True, True, False]) # 66% bias for demo
    print(f"[AUDIT] Liquidity: {val}")
    return val

def check_sentiment():
    """Mock Institutional NLP Sentiment analysis."""
    val = random.choice([True, False]) # 50% bias for demo
    print(f"[AUDIT] Sentiment: {val}")
    return val

# --- 2. THE HARDENED EXECUTION LOGIC ---

@trishula_veto_gate(
    get_structure=check_structure,
    get_liquidity=check_liquidity,
    get_sentiment=check_sentiment
)
async def strike_market(pair: str, direction: str):
    """The actual kinetic strike. Intercepted by the Veto Gate."""
    print(f"🚀 KINETIC STRIKE EXECUTED: {direction} {pair}")
    return True

@trishula_veto_gate(
    get_structure=check_structure,
    get_liquidity=check_liquidity,
    get_sentiment=check_sentiment
)
def simple_ping():
    """Synchronous ping example."""
    print("📡 SOVEREIGN PING SUCCESSFUL.")
    return True

# --- 3. EXECUTION HARNESS ---

async def main():
    print("=== TRISHULA VETO-GATE SDK DEMO START ===\n")
    
    # Test 1: Async High-Frequency Strike
    print("TEST 1: Async Kinetic Strike...")
    for i in range(3):
        try:
            print(f"-- Strike Attempt {i+1} --")
            await strike_market("EUR_USD", "BUY")
        except TrishulaVetoTriggered as e:
            print(f"❌ EXECUTION DENIED: {e}")
        print("-" * 30)

    # Test 2: Sync Sovereign Ping
    print("\nTEST 2: Sync Sovereign Ping...")
    try:
        simple_ping()
    except TrishulaVetoTriggered as e:
        print(f"❌ PING DENIED: {e}")

if __name__ == "__main__":
    asyncio.run(main())
