The hours Koko needs is a monotonic function of her speed: the faster she eats, the fewer hours it takes, and slower always takes more. That means the feasible speeds form a suffix — every speed at or above the answer works, everything below fails. Whenever the answer is the boundary of a monotonic yes/no range, binary search finds it in logarithmic time.

Search over the speed itself, not the array. The smallest sensible speed is 1 and the largest useful speed is the biggest pile. At each midpoint, compute the total hours; if it fits within `h`, the answer is this speed or something slower, so move the upper bound down — otherwise Koko is too slow and the lower bound must rise.

```java
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 0;
        for (int p : piles) hi = Math.max(hi, p);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            long hours = 0;
            for (int p : piles) {
                hours += (p + mid - 1) / mid;
            }
            if (hours <= h) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
```

## Why it works

`hours(k)` is non-increasing in `k`, so there is a single crossover speed where "finishes in time" first becomes true. The loop keeps `[lo, hi]` as the range still containing that crossover: a feasible `mid` means the answer is `<= mid` (keep `mid`), an infeasible `mid` means the answer is `> mid`. Using `long` for the running sum avoids overflow. The window shrinks each step and collapses onto the smallest feasible speed.

## Complexity

- Time: O(n · log m) — where m = max(piles); each of log m binary-search steps sums n piles.
- Space: O(1) — only the two bounds and a running total.
