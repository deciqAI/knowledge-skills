# deciqAI Knowledge Skills

**Open-source thinking-framework skills that make rigorous reasoning executable for AI agents.**

25 composable mental models — packaged as installable [Agent Skills](https://www.deciqai.com/skills). Each turns a reasoning method that usually lives in a book into a step-by-step process an AI agent can actually run, with worked historical examples and cited sources.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) · Built by [deciqAI](https://www.deciqai.com/skills?utm_source=github&utm_medium=readme&utm_campaign=knowledge-skills) · Contributions welcome

---

## Install

Add all 25 skills:

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

## The skills

| Skill | What it does |
|---|---|
| [First Principles](./first-principles) | Most reasoning is reasoning by analogy: X resembles Y, so do what Y does. |
| [Occams Razor](./occams-razor) | When several explanations all fit the evidence, prefer the one that assumes the least. |
| [Second Order Thinking](./second-order-thinking) | First-level thinking asks "what will happen?" and stops. |
| [Inversion](./inversion) | Most planning asks "how do I win?" and runs forward from there. |
| [Bayesian Reasoning](./bayesian-reasoning) | Bayes' theorem: Posterior odds = Prior odds × Likelihood ratio. |
| [Circle Of Competence](./circle-of-competence) | Every decision-maker has a domain where judgments are reliable (inside the circle) and one where they are not (outside). |
| [Margin Of Safety](./margin-of-safety) | Benjamin Graham introduced margin of safety in Security Analysis (1934) as the founding principle of value investing: buy assets at prices substantially below your estimate of intr |
| [Opportunity Cost](./opportunity-cost) | Opportunity cost is the true cost of any choice: the value of the next-best alternative you give up. |
| [Premortem](./premortem) | Before committing to a plan, the team imagines that plan has already failed catastrophically, then works backward to enumerate causes. |
| [Pareto Principle](./pareto-principle) | In most real systems, a small fraction of inputs produces the majority of outputs. |
| [Regret Minimization](./regret-minimization) | Most frameworks optimize expected value — pick the highest probability-weighted payoff. |
| [Chestertons Fence](./chestertons-fence) | Before removing a rule, process, code path, or institution — you must understand why it was put there. |
| [Compound Interest](./compound-interest) | Compound interest: a quantity grows at a rate proportional to its current size — growth itself grows — producing exponential accumulation. |
| [Confirmation Bias](./confirmation-bias) | Confirmation bias is the systematic tendency to seek, interpret, remember, and weight evidence in ways that support existing beliefs — and to correspondingly miss disconfirming evi |
| [Sunk Cost Fallacy](./sunk-cost-fallacy) | The sunk-cost fallacy is the tendency to let prior, irrecoverable investments (money, time, effort, reputation) distort current decisions. |
| [Mece](./mece) | MECE is a decomposition principle: break a problem, set of options, or population into sub-groups that are Mutually Exclusive (no overlap) and Collectively Exhaustive (no gaps) — e |
| [Economic Moat](./economic-moat) | An economic moat is the durable, structural competitive advantage that protects a business's returns on capital from being competed away. |
| [Porters Five Forces](./porters-five-forces) | Some industries earn 30%+ margins decade after decade; others fail to earn their cost of capital despite intelligent, well-funded firms. |
| [Jobs To Be Done](./jobs-to-be-done) | People don't buy products — they hire products to do a job (make progress in a specific circumstance, across functional, emotional, and social dimensions). |
| [Lean Startup](./lean-startup) | A startup is a temporary organization searching for a repeatable, scalable business model under extreme uncertainty (Steve Blank). |
| [Mvp](./mvp) | An MVP is not a small version of your product — it is a test instrument: the smallest artifact that produces trustworthy evidence about one specific demand-side assumption, with th |
| [Network Effects](./network-effects) | Some products get more valuable the more people use them — not because the company gets cheaper at scale, but because each user makes the product more useful to every other user. |
| [Antifragile](./antifragile) | Nassim Nicholas Taleb (2012) identified a third response to stress beyond fragile/robust: antifragile — systems that gain from disorder, with bounded downside and unbounded upside. |
| [Black Swan](./black-swan) | Taleb (2007): a black swan is (1) outside all prior expectations, (2) extreme impact, (3) obvious in hindsight only. |
| [Map Is Not The Territory](./map-is-not-the-territory) | Any representation — metric, model, strategy deck, org chart, or process manual — is a selective, simplified, aging abstraction. |

---

These 25 skills are a free taste of the 160+ skills wired into every [deciqAI](https://www.deciqai.com/skills?utm_source=github&utm_medium=readme&utm_campaign=knowledge-skills) agent.
