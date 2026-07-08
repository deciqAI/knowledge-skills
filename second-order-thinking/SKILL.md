---
name: second-order-thinking
description: "Activate when: user says 'and then what?', 'what are the second-order effects?', 'what could go wrong downstream?', 'what happens once everyone does this?', or brings a decision where the immediate effect is clear but downstream effects are not, or says 'everyone agrees this is good.' Do NOT activate when: the decision is genuinely low-stakes and reversible (e.g., a variable rename), or the user lacks a causal model and needs to build understanding first before tracing consequences."
---

# Second-Order Thinking

## Overview

First-level thinking asks "what will happen?" and stops. Second-order thinking asks "...and then what? and then what?" — tracing the chain of consequences past the immediate effect to the ones that aren't obvious, especially the ones that **reverse** the first effect once other people and the system respond.

This is the third motion in the collection, distinct from its neighbors: [first-principles](../first-principles/SKILL.md) decomposes *downward* to bedrock; [occams-razor](../occams-razor/SKILL.md) chooses *sideways* among competing explanations; second-order thinking traces *forward* through time and consequence. They compose — reduce to find the foundations, choose the simplest explanation that fits, then trace where the decision actually leads.

## When to Use

Apply when: immediate effect is obvious but downstream effects are not; "everyone agrees" (is it priced in?); other actors will respond or feedback loops exist; someone asks "and then what?" / "what are the second-order effects?" / "what could go wrong downstream?"

**When NOT to use:** genuinely low-stakes reversible decisions; you lack a causal model (build it first); the chain would be pure speculation with no grounding.

## Coaching Novices (Adaptive Front Door)

Before running the Process, read the user. This skill has two delivery modes — pick one, don't default to dumping a finished cascade.

- **Engine mode (do-it-for-me):** the user brought a concrete decision and wants the answer → run the full Consequence Cascade directly and concisely. Don't slow an expert down with questions they didn't ask for.
- **Coach mode (teach-me):** the user gave no concrete decision, or signals unfamiliarity ("what is this / how do I use it / does it apply to me?") → guide, don't analyze at them.

When unsure which they want, ask one line first: *"Want me to just run this on a specific decision, or walk you through it step by step?"*

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output that step's question and nothing more.

In coach mode:

1. **One-line what-it-is.** Say what second-order thinking buys them, in plain words (≤2 sentences, no jargon): most people stop at "what happens?"; this asks "...and then what?" to catch the effect that *reverses* the obvious one.
2. **Check fit.** Match their situation against *When to Use* / *When NOT to use*. If it doesn't fit, say so and point elsewhere — don't force the framework onto a first-order, low-stakes call.
3. **Elicit their real decision.** If they have no concrete case, ask for one. Never run the cascade on a hypothetical when a real one is available.

> **[WAIT — do not advance until user responds]**

4. **One order at a time.** Walk the Process one step per turn: pose this step's question, wait for their answer, then advance using *their* input. Surface what they missed as you go — never dump all orders at once.

> **[WAIT — do not advance until user responds]**

5. **Close by naming the payoff.** End with the one reversal or non-consensus insight *they* uncovered, so they remember the move, not just the answer.

> **[WAIT — do not advance until user responds]**

Then enter The Process below at the depth the chosen mode calls for.

## The Process

Run the **Consequence Cascade**. Trace forward, sweep all groups, and hunt reversals.

1. **State the decision and its first-order effect.** Write the action and the obvious immediate consequence — what first-level thinking concludes and what the consensus believes.
2. **Ask "and then what?" (second order).** How do the affected parties and the system respond to that first-order effect? Critically: **what does everyone else do once they see the same obvious thing?** If the answer is "they all act on it," the obvious play may already be priced in (Marks).
3. **Continue to third+ order.** Keep asking "and then what?" until the effects become negligible or too uncertain to ground. **Note the order at which you stop, and why.**
4. **Sweep all groups, and later in time (Hazlitt).** Trace effects not only on the target group and not only now — on every affected group and over the long run. The fallacy is seeing the immediate effect on one group and stopping.
5. **Reversal check — the payoff.** Flag any order where an effect **reverses the sign** of an earlier one: helps now, hurts later; protects one group, harms it via the system's response. Reversals are where second-order thinking earns its cost (subsidies that raise prices, safety features that increase risk-taking, an optimization that just moves the bottleneck).
6. **Consensus vs. non-consensus (Marks).** Is your conclusion different from the first-level take *and* better-reasoned? If it matches consensus, say why you still hold it (consensus is sometimes right). If it differs, name the second-order insight the crowd is missing. Different-and-wrong is worse than consensus.
7. **Stop-rule and humility.** State where you stopped and how confidence decays with each hop. Never present a speculative 5th-order chain as a prediction.

