**2-D dynamic programming** builds a table `dp[i][j]` where the answer depends on **two** shrinking parameters instead of one — two string indices, a grid's row and column, or an item index paired with a remaining capacity. Each cell is computed from a small number of neighboring cells, so once you know the recurrence, filling the table is mechanical.

Three shapes cover almost every problem in this bucket:

- **Two-string alignment** — `dp[i][j]` = best answer using `text1[:i]` and `text2[:j]`. Longest Common Subsequence, Edit Distance, Interleaving String.
- **Grid traversal** — `dp[i][j]` = best answer to reach cell `(i, j)`, built from the cell(s) you could have arrived from (usually above and left).
- **Knapsack-style** — `dp[i][cap]` = best answer using the first `i` items with `cap` capacity/sum remaining. 0/1 Knapsack, Coin Change II, Target Sum, Ones and Zeroes.

The recurrence almost always reduces to "did I use this character/item, or not?" — a choice between one or two prior cells.

```
dp = 2D table, sized (n+1) x (m+1), base cases filled on row 0 / column 0
for i from 1 to n:
    for j from 1 to m:
        if characters/items match at i, j:
            dp[i][j] = dp[i-1][j-1] + 1        (or similar "take" transition)
        else:
            dp[i][j] = combine(dp[i-1][j], dp[i][j-1])   (skip one side)
return dp[n][m]
```

Space is often the real interview twist: since row `i` only reads row `i-1`, you can usually collapse the table to two 1-D rows (or one row updated in place), turning O(n·m) space into O(m).
