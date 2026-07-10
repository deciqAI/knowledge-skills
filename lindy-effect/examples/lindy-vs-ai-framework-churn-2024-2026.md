# Method in Action: Lindy vs. AI-Framework Churn in the 2024–2026 Tech Stack

> *Example for the [lindy-effect](../SKILL.md) skill.*

The decision facing most engineering teams in the 2024–2026 AI build-out: when you assemble a new AI application, which layers do you bet on the time-tested foundations for, and which layers do you deliberately keep on the fast-churning new tools? The Lindy effect does not say "never use the new" — it tells you *where* the survival evidence is, so you can put the durable choices in your load-bearing tier and the disposable choices where you can afford to rip and replace.

This walks the anchor case through the skill's own Process.

## Step 1 — Items

- **Old items (approximate ages, as of 2026):** SQL / the relational model (Codd's relational model 1970; SQL from the mid-1970s, ~50 years), Unix and its POSIX interface (1969–1971, ~55 years), email/SMTP (SMTP standardized 1982, ~40 years), TCP/IP (deployed on ARPANET on 1 January 1983, ~40 years), HTTP/the web (~35 years).
- **New items (approximate ages):** the current generation of AI application frameworks, agent orchestration libraries, and vector/AI tooling — most under ~3 years old, many under 18 months, with a churn rate high enough that popular libraries are rewritten or abandoned within a year or two.
- **Decision:** for a production AI application, which layers do we anchor on Lindy-strong foundations and which do we leave on the churning new layer?
- **Time horizon:** the app is meant to run for 5–10+ years.
- **Switching cost:** very high for the foundational layers (data model, transport, deployment substrate), low-to-moderate for the AI-orchestration layer (glue code that can be rewritten).

## Step 2 — Applicability

- **Non-perishable?** Yes. Protocols, data models, and interfaces are ideas/standards, not organisms with deterministic life cycles. Lindy applies.
- **Elimination forces operating?** Yes — and this is the crux. SQL, Unix, email, and TCP/IP have not merely persisted; they have survived *repeated, well-funded attempts to replace them*. The NoSQL wave of the early 2010s was pitched as the end of the relational database; a decade later SQL is more central than ever, and many "NoSQL" systems added SQL-like query layers. This is survival under active competitive pressure, not survival by regulatory lock-in — exactly the condition Lindy requires.
- **Power-law plausible?** Yes. Technology-adoption survival is a canonical fat-tailed domain: a small number of standards carry the overwhelming majority of the infrastructure, and their remaining life scales with their current age.
- **Conditions changed?** The "AI changes everything" claim must be examined in Step 4 — but note it up front as the this-time-is-different candidate.

## Step 3 — Lindy prior

- **Old remaining life (≈ current age):** a ~50-year-old foundation like SQL has a Lindy prior of roughly another ~50 years; ~40-year-old TCP/IP and SMTP, roughly another ~40. These are order-of-magnitude priors, not forecasts.
- **New remaining life:** a framework that is ~1–2 years old has a Lindy prior measured in *the same one-to-two-year order* — its expected remaining life is short precisely because its track record is short.
- **Ratio:** the durability gap between the foundational tier and the AI-orchestration tier is roughly an order of magnitude or more. That gap is the whole decision.

## Step 4 — This-time-is-different

- **Claim:** "AI is a genuine paradigm shift, so the old stack is being obsoleted and we should build natively on the new AI-first tools."
- **Evidence:** AI genuinely changed one layer — the model/inference layer and the interface patterns around it (prompting, retrieval, agents). That is real novelty and the new tools legitimately live there.
- **Verdict:** the claim is *partially* true but does not transfer to the foundations. AI models still store their data in relational databases and object stores, still run on Unix-family servers and containers, still talk over TCP/IP and HTTP, and still send email. The paradigm shift sits *on top of* the Lindy-strong substrate, not in place of it. So "this time is different" is granted for the model/orchestration layer and denied for the foundational layers. Name which condition changed (the intelligence layer) and confirm it does not invalidate the survival evidence for transport, storage, and OS interfaces — it does not.
- **Cost if wrong:** betting the foundational tier on a 1-year-old AI-native framework risks a forced, expensive migration when that framework is abandoned — the high-switching-cost tier is the worst place to absorb churn.

## Step 5 — Decision

**Hybrid, split by layer.**

- **Load-bearing tier → lean Lindy.** Keep data on SQL/relational (or well-established object storage), keep the deployment substrate on Unix/Linux and standard containers, keep transport on TCP/IP and HTTP, keep messaging on email/SMTP where email is the job. High switching cost + long horizon = high Lindy weight.
- **Exploration tier → lean new.** Put the fast-moving AI frameworks, agent libraries, and model SDKs in the orchestration/glue layer, where switching cost is low and you *expect* to rewrite. Isolate them behind your own interfaces so churn stays contained.
- **Lindy weight documented:** high for storage/transport/OS, low for the AI-orchestration layer. The point is not old-vs-new tribalism; it is matching each layer's durability requirement to the survival evidence available for the candidates.

## Step 6 — Reversibility

Because the AI-orchestration layer is deliberately a bet *against* Lindy (using the young tool on purpose), design for reversal:

- **Reversal plan:** wrap each churning dependency behind an internal interface (an adapter/port) so swapping a framework is a contained change, not a rewrite.
- **Reversal signals:** the library's release cadence stalls, maintainers step away, the community migrates to a successor, or a breaking rewrite lands — any of these triggers re-evaluation.
- **Monitoring owner:** the team that owns the orchestration layer tracks the health of each young dependency and holds the swap decision.

---

**The core lesson of the anchor case:** the Lindy effect here is not a verdict that "old beats new." It is an allocation rule. Use longevity as a predictor of longevity where longevity is what you need — the load-bearing foundations — and spend your novelty budget on the exploration layer where you can afford to be wrong. SQL, Unix, email, and TCP/IP earned their place in the foundation by outliving every "this replaces it" cycle so far, including, so far, the AI wave itself.

*Sources: Codd, E. F. (1970), "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM 13(6); Ritchie & Thompson, Unix (Bell Labs, 1969–1971); Postel, J. (1982), RFC 821 (SMTP); the ARPANET TCP/IP transition of 1 January 1983 (RFC 801); Berners-Lee, the World Wide Web (CERN, 1989–1991); Taleb, N. N. (2012), Antifragile, Random House; Reinhart, C. M., & Rogoff, K. S. (2009), This Time Is Different, Princeton University Press.*
