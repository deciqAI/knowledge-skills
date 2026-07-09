---
name: herzberg-two-factor
description: "Activate when: someone says 'why isn't the team motivated,' 'we raised salaries but morale didn't improve,' 'people keep leaving for better opportunities,' 'employee engagement is low,' 'how do I retain engineers,' or when designing compensation, job roles, or performance systems.
  Do NOT activate when: the problem is a skill gap (people lack capability, not motivation); or the worker is in extreme economic precarity where basic survival income is the issue."
---

# Herzberg Two-Factor Theory

## Overview

Herzberg's 1959 Pittsburgh study found satisfaction and dissatisfaction are **two independent axes**. **Hygiene factors** (salary, working conditions, job security) only remove dissatisfaction — never create motivation. **Motivators** (achievement, recognition, responsibility, growth, the work itself) create genuine engagement. More hygiene spending never produces motivation; only **job enrichment** — redesigning work for higher responsibility and autonomy — does.

**Composition with neighbors:** Use [principal-agent](../principal-agent/SKILL.md) when incentive structures keep failing (designers mistake hygiene for motivators). Use [nudge-theory](../nudge-theory/SKILL.md) after Herzberg to design low-friction paths to the motivating actions identified.

## When to Use

- Team shows **adequate performance but low energy** — people meet the minimum but go no further
- Talent **leaving for "better opportunities"** and exit interviews are uninformative
- **Compensation recently increased** but morale didn't improve, or reset within months
- **Designing** compensation structure, job role, or performance review system
- **Bidding wars for scarce AI/ML talent** — matched counter-offers still lose people; AI-capex-driven pay bands keep rising but engagement doesn't follow (an AI-native competitor is out-motivating, not just out-paying, you)
- Someone says: *"motivation," "engagement," "retention," "why isn't the team energized"*

**When NOT to use:** Clear hygiene gap exists (salary below market, unsafe conditions) — fix those first. Skill gap, not motivation gap. Very short time horizon (72-hour sprint).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** specific team/role described → run The Process directly.
- **Coach mode:** unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: salary/benefits can only *remove unhappiness* — only challenging work, real responsibility, and recognition for achievement create genuine motivation.
2. Check fit against When to Use / When NOT to use. If clear hygiene gap exists, redirect to fixing hygiene first.
3. Elicit their real case — "people aren't motivated" is not a case; get the specific behavioral signal.
> **[WAIT — do not advance until user responds]**
4. Classify each complaint/satisfaction item as hygiene or motivator one at a time before prescribing.
> **[WAIT — do not advance until user responds]**
5. Close: "The reason raising salary didn't fix this is ___. The one motivator intervention most likely to move engagement here is ___."
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Two-Factor Diagnosis**. **Stop-rule:** if Step 2 reveals clear hygiene gaps (pay below market, unsafe environment), stop and address those before any motivator work.

1. **Collect complaint/satisfaction inventory** via exit interviews, stay interviews, 1:1s, or surveys — specific behavioral events, not abstract ratings.
2. **Classify each item:** Hygiene (context of work: salary, benefits, security, working conditions, policy, supervision, peer relationships) vs. Motivator (content of work: achievement, recognition for achievement, work itself, responsibility/autonomy, growth/advancement). Classification test: if removing it causes active unhappiness but adding more habituates quickly → hygiene.
3. **Assess hygiene baseline** vs. market standard. Set a "hygiene floor" — the threshold where it no longer drives active dissatisfaction. Prioritize: salary → job security → working conditions → interpersonal environment.
4. **Diagnose motivator gaps** across five core motivators: Achievement (challenging, completable goals?), Recognition (specific, prompt, tied to achievement?), Work itself (varied, challenging?), Responsibility (real ownership?), Growth (visible path forward?).
5. **Design job enrichment (vertical loading):** remove procedural controls while keeping accountability; give direct feedback from the work; assign whole units of work; add direct client/user contact; increase technical scope. Not horizontal loading (more same-type tasks).
6. **Monitor and iterate** quarterly — hygiene satisfaction habituates in weeks; motivator satisfaction is durable but evolves as people grow.

### Output: Two-Factor Diagnosis

