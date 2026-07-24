Reach for backtracking the moment a problem asks you to enumerate rather than compute a single number:

- **"Return all possible …"** — subsets, permutations, combinations, partitions. If the output is a list of lists, not a single value, backtracking is almost always in play.
- **"Generate all valid …"** — parentheses, IP addresses, phone-number letter combinations. Build character by character, prune invalid prefixes early.
- **Board / grid placement with constraints** — N-Queens, Sudoku Solver, Word Search. Place one piece or letter at a time, check row/column/diagonal or path constraints, undo if it fails.
- **"Every way to split/partition a string"** — Palindrome Partitioning: choose a cut point, recurse on the remainder, backtrack the cut.
- **Choose-or-skip over a fixed set with a target** — Combination Sum: at each element, either use it (possibly again) or move on, prune once the running sum exceeds the target.
- **Duplicates in the input but unique output required** — Subsets II, Permutations II, Combination Sum II. The signal is "avoid duplicate results" — that's a hint you'll need a sort-then-skip-equal-siblings rule.

Signal words: *"all possible"*, *"all valid"*, *"every combination/permutation/arrangement"*, *"generate"*, *"place N queens/pieces"*, *"solve the puzzle"*. If the answer count could blow up combinatorially and there's no obvious greedy or DP recurrence collapsing it to overlapping subproblems, it's backtracking, not dynamic programming.
