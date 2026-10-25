---
name: ai-output-verification-trust-tiers
description: "Activate when: user says 'can we use the AI's output directly?', 'what needs human review and what doesn't?', 'how do we verify AI output?', 'the AI made up data again', or needs review rules for AI outputs, or is deciding where an agent may act automatically and where a human must sign off.
  Do NOT activate when: the output is a personal draft that never leaves the user's hands and is never booked or sent; a regulator already mandates a fixed review procedure for this output; redoing a wrong output costs nothing; the task is brand voice and fact-base design for high-volume content (use ai-content-factory-brand-consistency). More: deciqai.com/s/ai-output-verification-trust-tiers"
---

# AI Output Verification Trust Tiers


## Overview

Teams usually make one of two mistakes with AI output. They trust all of it — and fabricated figures, citations or terms reach a client — or they review all of it, and the AI saves no time. Both are wrong, and the second quietly becomes the first: reviewers who check everything start approving without checking.

The core mechanism: **tier every type of output by error cost × verifiability → give each tier a verification method and an evidence requirement → set escalation rules → move tiers up or down based on spot-check results.** Trust is set by what an error costs, not by how good the model usually is.

Compose with [checklist](../checklist/SKILL.md) (a verification checklist per tier) · [margin-of-safety](../margin-of-safety/SKILL.md) (extra margin on high-cost outputs) · [agent-ops-monitoring](../agent-ops-monitoring/SKILL.md) (spot-checks and metrics in production) · [ai-content-factory-brand-consistency](../ai-content-factory-brand-consistency/SKILL.md) (the same gates applied to content at volume).

## When to Use

- AI output will be sent to a client, booked into the ledger, used to execute a payment or order, or will cite data or regulation
- Designing the boundary of what an agent may execute on its own
- Rebuilding the rules after an AI fabrication or error got through

**When NOT to use:** personal brainstorming drafts · a mandatory fixed review procedure already applies · a wrong output can be redone at zero cost.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user lists concrete output types → run The Process directly.
- **Coach mode:** user is unfamiliar → guide one step at a time.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is:** "Trust isn't all-or-nothing. The more an error costs, and the harder it is to check yourself, the more the output needs a human and evidence."
2. **Check fit:** "Does the AI's output leave your hands — sent out, booked, or used to take an action?"
3. **Elicit the real case:** "List 3–5 kinds of things the AI produces for you, and what happens if each one is wrong."
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "Let's place each one in the tier matrix — error cost on one axis, verifiability on the other."
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "Which outputs you can let run automatically, and which must carry evidence and a human signature."
> **[WAIT — do not advance until user responds]**

## The Process

**Output:** Trust Tier Table

1. **List output types.** By use: client emails, quotes, data summaries, code, citations, payment instructions, and so on. *Gate: a vague type ("the AI's answers") → split it → stop.*
2. **Score two dimensions.** Error cost (low / medium / high: money, compliance, client relationship, irreversibility) · verifiability (can it be checked quickly against a rule, a source document, or a calculation?).
3. **Assign the tier.**
   - **T1 Automatic:** low cost + easy to verify → rule-checked, then released; periodic spot-checks
   - **T2 Sampled:** medium cost, or verification needs a human → a fixed share sampled for human review
   - **T3 Mandatory review:** high cost → every item reviewed by a human before release
   - **T4 No automation:** high cost + irreversible (payments, signing, external commitments) → AI drafts only; a human executes
   *Gate: an irreversible action placed in T1 or T2 → stop and re-tier.*
4. **Attach verification methods.** Source check (every citation must open to the original) · rule / format validation · recalculation · cross-model or regenerate-and-compare · human spot-check. *Gate: T3 or T4 with no evidence requirement → stop.*
5. **Set the evidence requirement.** Facts, numbers and citations carry a source link or source-document location. **No source = unverified.**
6. **Set escalation.** Low confidence, amount over threshold, new output type, client complaint, or anyone disputing the output → move up a tier or route to a human; name the reviewer.
7. **Re-tier with data.** Move tiers up or down on spot-check error rates; moving down requires several consecutive periods meeting the bar.
8. **Stop-rule:** every output stays internal and can be redone at zero cost → collapse to T1 plus spot-checks.

**Output template:**
`output type | error cost | verifiability | tier | verification method | evidence requirement | escalation trigger + reviewer | spot-check rate`

*→ Method in Action: [Mata v. Avianca — the fabricated citations (2023)](examples/mata-v-avianca-fabricated-citations-2023.md)*

## Applying It Well

1. **Tier by error cost, not by the model's usual performance.** Average accuracy says nothing about this item.
2. **Agreement is not correctness.** Two models — or the same model asked twice — can agree on the same fabrication; facts are checked against the source.
3. **Reviewers check evidence, not prose.** Re-reading for flow is not verification.
4. **Watch for automation bias.** Over time, reviewers default to "approve"; measure it.
5. **A challenge is an escalation trigger.** When anyone questions an output, it moves up a tier immediately.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "This model is very accurate; no review needed" | Average accuracy does not make this item accurate. The tier follows the error cost. |
| [D] "A human looked at it" | Looked at ≠ checked. Without an evidence check it was not reviewed. |
| [D] "Review everything — that's safest" | Reviewing everything breeds fatigue and rubber-stamping, and the high-risk items slip through. |
| [D] "Have another model check it" | Models can make the same error; facts need a source check. |
| [D] "I asked the AI whether it was sure, and it said yes" | Self-confirmation is not verification. The model's confidence is not evidence. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Numbers and citations with no source · payments or external commitments the AI can execute directly
- Review approval rate near 100% with very short review times · tiers never adjusted · a challenged output left at its original tier

## Verification

- [ ] Every output type tiered on both dimensions
- [ ] Every irreversible action is T4
- [ ] T3 and above have evidence requirements
- [ ] Escalation triggers and reviewers written down
- [ ] Spot-check rates set, with a re-tiering log

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ai-output-verification-trust-tiers** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ai-output-verification-trust-tiers.json*
