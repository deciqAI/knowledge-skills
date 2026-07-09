---
name: emergence
description: "Activate when: user says 'our culture isn't working despite directives', 'the market behaves unexpectedly', 'this worked at small scale but not at large scale', 'we can't predict or control what's happening', 'designing a platform/community/open-source project'.
  Do NOT activate when: the system is simple or mechanical with few moving parts and knowable causation; the user needs a straightforward process analysis where reductionist breakdown is sufficient."
---

# Emergence

## Overview

**Emergence**: many interacting parts produce whole-level properties that cannot be predicted from the parts alone. Wetness, consciousness, market dynamics — none exist at the part level; they emerge from interaction at scale. Philip W. Anderson (Nobel 1977) formalized this in "More Is Different" (1972): reducing things to fundamental laws does not give you the ability to reconstruct the whole.

Composes with [`cynefin`](../cynefin/SKILL.md), [`feedback-loops`](../feedback-loops/SKILL.md), [`network-effects`](../network-effects/SKILL.md), [`tipping-point`](../tipping-point/SKILL.md), [`first-principles`](../first-principles/SKILL.md).

## When to Use

- Strategy in markets, cultures, ecosystems; platform / community / open-source design
- Diagnosing why a previously-working approach fails at scale
- Cultural change; codebase architecture at scale
- Reasoning about AI capex bets, AI adoption dynamics, or AI-native competition where capabilities appear unpredictably at scale

**Not when:** the system is simple or complicated with knowable causal structure.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete case → run The Process directly.
- **Coach mode:** new to framework → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: many interacting parts + no central control = emergent whole. Design seed conditions; observe; adjust. Don't predict and control.
2. Check fit: mechanical system (few parts, knowable causation)? Emergence doesn't apply.
3. Elicit: what's the system, the intervention, the outcome sought? > **[WAIT — do not advance until user responds]**
4. Diagnose: complex or complicated? What conditions and rules can you shape? What feedback loops operate? > **[WAIT — do not advance until user responds]**
5. Close: design intervention as "shape conditions and observe" + monitoring plan. > **[WAIT — do not advance until user responds]**

## The Process

**1. Identify** — system, parts count/type, central control Y/N, outcome sought.
**2. Diagnose** — simple (few parts, prediction works) / complicated (many parts, analysis works) / complex (emergent, reductionist fails) / complex-adaptive (parts adapt to system state).
**3. Structural drivers** (if complex) — feedback loops (reinforcing/balancing) | network structure | info flows | time delays | initial conditions.
**4. Design seed conditions** — initial conditions | simple local rules | feedback structures | constraints against destructive dynamics.
**5. Probe-observe-adjust** — small probes → observe what emerges → identify productive vs. unintended dynamics → adjust and re-probe.
**6. Defend against "we'll plan it"** — recognize linear cause-effect planning as reductionist relapse; pre-commit to probe-and-observe.

## Output: Emergence Analysis
```markdown
# Emergence Analysis: <system>
System: | Parts: | Central control: Y/N | Outcome:
Domain: simple/complicated/complex/complex-adaptive | Evidence:
Structural drivers: feedback loops | network | info flows | delays | initial conditions
Design: seed conditions | local rules | feedback structures | constraints
Probe plan: probes | observation metrics | adjustment criteria | iteration cycle
```

*→ Method in Action: [Anderson 1972 + Ant Colonies + Modern Business Emergence](examples/anderson-1972-ant-colonies-modern-business-emergence.md)*

*→ 2026 lens: [Emergent Capabilities in Large Language Models (2023–2026)](examples/emergent-capabilities-large-language-models-2023-2026.md)*

## Pack: Emergence Application Patterns

| System | Failed approach | Effective approach |
|---|---|---|
| Market / adoption | "Lower price → demand rises predictably" | Shape conditions; observe; iterate |
| Culture | "We declare our values" | Hire for fit; reward behavior; tell stories |
| Platform / community | "We design every interaction" | Seed conditions; adjust constraints |
| Codebase at scale | "We dictate the architecture" | Set principles; refactor as patterns emerge |

## Applying It Well

Shape conditions, rules, and feedback structures — not outcomes. The leverage point is the structure of interactions. Operate in probe-observe-adjust cycles; abandon predict-execute once you confirm complexity.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Analyze enough and I can predict it" | Complex systems resist analytical prediction. Probe and observe. |
| [D] "We can plan our culture" | You can shape conditions; culture emerges from interactions, not mandates. |
| [D] "We need more control" | More control often produces dysfunction. Loosen constraints; tighten feedback. |
| [D] "It worked at small scale, it'll scale" | Scale changes emergent dynamics. 10→100→1000 all behave differently. |
| [D] "Emergence is mystical" | It's structural — feedback loops, network topology, thresholds can be shaped. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Strategy developed as if the system were mechanical; "we can mandate this"
- Surprise at how culture / market / community has evolved
- Previously-working approach failing at scale
- Over-investing in prediction, under-investing in observation
- Command-and-control used where condition-shaping is required

## Verification

- [ ] System classified (simple / complicated / complex / complex adaptive)
- [ ] Structural drivers identified if complex (feedback, network, info flow)
- [ ] Intervention framed as "shape conditions" not "mandate outcomes"
- [ ] Probes planned with observation metrics
- [ ] Pre-committed to probe-observe-adjust, not predict-execute

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/emergence** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
