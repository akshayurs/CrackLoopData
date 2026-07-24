Think of the choice as *where to place the cuts*. Let `best[j][i]` be the smallest possible "largest piece" when the first `i` elements are split into `j` groups. To fill it, let the last group start at index `t`: everything before `t` is split into `j-1` groups, and the last group `nums[t..i-1]` contributes its own sum. The cost of that plan is the *max* of the earlier answer and the last group's sum, and we take the minimum over every valid start `t`.

Prefix sums give each subarray sum in O(1), and we sweep `j` from 1 to `k` and `i` over the array, so the whole table is built bottom-up.

```java
class Solution {
    public int splitArray(int[] nums, int k) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        long INF = Long.MAX_VALUE;
        long[][] best = new long[k + 1][n + 1];
        for (long[] row : best) java.util.Arrays.fill(row, INF);
        best[0][0] = 0;
        for (int j = 1; j <= k; j++) {
            for (int i = 1; i <= n; i++) {
                for (int t = j - 1; t < i; t++) {
                    if (best[j - 1][t] == INF) continue;
                    long last = prefix[i] - prefix[t];
                    long cost = Math.max(best[j - 1][t], last);
                    if (cost < best[j][i]) best[j][i] = cost;
                }
            }
        }
        return (int) best[k][n];
    }
}
```

## Why it works

Any split of `i` elements into `j` groups is uniquely defined by where the last group begins. Trying every start `t` and combining the optimal sub-solution `best[j-1][t]` with the last group's sum covers all splits, and the `max` captures that the objective is the largest piece. Taking the minimum over `t` gives the optimum for `best[j][i]`, so `best[k][n]` is the answer.

## Complexity

- Time: O(k · n²) — three nested loops over groups, endpoints, and cut positions.
- Space: O(k · n) — the DP table.
