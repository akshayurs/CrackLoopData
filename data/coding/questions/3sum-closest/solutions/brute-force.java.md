The most direct reading of the problem: examine every triple `(i, j, k)`, compute its sum, and remember the one whose distance to `target` is smallest. No sorting, no cleverness — just three nested loops.

It is the honest baseline you would state first in an interview before reaching for a faster structure.

```java
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        int best = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    int s = nums[i] + nums[j] + nums[k];
                    if (Math.abs(s - target) < Math.abs(best - target)) {
                        best = s;
                    }
                }
            }
        }
        return best;
    }
}
```

## Why it works

The strictly increasing loop bounds generate each unordered triple of distinct indices exactly once. `best` starts at a genuine triple sum and is overwritten only when a new sum is strictly closer to `target`, so after the scan it holds the global closest sum.

## Complexity

- Time: O(n³) — every triple of the n elements is checked.
- Space: O(1) — only the running best and loop counters.
