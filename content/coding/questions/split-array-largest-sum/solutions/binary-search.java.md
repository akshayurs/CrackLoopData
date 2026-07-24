Instead of searching over split points, search over the *answer* itself. Suppose we guess a cap `x` for the largest allowed piece. We can greedily walk the array, starting a new piece whenever adding the next number would exceed `x`, and count how many pieces that takes. If it takes at most `k` pieces, then `x` is achievable; if it needs more, `x` is too small.

The number of pieces needed is monotonic in `x` — a bigger cap never needs more pieces — so we binary search `x` over the range `[max(nums), sum(nums)]`. The lower bound must be at least the largest single element (no piece can be smaller than that), and the upper bound is one piece holding everything.

```java
class Solution {
    public int splitArray(int[] nums, int k) {
        long lo = 0, hi = 0;
        for (int x : nums) {
            lo = Math.max(lo, x);
            hi += x;
        }
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (piecesNeeded(nums, mid) <= k) hi = mid;
            else lo = mid + 1;
        }
        return (int) lo;
    }

    private int piecesNeeded(int[] nums, long cap) {
        int count = 1;
        long running = 0;
        for (int x : nums) {
            if (running + x > cap) {
                count++;
                running = x;
            } else {
                running += x;
            }
        }
        return count;
    }
}
```

## Why it works

For a fixed cap, the greedy "extend until it would overflow, then cut" uses the fewest pieces possible, so it correctly decides feasibility. Feasibility is monotonic: any cap `>=` the true answer is feasible, any smaller cap is not. Binary search converges on the smallest feasible cap, which is exactly the minimized largest sum.

## Complexity

- Time: O(n · log(sum − max)) — each feasibility check is O(n), run for a logarithmic number of guesses.
- Space: O(1) — only a few counters.
