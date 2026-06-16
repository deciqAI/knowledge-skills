# Method in Action: Pólya at Stanford and Schoenfeld at Berkeley (1942 → 1985)

> *Example for the [metacognition](../SKILL.md) skill.*

A worked example. Not folklore — university teaching records and peer-reviewed experimental data.

In 1942, **George Pólya** — by then one of the world's leading mathematicians (Hungarian-American, Stanford from 1942) — published *How to Solve It* as a deliberate **operational protocol for monitoring mathematical reasoning**. The book sold over 1 million copies in 17 languages and became one of the most-cited mathematics-education texts of the 20th century. Pólya's claim was that mathematical genius was less about raw intelligence and more about **disciplined monitoring** of the four-stage process; the four stages were not new ideas but a *checklist to keep monitoring loops active*.

For decades, Pólya's claim was treated as plausible-but-unproven. The empirical test came from **Alan Schoenfeld** at the University of California, Berkeley, beginning in 1979 and culminating in his 1985 book *Mathematical Problem Solving* (Academic Press). Schoenfeld's experimental setup:

- Recruit expert mathematicians (PhD-holding research mathematicians) and undergraduate students with completed calculus
- Give both groups the *same* hard problems (non-routine math problems at the level of an Olympiad)
- Videotape every problem-solving session
- Code each minute of activity: was the subject *executing* (working forward on a strategy) or *monitoring* (questioning the strategy, evaluating progress, considering a switch)?

The result, summarized in Schoenfeld's data tables (1985, ch. 4):

> "Mathematicians characteristically spent 30 to 40 percent of their problem-solving time on monitoring and regulatory activity. Students … characteristically spent less than 5 percent of their time on monitoring. The students continued to execute on their initial strategy for the full session even when no progress had been made for 20 minutes."
> — Alan H. Schoenfeld, *Mathematical Problem Solving* (Academic Press, 1985), ch. 4, p. 110.

Schoenfeld then ran the critical follow-up: he taught students to use Pólya's four-stage protocol explicitly, with prompts like "Why are you doing this?" and "What are you trying to accomplish?" interrupting them every 5 minutes during problem-solving practice over a semester. The treated students' problem-solving performance on *new* problems — held out of the training — improved by approximately one full standard deviation on standardized assessments (Schoenfeld 1985, ch. 9). **Metacognition was learnable, distinct from domain knowledge, and load-bearing for performance.**

Walk the protocol on a Schoenfeld-class problem (illustrative): *"Prove that for any integer n ≥ 0, the number 4^n + 6n − 1 is divisible by 9."*

- **Understand (Stage 1):** Restate: I need to show 9 | (4ⁿ + 6n − 1) for all n ≥ 0. Honest check: I recognize this as a number-theory divisibility problem — but do I understand *why* this specific combination? Not yet.
- **Plan (Stage 2):** Strategy: try induction on n. Reason for this strategy: the form "for all n ≥ 0" is the canonical induction signal; also, 4ⁿ is multiplicative in n, suggesting the inductive step will use 4ⁿ⁺¹ = 4·4ⁿ. Time budget: 20 minutes.
- **Execute (Stage 3):** Base case n=0: 4⁰ + 6·0 − 1 = 0, divisible by 9. ✓ Inductive step: assume 9 | (4ⁿ + 6n − 1); show 9 | (4ⁿ⁺¹ + 6(n+1) − 1). Compute: 4ⁿ⁺¹ + 6n + 5 = 4·4ⁿ + 6n + 5. Subtract the inductive hypothesis (mod 9): 4·4ⁿ + 6n + 5 − (4ⁿ + 6n − 1) = 3·4ⁿ + 6. Need: 9 | (3·4ⁿ + 6), i.e., 3 | (4ⁿ + 2). Since 4 ≡ 1 (mod 3), 4ⁿ ≡ 1 (mod 3), so 4ⁿ + 2 ≡ 0 (mod 3). ✓ Monitoring check at minute 12: am I genuinely understanding this, or just symbol-manipulating? Looking back at each step, the logic flows; I understand. ✓
- **Look back (Stage 4):** The proof worked. Meta-lesson: when a divisibility-for-all-n problem has a non-trivial structure, induction with mod-arithmetic on the difference is often the right tactic; the monitoring move that mattered was the minute-12 honesty check that flagged "am I just pushing symbols?"

This is what Schoenfeld measured experts doing routinely and students failing to do. The framework's payoff is not "solve this specific problem"; it is **the monitoring loop transfers across problems**. The student who learned to ask "am I just pushing symbols?" in calculus asks it in their first job analyzing financial data. **Metacognition is the most transferable skill in cognition.**
