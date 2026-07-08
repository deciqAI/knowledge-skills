---
name: tax-season-throughput-constraints
description: "Activate when: returns are piling up before a deadline; reviewer/preparer is the bottleneck; 'we can't get through them all,' 'clients waiting on missing docs,' planning staffing for Jan–Apr. Do NOT activate when: off-season, low volume; the issue is a single stuck return (use debugging, not capacity theory)."
---

# Tax Prep — Season Throughput (Theory of Constraints)

> **Industry front door for [theory-of-constraints](../theory-of-constraints/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.

**Activate when:** returns are piling up before a deadline; reviewer/preparer is the bottleneck; "we can't get through them all," "clients waiting on missing docs," planning staffing for Jan–Apr.
**Do NOT activate when:** off-season, low volume; the issue is a single stuck return (use debugging, not capacity theory).

## Why this variant
The parent [theory-of-constraints](../theory-of-constraints/SKILL.md) finds the one step that caps total output and subordinates everything to it. In a tax practice the constraint is almost never "preparation" — it's usually **the reviewer** or **client missing-documents**. Optimizing anything else is wasted motion during season.

## Domain inputs → parent's Process
Pipeline stages: intake → doc-complete → prep → review → e-file.
1. Measure WIP at each stage; the stage with the growing queue = constraint.
2. Exploit: protect reviewer time (no admin), pre-triage returns so review is fast.
3. Subordinate: preparers pace to reviewer capacity, not their own.
4. Elevate: add reviewer capacity / async review / raise complexity threshold for partner review.

## Worked example
80 returns in "prep-done," 6 cl2ear/day through review → 13-day backlog vs 5 days to deadline.
→ Constraint = review. Exploit: batch simple returns for a fast lane; move partner off prep entirely. Missing-docs is the upstream feeder — a chaser (see onboarding/data-room agents) protects the constraint from starving.

## Packs
- **Solo:** one fast-lane vs deep-lane split; cap daily complex intake.
- **Firm:** reviewer-protected calendar; WIP board; extension-triage rule when backlog > days-remaining.

## Red flags
- Preparers "busy" but review queue growing = optimizing the non-constraint.
- Missing-docs starving the constraint (idle reviewer waiting on clients).

## Verification
- [ ] Constraint stage identified by queue growth, not opinion
- [ ] Non-constraint work subordinated to it
- [ ] Extension policy triggered when backlog > remaining days
- [ ] Upstream doc-chaser keeps constraint fed

---
Part of **deciqAI Knowledge Skills**. Core method: [theory-of-constraints](../theory-of-constraints/SKILL.md).
