**1-D dynamic programming** solves a problem by breaking it into subproblems that line up along a single index — `dp[i]` means "the answer for the first `i` elements" (or "ending at index `i`"). Each state is built from a small number of earlier states, so you never re-solve the same subproblem twice.

The core insight is **overlapping subproblems + optimal substructure**: the naive recursive solution (e.g. plain Fibonacci, or "rob this house or skip it") branches exponentially, but most branches recompute the exact same smaller inputs. Caching those results — top-down with memoization, or bottom-up with a table — collapses the runtime from exponential to O(n).

A typical bottom-up shape:

```
dp = array of size n
dp[0] = base case
for i from 1 to n-1:
    dp[i] = combine(dp[i-1], dp[i-2], ..., element[i])
return dp[n-1]
```

Most 1-D DP problems reduce to one of a few recurrences: **take-or-skip** (House Robber — either use element `i` or don't), **best-of-k-choices** (Coin Change — try every coin/step size and keep the best), or **running/extending state** (Longest Increasing Subsequence, Kadane's Maximum Subarray — extend the previous chain or start fresh).

**Space optimization** is the natural next step: if `dp[i]` only depends on the last one or two entries, you don't need the whole array — two or three rolling variables suffice, dropping space from O(n) to O(1). Recognizing when a table collapses to a handful of variables is a strong interview signal that you understand the pattern, not just memorized the code.
