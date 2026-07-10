Think of the choice as *where to place the cuts*. Let `best[j][i]` be the smallest possible "largest piece" when the first `i` elements are split into `j` groups. To fill it, let the last group start at index `t`: everything before `t` is split into `j-1` groups, and the last group `nums[t..i-1]` contributes its own sum. The cost of that plan is the *max* of the earlier answer and the last group's sum, and we take the minimum over every valid start `t`.

Prefix sums give each subarray sum in O(1), and we sweep `j` from 1 to `k` and `i` over the array, so the whole table is built bottom-up.

```python
def split_array(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    INF = float("inf")
    best = [[INF] * (n + 1) for _ in range(k + 1)]
    best[0][0] = 0
    for j in range(1, k + 1):
        for i in range(1, n + 1):
            for t in range(j - 1, i):
                last = prefix[i] - prefix[t]
                cost = max(best[j - 1][t], last)
                if cost < best[j][i]:
                    best[j][i] = cost
    return best[k][n]
```

## Why it works

Any split of `i` elements into `j` groups is uniquely defined by where the last group begins. Trying every start `t` and combining the optimal sub-solution `best[j-1][t]` with the last group's sum covers all splits, and the `max` captures that the objective is the largest piece. Taking the minimum over `t` gives the optimum for `best[j][i]`, so `best[k][n]` is the answer.

## Complexity

- Time: O(k · n²) — three nested loops over groups, endpoints, and cut positions.
- Space: O(k · n) — the DP table.
