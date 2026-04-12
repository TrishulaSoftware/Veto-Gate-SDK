# Arbiter Veto-Gate SDK: Core Definitions

This document establishes the deterministic terminology used within the Veto-Gate SDK and its parity enforcement logic.

## █ TERMINOLOGY INDEX

### 1. Veto-Gate
A **Veto-Gate** is a programmatic interceptor (implemented as a Python decorator) that validates external conditions before allowing a high-value function to execute. It acts as a logical firewall.

### 2. 3-Factor Lock
The **3-Factor Lock** is the fundamental principle of the Arbiter's authority. Execution only proceeds if there is a deterministic "YES" from three independent verification streams:
1.  **Structure**: Technical chart formations and patterns.
2.  **Liquidity**: Available depth and spread tightness.
3.  **Sentiment**: NLP conviction meeting the regime threshold.

### 3. MC/DC Alignment
**Modified Condition/Decision Coverage** alignment. In the context of the SDK, this refers to the requirement that each condition in the 3-Factor lock independently affects the outcome, ensuring no redundant or bypassed logic.

### 4. Zero-Dependency Purity
The architectural requirement that the SDK must not rely on any 3rd party libraries outside the Python Standard Library. This minimizes the attack surface and prevents supply-chain "drift."

### 5. Forensic Audit Logger
The local logging subsystem within the SDK that records the exact state of the Structural, Liquidity, and Sentiment factors at the moment of a veto. It provides the "black box" data for post-mission analysis.

### 6. Veto Trigger (`TrishulaVetoTriggered`)
The unmaskable exception raised by the SDK when any of the 3 factors fail to reach parity. This exception cannot be silently caught within the regime's standard execution flow.

---
**PROPERTY OF TRISHULA SOFTWARE — LEVEL 5 SOVEREIGNTY ENFORCED**
