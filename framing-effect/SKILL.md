---
name: framing-effect
description: "Activate when: user says 'how you say it matters', 'they're spinning the numbers', 'same data but sounds different', 'is this just framing?', wants to write a persuasive message, suspects a statistic is one-sided, or is evaluating options where the language feels loaded. Do NOT activate when: the different descriptions convey genuinely non-equivalent information (one frame omits real facts); the decision is trivial and multi-frame analysis exceeds the stakes."
---

# Framing Effect

## Overview

The **framing effect**: logically equivalent descriptions of the same decision produce different choices depending on whether outcomes are cast as gains or losses. Frame determines whether the brain enters gain-mode or loss-mode; the choice follows from the mode.

Three types: **risky-choice** (gain vs. loss on probabilities), **attribute** ("95% fat free" vs. "5% fat"), **goal** ("do X to gain Y" vs. "skip X, lose Y"). Real frames often compound all three.

Corrective: force both framings. If the decision is stable across frames, the frame is not driving it. If it flips, inspect why.

Composes with [`loss-aversion-prospect-theory`](../loss-aversion-prospect-theory/SKILL.md), [`anchoring`](../anchoring/SKILL.md), [`pricing-strategy`](../pricing-strategy/SKILL.md), [`signaling-games`](../signaling-games/SKILL.md), [`critical-thinking`](../critical-thinking/SKILL.md).

## When to Use

- Decision presented with strong gain-only or loss-only language
- Statistic shown in one form only (survival rate without mortality, or vice versa)
- Evaluating persuasive communication: ad, political message, medical recommendation, pitch
- Team moving toward a decision whose framing was not chosen neutrally
- You suspect manipulation by frame choice
- Framing a market or capex bet as "visionary investment" vs "bubble/overbuild" (e.g. AI capex, AI valuations, or AI-adoption spend cast as gain vs loss on identical facts)

**Not when:** the alternative frame is genuinely misleading (not logically equivalent); analysis cost exceeds decision stakes.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete framed decision → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before accepting a framed decision, restate it in the opposite frame — do you choose differently?
2. Check fit: if the alternative frame is not equivalent, single-frame may be appropriate.
3. Elicit their real case: what's being decided? What gain/loss/do/don't language is in use?
> **[WAIT — do not advance until user responds]**
4. Run the audit one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close by naming what the frame was doing and what the frame-independent choice is.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify the frame:** gain/loss/attribute/goal; verbatim language; who chose it.
**Step 2 — Construct the equivalent alternative frame:** same math, opposite wording.
**Step 3 — Re-evaluate:** does your choice change under the alternative frame? If yes, the frame is doing the work.
**Step 4 — Compute frame-independent EV:** strip the language; which option is rationally best?
**Step 5 — Diagnose framer intent:** who benefits from the framed choice? Was the frame chosen to steer?
**Step 6 — Choose response:** take framed option (if aligned with EV), take frame-independent option, or expose the frame.

## Output: Framing Audit

```
Frame in use: [type] | Verbatim: [quote] | Framer: [self/counterparty/advertiser]
Alternative frame: [restatement] | Mathematically equivalent: Y/N
Cross-frame decision: Original → [choice] | Alternative → [choice] | Stable: Y/N
EV (frame-independent): [best option + rationale]
Framer intent: [who benefits, is frame steering]
Decision taken: [choice + justification]
```

*→ Method in Action: [Tversky and Kahneman's 1981 "Asian Disease" Study](examples/tversky-and-kahnemans-1981-asian-disease-study.md)*

*→ 2026 lens: [AI Capex — "Visionary Investment" vs "Bubble Overbuild" (2024–2026)](examples/ai-capex-visionary-investment-vs-bubble-overbuild-2024-2026.md)*

## Pack: Framing Patterns

| Domain | Manipulation | Use or counter |
|---|---|---|
| Medical | "X% survive" vs "Y% die" | Demand both framings of the same data |
| Pricing | "Save $X" vs "Cost $Y" | Recognize loss-avoidance frame when buying |
| Politics | "Death tax" vs "Estate tax" | Identify framer's goal; switch frame to expose |
| Public health | Gain frame → prevention; loss frame → detection | Match frame to desired behavior type |

## Applying It Well

- Always construct the logically equivalent opposite frame before acting on any framed decision.
- The structural defense is multiple frames in the same environment — not vigilance alone.
- Match frame to behavior type: loss for detection behaviors, gain for prevention behaviors.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The numbers speak for themselves" | They don't; the frame is doing the work. Same numbers, different frame → different choices. |
| [D] "I'm not affected by framing" | Self-rated immunity has near-zero correlation with measured immunity in the literature. |
| [D] "There's only one way to describe this" | Almost never true. Any decision with gains and losses has at least one equivalent inversion. |
| [D] "Reframing is just spin" | The original frame is also spin. Calling reframing "spin" is itself a frame defense. |
| [D] "The other frame would be misleading" | Test: is it mathematically equivalent? If yes, both frames are equally accurate or misleading. |
| [D] "We just need to communicate the facts" | Words frame. There is no frame-neutral way to state most facts; choose deliberately or by default. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Decision presented with gain-only or loss-only language; no alternative frame offered
- Statistic shown in one form only; alternative form dismissed as "spin"
- Framer benefits from the choice they're steering you toward
- "We have to use this language for the audience" used to block reframing

## Verification

- [ ] Frame in use identified explicitly
- [ ] At least one logically equivalent alternative frame constructed
- [ ] Decision re-evaluated under the alternative frame
- [ ] If decision flips, dependency examined and deliberate choice made
- [ ] Framer intent considered
- [ ] If communicating, frame matched to desired behavior type

---

*Part of **deciqAI Knowledge Skills** — 223 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/framing-effect** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
