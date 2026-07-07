# Method in Action: Penalty Kicks and the Minimax Test (1995-2003)

> *Example for the [nash-equilibrium](../SKILL.md) skill.*

Mixed-strategy Nash equilibrium makes a strange prediction: in games with no stable pure strategy, rational players should randomize — and randomize in exactly the proportions that make their opponent indifferent between responses. For decades this prediction fared poorly in laboratory experiments, where subjects failed to randomize properly. The economist Ignacio Palacios-Huerta asked a sharper question: do *professionals*, playing for real stakes at the top of their craft, play the equilibrium? He tested it on soccer penalty kicks.

**Specify the game (Step 1).** Two players: kicker and goalkeeper. A penalty kick travels to the goal in roughly a third of a second — too fast for the keeper to react to the ball — so both players effectively choose simultaneously: kicker aims to his natural side or the opposite side; keeper dives one way or the other. Payoffs are opposed: the kicker wants to score, the keeper wants to save. Information is public — professional teams scout each other's penalty histories.

**Best-response analysis (Step 2).** No pure strategy survives: if the kicker always shoots to his natural side, the keeper's best response is to always dive there, at which point the kicker's best response flips — and so on, forever. The best-response cycle never settles on a deterministic pair.

**Identify the equilibrium (Step 3).** The game has a unique mixed-strategy Nash equilibrium (the minimax solution, since the game is zero-sum). Each player randomizes with probabilities that make the opponent indifferent. The equilibrium yields two testable predictions: (a) each player's success rate must be *equal* across his own actions — if kicking left scored more often than kicking right, he should kick left more, contradicting equilibrium; (b) each player's sequence of choices must be *serially independent* — any detectable pattern could be exploited.

**Evaluate against data (Step 4).** Palacios-Huerta assembled roughly 1,400 penalty kicks from professional league matches in Spain, Italy, and England (1995-2000), recording kicker, keeper, direction, and outcome. Both predictions held. Scoring probabilities were statistically indistinguishable across a kicker's directions (in the neighborhood of 80% overall), and keepers' save rates were likewise equal across their choices. Player-by-player tests could not reject equality of payoffs for the overwhelming majority of individuals. And unlike laboratory subjects — who notoriously over-alternate when asked to randomize — professionals' direction choices passed standard tests of serial independence. Professionals play minimax.

**Act or redesign (Step 5).** For the players there is nothing to redesign: the equilibrium *is* the optimal policy, and any deviation from it is exploitable. The operational lesson runs the other way — if you face a rival in a genuinely opposed, repeated interaction (competitive bidding, audit scheduling, security patrols), the equilibrium prescribes calibrated unpredictability, and your rival's data on you is the test of whether you achieved it.

**Plan counterparty response (Step 6).** A kicker with a detectable bias hands the keeper a profitable deviation; scouting departments exist precisely to find such biases. Equilibrium play is the only strategy that leaves no pattern for the counterparty to exploit — the contingency plan is built into the randomization itself.

The mapped steps:
1. Specify the game: kicker vs. keeper, simultaneous moves, opposed payoffs, public histories
2. Best-response analysis: no pure strategy is a mutual best response; the cycle never settles
3. Equilibria: a unique mixed-strategy (minimax) equilibrium with equal payoffs across own actions and serially independent choices
4. Evaluate quality: field data on ~1,400 professional kicks matched both equilibrium predictions
5. Act or redesign: equilibrium randomization is the optimal, unexploitable policy
6. Counterparty response: any bias is scouted and punished; unpredictability is the defense

Primary source: Palacios-Huerta, I. (2003). "Professionals Play Minimax." *Review of Economic Studies*, 70(2), 395-415.
