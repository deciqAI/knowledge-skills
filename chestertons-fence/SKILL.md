---
name: chestertons-fence
description: "Activate when: someone says 'let's just remove this', 'why do we still have this rule?', 'this seems useless/outdated', 'nobody knows why this is here', new leadership restructuring without knowing the history, a developer deleting code whose purpose isn't documented, a regulator repealing a law without tracing its origin.
  Do NOT activate when: the fence's history is fully documented and the documented purpose is confirmed obsolete (investigation already done); the reformer is the original builder and the rationale is fully understood."
---

# Chesterton's Fence

## Overview

Before removing a rule, process, code path, or institution — you must understand why it was put there. Only when you can articulate the original purpose are you qualified to decide whether it still applies. Three components: (1) "I can't see the purpose" is evidence about you, not the fence; (2) investigation is mandatory, not optional; (3) demonstrated understanding is the prerequisite for change.

Composes with [`survivorship-bias`](../survivorship-bias/SKILL.md), [`second-order-thinking`](../second-order-thinking/SKILL.md), [`feedback-loops`](../feedback-loops/SKILL.md), [`first-principles`](../first-principles/SKILL.md).

## When to Use

- A rule, process, code path, or practice is proposed for removal
- New leadership restructuring an organization with unfamiliar practices
- A developer "cleaning up" code whose purpose isn't documented
- A regulator or legislator repealing existing protections
- Someone says "why is this here?", "let's just remove this", "this seems useless"

**Not when:** fence history is fully documented and purpose is confirmed obsolete; reformer is the original builder with full rationale understood.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete fence-removal case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before removing a rule/code/process whose purpose you can't articulate, investigate — your inability to see the purpose is data about you, not the rule.
2. Check fit: if the fence's history is fully documented and the purpose is clearly obsolete, the investigation is already done.
3. Elicit the specific fence and proposed removal. What's being removed? Who proposes it? Why?
> **[WAIT — do not advance until user responds]**
4. One question at a time: when was the fence put there? by whom? what problem was it solving? does that problem still exist? are there other defenses?
> **[WAIT — do not advance until user responds]**
5. Close: investigation summary (purpose found / not found) + decision (remove / keep / modify) + documentation so the next reformer can read the history.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify:** fence (rule/code/practice/institution) | proposed change | proposer | stated reason | time pressure

**Step 2 — Investigate origin:** when put there | by whom | problem being solved | pre-fence situation | documented reason | implicit/undocumented reason. Methods: git blame, institutional memory, regulatory history, failure mode analysis.

**Step 3 — Judge current applicability:** does the original problem still exist? what changed? are there redundant fences? cost of keeping vs. cost of failure mode if removed?

**Step 4 — Decide:** Remove / Modify / Keep / Replace — with explicit reasoning.

**Step 5 — Document:** update fence docs if kept; leave a removal note + monitoring plan + rebuild criteria if removed.

### Output template
```
Fence Investigation: <fence>
Fence/proposed change/proposer/stated reason
Origin: when | by whom | problem solved | pre-fence situation
Current: original problem still exists (Y/N) | alternative defenses | cost delta
Decision: Remove/Modify/Keep/Replace — reasoning
Docs: updated fence docs / removal note / monitoring owner + rebuild criteria
```

*→ Method in Action: [Chesterton 1929 and the Modern Software / Regulatory Application](examples/chesterton-1929-and-the-modern-software-regulatory-application.md) · [The 1958 Great Sparrow Campaign](examples/1958-great-sparrow-campaign-and-the-ecological-fence.md)*

## Pack: Application Patterns by Domain

| Domain | Pattern | Investigation |
|---|---|---|
| Software code | "This null check seems unnecessary" | Git blame → original PR → bug report |
| Legacy regulations | "This 1970s rule seems outdated" | Legislative history; original committee hearings |
| Database fields | "This column isn't used, drop it" | Archival queries, regulatory compliance |
| Inherited org structure | "Fold Compliance into Legal" | Why was Compliance separated from Legal? |

## Applying It Well

- Investigate before judging — mandatory, not optional; articulate the original purpose in your own words before deciding
- When history is unrecoverable: small-scale reversible experiment with monitoring, not bulk removal

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "It's obvious why this isn't needed anymore" | If truly obvious, articulate the original purpose AND why it's obsolete. Can't articulate it? You don't know yet. |
| [D] "We've been moving too slowly" | Speed without investigation produces oscillating reform. Investigation up front is faster for durable change. |
| [D] "Nobody knows why this is here" | "Nobody knows" is the warning. The right response is investigation, not removal. |
| [D] "The history is too hard to dig up" | Then: small-scale reversible experiment with monitoring — not bulk removal. |
| [D] "Modern conditions are different" | Verify that what changed neutralizes the original purpose. "Things are different" is not investigation. |
| [D] "Trust me, I've been doing this for years" | Domain expertise doesn't substitute for investigating this specific fence's history. |
| [D] "It's just a small change" | The load the fence bears is the relevant metric, not the size of the change. |
| [D] "We can always put it back" | Reinstallation often requires consent the removal didn't, or failure compounds before you notice. |
| [D] "Chesterton's Fence is just conservatism" | Chesterton allowed removal after investigation. The principle is procedural, not substantive. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Removal proposed without investigation of the fence's history
- Proposer cannot articulate the fence's original purpose
- Proposer dismisses investigation as "slowing things down"
- Long-tenured employees / domain experts not consulted
- "Let's clean things up" initiative without case-by-case investigation

## Verification

- [ ] Fence's original purpose has been investigated
- [ ] Investigation methodology specified (git blame, institutional memory, regulatory history)
- [ ] Current applicability of the original purpose judged
- [ ] Alternative defenses identified
- [ ] Decision (remove/modify/keep/replace) documented with reasoning
- [ ] If kept: fence documentation updated for the next reformer
- [ ] If removed: note left in commit/regulation explaining the investigation
- [ ] If removed: monitoring for the failure mode established

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/chestertons-fence?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=chestertons-fence** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
