# Method in Action: Loss Aversion on the PGA Tour — Par Putts vs. Birdie Putts (2011)

> *Example for the [loss-aversion-prospect-theory](../SKILL.md) skill.*

The Pope-Schweitzer golf study is the strongest field test of loss aversion under conditions designed to kill it: the most experienced professionals in the world, enormous financial stakes, thousands of repetitions, and immediate feedback. If loss aversion were a lab artifact, it should vanish on the PGA Tour. It does not.

**The decision:** Economically, every stroke in a golf tournament counts exactly the same toward final score and prize money. A putt attempted for birdie and an identical putt attempted for par — same distance, same green, in some cases the same hole location on the same day — are the same physical and financial problem. "Par" is a number printed on the scorecard with no economic content. It is, in prospect-theory terms, a pure reference point.

**The prediction:** Prospect theory says missing a par putt is coded as a *loss* (dropping to bogey), while missing a birdie putt is coded as a *forgone gain* (settling for par). Because losses loom larger than gains, players should invest more precision in par putts than in economically identical birdie putts.

**The evidence:** Pope and Schweitzer analyzed over 2.5 million putts recorded by the PGA Tour's ShotLink laser-measurement system, controlling for putt distance, player fixed effects, hole and green characteristics, and — in the tightest specification — putts attempted from nearly the same spot on the same green. The result: par putts were sunk at a rate roughly two percentage points higher than otherwise comparable birdie putts. The mechanism check confirmed the risk-attitude signature of the value function: birdie putts were struck less firmly and were more likely to be left short — risk-averse "lay-up" behavior in the gain frame — while par putts were struck with more commitment in the loss frame.

**The counter-conditions all failed:** The bias persisted among the very best players in the world, including Tiger Woods; it shrank only modestly with experience; and it survived the last rounds of tournaments, when prize-money differences per stroke are largest. Expertise, stakes, and repetition attenuated but did not eliminate the reference-point distortion.

**The cost:** The authors estimated the bias costs a professional on the order of one stroke per 72-hole tournament — for top players, worth on the order of a million dollars a year in forgone prize money. This is a pure expected-value giveaway to an arbitrary reference point, paid by agents with every incentive and every opportunity to correct it.

**The corrective:** Because the bias survives awareness and expertise, the fix is procedural, not motivational: erase the scorecard reference point and treat every putt identically — strike each one with the commitment reserved for par putts. Several players and coaches have described exactly this discipline; the study explains why it is worth a stroke per tournament.

The mapped steps:

1. **Specify decision:** how firmly to strike a given putt; options are aggressive vs. cautious lines; the implicit reference point is par, imported from the scorecard and economically arbitrary.
2. **Compute EV:** every stroke counts equally toward score and prize money, so two putts of identical distance and lie have identical EV regardless of whether they are "for" birdie or par.
3. **Identify distortions:** reference dependence plus loss aversion — the loss frame (bogey looming) extracts more precision than the gain frame (birdie available); diminishing sensitivity shows up as cautious, short-left birdie putts.
4. **Reframe and re-test:** hold the physical putt constant and vary only the frame; the ~2-percentage-point accuracy gap on matched putts shows the frame, not the golf, is doing the work.
5. **Choose decision rule:** stakes are moderate and massively repeatable → maximize EV; override the reference point and putt every ball as if for par.
6. **Document:** roughly one stroke per tournament recoverable; because the bias persists in experts, the override must be built into routine rather than left to awareness.

**Why this case matters for the skill:** It answers the most common rationalization against debiasing — "experts under real stakes don't do this." They do, at a measurable rate, with real money on the table. When a client claims immunity to loss aversion by virtue of experience, cite this case and move directly to Step 2: compute the EV, make the reference point explicit, and check whether behavior differs across frames of the economically identical choice. If the world's best golfers pay a stroke per tournament to an arbitrary reference point, self-rated immunity is not evidence.

Primary source: Pope, D. G., & Schweitzer, M. E. (2011). "Is Tiger Woods Loss Averse? Persistent Bias in the Face of Experience, Competition, and High Stakes." *American Economic Review*, 101(1), 129-157.
