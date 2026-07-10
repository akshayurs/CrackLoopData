The hours Koko needs is a monotonic function of her speed: the faster she eats, the fewer hours it takes, and slower always takes more. That means the feasible speeds form a suffix — every speed at or above the answer works, everything below fails. Whenever the answer is the boundary of a monotonic yes/no range, binary search finds it in logarithmic time.

Search over the speed itself, not the array. The smallest sensible speed is 1 and the largest useful speed is the biggest pile. At each midpoint, compute the total hours; if it fits within `h`, the answer is this speed or something slower, so move the upper bound down — otherwise Koko is too slow and the lower bound must rise.

```python
import math

def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## Why it works

`hours(k)` is non-increasing in `k`, so there is a single crossover speed where "finishes in time" first becomes true. The loop keeps `[lo, hi]` as the range still containing that crossover: a feasible `mid` means the answer is `<= mid` (keep `mid`), an infeasible `mid` means the answer is `> mid`. The window shrinks each step and collapses onto the smallest feasible speed.

## Complexity

- Time: O(n · log m) — where m = max(piles); each of log m binary-search steps sums n piles.
- Space: O(1) — only the two bounds and a running total.
