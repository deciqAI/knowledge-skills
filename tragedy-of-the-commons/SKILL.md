---
name: tragedy-of-the-commons
description: >
  Activate when: shared resource is degrading even though no one is doing anything "wrong"; team complains about free riders or overuse; designing API quotas, rate limits, or open-source governance; someone says "everyone is overusing this" or "the system worked fine until it got popular"; evaluating why a platform or community is burning out.
  Do NOT activate when: the resource is fully non-rival (unlimited supply, zero marginal cost); the problem is a purely individual-action issue with no shared resource.
---

# Tragedy of the Commons

## Overview

When a shared resource has individual access but no individual responsibility for preservation, rational users extract private benefit while the cost of overuse is shared — leading to collective degradation. Garrett Hardin named this in 1968; Elinor Ostrom corrected it in 1990 (Nobel 2009): many communities self-govern commons via her 8 design principles without privatization or coercion.

Composes with [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md), [`principal-agent`](../principal-agent/SKILL.md), [`network-effects`](../network-effects/SKILL.md), [`goodharts-law`](../goodharts-law/SKILL.md), [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md).

## When to Use

- Diagnosing why a shared resource is degrading (open-source burnout, API abuse, attention market polarizing)
- Assessing AI-era shared-resource strain from AI capex and AI-native competition (open web scraped for training data, grid/power capacity, GPU allocation)
- Designing platforms, marketplaces, shared infrastructure, API quotas, or rate limits
- Designing workplace norms around shared resources (meetings, Slack, email)
- Evaluating regulatory or policy responses to shared-resource problems

**Not when:** resource is genuinely non-rival; fully private; "commons" framing is misapplied to individual-action problems.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete commons case → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: when a shared resource degrades despite each user acting rationally, you have a commons problem — the answer is institutional design per Ostrom's 8 principles, not just "privatize" or "regulate."
2. Check fit: shared resource + individual extraction + shared cost? If not, different frameworks apply.
3. Elicit the resource, users, and current rules: What's shared? Who has access? What rules govern use? What's failing?
> **[WAIT — do not advance until user responds]**
4. Audit which of Ostrom's 8 principles are present / weak / absent in their situation.
> **[WAIT — do not advance until user responds]**
5. Close: name the institutional gaps + propose design applying missing principles + monitoring plan.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify:** shared resource · user community · failure mode · current rules.
**Step 2 — Verify commons structure:** shared access + rivalrous + diffuse responsibility + Hardin pattern (individually rational, collectively destructive). All four yes → commons.
**Step 3 — Ostrom audit** (mark present / weak / absent): 1 Boundaries · 2 Congruence · 3 Collective-choice · 4 Monitoring · 5 Graduated sanctions · 6 Conflict resolution · 7 Right to organize · 8 Nested enterprises. Weak/absent = design targets.
**Step 4 — Intervene:** for each weak/absent principle, design a specific fix. Avoid the "privatize or regulate" binary — Ostrom's institutional design often outperforms both.
**Step 5 — Monitor:** sequence · metrics (resource health, sanctions issued) · quarterly review.

## Output Template
```
Commons Design: <resource>
Structure: shared resource | boundaries | failure mode | current rules
Verification: shared Y/N · rivalrous Y/N · diffuse responsibility Y/N · Hardin pattern Y/N
Ostrom audit: [1–8: present/weak/absent]
Intervention: [per weak/absent principle] · why not privatize · why not pure regulation
Implementation: sequence · metrics · review cycle
```

*→ Method in Action: [Hardin 1968 + Ostrom's Empirical Correction + Modern Digital Applications](examples/hardin-1968-ostrom-empirical-correction-modern-digital-applications.md) · [Grand Banks Cod Collapse](examples/grand-banks-cod-collapse-and-1992-moratorium.md)*
*→ 2026 lens: [The AI-Era Commons — Open Web, Power, and GPUs (2024–2026)](examples/ai-era-commons-open-web-power-gpus-2024-2026.md)*

## Pack: Commons Patterns

| Commons | Failure mode | Ostrom countermeasure |
|---|---|---|
| Open-source project | Maintainer burnout | Contribution rules; governance council; sustaining funding |
| API / cloud infrastructure | Abuse degrades service for all | Tiered quotas; monitoring; graduated sanctions |
| Slack / meetings | Notification overload | Norms; meeting-free blocks; signal-noise metrics |
| Fisheries / antibiotic efficacy | Stock collapse / resistance | Quotas; stewardship programs; surveillance |
| Atmospheric carbon | Climate change | Carbon pricing; international agreements; local action |

## Applying It Well

- Ostrom's 8 principles are load-bearing, not optional: missing several reliably produces Hardin tragedy.
- Privatization works when exclusion is feasible and transaction costs are low. Regulation works when the regulator has information and legitimacy. Ostrom's self-governance works when users can communicate, monitor, and self-organize — often best for technical commons.
- Peer monitoring (users see each other's behavior) differs from punitive surveillance; successful commons use the former.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Commons always fail; we have to privatize" | Hardin over-stated this. Ostrom's empirical evidence: many commons endure for centuries with the 8 principles. |
| [D] "The government must regulate" | Sometimes. Often community self-governance is faster, cheaper, and more legitimate. |
| [D] "Punish free riders; that's enough" | Graduated sanctions is one of 8 principles. Punishment alone without monitoring, boundaries, etc. doesn't work. |
| [D] "Open source means free; we don't owe anything" | Maintainer labor is a commons; without contribution mechanisms it depletes (xz 2024 was the warning). |
| [D] "Our users would never abuse the API" | The Hardin structure predicts abuse from a substantial fraction regardless of intent. Design accordingly. |
| [D] "We don't need formal governance; people are reasonable" | Even reasonable people benefit from boundaries, monitoring, and conflict resolution. |
| [D] "Monitoring is surveillance; we don't do that" | Ostrom distinguishes cooperative peer-monitoring from punitive surveillance. Successful commons use the former. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Shared resource degrading; rules unclear or unenforced
- Free-rider complaints but no graduated sanctions exist
- Users have no voice in rule-setting (Ostrom principle 3 absent)
- Default response is "regulate it" or "privatize it" without considering institutional design

## Verification

- [ ] Shared resource and user boundaries specified
- [ ] Commons structure verified (shared + rivalrous + diffuse responsibility)
- [ ] Ostrom's 8 principles audited; weak/absent identified
- [ ] Institutional intervention designed; privatize-or-regulate alternatives addressed
- [ ] Monitoring metrics and review cycle scheduled

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/tragedy-of-the-commons** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
