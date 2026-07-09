# Method in Action: The Frontier-AI Training Race (2023–2026)

> *Example for the [red-queen-effect](../SKILL.md) skill.*

Between 2023 and 2026 the leading frontier AI labs — OpenAI, Anthropic, Google DeepMind, Meta, xAI, and others — entered a textbook Red Queen race. Each must keep training ever-larger and better models, and keep buying more compute, simply to hold relative position while every rival does the same. The absolute capability of the frontier rises fast; the relative ordering among the top labs churns but never settles; and the cost of merely staying in the pack escalates every cycle. This walks the case through the skill's own six-step Process.

## Step 1 — Diagnose

- **Primary competitive investment:** training compute (GPUs/accelerators), the capital and data-center capacity to run them, and the scarce research/engineering talent to use them. Frontier training runs and the infrastructure behind them are the arms.
- **Imitation speed:** roughly one model generation — on the order of months. When one lab ships a materially stronger model, rivals close much of the gap with a comparable release within a similar window, and capability benchmarks that one lab tops are frequently overtaken shortly after.
- **Margin trend:** frontier model development has been heavily loss-making for the leading labs through this period. Revenue has grown quickly, but training and inference costs — and the capex commitments behind them — have grown at least as fast, so the leading pure-play frontier labs were reported to be spending well in excess of revenue.
- **Are all major competitors investing at roughly the same rate?** Yes. Multiple large players are all committing very large sums to compute and data centers in the same window, and the biggest cloud/hyperscaler backers publicly raised their AI-related capital-expenditure guidance repeatedly across 2024–2025.

## Step 2 — Confirm Red Queen

- Absolute performance improving for all (Y): frontier model capability rose steeply and continuously across the field.
- Relative share/position stable-but-contested (Y): no lab established a durable, uncontested lead; the "best model" title changed hands repeatedly and quickly.
- Investment to maintain position growing (Y): the compute and capital required just to stay at the frontier increased each generation.
- Margins thin/negative despite high activity (Y): frontier training remained deeply unprofitable for the leading pure-play labs despite rapid revenue growth.

Four of four → **Red Queen confirmed.** All the running keeps each lab in roughly the same relative place while the treadmill speeds up.

## Step 3 — Map imitation speed

The half-life of a frontier-capability advantage is short — measured in months, not years. A benchmark lead is routinely matched or exceeded by the next competitor release. And imitation speed is **accelerating** in some respects: the diffusion of methods (RLHF/RLAIF, mixture-of-experts, reasoning/inference-time compute, distillation) plus the emergence of strong open-weight models means that a given capability level becomes broadly reproducible faster than before. Distillation and open-weight releases in particular compress the time for a frontier result to become widely available.

## Step 4 — Identify escape vector

- **Differentiation:** compete on an axis rivals under-serve — enterprise trust/safety, reliability, vertical depth, developer experience, or agentic/product surface — rather than only on raw benchmark score.
- **Vertical integration:** control a compute layer rivals rent externally — custom silicon and secured, long-term data-center/energy capacity — to blunt the cost treadmill.
- **Technology generation gap:** a new architecture or training paradigm (e.g., shifting the axis of competition from pretraining scale toward inference-time reasoning, or efficiency breakthroughs) that partly obsoletes the current pure-scale race.
- **Geographic / regulatory avoidance:** markets or deployment contexts where incumbents are structurally constrained.
- **Platformization:** become the environment competitors and downstream builders run inside — the default API/model layer, distribution, and ecosystem lock-in — so that switching costs and data flywheels retain value the raw model cannot.

## Step 5 — Calculate running cost vs. escape cost

- **Annual cost to maintain position:** very high and rising — the multi-billion-dollar compute and data-center commitments are the price of a seat at the frontier, not a winning move.
- **Probability of winning from inside the race:** low for "permanent lead." With months-long imitation half-lives and no strong structural moat on model quality alone, staying in the scale race mostly buys survival to the next, more expensive round.
- **Cost / expected value of escape:** platformization and vertical integration (custom silicon + secured energy/compute + ecosystem lock-in) are expensive and slow but produce durability that a raw benchmark lead does not. Distribution and switching costs — not model weights — are where captured value persists.

## Step 6 — Decide

- **Run faster** only where there is a genuine near-term winning condition (a real generation lead you can convert into distribution before it is copied). Pure benchmark-matching is table stakes.
- **Change tracks** is the durable answer: convert transient capability leads into platform, distribution, ecosystem, and integrated-compute advantages that survive the next model release — because the model advantage itself will not.
- **Exit / narrow** is rational for players without the capital or a differentiated axis: specialize, build on open weights, or serve a defensible vertical rather than fund an unwinnable scale race.
- **Timing:** treat each capability lead as a months-long window, and allocate toward escape vectors *before* the sunk-cost logic of "we can't afford not to keep spending" becomes the company's primary organizing principle.

**Operational lesson for founders and operators:** in the frontier-AI race the running is real and the absolute progress is genuine — but relative position among the leaders is not durably purchased by compute alone. The value of the arms race accrues heavily to users (rapidly cheaper, more capable models) and to the compute suppliers; the escape is to own a layer the race cannot immediately replicate.

*Sources: Van Valen, L. (1973), "A New Evolutionary Law," Evolutionary Theory 1:1–30; Carroll, L. (1871), Through the Looking-Glass, Ch. 2; Barnett, W. P. (2008), The Red Queen Among Organizations, Princeton University Press. Contemporary context on frontier-lab compute and capex escalation drawn from widely reported 2024–2026 public disclosures and reporting by major hyperscalers and AI labs (e.g., published capital-expenditure guidance and earnings commentary). Specific figures are omitted or qualified where exact public values were not verified.*
