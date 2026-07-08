---
name: six-thinking-hats
description: "Activate when: a meeting keeps going in circles, people have different agendas, someone says 'we need structure' or 'let's look at this from all angles,' a proposal needs evaluation from multiple sides, or creative ideas keep getting killed before development. Do NOT activate when: the question has a clear empirical answer (use critical-thinking instead), or time is under 10 minutes and no setup is possible."
---

# Six Thinking Hats

## Overview

**Six Thinking Hats** (Edward de Bono, 1985) prevents the most common meeting failure: different thinking modes colliding simultaneously. The fix is *parallel thinking* — everyone uses the same mode at the same time. Six hats: **White** (data/facts), **Red** (gut/emotions), **Black** (caution/risk), **Yellow** (optimism/value), **Green** (creativity/alternatives), **Blue** (process/meta).

ABB CEO Percy Barnevik cut 12-hour cross-cultural management meetings to under 2 hours after adoption. IBM and DuPont embedded the method in leadership development.

**Compose with neighbors:** [lateral-thinking](../lateral-thinking/SKILL.md) populates Green Hat. [critical-thinking](../critical-thinking/SKILL.md) runs inside Black Hat. [mece](../mece/SKILL.md) structures the White Hat data phase.

## When to Use

**Use when:** group decision degenerates into debate; proposal needs multi-angle evaluation; creative ideas get killed by habitual criticism; someone says *"let's look at this from all angles," "we keep going in circles," "we need structure"*; individual high-stakes decision needs forced multi-angle review.

**When NOT:** deep specialist analysis required (use hats for framing only); group too political (hat roles used as cover); time under 10 minutes; question is purely factual (run [critical-thinking](../critical-thinking/SKILL.md)).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific decision ready → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.
In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line what-it-is.** Six Thinking Hats separates discussion into six modes so everyone explores each angle *together* instead of arguing from different angles simultaneously.
2. **Check fit** — if the group is too political, question is purely factual, or time is under 10 minutes, redirect or modify.
3. **Elicit the specific decision or proposal.** "We need better meetings" is not workable; "should we launch feature X in Q3 or delay to Q4" is.
> **[WAIT — do not advance until user responds]**
4. **One hat at a time.** Walk through each hat in sequence, posing the hat's key question and waiting for input before moving to the next.
> **[WAIT — do not advance until user responds]**
5. **Close by naming which hat revealed the most unexpected insight** — the angle the team would have missed in an unstructured discussion.
> **[WAIT — do not advance until user responds]**

## The Process

Six phases → **Six Hats Analysis**. **Stop rule:** if Blue Hat close reveals no dominant direction, identify the most contested hat phase and schedule a focused session on it alone rather than forcing a decision.

1. **Blue Hat opens (5 min):** Define the question, hat sequence, time limits, and rules (no switching modes during a hat phase).
2. **White Hat — facts and data (10 min):** State known facts only. Distinguish confirmed data from soft data. List information gaps explicitly.
3. **Yellow Hat — optimism and value (8 min):** Generate specific benefits with logical basis. Run before Black to prevent habitual pessimism dominating.
4. **Black Hat — caution and risk (10 min):** Identify specific, evidence-based risks. "I don't like it" is Red Hat. "The API will fail under rate limits because X" is Black Hat. Do not abbreviate.
5. **Green Hat — creativity and alternatives (8 min):** Generate alternatives — no evaluation. Facilitator must actively block Black Hat intrusions.
6. **Red Hat — gut feeling (2 min, 30 sec per person):** One sentence per person, no justification required or permitted.
7. **Blue Hat closes (5 min):** Synthesize decision, action items, most critical Black Hat risk, most promising Green Hat direction.

### Output: Six Hats Analysis

```markdown
# Six Hats Analysis: <decision or proposal>
## Setup (Blue Hat): Question | Hat sequence
## White Hat: Confirmed facts | Information gaps
## Yellow Hat: <specific benefit — logical basis>
## Black Hat: <specific risk — logical basis> | Most critical: <...>
## Green Hat: <alternative direction>
## Red Hat: <person>: <one-sentence gut response>
## Blue Hat Close: Decision | Actions | Critical Black risk | Best Green direction
```

*→ Method in Action: [ABB Global Management Meetings (1990s)](examples/abb-global-management-meetings-1990s.md)*

## Hat Packs

| Domain | White | Black | Yellow | Green | Note |
|---|---|---|---|---|---|
| Investment | metrics/comparables | thesis risks/exit obstacles | base-case return | alternative deal structures | Red Hat critical — legitimizes gut reaction |
| Product feature | usage data/research | tech debt/adoption risk | user value/revenue | MVP alternatives | — |
| Crisis | facts only | risks first | defer Yellow | alternatives | Red Hat runs first; Blue sequence = W→B→G→Blue |

## Applying It Well

- **Blue Hat opening is the most critical 5 minutes.** Without explicit sequence, time limits, and rules, debate resumes by hat 3.
- **Black Hat is the most valuable and most compressed hat.** Resist pressure to cut it "to stay positive."
- **Run Yellow before Black** — establishes value worth protecting before naming threats.
- **Green Hat needs active protection.** One evaluative comment collapses the whole phase.
- **Red Hat is information, not complaint.** One sentence per person, no justification, no rebuttal.
- **Blue Hat close is the deliverable.** Always allocate 5 minutes regardless of time pressure.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Compressing Black Hat "to keep things positive."** | Black Hat is the session's risk register. Compressing it means deciding without the most important input. |
| [D] **Using Red Hat as an argument channel.** | Red Hat is 30 seconds, one sentence, no justification. Extended statements are Black/Yellow in disguise. |
| [D] **Fixed universal hat sequence regardless of context.** | Crisis → White-Black-Green-Blue. Strong internal advocates → Black before Yellow. Sequence must match decision type. |
| [D] **No Blue Hat close — calling the session "done."** | Without Blue Hat close, the session produced discussion, not analysis. |
| [D] **Facilitator expressing content preferences during a hat phase.** | Facilitator power is structural only. Content signals collapse the parallel thinking contract. |
| [D] **Evaluating Green Hat ideas during the Green Hat phase.** | Green Hat ideas are candidates, not proposals. One evaluative comment collapses the whole phase. |
| [D] **Only running hats natural to the team's culture.** | The method's value is forcing under-used modes. Risk-averse teams over-invest Black; innovator cultures skip it. |
| [D] **White Hat shading into interpretation.** | "Sales down 15% — clearly the product isn't working" is not White Hat. Interpretation belongs in Yellow/Black/Green. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Facilitator expressed content preferences during a hat phase
- Black Hat compressed or skipped "to keep energy positive"
- Green Hat ideas evaluated during the Green Hat phase
- No Blue Hat close — session ended without a synthesized conclusion
- Red Hat became an extended argument, not a one-sentence gut response
- Same sequence used regardless of decision type

## Verification

- [ ] Blue Hat opening: question defined, sequence set, time limits and rules stated
- [ ] White Hat: confirmed vs. soft data distinguished; information gaps listed
- [ ] Yellow Hat: logically grounded value statements (not wishful)
- [ ] Black Hat: specific evidence-based risks (not emotional objections); not abbreviated
- [ ] Green Hat: zero evaluation during the phase; alternatives captured unfiltered
- [ ] Red Hat: one sentence per person, no justification, no rebuttal
- [ ] Blue Hat close: decision or next action named; critical Black risk and best Green direction identified

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/six-thinking-hats** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
