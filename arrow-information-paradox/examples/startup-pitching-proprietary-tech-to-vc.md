# Method in Action: A Startup Pitching Proprietary Tech to a VC

> *Example for the [arrow-information-paradox](../SKILL.md) skill.*

A common early-stage founder anxiety is a pure instance of Arrow's paradox: *"If I explain how our technology actually works, the VC — or one of their portfolio companies — could just take it. But if I don't explain it, how will they know it's worth funding?"* This composite case (not a single named company) walks the founder's disclosure decision through The Process. The date context is July 2026; the AI-era version of this problem is sharper than ever, because a described mechanism can be re-implemented faster than at any prior time.

**Step 1 — Audit appropriability.** The information is the startup's core mechanism — say, a proprietary model architecture and training pipeline that produces materially better results than off-the-shelf approaches. The concrete leak: a VC hears many pitches and funds competitors; a described architecture could be passed (deliberately or by osmosis) to a portfolio company that out-executes the startup. That is a nameable leak. Gate passed. (Note the standard reality: VCs rarely sign NDAs at a first meeting, and asking signals inexperience — so an NDA is *not* on the table as the primary mechanism.)

**Step 2 — Identify the minimum the VC needs.** A VC does not need to reproduce the technology to fund it. They need to update on: *does it work, is it better than alternatives, is there traction, can this team execute?* Those are **outcome** questions. The reproducible core — how the mechanism is actually built — answers a *reproduction* question the VC does not need answered to write a check. The convince-vs-reproduce gap is wide.

**Step 3 — Choose the mechanism.** With NDAs off the table, the fitting stack is **proxy demonstration + reputation**, with the reproducible core reserved for **staged disclosure** post-term-sheet.
- *Proxy demonstration:* a live demo on the VC's own or a neutral held-out dataset; benchmark results against named baselines; metrics (retention, unit economics). These prove *outcomes* without exposing *mechanism*.
- *Reputation:* prior shipping track record and traction substitute evidence-of-capability for disclosure.
- *Staged disclosure:* the training pipeline / weights / exact architecture are shown only in confirmatory technical diligence *after* a term sheet, when the VC has a real commitment and the information is protected by the deal's confidentiality terms.
This closes the specific leak — the VC gets everything they need to value the company without ever holding the thing a competitor could copy.

**Step 4 — Build the disclosure ladder.**
```
Rung 1 (first meeting, no commitment): problem, market, demo on neutral data, headline metrics, team track record
Rung 2 (partner meeting / interest):   deeper metrics, architecture at a *behavioral* level, references
Rung 3 (post-term-sheet diligence):    reproducible core — pipeline, model details — under deal confidentiality
```
The reproducible core sits on Rung 3, gated by a term sheet. No rung reveals more than its commitment justifies.

**Step 5 — Pre-commit the walk-away.** Before pitching, the founder decides: *the training pipeline and weights are not shown pre-term-sheet, no matter how engaged the VC seems.* The "they seem really interested, let's just show them the architecture to close it" impulse is exactly the move the paradox punishes.

**Disclosure Plan:**
```
# Disclosure Plan: proprietary model tech → VC
## The information: model architecture + training pipeline producing better results
## Appropriability leak: VC funds/tells a competing portfolio company; described mechanism gets re-implemented
## Minimum-to-convince: it works, it's better, there's traction, the team can execute (all outcomes)
## Reproducible core (Rung 3 only): training pipeline, weights, exact architecture
## Mechanism: proxy demo + reputation now; staged disclosure of core post-term-sheet (NDAs not available)
## Disclosure ladder:
   Rung 1 (first meeting):        demo on neutral data, metrics, team track record
   Rung 2 (interest):             behavioral architecture, references, deeper metrics
   Rung 3 (post-term-sheet):      pipeline / model details under deal confidentiality
## Walk-away: do not reveal the pipeline pre-term-sheet, regardless of apparent interest
```

**What it explains.** The founder's fear is real but the remedy is not secrecy-by-silence — it is *disclosing the right layer*. Outcomes fund companies; mechanisms get copied. By proving value on a proxy and holding the reproducible core behind a term-sheet-gated rung, the founder gives the VC near-full ability to value the company with near-zero appropriability leak.

The mapped steps:
1. Audit: mechanism could reach a competitor via the VC → real leak
2. Minimum: VC funds on outcomes, not reproduction → wide gap
3. Mechanism: proxy demo + reputation now, staged core post-term-sheet (NDAs unavailable)
4. Ladder: demo/metrics → behavioral architecture → core under deal confidentiality
5. Walk-away: pipeline stays locked pre-term-sheet

**Founder takeaway:** Do not solve pitch-anxiety by refusing to disclose (you'll fail to raise) or by over-disclosing (you'll leak your edge). Solve it by layering: traction, a demo on real data, and your track record prove value; the reproducible core waits behind the term sheet. In the AI era especially, a described mechanism is a re-implemented mechanism — so your durable appropriability is execution speed and reputation more than secrecy.

*Sources: Arrow, K. J. (1962). "Economic Welfare and the Allocation of Resources for Invention." In *The Rate and Direction of Inventive Activity: Economic and Social Factors*, NBER, Princeton University Press, pp. 609–626 (https://www.nber.org/system/files/chapters/c2144/c2144.pdf). The norm that VCs generally decline to sign NDAs on first contact is widely documented in startup-fundraising guidance; this case is a composite illustration, not an account of a specific company or fund. The "described mechanism re-implemented faster in the AI era" observation is presented as a contemporary (July 2026) framing, not an empirical claim from a cited study; the related "Reverse Information Paradox" inversion was named publicly by Satya Nadella (post on X, 12 July 2026).*
