# Method in Action: M&A Tech Due Diligence — Revealing Enough to Be Valued Without Giving Away the Technology

> *Example for the [arrow-information-paradox](../SKILL.md) skill.*

When a technology company is being acquired, due diligence is Arrow's paradox at industrial scale. The acquirer must inspect the target's technology to price it. But the acquirer is frequently also a *potential competitor* — and even a genuine acquirer can walk away from the deal having learned how the target's technology works. The target must reveal enough to be valued without handing over the very asset being sold. This composite case walks a target's disclosure strategy through The Process.

**Step 1 — Audit appropriability.** The information is the target's core technology: source code, architecture, key algorithms, and process know-how that constitute its advantage. The concrete leak: a "buyer" conducting deep technical diligence and then abandoning the deal has effectively received a guided tour of the crown jewels — enough to build, buy, or fund a substitute. A distinct, nameable leak. Gate passed.

**Step 2 — Identify the minimum the acquirer needs.** The acquirer needs to confirm: the technology exists and works as claimed, it is not encumbered (clean IP ownership, no fatal open-source or licensing problems), it is maintainable, and it scales. Most of these are *verification* questions answerable by a qualified inspector — they do not require the acquirer's own engineers to read every line and internalize the design. The convince-vs-reproduce gap is real and exploitable.

**Step 3 — Choose the mechanism.** The fitting stack is **staged disclosure gated by an LOI + exclusivity**, plus a **trusted intermediary / clean team**, plus **source escrow**, with an **NDA as the floor**.
- *NDA as floor:* signed before anything, with non-compete/non-solicit terms — necessary but not sufficient (it does not stop what an engineer *learns and remembers*).
- *LOI + exclusivity gate:* the sensitive rungs open only after a letter of intent with exclusivity, so the target is not giving a guided tour to a party still shopping.
- *Trusted intermediary / clean team:* the most sensitive IP is reviewed by a neutral technical assessor or a "clean team" (individuals walled off from the acquirer's competing product teams) who certify findings to the acquirer *without passing the code through* the acquirer's own engineers.
- *Source escrow:* source is escrowed with a neutral agent, released on closing, rather than handed over during diligence.
This closes the specific leak: the acquirer gets certified answers to its value questions without the target's competitors-in-waiting reading the source.

**Step 4 — Build the disclosure ladder.**
```
Rung 1 (NDA):                    architecture at a high level, capability claims, redacted metrics
Rung 2 (LOI + exclusivity):      deeper technical review by a trusted intermediary / clean team; IP-ownership audit
Rung 3 (signed deal / escrow):   full source released to the acquirer only at/after closing, via escrow
```
The reproducible core — full source — sits on Rung 3, released against a binding, closed deal.

**Step 5 — Pre-commit the walk-away.** Before diligence opens, the target sets: *no full-source access, and no unfiltered access to key engineers, before an LOI with exclusivity; the most sensitive IP goes through a clean team, not the acquirer's own product engineers.* The pressure move to resist is "the acquirer's team wants to review the code themselves to get comfortable" *before* committing — the exact move the paradox punishes.

**Disclosure Plan:**
```
# Disclosure Plan: target's core technology → acquirer
## The information: source, architecture, key algorithms, process know-how
## Appropriability leak: a walk-away "buyer" learns enough to build/buy/fund a substitute
## Minimum-to-convince: tech works, IP is clean, it scales, it's maintainable (verification, not reproduction)
## Reproducible core (Rung 3 only): full source code
## Mechanism: NDA floor + LOI/exclusivity gate + clean-team/intermediary review + source escrow
## Disclosure ladder:
   Rung 1 (NDA):                high-level architecture, capability claims, redacted metrics
   Rung 2 (LOI + exclusivity):  clean-team technical review, IP-ownership audit
   Rung 3 (closing / escrow):   full source via escrow at/after close
## Walk-away: no full source and no unfiltered engineer access before LOI + exclusivity
```

**What it explains.** The target cannot simply "open the repo" for an acquirer to value it — that would hand the asset to a party who might walk (or who is really scouting). By routing the sensitive core through a clean team and escrow and gating the deep rungs behind an LOI with exclusivity, the target lets the acquirer *verify* value without *acquiring* the technology prematurely. The intermediary is doing the paradox's heavy lifting: near-full information to the buyer, near-zero leak of the reproducible core.

The mapped steps:
1. Audit: a walk-away buyer/scout gets the crown jewels → real leak
2. Minimum: acquirer needs verification, not reproduction → exploitable gap
3. Mechanism: NDA floor + LOI/exclusivity + clean team/intermediary + escrow
4. Ladder: high-level (NDA) → clean-team review (LOI) → full source (closing)
5. Walk-away: no core access before exclusivity

**Founder takeaway:** If your company is being acquired, treat diligence as a disclosure ladder, not an open house. An NDA is the floor, not the wall — it can't un-teach what an engineer reads. Gate deep technical review behind an LOI with exclusivity, route the crown jewels through a clean team or neutral assessor, and escrow source for release at closing. The acquirer can value you fully without ever holding the thing a competitor could rebuild.

*Sources: Arrow, K. J. (1962). "Economic Welfare and the Allocation of Resources for Invention." In *The Rate and Direction of Inventive Activity: Economic and Social Factors*, NBER, Princeton University Press, pp. 609–626 (https://www.nber.org/system/files/chapters/c2144/c2144.pdf). Adverse-selection cousin: Akerlof, G. A. (1970). "The Market for Lemons." *Quarterly Journal of Economics*, 84(3), pp. 488–500 (https://doi.org/10.2307/1879431). Clean-team, escrow, and staged-diligence practices are standard in technology M&A; this case is a composite illustration, not an account of a specific transaction.*
