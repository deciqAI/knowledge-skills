# Method in Action: Axelrod's Computer Tournament (1980)

> *Example for the [non-zero-sum](../SKILL.md) skill.*

Primary-source-documented case. Axelrod ran the first computer Prisoner's Dilemma tournament in 1980, inviting submissions from specialists in game theory across multiple disciplines. He ran a second tournament in 1981 with 62 entries. Both are fully documented in *The Evolution of Cooperation* (1984).

**Step 1 — Positions vs. interests:**
In the Prisoner's Dilemma (as in most real strategic interactions), the *position* of each player is "defect if the other defects, cooperate only if cooperation is guaranteed." The *interest* of each player is to maximize total accumulated payoff over repeated interactions. These are not the same.

**Step 2 — Payoff matrix:**
Mutual cooperation: both players receive R (reward). Mutual defection: both receive P (punishment, worse than R). Temptation: one defects while the other cooperates — defector receives T (temptation, highest single-round payoff); cooperator receives S (sucker's payoff, lowest). The standard ordering: T > R > P > S. The non-zero-sum gap: if both cooperate repeatedly (R per round) vs. if both defect repeatedly (P per round), the cooperation stream produces more total value. The gap is the non-zero-sum dividend.

**Step 3 — Shadow of the future:**
The tournament was designed as iterated (indefinitely repeated) interactions. Axelrod showed mathematically that the minimum condition for Tit-for-Tat to be the stable strategy is: the discount factor (how much each player values future payoffs) must exceed (T − R) / (T − P). When interactions are repeated and future payoffs are valued, defection becomes irrational even for purely self-interested players.

**Step 4 — Cooperation mechanism:**
Direct reciprocity (Tit-for-Tat) was the winning mechanism in both tournaments. Tit-for-Tat's structural properties: (a) it starts cooperating (not exploitable through pre-emptive defection); (b) it retaliates immediately (defectors receive P immediately, not with delay); (c) it forgives after one retaliation (the relationship can recover, unlike strategies that defect forever after one betrayal). These properties map precisely to what makes cooperation self-sustaining.

**Step 5 — First move:**
Axelrod's result: the optimal first move is unconditional cooperation, combined with credible and immediate retaliation capability. Strategies that started defecting never recovered: they generated defection spirals that left both parties worse off than the mutual cooperation equilibrium.

**What the tournament shows:** Cooperation can emerge and be sustained in non-zero-sum repeated interactions *without* any central authority, enforcement mechanism, or moral instruction. The self-sustaining mechanism is the payoff structure itself, combined with a sufficiently strong shadow of the future. The implication for institutional design: if you want cooperation, ensure the interaction is repeated, make defection immediately visible, and create recovery paths after retaliation.

**Source:** Axelrod, Robert. *The Evolution of Cooperation.* Basic Books, 1984. The complete tournament design, results, and theoretical framework are in chapters 1–5. Mathematical proofs for the stability conditions are in the Appendix.
