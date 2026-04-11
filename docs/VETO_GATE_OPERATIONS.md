# █ VETO-GATE SDK v1.0: OPERATIONS GUIDE
**DOCUMENT ID:** TRISHULA-VG-OPS-005
**VERSION:** COMMERCIAL-v1.0

---

## 1. HOW-TO: INTEGRATION

### A. Local Installation
The SDK is designed as a drop-in package.
1. `cp -r trishula_sdk /your/project/path/`
2. `from trishula_sdk.core import trishula_veto_gate`
3. `from trishula_sdk.exceptions import TrishulaVetoTriggered`

### B. Decorator Usage
Wrap your execution functions with the 3-Factor interceptor:
```python
@trishula_veto_gate(
    get_structure=my_structure_func,     # Must return bool
    get_liquidity=my_liquidity_async,    # Can be async
    get_sentiment=my_sentiment_func      # Must return bool
)
def my_trading_strike():
    # Only executes if all providers return True
    pass
```

## 2. TROUBLESHOOTING MATRIX

| Fault | Manifest | Cause | Resolution |
| :--- | :--- | :--- | :--- |
| **TrishulaVetoTriggered** | `Exception Raised` | At least one factor returned `False`. | Alignment check passed. Market conditions are not sovereign. **Do not execute.** |
| **TypeError** | `Callable not found` | The provider assigned to a factor is not a function. | Ensure you pass the function object (e.g., `func`), not the result (`func()`). |
| **Audit Silent** | `Logs empty` | Logging level not set to INFO. | Set `logging.basicConfig(level=logging.INFO)` in your host application. |

## 3. PROOF OF FUNCTION (PoF)
The following state metrics were captured during the **SQA_v5 Ascended** audit of the `quant_implementation.py` demo:

- **Scenario 1: Full Factor Alignment (1,1,1)**
  - `Inputs`: S=True, L=True, N=True
  - `Result`: **AUTHORIZED**
  - `Audit`: Function execution confirmed. 100% logic parity.
  
- **Scenario 2: Dissonant State (1,1,0)**
  - `Inputs`: S=True, L=True, N=False
  - `Result`: **VETO TRIGGERED**
  - `Log`: `VETO TRIGGERED | FN: strike_market | FAILED: ['sentiment']`
  - `Outcome`: Host application successfully intercepted. Zero market risk incurred.

## 4. MAINTAINER GATES
- **Purity**: Never add external dependencies to the `trishula_sdk` core.
- **Async**: Ensure `asyncio` loop is running if using asynchronous providers.

---
**THE SOUL IS IN THE MACHINE. PERSISTENCE IS ABSOLUTE.**
