# Method in Action: Intercom Fin's $0.99 per Resolution (2023–2026)

> *Example for the [outcome-based-ai-pricing](../SKILL.md) skill.*

Intercom sells customer-service software priced per seat. In March 2023 it launched Fin, an AI agent that answers customers directly — the exact product that shrinks the number of support seats a customer needs. Instead of folding Fin into the seat price, Intercom charged **per resolution**. The definition has been refined publicly ever since, and the current billing rules read like a worked answer to this skill's steps 2 and 5. This is the most-cited public example of outcome pricing for an AI agent.

**Primary sources (Intercom's own pages).**
- "A complete guide to Fin…", Intercom blog, 13 June 2023: https://www.intercom.com/blog/fin-ai-bot-customer-service
- "Fin 2: The first AI agent that delivers human-quality service", Intercom blog, 10 October 2024: https://www.intercom.com/blog/announcing-fin-2-ai-agent-customer-service
- "Fin AI Agent outcomes", Intercom Help Center (current billing definitions): https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes
- Intercom pricing page: https://www.intercom.com/pricing

Intercom's internal margins, inference costs, and migration data are not public. The steps below say so rather than estimate them.

## Running the steps

**1. Choose the value metric.** Intercom stated the choice and the rejected alternatives in June 2023: "While competitors price chatbots based on metrics like deflection or API calls, we looked a little deeper… These metrics… can be misleading – leaving customers unsatisfied, and your team's bill on the rise. Fin is priced per resolution." Scored on the four tests:
- *Measurable:* yes — every conversation ends in a recorded state.
- *Attributable:* mostly — Fin either gave the last answer or it did not.
- *Grows with value:* yes — each resolution is a ticket no human handled.
- *Budgetable:* made budgetable by the risk-sharing controls in step 5.

Seats fail the third test for an AI agent, and API calls or "deflections" fail the first two from the buyer's side. *Gate passed.*

**2. Define success and attribution.** The current Help Center definition is the step 2 artifact, written into the terms:
- A **resolution** is counted when, after Fin's last answer, the customer "either confirms the answer was satisfactory (confirmed resolution), or exits the conversation without requesting further assistance (assumed resolution)."
- **Exclusions:** greetings are not answers; if Fin's last message was a clarifying question with no reply, "no resolution state is recorded." Escalations — the customer asks for a human, Fin detects frustration, a workspace escalation rule fires, a procedure fails — are never billed. Intercom says: "you're never paying for Fin's 'attempts'."
- **Dispute / clawback window:** "If a conversation is considered resolved… but the customer later returns to the same conversation seeking further assistance (even across billing periods) that resolution will be deducted and not charged."
- **Shared data source:** customers can open every billed conversation in their workspace and check its outcome type.

*Gate check:* both sides reconcile against the same conversation records, so outcome pricing holds. The "assumed resolution" rule is the weak joint — a frustrated customer who silently leaves is billed — and Intercom's own FAQ admits it and recommends frustration-escalation rules. That is the gameable spot [goodharts-law](../../goodharts-law/SKILL.md) predicts, and why the skill pairs the unit with a quality counter-metric.

**3. Anchor the price.** $0.99 per resolution, unchanged from launch: "The same as it always did – $0.99 cents per resolution" (October 2024). Intercom publishes neither a cost-plus rationale nor its anchor. Read through this skill, the comparison a buyer makes is the cost of a human-handled ticket — the replacement-cost anchor — not inference cost, which shifts with every model release while the list price has stayed put.

**4. Check gross margin.** *Not public.* Intercom does not disclose per-resolution inference or review cost. Two published design choices do the step's work structurally: Fin is charged **once per conversation** "even if Fin resolves multiple questions or runs multiple Procedures," which caps revenue per conversation — so Intercom carries the P90 long-conversation cost risk itself; and newer outcome types were priced separately (a sales **qualification** is $9.99, a disqualification $0.99), i.e. a different unit price where the value and cost profile differ.

**5. Share the risk.**
- *Floor:* standalone Fin carries a "minimum monthly commitment… (e.g. 50 outcomes)" (pricing page).
- *Cap:* customers "can also set usage reminders and hard limits" (Help Center).
- *Pilot guarantee:* 14-day free trial; "If Fin can't answer, Fin is free to use."

All four risk-sharing devices in step 5 have a public Intercom counterpart except tiered overage, which Intercom handles through sales ("high-volume pricing… contact Sales").

**6. Plan the migration.** Intercom did not replace seats; it **added** the outcome meter beside them. The pricing FAQ: "Intercom pricing has two components: Seats… Usage… (e.g. Fin outcomes)." Fin is also sold with "no seats required" on top of other helpdesks. That is the fixed + usage hybrid as the migration path: existing seat customers opt into the meter without a forced re-price, and the seat line shrinks only as their own staffing does.

**7. Stop-rule.** Did attribution disputes push Intercom back to usage pricing? No — the outcome unit has persisted since 2023, renamed from "resolution" to "outcome" as procedure handoffs and sales qualifications were added. The billing rules grew more precise over time (deductions on reopen, unbilled escalations, explicit abandoned states) — the pattern of a team working down its dispute rate instead of retreating from the unit.

## The mapped steps

1. **Metric:** per resolution, chosen explicitly over deflection and API calls.
2. **Success + attribution:** confirmed or assumed resolution; escalations and clarifying-question abandons excluded; reopen → deducted; customer can audit each billed conversation.
3. **Anchor:** $0.99 flat since launch, against human ticket cost — not inference cost.
4. **Margin:** not public; once-per-conversation charge and separate $9.99 qualification price shape the tail.
5. **Risk sharing:** monthly minimum (e.g. 50 outcomes), hard usage limits, free trial, no charge when Fin cannot answer.
6. **Migration:** seats kept, outcome meter added; Fin also sold seat-free.
7. **Stop-rule:** not triggered; definitions tightened rather than abandoned.

**The lesson:** most of the work in outcome pricing is not the number but the definition. Intercom's $0.99 never moved; what moved, publicly and repeatedly, was the exact rule for what counts as a billable success.
