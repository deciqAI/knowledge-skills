---
name: network-effects
description: "Activate when: user says 'we have network effects,' 'winner-take-most,' 'two-sided platform,' 'Metcalfe's law,' 'marketplace liquidity,' or 'the more users the better'; user is building a marketplace, social product, communication tool, or platform and needs to model when the dynamic activates; user is evaluating whether a competitor's moat claim is structural or rhetorical.
  Do NOT activate when: the product is standard B2B SaaS with no interaction between customers; the claimed 'network effect' is lower hosting cost at scale (that is a cost-side scale economy, not a value-side effect). More: deciqai.com/s/network-effects"
---

# Network Effects

## Overview

Some products get more valuable the more people use them — not because the company gets cheaper at scale, but because each user makes the product more useful to every other user. This is the **network effect**: value per user is an increasing function of total user count. Most products that claim this don't have it; they have scale economies, virality, or social proof — valuable, but structurally different. The skill diagnoses which is which, estimates the critical-mass threshold, and designs for amplification.

Composes with [`s-curve-technology-adoption`](../s-curve-technology-adoption/SKILL.md), [`pmf-crossing-the-chasm`](../pmf-crossing-the-chasm/SKILL.md), [`feedback-loops`](../feedback-loops/SKILL.md), and [`signaling-games`](../signaling-games/SKILL.md).

## When to Use

- A pitch or strategy document claims "network effects" as a moat — most don't survive scrutiny
- Building a marketplace, social product, communication tool, or platform; need to model when the dynamic activates
- Evaluating whether a competitor's network-effect claim is structural or rhetorical
- Suspecting you have scale effects but not network effects — the strategic difference is large
- Auditing an AI moat claim — CUDA/developer ecosystems, model or app marketplaces, "data flywheels," AI-capex or AI-bubble debates — where genuine network effects blur with chip-scale economies and export-control-fragmented markets

**When NOT to use:** standard B2B SaaS with no inter-customer interaction; the "effect" is lower cost at scale; single-player product with no user-generated value.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete product/case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: some products get more valuable as more people use them because users create value for each other — but most claiming this have ordinary scale or viral growth, which look similar but behave differently.
2. Check fit against When to Use / When NOT to use. If single-player, point elsewhere.
3. Elicit their real case — a specific product or strategic claim, not a hypothetical.
> **[WAIT — do not advance until user responds]**
4. Walk the diagnostic one question at a time: who interacts with whom, what is the per-user value formula, what happens at 10x users, what is the critical-mass threshold.
> **[WAIT — do not advance until user responds]**
5. Close with the verdict: "true network effects + strategic implication" or "scale/viral effects but not network effects + strategic implication."
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Network-Effect Audit**: diagnose, classify, size, design.

**Step 1 — Test.** Apply the value-per-user test: *"Does value to a typical user increase when more people use it, holding everything else constant?"* Name the specific mechanism. If you cannot name it, the product likely does not have network effects.

**Step 2 — Classify.** Direct (users interact with each other) | Indirect/two-sided (two user types create value for each other) | Data (more users → better product) | Social (status, signaling) | Platform (third-party developers/sellers) | Local (effect within a sub-population).

**Step 3 — Estimate critical-mass threshold.** Name: (a) unit of network density — global / per-city / per-company; (b) threshold count or %; (c) current position vs threshold. Below threshold → build focused density in a narrow segment first.

**Step 4 — Stress-test against 4 imposters.** Scale economies (cost-side, not value-side) | Virality/K-factor (growth without per-user value increase) | Social proof (adoption reason, not structural) | Brand (marketing scale, reversible). Name which mechanism is doing how much work.

**Step 5 — Design for amplification** (if genuine): lower cold-start barrier; create invite pressure; make the network visible; defend against multi-homing; sequence by density.

**Step 6 — Plan the defense if trailing:** differentiate the network's purpose; bundle into a different value prop; dominate a vertical where the leader is weak; or exit.

### Output

```
# Network-Effect Audit: <product>
- Value-per-user mechanism: <specific mechanism, or "no mechanism">
- Verdict: <true NE / scale economies / virality without NE / mixed>
- Primary type: <direct / indirect-two-sided / data / social / platform / local>
- Critical-mass unit + threshold + current position vs threshold
- Confusion check: scale / virality / social proof / brand — each present? how much?
- Strategy: pre-threshold (focused build) | post-threshold (amplify + multi-homing defense) | trailing (differentiate / vertical / exit)
- Falsifier: <what observation would disprove the NE diagnosis>
```

*→ Method in Action: [Theodore Vail at AT&T, 1907-1913 — and Metcalfe's Law, 1980](examples/theodore-vail-at-att-1907-1913-and-metcalfes-law-1980.md) · [The VHS vs. Betamax Format War](examples/vhs-vs-betamax-format-war.md)*
*→ 2026 lens: [Nvidia's CUDA moat and the AI ecosystem (2023–2026)](examples/nvidia-cuda-and-ai-ecosystem-2023-2026.md) — separating a real developer-platform network effect from AI-capex scale economies*

## Pack: Network-Effect Patterns

| Domain | Mechanism | Typical threshold |
|---|---|---|
| Marketplaces (eBay, Etsy) | Indirect / two-sided | 5-15% local market share |
| Social platforms (Facebook, TikTok) | Direct + social + data | "My 5 closest friends are on it" |
| Communication tools (WhatsApp, Slack) | Direct, bounded | 3-10 close contacts on platform |
| Gig economy (Uber, DoorDash) | Local indirect | ~15% local market share |
| Data NE (Google Search, Waze) | Data improving product | Years of accumulated queries |
| Developer platforms (GitHub, AWS) | Direct + data | Critical-mass of repos/community |

## Applying It Well

- Always name the specific mechanism — "users make the product better for each other *because*..."
- Model the critical-mass threshold explicitly; never assume automatic activation
- Distinguish local from global network effects before capital-allocation decisions
- Assess multi-homing risk before claiming winner-take-most dynamics

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our growth proves network effects" | Growth can come from paid acquisition or virality. The test is value-per-user-vs-n, not user count. |
| [D] "More sellers = network effect" | More sellers is the substrate. Verify buyers actually experience more value because of those sellers. |
| [D] Scale economies = network effects | Cost-side ≠ value-side. Scale economies don't produce winner-take-most and erode when competitors hit similar volume. |
| [D] Virality = network effects | K-factor > 1 produces growth; NE produces value increase with growth. Can coexist; not the same moat. |
| [D] "NE will kick in with more users" | Below critical mass, users churn before the dynamic activates. Model the threshold; build to cross it. |
| [D] Easy multi-homing + winner-take-most claimed | Winner-take-most is the equilibrium only when multi-homing is low. If users can be on both platforms, the dynamic weakens. |
| [D] Local NE treated as global | Per-company or per-city effects require winning many small networks separately, not one global win. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "Network effects" claimed without naming the specific mechanism; data shown is user growth, not value-per-user
- Two-sided marketplace with no cross-side liquidity benefit; local NE modeled as global; multi-homing ignored

## Verification

- [ ] Value-per-user mechanism named; product classified into right type; critical-mass threshold estimated with a unit
- [ ] Each of 4 imposters (scale, virality, social proof, brand) checked; local vs global NE distinguished
- [ ] Multi-homing risk assessed; falsifier named

---

*Part of **deciqAI Knowledge Skills** — 233 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/network-effects** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/network-effects.json*
