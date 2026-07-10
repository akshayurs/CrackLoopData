The most direct reading of the problem: there are `n - k + 1` windows of length `k`, so line them all up, add each one, and keep the biggest average you see.

Because every window is summed independently, the same neighbouring elements get added over and over — correct, but wasteful. A `long` accumulator keeps the sum safe even when many large values stack up.

```java
class Solution {
    public double maxAverage(int[] nums, int k) {
        double best = Double.NEGATIVE_INFINITY;
        for (int i = 0; i + k <= nums.length; i++) {
            long windowSum = 0;
            for (int j = i; j < i + k; j++) windowSum += nums[j];
            best = Math.max(best, (double) windowSum / k);
        }
        return best;
    }
}
```

## Why it works

The outer loop fixes each valid start `i`; the inner loop sums the `k` elements from there. Casting to `double` before dividing gives the true average, and `Math.max` folds every window into a running best seeded at negative infinity so negative-only arrays are handled.

## Complexity

- Time: O(n·k) — ~n windows, each summed in O(k).
- Space: O(1) — no auxiliary structures.
