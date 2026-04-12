# ⚖️ ARBITER VETO-GATE SDK v1.0
## [3-Factor Deterministic Interception SDK]

[![SQA v5](https://img.shields.io/badge/SQA-v5_Ascended-gold.svg)](docs/SQA_v5.md)
[![Type](https://img.shields.io/badge/Logic-Deterministic-orange.svg)](docs/DEFINITIONS.md)
[![Zero Dependency](https://img.shields.io/badge/Deps-Zero-brightgreen.svg)](requirements.txt)

The **Arbiter Veto-Gate SDK** is a zero-dependency Python framework providing a hybrid sync/async decorator to enforce the **Trishula 3-Factor Lock** in any quant or execution logic. It acts as the final programmatic authority, intercepting execution before probabilistic drift can manifest.

---

## █ THE 3-FACTOR LOCK
The SDK enforces deterministic agreement across three independent streams. Failure in a single stream triggers an immediate, unmaskable veto.

```mermaid
graph TD
    A[Execution Function] -- Intercepted by --> B{Veto Gate}
    B -- Structure Check --> C[Parity?]
    B -- Liquidity Check --> D[Parity?]
    B -- Sentiment Check --> E[Parity?]
    C & D & E -- AGREE --> F[AUTHORIZED: Proceed]
    C | D | E -- DISAGREE --> G[VETO: Forensic Shutdown]
```

### Factors of Sovereignty:
1.  **Structure**: Parity in technical formation (e.g., ATR/EMA alignment).
2.  **Liquidity**: Depth and spread verification for institutional execution.
3.  **Sentiment**: Institutional magnitude meeting the 0.75 threshold.

---

## █ CORE DEFINITIONS
*For a full technical glossary, see [DEFINITIONS.md](docs/DEFINITIONS.md).*

- **Veto-Gate**: A deterministic interceptor ensuring all factors are "In-Lock."
- **3-Factor Lock**: The requirement of total parity across the Triangulation Matrix.
- **Forensic Audit**: Local capture of vetoed factors for post-mission analysis.

---

## █ IMPLEMENTATION

### Zero-Dependency Install
```bash
# SQA_v5 Ascended Standard
pip install trishula-veto-sdk
```

### Institutional Usage
Enforce the 3-Factor Lock on any business logic with a single decorator.

```python
from trishula_sdk import trishula_veto_gate

@trishula_veto_gate()
async def execute_trade(pair, lot):
    # Logic only runs if Structure, Liquidity, and Sentiment agree.
    print(f"Executing strike on {pair}")
```

---

## █ REGIME WORKFLOWS
Veto-Gate-SDK utilizes the universal Trishula CI/CD suite. See [WORKFLOWS.md](docs/WORKFLOWS.md) for details.

- **Sentinel Weld**: Structural audit ensuring zero external dependencies are introduced.
- **Adversarial Crucible**: Stress-testing the decorator against disparate factor failures.

---
**PROPERTY OF TRISHULA SOFTWARE — LEVEL 5 SOVEREIGNTY ENFORCED**
