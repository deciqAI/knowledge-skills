<!--
Template for a new Knowledge Skill.
Copy into your-skill-slug/SKILL.md and fill in every section.
Delete all HTML comments before submitting. See CONTRIBUTING.md for quality bars.
-->

---
name: your-skill-slug
description: "Activate when: user says '<trigger phrase>', '<trigger phrase>', asks '<question shape>', or <situation the skill is built for>.
  Do NOT activate when: <real negative condition>, or <another one>."
---

# Your Skill Name

## Overview

<!-- 2-3 paragraphs. What problem of thinking does this solve? What goes wrong without it?
     State the core mechanism in one sentence a reader could repeat. -->

Compose with [related-skill] (why) · [another-skill] (why).

## When to Use

- <concrete situation>
- <concrete situation>
- <concrete situation>

**When NOT to use:** <condition> · <condition> · <condition>.

## Coaching Novices (Adaptive Front Door)

**Engine mode:** user has a concrete case → run The Process directly.
**Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What-it-is:** "<one-sentence explanation of the mechanism>"
2. **Check fit:** "<question that tests whether the user's case fits>"
3. **Elicit the real case:** "<question that pulls out the user's concrete situation>"
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "<first substantive step applied to their case>"
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "<the takeaway the user should be able to state>"

## The Process

**Output:** <name the artifact the process produces>

1. **<Step name.>** <What to do.> *Gate: <condition that must hold> → stop.*
2. **<Step name.>** <What to do.> *Gate: …*
3. **<Step name.>** <What to do.> *Gate: …*
4. **Stop-rule:** <the condition under which the method does not apply — return to step N or exit>.

**Output template:**
`<compact one-line schema of the artifact>`

*→ Method in Action: [Case Study Title](examples/your-case-study.md)*

## Applying It Well

1. **<Principle.>** <One or two sentences.>
2. **<Principle.>** <One or two sentences.>
3. **<Principle.>** <One or two sentences.>

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "<the excuse people use to dodge the method>" | <the reality check> |
| [D] "<another excuse>" | <the reality check> |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- <observable sign the method is being faked> · <sign> · <sign>

## Verification

- [ ] <check that the process was actually run, not narrated>
- [ ] <check on the output artifact>
- [ ] <check on evidence/sources>