### Output: the Consequence Cascade

```
First-order:    <obvious/consensus effect>
Second-order:   <system/actor response to first-order>
Third+ order:   <continue until negligible or ungroundable — state stop-point>
All-groups:     <effects on every group and later in time, not just the target>
Reversals:      <orders where a later effect flips the sign of an earlier one> ← the payoff
Consensus check:<differs from first-level view? name the insight the crowd misses, or why it still holds>
Confidence:     <where tracing turned to speculation; decay by hop>
```

*→ Method in Action: [US Prohibition (1920–1933)](examples/us-prohibition-1920.md) · [The Hanoi Rat Bounty (1902)](examples/hanoi-rat-bounty-1902.md)*

## Cascade Packs

The Consequence Cascade runs the same way everywhere, but actors, equilibrium mechanisms, and stop-rules differ by domain. In **policy/regulation**: actors are affected publics, regulated industries, black markets, and coalitions. In **product/feature work**: users, competitors, partners, and the platform. In **investing**: the central question is "what is priced in." A cascade pack captures (a) dominant actors and feedback loops, (b) typical reversal patterns, and (c) the domain-specific stop-rule. **Adding a cascade pack for your domain is the easiest way to contribute** — see the template at the repo root.

## Applying It Well

- **First-order is free; the premium is downstream.** Your value starts at "and then what?"
- **The obvious is priced in.** The edge is in what happens *after* everyone acts on the same obvious conclusion.
- **Reversals are the jackpot.** Hunt sign-flips explicitly — that's where the most expensive misses and best opportunities live.
- **Know when to stop.** A grounded third-order beats a speculative sixth-order. State where confidence runs out.
- **Always trace the equilibrium response** — not just "what does this do?" but "what does this do once everyone adjusts?"

*→ Sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**Note — [D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The effect is obvious, so we're done" | That's first-level thinking. If it's obvious to you, it's obvious to everyone and likely priced in (Marks). The value lives at order 2+. |
| [D] Tracing one group's effects, ignoring the rest | Hazlitt's fallacy: secondary consequences fall on all groups, not just the target — and later, not just now. Sweep all of them. |
| [D] Stopping at the first "and then what?" | Second-order is not one step past first; keep tracing until effects are negligible or ungroundable. |
| [D] A long, confident, speculative chain | Each hop loses confidence. An ungrounded sixth-order link is storytelling dressed as rigor. State where you stop and why. |
| [D] Missing the reversal | The costliest misses are where a later effect flips an earlier one. If you didn't look for sign-flips, you didn't do the work. |
| [D] "It's non-consensus, so I'm right" / "it's consensus, so I'm right" | The goal is non-consensus *and* correct (Marks). Different-and-wrong is worse than agreeing with the crowd. Consensus is the prior, not the enemy. |
| [D] **Tracing effects without naming the actor** who causes them | Cascades do not propagate by magic. Each hop is *some specific actor* responding to incentives — a regulator, a competitor, a class of users. If you cannot name who acts and why, you are writing fiction, not tracing a chain. |
| [D] Conflating **possibility with prediction** | "This *could* happen" is not "this is what's most likely." Multiple second-order effects exist; you must weight them by which actor has the strongest incentive and which feedback loop has the shortest delay. |
| [D] Treating all reversals as equally important | Finding a reversal does not finish the work. The question is whether it is **load-bearing** at the size and time-scale that matters. Many micro-reversals exist and do not change the verdict; do not decorate. |
| *To add [O] entries: paste a real failure instance here after each production use* | *Description of what happened* |

## Red Flags / Verification

**Red flags:** analysis stops at first-order; only the target group's effects considered; long chain with no confidence decay or stop-point named; no reversal check; conclusion identical to obvious first-level take with no pricing-in check; speculative Nth-order presented as prediction.

**Checklist:**
- [ ] First-order effect (consensus view) stated explicitly
- [ ] Second-order traced including how other actors respond
- [ ] All affected groups swept, and later-in-time effects
- [ ] Reversal check done; sign-flips flagged
- [ ] Stop-point named with confidence decay
- [ ] Conclusion positioned against first-level consensus

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/second-order-thinking** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*