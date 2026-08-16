# Contributing to deciqAI Knowledge Skills

Thanks for helping make rigorous reasoning executable. Two kinds of contributions are welcome:

1. **Improving an existing skill** — sharper triggers, better worked examples, real-world failure patterns, missing sources.
2. **Proposing a new skill** — a thinking framework not yet in the library.

Open a pull request either way. For a new skill, consider opening an issue first (see the issue templates) so we can confirm it isn't a duplicate or an overlap with an existing skill.

## Two kinds of skill

The library holds two genres. They have different shapes and different bars, and picking the wrong one is the most common reason a PR needs rework.

**Thinking-framework skills** — `first-principles`, `bayesian-reasoning`, `inversion`, `second-order-thinking`. A reasoning method that usually lives in a book, made runnable. It generalises across domains, and it has a documented history someone can check.

**Practice-playbook skills** — `cpa-return-review`, `customs-hts-classification-mece`, `ria-fiduciary-conflict-disclosure`, `freight-carrier-vetting-checklist`. A specific profession's repeatable workflow, with the rules it operates under. The method *is* the sequence and its gates; there is no parent framework it reduces to, and usually no citable public case, because this work happens inside client files that never become public record.

If your skill is a named framework with a literature, write genre 1. If it is "how this job is actually done, in order, with the places you must stop", write genre 2.

## Skill anatomy

**Thinking-framework skills** are a folder:

```
your-skill-slug/
├── SKILL.md              # the skill itself
├── examples/
│   └── <case-study>.md   # at least one worked historical example
└── references/
    └── sources.md        # primary sources, cited properly
```

**Practice-playbook skills** are a single `SKILL.md`, with the worked example inline. No `examples/`, no `references/`. See [cpa-return-review](./cpa-return-review/SKILL.md) or [customs-origin-usmca-decision](./customs-origin-usmca-decision/SKILL.md).

Start from [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) — it mirrors the thinking-framework structure. Practice playbooks drop `## Overview` / `## When to Use` / `## Coaching Novices` in favour of a short `## Why this skill` plus inline `**Activate when:**` / `**Do NOT activate when:**` lines.

## Quality bars

### Both genres

A PR is ready when it clears all of these:

- **Triggers are explicit.** The frontmatter `description` must contain `Activate when:` with concrete user phrasings, and ideally `Do NOT activate when:` with real negative conditions. This is what lets an agent load the right skill at the right time — it is the most important part of the file.
- **The Process is executable.** Numbered steps with hard gates (`*Gate: … → stop.*`), not prose about the idea. A reader should be able to run it mechanically.
- **Anti-patterns are named.** The "Common Rationalizations" table lists the fake moves people use to dodge the method, each with the reality check. Mark entries `[D]` (designed upfront) or `[O]` (observed in real use), with the marker leading the cell: `| [O] "the excuse" | the reality |`.
- **Red flags and Verification.** Observable signs the method is being faked, and a checklist that the process was run rather than narrated.
- **No placeholders.** No TODO, no "coming soon", no empty files.
- **English throughout.** Frameworks originating in other languages are welcome — gloss original terms at first use (e.g. `势 (shì)`), then use the English name.
- **Cross-links use the bare form.** Reference other skills as `[skill-slug]` in prose. Links to skills outside this library are converted to plain text at publish time.
- **Skill boundaries live in the `description`.** A router picks between skills from frontmatter alone — it never sees your prose. If your skill sits next to an existing one, name that one in your `Do NOT activate when:` clause, and expect the reverse edit too. A cross-link in the body does not disambiguate anything.

### Thinking-framework skills only

- **At least one worked example.** A real historical case in `examples/`, walked through the skill's own steps, with a primary source cited. No invented case studies.
- **Sources are primary.** `references/sources.md` cites the original book/paper with links. If part of the framework is synthesis rather than citation, say so explicitly in a "What is NOT cited and why" note — several skills in the library show the pattern.

### Practice-playbook skills only

- **Compliance anchors.** Name the rules the work actually sits under — statute, regulation, professional standard, firm policy. Cite them by section, and check the section numbering is current: renumbering happens (the AICPA tax standards went from seven statements to four in 2024) and a stale citation is the kind of thing a practitioner copies into a signed file.
- **The worked example is inline, and may be a composite.** Real client matters are confidential, so a representative composite is expected. Make it earn its place: it should show the method surfacing something a flat reading would have missed.
- **No expiring content, and say so.** Thresholds, dollar limits, rates, phase-outs, eligibility tests and filing dates do not belong in a prompt file — they go stale and a practitioner may rely on them. Route every such question to current authority instead.
- **Constrain the runtime, not just the file.** Keeping numbers out of your file is not enough: the agent running it will supply remembered ones, including inside text drafted for a client. Add an explicit instruction and a Verification item saying figures are routed, never answered from memory. Files that only carry a disclaimer leak; files that instruct the running agent do not.
- **Gates are hard stops.** Where the professional consequence of continuing is real — conflict of interest, criminal exposure, an unfiled prerequisite — the Process must stop, not warn.

Don't hand-write the footer line (`*Part of **deciqAI Knowledge Skills**…`) or edit the README table — both are generated by the maintainers' publish pipeline. Leave them out of new skills; they'll be injected.

## Where the library currently falls short

Stated honestly, because a bar nobody meets is not a bar.

Of 237 skills, 69 ship without `examples/` and `references/`. That splits two ways, and only one of them is fine:

- **41 are practice playbooks** — the `cpa-*`, `customs-*`, `freight-*`, `insurance-*`, `mortgage-*`, `realtor-*`, `ria-*`, `tax-*` and `travel-*` families. Genre 2. They meet their own bar and need no folders.
- **28 are thinking-framework skills that are simply incomplete** — `the-mom-test`, `cash-conversion-cycle`, `contrarian-question`, `unit-economics-cac-ltv-payback` and others in the founder and Zero to One batches. They have `## Overview` and read like genre 1 because they *are* genre 1; their `examples/` and `references/` were never written.

**The second group is a backlog, not an exemption.** Adding a case study and a sources file to one of those 28 is one of the most useful PRs you can open here, and a good first contribution: the method is already written and the shape to copy is in any completed sibling.

## Style

- Keep SKILL.md roughly 100–240 lines — dense, not exhaustive. Depth goes in `examples/` and `references/` for thinking frameworks, and stays inline for practice playbooks.
- Write for an agent executing the method, not a human reading about it. Imperatives over descriptions.
- Match the voice of existing skills: read [first-principles](./first-principles/SKILL.md) and [bayesian-reasoning](./bayesian-reasoning/SKILL.md) before writing.

## What happens after merge

Merged skills are synced into the deciqAI skill library and mirrored to the [HuggingFace dataset](https://huggingface.co/datasets/deciqAI/knowledge-skills) and ClawHub. Your skill ships everywhere the library ships.

## License

By contributing you agree your contribution is licensed under the [MIT License](LICENSE).