```
# Two-Factor Diagnosis: <team / role>
Hygiene floor status: <below / at / above floor> | Required fixes: <>
| Hygiene Factor | Current | Market std | Gap | Priority |
| Motivator | Signal (strong/weak/absent) | Evidence |
Primary motivator gap: <>
| Enrichment Intervention | Motivator targeted | What changes | Owner |
Monitoring: hygiene cadence <> | motivator cadence <> | lead indicator <>
```

*→ Method in Action: [Herzberg's Pittsburgh Study and the Critical Incident Method (1959)](examples/herzbergs-pittsburgh-study-and-the-critical-incident-method-1959.md)*

*→ 2026 lens: [Retaining Scarce AI/ML Talent in a Red-Hot Market (2024–2026)](examples/retaining-scarce-ai-ml-talent-2024-2026.md)*

## Motivation Packs

- **Software engineering:** hygiene failures = opaque promotion, inconsistent code review. Motivators: full-feature ownership, tech decision authority, open-source/conference recognition.
- **Early-stage startups:** fix hygiene (salary at living-cost threshold, equity clarity) before mission rhetoric — narrative doesn't motivate someone who can't pay rent.
- **Sales:** commission is hygiene when expected at market; becomes motivator only tied to specific achievement. Recognize wins publicly; give territory/account ownership.
- **Product management:** dominant gap = work fragmentation (PMs as request-gatherers). Enrichment: direct user access, full problem-space ownership, visible path to measurable outcomes.

## Applying It Well

- Fix hygiene to the floor, not best-in-class — above-market hygiene costs more with zero retention advantage.
- Salary raises decay in weeks; design for motivators, not raises.
- Recognition must be specific, proximate, and tied to a named achievement — not generic and annual.
- Vertical loading only: more authority, accountability, direct feedback, complete ownership — not more tasks of the same type.
- Motivators habituate upward; job enrichment is continuous design, not a one-time fix.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **"We gave everyone a 15% raise and retention improved, so salary is a motivator."** | Short-term retention = hygiene restoration. Track the same cohort 6–12 months: discretionary effort returns to pre-raise baseline. |
| [D] **"Our employees say they care most about compensation in surveys."** | Surveys skew toward hygiene factors (legible, discussable). Critical incident data consistently surfaces achievement and recognition as primary. |
| [D] **"We added flexible hours and a gym benefit — that should help motivation."** | Both are hygiene factors. Neither creates engagement when work is unchallenging and responsibility is absent. |
| [D] **"If we give people more autonomy, they'll make mistakes."** | Studies show increased autonomy improves both performance and retention when paired with clear accountability structures. |
| [D] **"We recognize people with annual awards."** | Annual generic awards sever the motivational connection. Recognition must be specific, proximate, and tied to a named achievement. |
| [D] **"Our engineers leave for Google salaries — this is a hygiene problem."** | When they leave for similar-level roles at similar salaries, it's almost always a motivator failure wearing hygiene language in the exit interview. |
| [D] **"We enriched jobs by adding more projects."** | Horizontal loading. Enrichment = vertical loading: higher-scope responsibility, direct accountability, genuine decision authority. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Retention interventions default to compensation without a two-factor diagnosis
- Exit interview data not classified by hygiene vs. motivator before designing intervention
- Recognition is non-specific, annual, disconnected from observed achievement
- Job enrichment operationalized as more work (horizontal) rather than more responsibility (vertical)
- "Culture" used as substitute for diagnosing whether motivators are present in the actual role

## Verification

- [ ] Problem classified: hygiene-domain (dissatisfaction) vs. motivator-domain (low engagement despite adequate hygiene)
- [ ] Hygiene baseline assessed against market standards before any motivator intervention
- [ ] Motivator gaps identified through behavioral data, not attitude ratings
- [ ] Interventions are vertical loading (responsibility, autonomy, scope) not horizontal loading
- [ ] Recognition is specific and proximate (close in time to the achievement)
- [ ] Monitoring plan defined with cadence for both axes
- [ ] Two-factor asymmetry stated explicitly: fixing hygiene will not create motivation

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/herzberg-two-factor** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
