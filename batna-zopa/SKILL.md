---
name: batna-zopa
description: "Activate when: user says 'walk-away point', 'reservation price', 'should I take this deal', 'what's my leverage', 'they won't budge', or any salary/term-sheet/vendor/M&A negotiation where stakes are non-trivial. Do NOT activate when: the situation is a purely emotional relationship dispute with no transactional dimension; cultural context makes explicit BATNA discussion taboo."
---

# BATNA & ZOPA

## Overview

**BATNA** (Best Alternative to a Negotiated Agreement) is the value of your best fallback if no deal happens — the floor below which you walk away. A negotiator without a clear BATNA negotiates from fear; with one, from position.

**ZOPA** (Zone of Possible Agreement) is the overlap between what each side will accept. If it exists, a deal is possible; if not, the question is structural change — not harder negotiating.

Composes with [`anchoring`](../anchoring/SKILL.md), [`signaling-games`](../signaling-games/SKILL.md), [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md), and [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md).

## When to Use

- Any non-trivial negotiation: term sheets, salary, partnership, M&A, vendor contracts, customer pricing
- You feel pressure to take a deal that "feels bad" — usually a sign your BATNA is weak or not modeled
- Assess whether a deal *can* happen before investing time in tactics

**Not when:** purely emotional/non-transactional disputes; cultures where direct BATNA discussion is taboo.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete deal → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: BATNA = your walk-away value; ZOPA = the range where both sides say yes.
2. Check fit: relationship-only situations → point elsewhere.
3. "What negotiation are you in right now?"
> **[WAIT — do not advance until user responds]**
4. One question at a time: What's your BATNA? What's theirs? Where's the overlap?
> **[WAIT — do not advance until user responds]**
5. Name the specific opening offer and walk-away point they've identified.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Compute your BATNA:** specific alternative + dollar value + timeline + probability → risk-adjusted value. "Going elsewhere" is not a BATNA. Strengthen before negotiating (parallel processes, extended runway).

**Step 2 — Set reservation & aspiration:** Reservation > BATNA (with buffer). Opening offer > aspiration, but defensible.

**Step 3 — Estimate their BATNA:** Ask directly; research alternatives; observe behavior (patient = strong, pressured = weak). Their reservation caps your ceiling.

**Step 4 — Find the ZOPA:** Overlap of reservation prices. If none exists → structural move (add issues, extend time, find new counterparty). Not "negotiate harder."

**Step 5 — Distribute within ZOPA:** Open at your favorable boundary ([`anchoring`](../anchoring/SKILL.md)). Make small concessions — don't split. Trade variables when single-issue stalls. Walk at reservation, not earlier or later.

## Output: BATNA & ZOPA Analysis

```markdown
# BATNA & ZOPA Analysis: <deal>
## My side:  BATNA <value> | Reservation $__ | Aspiration $__ | Opening $__
## Their side: Est. BATNA <…> | Est. reservation $__
## ZOPA: $__ to $__ | Exists? yes/no
## Strategy: [if ZOPA] open at __; walk at __; concede via __
##            [if no ZOPA] structural move: __
## Falsifier: observation that would tell me my estimates are wrong: __
```

*→ Method in Action: [Fisher and Ury, 1981 — The Harvard Negotiation Project](examples/fisher-and-ury-1981-the-harvard-negotiation-project.md) · [Camp David Accords, 1978](examples/camp-david-accords-sinai-1978.md)*

## Pack: BATNA & ZOPA Patterns

| Negotiation | Your BATNA | Their BATNA |
|---|---|---|
| Term sheet | Other investors / bridge / status quo | Other pipeline deals |
| Salary | Other offers, current job, savings runway | Next candidate, leave role open |
| Vendor contract | Other vendors, build in-house, defer | Other customers, lower revenue |
| M&A | Continue independent, alternative acquirer | Build in-house, acquire competitor |

## Applying It Well

- Compute BATNA *before* any negotiation session — mid-session computation is slow and biased
- Model their BATNA with the same rigor as your own — it sets your ceiling
- Multi-issue deals: identify what each side values most and trade across variables

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "My BATNA is strong" without specifics | Where exactly, with what offer, by when? If you can't answer, BATNA is weak. |
| [D] No estimate of their BATNA | Their BATNA caps your aspiration — without it you over-ask or under-ask. |
| [D] ZOPA non-existence = "they're being difficult" | Sometimes no deal exists. Structural change, not harder negotiation. |
| [D] Splitting the difference | Signals you have room. Make small concessions instead. |
| [D] Walking at aspiration, not reservation | Walking early leaves money on the table. |
| [D] Staying past reservation (sunk costs) | Negotiation effort is irrelevant. If deal < BATNA, walk. |
| [D] Bluffing about BATNA | If discovered, credibility collapses. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "My BATNA is going elsewhere" without specifics — No estimate of their BATNA
- Pressure to close before BATNA computation is done — ZOPA not explicitly checked
- Reservation price not pre-committed before negotiating

## Verification

- [ ] BATNA: specific alternative, value, timeline, risk-adjusted
- [ ] Reservation > BATNA (with buffer); opening > aspiration
- [ ] Their BATNA estimated with reasoning; ZOPA checked
- [ ] If no ZOPA: structural move identified
- [ ] If ZOPA: opening, concession pattern, walk-point pre-committed

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/batna-zopa?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=batna-zopa** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
