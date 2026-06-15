# deciqAI Knowledge Skills

**Open-source thinking-framework skills that make rigorous reasoning executable for AI agents.**

Five composable mental models — first-principles, Occam's razor, second-order thinking, inversion, and Bayesian reasoning — packaged as installable [Agent Skills](https://www.deciqai.com/skills). Each one turns a reasoning method that usually lives in a book into a step-by-step process an AI agent can actually run, with worked historical examples and cited sources.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) · Built by [deciqAI](https://www.deciqai.com/skills?utm_source=github&utm_medium=readme&utm_campaign=knowledge-skills) · Contributions welcome

---

## Install

Add all five skills:

```bash
npx skills add deciqAI/knowledge-skills
```

List what's inside, or grab a single skill:

```bash
npx skills add deciqAI/knowledge-skills --list
npx skills add deciqAI/knowledge-skills --skill first-principles
```

Each folder is also a self-contained `SKILL.md` with `examples/` and `references/` — copy it into your agent's skills directory directly if you prefer.

---

## The five skills

| Skill | Motion | What it does | Worked example |
|---|---|---|---|
| [first-principles](./first-principles) | Decompose **downward** to bedrock | Strip a problem to what can't be reduced further — law, definition, cited fact — then rebuild using only those. | The Wright Brothers, 1901 |
| [occams-razor](./occams-razor) | Choose **sideways** among explanations | When several explanations fit, prefer the one that assumes the least. A heuristic for what to bet on first. | Wegener & continental drift, 1912 |
| [second-order-thinking](./second-order-thinking) | Trace **forward** through consequence | First-level asks "what happens?" Second-order asks "…and then what?" — catching the effect that reverses the obvious one. | US Prohibition, 1920 |
| [inversion](./inversion) | Trace **backward** from failure | Instead of "how do I win?", ask "how could this fail catastrophically?" — then eliminate the failure paths that matter. | Apollo 1 FMEA, 1967 |
| [bayesian-reasoning](./bayesian-reasoning) | **Update** beliefs with evidence | Posterior odds = prior odds × likelihood ratio. Belief after evidence equals belief before, times how diagnostic it is. | The Sally Clark case, 1999 |

## How they compose

They aren't five isolated tricks — they're five motions through a single decision:

1. **Reduce** to bedrock (first-principles)
2. **Pick** the simplest hypothesis that fits (occams-razor)
3. **Trace** where that pick leads (second-order-thinking)
4. **Invert** to find what would kill it (inversion)
5. **Update** as evidence arrives (bayesian-reasoning)

Each skill stands alone; together they form a reasoning loop. Every skill's `SKILL.md` cross-links to its neighbors and tells the agent when to compose them.

## What's in each skill

```
first-principles/
├── SKILL.md      # the method: when to use, the process, the output contract
├── examples/     # a fully worked historical case
└── references/   # cited sources
```

Skills are model-agnostic and work with any agent that supports the Agent Skills format (Claude Code, Cursor, and others).

---

## Why these exist

These are five of the **130+ skills wired into every [deciqAI](https://www.deciqai.com/skills?utm_source=github&utm_medium=readme&utm_campaign=knowledge-skills) agent** — the thinking layer behind an agentic operator team for founders. Most AI runs the work; deciqAI runs the thinking before it. We open-sourced the thinking part because rigor should be free. The product is the part that runs these skills *autonomously* to operate a company.

**→ [See the agents that run these, free](https://www.deciqai.com/skills?utm_source=github&utm_medium=readme&utm_campaign=knowledge-skills)**

## Contributing

Issues and PRs welcome — a new worked example, a sharper failure mode, a translation. Each skill aims to be rigorous, sourced, and genuinely executable rather than inspirational. Keep that bar.

## License

[MIT](LICENSE) © 2026 deciqAI. Free to use, fork, and adapt.
