---
name: design-thinking
description: "Activate when: user asks 'why isn't anyone using our product?', 'how do we understand what customers really want?', 'we know the tech works but the market isn't responding', team is stuck on a single solution and needs divergent ideas, or someone discusses user research / personas / prototyping / iterative design.
  Do NOT activate when: the problem and solution are both already validated and the challenge is pure execution; or the team cannot access real users at any point."
---

# Design Thinking

## Overview

Design thinking — formalized by Tim Brown at IDEO and Stanford's d.school, grounded in Simon (1969) and Rittel's "wicked problems" — replaces assumption-driven decisions with evidence from observed human behavior. Its three-lens test: every viable innovation must sit at the intersection of desirability, feasibility, and viability. Most product failures are desirability failures; teams built something technically sound that people did not want.

Composes with neighbors: use [`jobs-to-be-done`](../jobs-to-be-done/SKILL.md) alongside the Define stage; use [`mvp`](../mvp/SKILL.md) after Prototype; use [`lean-startup`](../lean-startup/SKILL.md) as the execution engine after the full five-stage cycle.

## When to Use

Apply when:
- The real user problem is not yet understood — team has a solution but no observed-behavior evidence
- User adoption is failing despite a technically sound product (unresolved desirability gap)
- Team is locked into one solution direction and needs divergent thinking first
- Problem has multiple conflicting stakeholders and no single correct answer
- Team states "we already know what users need" without observational evidence

**When NOT to use:**
- Problem and solution both well-understood; challenge is execution only
- Less than two weeks available for genuine user research (produces assumption-laundering)
- Regulatory constraints preclude prototyping before specification
- Team cannot access real users at all

## Coaching Novices (Adaptive Front Door)

**Engine mode:** concrete challenge → run The Process. **Coach mode:** unfamiliar user → guide step by step.
In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. Design thinking is a five-step process for building things people actually want: observe first, prototype cheaply, iterate on what you observe (not what you assumed).
2. Check fit: does the team know — based on observation, not assumption — why users behave as they do? If yes and solution is validated, divergent stages may not be needed.
3. Elicit their real case: product/service, who are the users, what is the current evidence of user behavior?
> **[WAIT — do not advance until user responds]**
4. Start with Empathize: "When did someone on the team last directly observe a user — not a survey, not analytics, but watch a person use the product?"
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight they most need and which stage is most likely to surface it.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Design Sprint** through five stages (divergent → convergent, checkable output at each).

1. **Empathize:** Observe real users in context (30–60 min interviews; contextual observation; extreme users). Stop-rule: survey responses alone = stage incomplete.
2. **Define:** Sort observations by theme → find say/do contradictions → write insight statement → reframe as "How Might We" (HMW). Deliverable: 3–5 ranked HMWs. Stop-rule: HMW contains a solution → return to synthesis.
3. **Ideate:** Silent writing → share → cluster → dot-vote → select 3–5 for prototyping. Stop-rule: <20 concepts before convergence = ideation was skipped.
4. **Prototype:** Minimum artifact to test the core assumption; one explicit learning question per prototype; 4-hour ceiling. Stop-rule: polishing without a new assumption = stop.
5. **Test:** Define 3 hypotheses → observe, do not defend → debrief immediately → iterate within 24 h. Run 2–3 full cycles. Stop-rule: "users loved it" = insufficient testing.

### Output: Design Sprint Report

```markdown
# Design Sprint: <challenge>
## Empathize: participants / key observations / say-do contradictions / most surprising finding
## Define HMWs: 1. <HMW> 2. <HMW> 3. <HMW> — Selected: <which and why>
## Ideate: concepts generated <n> — selected for prototyping: <3–5 descriptions>
## Prototype: concept / form / learning question: <assumption tested>
## Test: sessions / H1–H3: confirmed|disconfirmed|inconclusive + behavior / next iteration
## Recommended direction: <concept, evidence, what to build next>
```

*→ Method in Action: [GE Healthcare — Pediatric MRI Redesign (2007)](examples/ge-healthcare-pediatric-mri-redesign-2007.md)*

## Empathy Packs

- **Consumer products:** Go where people use the product and watch. Surveys reveal stated preferences; observation reveals actual behavior.
- **B2B / enterprise:** Shadow research surfaces workarounds and parallel Excel sheets that interviews never reveal.
- **Public services:** Start with extreme users — heaviest users know every workaround; non-users reveal barriers designers never imagined.
## Applying It Well

- Separate divergent/convergent modes — never evaluate during ideation; name the mode at the start of each stage.
- The say/do gap is where insight lives — contradictions between stated needs and observed behavior are the design opportunity.
- Prototype fidelity must match the question being asked; never invest fidelity before the concept is validated.
- Test to learn, not to confirm — all-positive sessions mean you are not challenging the hard parts.
- Define is the hardest stage — quality of ideation is entirely determined by quality of the HMW.

*→ Primary sources: [references/sources.md](references/sources.md)*
## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We already know our users" | Even teams who shipped to millions discover gaps in fresh Empathize research. Knowing users is ongoing practice, not a historical achievement. |
| [D] "We ran a survey — that counts as user research" | Surveys measure what users say; observation reveals what they do. Surveys without observation are assumption laundering. |
| [D] "The prototype needs to be high quality before testing" | High fidelity at concept stage is sunk cost. Use the lowest-fidelity artifact that answers the current question. |
| [D] "Three of five users liked it" | Three positive concept responses is not PMF evidence. Testing must challenge the concept, not sample sentiment. |
| [D] "Design thinking takes too long" | A 4-week Empathize stage pays for itself by preventing one 3-month rebuild after shipping the wrong thing. |
| [D] "We did a workshop — now we're doing design thinking" | A workshop is vocabulary practice; design thinking is a continuous process tied to real user research and actual iteration decisions. |
| [D] "We'll do user testing after we build the MVP" | Highest ROI comes from testing concepts before any code is written — when iteration costs are zero. |
| [D] "HMW: how might we build a better app?" | That is a solution disguised as a problem. A valid HMW describes a human need, not a product form. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No specific user observation (not survey, not analytic) drove the design direction
- HMW question contains a solution ("how might we build X?")
- Prototype was built to show stakeholders, not test a hypothesis
- Testing sessions produced only positive feedback — no confusion moments recorded
- Define stage skipped: jumped from interviews directly to solutions
- Direction unchanged after three rounds of testing — the test is not challenging the right assumptions

## Verification

- [ ] ≥5 users directly observed (not surveyed) in Empathize
- [ ] ≥1 say/do contradiction identified
- [ ] HMW describes a user need, not a solution form
- [ ] ≥20 concepts generated before any were evaluated
- [ ] Each prototype has one explicit learning question stated before testing
- [ ] ≥2 full test cycles (prototype → test → iterate) completed
- [ ] Sessions recorded behavioral observations, not only user sentiment
- [ ] Final direction traces to observed behavior, not team preference

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/design-thinking?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=design-thinking** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
