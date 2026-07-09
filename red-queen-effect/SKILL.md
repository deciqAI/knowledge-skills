---
name: red-queen-effect
description: "Activate when: user says 'we keep investing but market share won't move,' 'why does nobody make money in this industry,' 'our competitor copied us again within a year,' 'we improve but the gap stays the same,' or is evaluating whether to enter a low-margin high-activity industry. Do NOT activate when: the competitive advantage is protected by strong IP, regulatory approval, or deep network effects that genuinely slow imitation; or when the situation is pre-competitive with no direct rivals yet."
---

# Red Queen Effect

## Overview

The **Red Queen Effect**: competitors must continuously improve just to maintain relative position — because everyone else is improving simultaneously. Absolute performance rises; relative position barely shifts; cumulative effort primarily produces consumer surplus, not corporate profit. Named after Leigh Van Valen's 1973 evolutionary law and Lewis Carroll's Red Queen ("It takes all the running you can do, to keep in the same place").

Composes with [`porters-five-forces`](../porters-five-forces/SKILL.md) (diagnoses structure; Red Queen explains why strong competitors still don't earn), [`second-curve`](../second-curve/SKILL.md) (escaping the Red Queen is the primary case for a second curve), [`network-effects`](../network-effects/SKILL.md) (temporary escape until the next technology generation resets the field), and [`antifragile`](../antifragile/SKILL.md) (gaining from Red Queen stress rather than merely surviving it).

## When to Use

- Investing heavily but market share is not moving; industry growing but margins chronically thin
- Competitive gap stays constant despite continuous product improvement
- Post-mortem: advantage was copied within 12–24 months; team keeps asking "should we match them?"
- Evaluating whether to enter an industry or whether an initiative will produce durable advantage
- Escalating AI capex / compute arms race, or AI-native competition where everyone must adopt AI just to keep pace and no durable lead emerges

**Not when:** genuine structural barriers to imitation exist (IP, regulatory approvals, deep network effects); pure operational efficiency decision; pre-competitive with no direct rivals. **Stop:** once Red Queen is confirmed + escape vector identified, or NOT confirmed + durability factor named.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific competitive situation → run The Process directly.
- **Coaching mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: in a Red Queen race, all the running keeps you in the same place — run faster, change tracks, or exit?
2. Check fit: are competitors all improving simultaneously, share barely shifting, margins thin? If yes, Red Queen is active.
3. Elicit the structure: what is the key competitive investment? How long to copy a new advantage? What does the margin history look like?
> **[WAIT — do not advance until user responds]**
4. One question at a time: is copying speed accelerating? Is required investment growing? Is there any differentiation vector competitors are structurally unable to copy?
> **[WAIT — do not advance until user responds]**
5. Close: Red Queen confirmed or denied + escape vector identified + recommendation: run faster / change games / exit.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Diagnose:** primary competitive investment; imitation speed (months); margin trend 5–10 years; are all major competitors investing at roughly the same rate?

**Step 2 — Confirm Red Queen:** absolute performance improving for all (Y/N); relative share stable (Y/N); investment to maintain position growing (Y/N); margins thin despite high activity (Y/N). 3+ Y = Red Queen confirmed.

**Step 3 — Map imitation speed:** half-life of a competitive advantage; is imitation speed accelerating or decelerating?

**Step 4 — Identify escape vector:** Differentiation (competing on an axis rivals ignore) / Vertical integration (control a supply layer rivals rely on externally) / Technology generation gap (new architecture that obsoletes the current race) / Geographic avoidance (less mature markets) / Platformization (become the environment competitors run in).

**Step 5 — Calculate running cost vs. escape cost:** annual cost to maintain position; probability of winning from inside the race; cost and expected value of escape vector; race vs. escape comparison.

**Step 6 — Decide:** Run faster (only if genuine near-term winning condition) / Change tracks (escape vector identified) / Exit (unwinnable; capital better deployed elsewhere). Set timing: how long can current position be maintained while preparing escape?

## Output Template
```
Red Queen Diagnosis: <context>
Imitation speed (months): | Margin trend 5yr: | Investment escalation Y/N:
Verdict: [Red Queen Active / Partial / Not Applicable]

Escape Vector | Feasibility H/M/L | Time to implement | Advantage durability
Differentiation | | |
Vertical integration | | |
Technology leap | | |
Geographic avoidance | | |
Platformization | | |

Recommendation: [run faster / change tracks / exit] — [rationale] — Timeline:
```

*→ Method in Action: [Van Valen 1973 + Intel vs. AMD 1990–2010](examples/van-valen-1973-intel-vs-amd-1990-2010.md)*

*→ 2026 lens: [The Frontier-AI Training Race (2023–2026)](examples/frontier-ai-labs-training-race-2023-2026.md)*

## Pack: Red Queen Across Industries

| Industry | Primary arms race | Imitation speed | Escape example |
|---|---|---|---|
| Airlines | Frequent-flyer, yield management | 12–24 mo | Southwest (different segment) |
| Retail | Supply chain, loyalty | 18–36 mo | Amazon (platform + logistics) |
| Smartphones | Features, camera, processor | 12–18 mo | Apple (ecosystem lock-in) |
| Semiconductors (x86) | Process node, microarchitecture | 18–24 mo | ARM (technology generation gap) |
| Online advertising | Bidding, targeting | 3–6 mo | Google/Meta (first-party data) |

## Applying It Well

- Diagnostic question: not "are we improving?" but "are we improving *faster* than all competitors simultaneously?"
- Recognize the Red Queen early — allocate capital toward escape vectors before the sunk-cost trap takes hold.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We need to match their feature" | Entering the Red Queen — table stakes in 12 months, no durable advantage. |
| [D] "Once we win this round, we'll have a clear lead" | Winning a round means surviving to the next round at higher investment levels. No stable lead. |
| [D] "We're innovating faster than they can copy" | Temporary windows, not moats. Is your lead measured in quarters or years? |
| [D] "Our market share is stable, so we're doing well" | Stable share = running hard enough to maintain position. Check margins. |
| [D] "We just need more investment to break through" | More investment → more improvement → immediately replicated. Escalation is the Red Queen's self-reinforcing mechanism. |
| [D] "The winner of this arms race will take all" | Most Red Queen races have no winner — only survivors at higher cost. Winner-take-all requires structural network effects most industries lack. |
| [D] "We should focus on execution, not strategy" | Excellent execution in a Red Queen race produces excellent running. If the track leads nowhere, execution delays the strategic question. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Investment in competitive capabilities growing 3+ years without margin improvement
- Every advantage can be named along with the month competitors copied it
- Team is debating "whether to match" rather than "whether to change the game"
- "Staying competitive" has replaced "building advantage" as the primary strategic frame
- The company's strongest argument for continued investment is "we can't afford not to"

## Verification

- [ ] Imitation speed estimated explicitly (months); margin trend 5+ years examined
- [ ] Red Queen presence confirmed or denied against three structural criteria
- [ ] At least one escape vector evaluated for feasibility and cost
- [ ] Cost of race vs. escape vector compared; "run faster" vs. "change game" distinguished

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/red-queen-effect** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
