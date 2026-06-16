---
name: signaling-games
description: "Activate when: user asks 'how do we prove we're high quality when they can't verify it', 'what credential or signal would work here', 'why is everyone spending so much on brand advertising', 'how do we tell who's the real one among these candidates', 'cheap talk isn't working — we need something credible', or describes a market where one side can't verify the other's quality/intentions/type (hiring, fundraising, B2B procurement, branding, M&A due diligence).
  Do NOT activate when: information is fully symmetric and both parties already know the relevant facts; or the question is about game theory in general without an information asymmetry component."
---

# Signaling Games

## Overview

One party knows something the other cannot verify. **Cheap talk fails** — anyone can claim high quality. A signal works when its cost differs by type: only a capable worker can bear four years of demanding study; only a quality manufacturer can afford a lifetime warranty. The signal conveys truth *exactly when it would be unbearable for the wrong type to fake it*. Spence (1973) formalized this; Akerlof (1970) showed what happens when no signal exists (lemons).

Composes with [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md), [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md), and [`pricing-strategy`](../pricing-strategy/SKILL.md).

## When to Use

Apply when:
- One party **cannot verify** what the other knows — hiring, fundraising, M&A, B2B, branding, diplomacy
- A market is **failing to price quality correctly** (Akerlof lemons problem) and you need a fix
- You're **designing a credential, certification, warranty, or brand investment**
- You're trying to **break into a market** with a signal competitors can't cheaply imitate
- You need to **detect** real quality among multiple claimants

**When NOT to use:** information is symmetric; signal cost is the same for both types (expense, not signal); one-shot low-stakes interaction where direct verification is cheap.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is (≤2 sentences): when one side knows something the other can't verify, anyone can claim it — so only actions **too expensive for the wrong type to fake** actually communicate truth.
2. Check fit against When to Use / When NOT to use. If symmetric info, point elsewhere.
3. Elicit their real case (hiring, branding, fundraising, partnership — never run on hypotheticals).
> **[WAIT — do not advance until user responds]**
4. Walk The Process one step per turn — what's asymmetric, candidate signals, single-crossing test, equilibrium.
> **[WAIT — do not advance until user responds]**
5. Close by naming the one signal that fits their situation and what makes it credible.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Signaling Diagnosis**:

1. **Asymmetry.** Who knows what the other can't verify? Be specific — not "they don't know us" but "they can't verify whether our team ships in 18 months."
2. **Types.** Name the hidden attribute: high-productivity vs low-productivity; going-concern vs flash-in-the-pan.
3. **Adverse selection.** Without a signal, the receiver prices the average — subsidizing low types, underpaying high types (Akerlof 1970).
4. **Enumerate candidate signals.** Credentials, brand spend, warranty, equity vesting, personal capital in round, third-party cert, public commitment, hostage/collateral.
5. **Test single-crossing.** Is cost *meaningfully lower* for the high type? If the low type can imitate at similar cost, the signal pools and conveys nothing.
6. **Determine equilibrium.** Separating (high sends, low doesn't), pooling (all same, no info), or hybrid.
7. **Check receiver response.** Does the receiver reward signal-holders enough to sustain sender investment? If not, the equilibrium unravels.
8. **Watch for signal inflation.** Signals erode as imitation costs fall. Plan re-investment or move up the cost ladder.
9. **As receiver, decode carefully.** What cost did the sender actually bear? Fake signals (imitations the low type *could* afford) and misread signals (family money, not investor conviction) are the main traps.
10. **Stop-rule.** Cost differential must be substantial and sustained — marginal differentials collapse.

### Output: Signaling Diagnosis

```
# Signaling Diagnosis: <situation>
## Asymmetry: what hidden | who knows | who doesn't
## Types: high type | low type
## Adverse selection: what happens without a signal
## Candidate signals: <signal>: passes/fails single-crossing because <…>
## Recommended signal: <which + cost differential high vs low>
## Equilibrium: separating / pooling / hybrid
## Receiver response: does receiver reward signal-holders?
## Inflation risk: half-life + re-investment plan
## Decoding: what cost is sender actually bearing? failure mode?
```

*→ Method in Action: [Michael Spence, "Job Market Signaling," 1973](examples/michael-spence-job-market-signaling-1973.md)*

## Pack: Common Signaling Mechanisms

- **Hiring:** credential/audition signals cognitive type; cost lower for capable workers; failure = credential inflation
- **B2B sales:** named logos + audited financials signal reliability; only real customers sustain it; failure = logo gaming
- **Fundraising:** founder personal capital signals conviction; only true believers risk ruin; failure = pedigree-shopping
- **Brand:** sustained ad spend signals longevity; quality firms amortize on repeat sales; failure = ad spend pools
- **Diplomacy:** troop deployments + ratified treaties signal commitment; only committed states bear cost; failure = brinkmanship read as bluff

*→ Primary sources: [references/sources.md](references/sources.md)*

> Applying it well: imitation must be **unbearable** for the low type. Absence of a signal is itself a signal. Concentrate on 1–2 signals with substantial, sustained differentials.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We told them, and they should believe us" | Cheap talk fails by construction — anyone can claim high quality. Find an action whose cost differs by type. |
| [D] "Brand investment is too expensive, let's cut it" | The cost *is* the signal. Cutting destroys credibility. Plan what replaces it or you have un-signaled. |
| [D] "Cheap signals work too" | Cheap signals collapse to pool. If anyone can do it, its presence is uninformative. |
| [D] Designing a signal without testing single-crossing | The one test: is cost meaningfully lower for the type you want to signal? Without this, it's a marketing expense. |
| [D] "Everyone has this credential — it's the new baseline" | When everyone has it, it has pooled. The strategic move is to invest in the *next* signal up the cost ladder. |
| [D] Receiving a signal at face value | Decompose the signal; check the actual cost the sender bore. "Ex-Famous-Company" can be heavy or light. |
| [D] Treating signaling and substantive performance as substitutes | Signals clear the asymmetry barrier; underlying quality still has to be there. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Signal costs the same for both types — cheap talk in signal costume
- Receiver not rewarding signal-holders — equilibrium will not hold
- Treating a pooled signal (everyone has it) as informative
- No plan for signal credibility as imitation costs fall
- Reading a signal without examining the actual cost the sender bore

## Verification

- [ ] Asymmetry precisely specified — what hidden, who knows, who doesn't
- [ ] Type concretely defined (not "quality in general"); adverse selection named
- [ ] Candidate signals tested against single-crossing — cost differential quantified
- [ ] Equilibrium type identified; receiver response confirmed adequate
- [ ] Signal-inflation risk acknowledged with re-investment plan
- [ ] When reading a signal, actual sender cost was examined

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/signaling-games?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=signaling-games** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
