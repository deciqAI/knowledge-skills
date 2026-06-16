# Method in Action: Magee 1964 — Chemical Plant Investment (HBR)

> *Example for the [decision-tree](../SKILL.md) skill.*

**John F. Magee** (1926–2015) was a partner at Arthur D. Little and the first analyst to systematize decision tree methodology for business. His two 1964 *Harvard Business Review* articles introduced the framework to a generation of executives and consultants who had previously made multi-million-dollar investment decisions through intuition and scenario narratives.

Magee's canonical case: a chemical company facing a ten-year capital investment decision with uncertain demand. Two options — build a **large plant** (high fixed cost, high capacity) or a **small plant** (low fixed cost, low capacity with an option to expand in year 2). Demand over the period could be high or low, with a possibility of reversal between years 1–2 and years 3–10.

The HBR framing:

> "A decision tree is a diagram that describes graphically the various possible combinations of events and the decisions associated with them. It draws out the sequential decisions with their alternative choices and their consequences ... forcing managers to be explicit about the alternatives at each stage of the decision process."
>
> — Magee (1964), "Decision Trees for Decision Making," HBR, p. 127.

The tree structure:
- Root: Large plant vs. Small plant (decision node, square)
- Year 1–2 demand: High (0.60) vs. Low (0.40) — chance node on each branch
- If Small plant + High demand: expand or do not expand (second decision node)
- Years 3–10 demand conditional on years 1–2 outcome

**Rollback results:** Magee calculated that the large plant had a higher expected NPV than the small plant — but only because the probability assigned to high demand was above a critical threshold of approximately 0.55. When the team was asked to justify that 0.60 probability, three executives disagreed: one said 0.70, one said 0.50, one said 0.55. The tree converted a boardroom argument from "I think we should build big" to "what probability do you assign to high demand in years 1–2?" — a precise, revisable, evidenced question.

**Howard Raiffa's formalization (1968)** built on Magee's work to establish the rollback procedure as a mathematical discipline, introduce formal sensitivity analysis (the switchover probability), and define the **Expected Value of Perfect Information (EVPI)** — the maximum a decision-maker should pay to resolve an uncertainty before deciding. Raiffa's EVPI formula:

> "EVPI is the expected gain from having perfect information about the state of the world before committing to a choice. It sets the upper bound on the value of any research or investigation that reduces uncertainty about that state."
>
> — Raiffa (1968), *Decision Analysis*, p. 112.

If EVPI for the demand forecast uncertainty was $2M, and a market research study costs $500K, the study is worth commissioning. If EVPI is $200K and the study costs $500K, decide immediately.

**Operational lessons from Magee + Raiffa:**

The three-step discipline they established:

1. **Draw before calculating.** The visual structure surfaces assumptions that participants didn't realize they were making. The act of drawing the tree is worth more than the rollback calculation.
2. **Assign probabilities explicitly.** "High demand" means nothing until it has a probability. Force every probability owner to state a number and a basis. Disagreements about numbers are more productive than disagreements about direction.
3. **Compute EVPI before gathering data.** The tree tells you what information is worth buying. Spending $1M on research that could only change the decision by $200K is irrational. EVPI makes that explicit.

**McKinsey and BCG adoption (1970s–80s).** Both firms used decision trees as their primary tool for capital investment visualization. The tree format allowed consultants to walk executives through complex multi-stage decisions in one diagram — making implicit assumptions visible, driving consensus on probabilities, and producing a defensible recommendation with explicit conditions.

The most important lesson from the HBR case: **the tree revealed the threshold, not just the recommendation.** Knowing that the large plant wins only if demand probability exceeds 0.55 — and that the team had uncertainty around that threshold — was more valuable than the expected value itself. The recommendation was: proceed with large plant AND commission a targeted demand study to validate the 0.60 probability estimate before ground-breaking.
