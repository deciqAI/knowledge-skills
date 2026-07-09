# Method in Action: The AI Ecosystem — Positive-Sum vs. "AI Eats Everything" (2024–2026)

> *Example for the [non-zero-sum](../SKILL.md) skill.*

The dominant popular framing of the 2024–2026 AI boom is zero-sum: "AI will take all the jobs," "the foundation-model labs will capture all the margin," "the cloud providers own everything, so app builders are just renting a commodity that will crush them." This example runs the skill's process over the three main layers of the AI stack — foundation-model providers (e.g., OpenAI, Anthropic, Google DeepMind), cloud/compute providers (e.g., Microsoft Azure, AWS, Google Cloud, plus the chip supplier Nvidia), and application builders (the startups and incumbents building products on top of the models) — to test whether the interaction is actually zero-sum, or whether the layers can grow together.

**Step 1 — Map positions vs. underlying interests:**

| Party | Stated position ("who wins the fixed pie") | Underlying interest |
| Foundation-model labs | "We own the intelligence layer; everyone above us is a thin wrapper." | Maximize inference demand and paying usage; need distribution to reach end users and real-world feedback to improve models. |
| Cloud / compute providers | "Compute is the bottleneck; we capture the rent." | Maximize durable, high-utilization compute consumption; need a growing population of workloads to justify enormous capex. |
| App builders | "We'll be commoditized the moment the labs move up-stack." | Ship differentiated products with proprietary data, workflow, and distribution; need cheaper, better, more reliable models. |

The *positions* are stated as a fight over one fixed pie of AI margin. The *interests* are not symmetric claims on one pool — each layer's interest is served by the *others' growth*: labs need distribution (app builders) and compute (cloud); cloud needs workloads (both); app builders need cheaper, better models (labs) running on reliable infrastructure (cloud).

**Step 2 — Construct the payoff matrix:**

Reduce to two representative players — the model/compute *platform* layer and the *app-builder* layer — and ask whether total value is fixed or variable.

| | App builders invest / build on the platform | App builders retreat / hedge away |
| **Platform invests in capability + access** | Both gain: cheaper, more capable models expand what apps can profitably do → more usage → more inference revenue and compute consumption. New categories (coding assistants, customer support, document workflows) become viable that did not exist before. | Platform loses: capex is stranded, utilization drops. Builders lose the capability they were waiting for. |
| **Platform extracts / locks in aggressively** | Builders lose margin and autonomy; platform gains short-term rent but starves the ecosystem that generates demand and feedback. | Both lose: builders route around the platform (open-weight models, multi-vendor abstraction), platform's demand shrinks, the category's growth stalls. |

**Non-zero-sum gap (the cooperation dividend):** In the mutual-investment quadrant, the *total* value is not fixed — it grows. Falling cost-per-token and rising model capability across 2024–2026 lowered the threshold at which an AI application is worth building, which *created new demand* rather than redividing old demand. That new demand simultaneously feeds inference revenue (labs), compute consumption (cloud/chips), and product markets (app builders). This is Wright's specialization-and-trade dynamic reappearing: a division of labor across layers produces more total value than any single layer capturing everything. The zero-sum "AI eats the margin" framing looks only at the redistribution quadrants and ignores that the pie itself is variable.

**Step 3 — Assess the shadow of the future:**

**Strong.** These are deeply repeated, multi-year interactions, not one-shot deals. Labs and cloud providers have entered multi-year commercial and infrastructure partnerships (the best-documented being the ongoing Microsoft–OpenAI relationship, publicly reported since 2019 and expanded in 2023). App builders make sticky, repeated choices about which models to depend on. Reputational effects are large: a platform that is seen to cannibalize its own developers (build a first-party app that competes with its best customers) damages the trust that future builders price in — so defection carries costs well beyond any single round. Because so much of the value is in *future* growth rather than this year's revenue split, the discounted value of continued cooperation dominates the one-time gain from extraction.

**Step 4 — Identify the cooperation mechanism:**

Multiple mechanisms operate at once:
- **Institution (pricing + platform design):** Usage-based pricing and published API access make the platform's revenue *grow with*, not *at the expense of*, builder success — the same tiered-take logic as an app store or Stripe Connect. Cloud "credits" and startup programs subsidize early builders because their later consumption is the payoff.
- **Reframing:** Treating the stack as an *ecosystem* rather than a value-chain tug-of-war makes the mutual gain visible: model capability improvements are a shared input, not a transfer.
- **Reputation:** Publicly signaling "we won't compete with our developers" (or credibly the opposite) shapes how much builders are willing to invest on top of a given platform.
- **Reciprocity / hedging as discipline:** Builders' ability to adopt open-weight models or multi-vendor abstraction layers is the Tit-for-Tat move — it keeps any single platform's temptation to extract in check.

**Step 5 — Design the first move:**

A cooperative, legible, resilient opening for whichever party you are:
- *If you are the platform:* lead with cheaper, more capable, well-documented access and a credible commitment not to cannibalize your best builders. Make the win visible (case studies, revenue share), and make any future move up-stack pre-announced so it is not read as a surprise defection.
- *If you are the app builder:* commit real product investment on top of a primary model — but keep a legible hedge (a portability layer, an open-weight fallback). The hedge is not hostility; it is the unambiguous defection-detection mechanism that keeps the relationship honest.
- **Defection signal:** the platform launches a first-party product directly targeting its largest builders' core use case without notice; or a builder silently exfiltrates the platform's outputs to train a competing model.
- **Recovery path:** because ambiguity is high (is a new first-party feature "competition" or "platform completeness"?), use *generous* Tit-for-Tat — respond to a single ambiguous move with a proportional, reversible hedge rather than a full exit, so one misread does not collapse a multi-year, positive-sum relationship.

**What this case shows:** The "AI takes all the jobs / all the margin" narrative is a zero-sum reading of an interaction whose total value is demonstrably *variable*. When the cost of capability falls and repeated interaction is strong, the layers of the AI stack are structurally positioned to grow together — the same non-zero-sum logic Axelrod formalized for repeated play and Wright traced across economic history. The dividend is real but *not automatic*: capturing it requires pricing and platform design that make each layer's success feed the others', plus credible mechanisms (reputation, portability) that keep the extraction temptation in check.

*Sources: Wright, Robert. *Nonzero: The Logic of Human Destiny* (Pantheon, 2000) — the specialization/trade positive-sum thesis. Axelrod, Robert. *The Evolution of Cooperation* (Basic Books, 1984) — repeated-play cooperation conditions. Microsoft and OpenAI partnership publicly announced 2019 and expanded January 2023 (Microsoft and OpenAI press releases / blog posts). Falling AI inference cost-per-token and rising model capability across 2024–2025 are widely reported industry trends (e.g., successive OpenAI, Anthropic, and Google model/pricing releases). Figures and exact terms are omitted where not verifiable; qualitative dynamics are stated as reported industry trends as of early 2026.*
