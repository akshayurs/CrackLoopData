Reach for a 2-D DP table the moment a problem gives you **two sequences, or one sequence plus a budget**, and asks for an optimum or a count:

- **"Given two strings…"** — longest common subsequence, edit distance, interleaving, wildcard/regex matching. Two indices in, one recurrence out.
- **"Number of ways to reach the bottom-right corner"** — grid problems with obstacles or costs (Unique Paths, Minimum Path Sum, Dungeon Game). The two indices are the row and column.
- **"Subset that sums to / is within a target"** — 0/1 Knapsack, Target Sum, Coin Change II, Ones and Zeroes. One dimension is the item index, the other is remaining capacity or target.
- **"Longest/count of palindromic substrings"** — `dp[i][j]` = is `s[i..j]` a palindrome, built from `dp[i+1][j-1]`.
- **"Minimum number of operations to convert A into B"** — insert/delete/replace, classic Edit Distance phrasing.

Signal words: *"two strings"*, *"subsequence"*, *"edit distance"*, *"grid"*, *"paths"*, *"ways to reach"*, *"subset sum"*, *"partition into two equal…"*, *"knapsack"*, *"palindromic substring"*.

A strong tell versus 1-D DP: the state cannot be described by a single index. If you find yourself wanting to write `dp[i]` but the recurrence keeps needing "and also where we are in the other string/the capacity used so far," that second variable belongs in the state — promote it to `dp[i][j]`.

If brute force would be trying every pair of cut points, every alignment, or every subset, and the problem has small-ish bounds (≤ ~1000² or ≤ ~10⁴ item-capacity pairs), that is the cue: define the two-parameter state, write the recurrence for one cell in terms of a few neighbors, then fill the table in the right order (usually row by row, or by increasing substring length for interval problems).
