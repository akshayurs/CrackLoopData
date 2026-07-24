The slowest workable speed is somewhere between 1 and the largest pile — eating faster than the biggest pile never helps, since Koko can only touch one pile per hour. So the direct approach is to try every candidate speed starting from 1 and return the first one that finishes in time.

For a given speed `k`, a pile of size `p` takes `ceil(p / k)` hours, and the total is just the sum over all piles. Because larger speeds only ever reduce the total hours, the first speed that fits within `h` is the answer.

```python
import math

def min_eating_speed(piles, h):
    for k in range(1, max(piles) + 1):
        hours = sum(math.ceil(p / k) for p in piles)
        if hours <= h:
            return k
    return max(piles)
```

## Why it works

`ceil(p / k)` is exactly the hours Koko spends on one pile, because she cannot carry leftover eating into the next hour. Summing gives the total time at speed `k`. Since that total is non-increasing in `k`, scanning upward finds the minimum feasible speed first. Speed `max(piles)` always works (one pile per hour), so the loop is guaranteed to return.

## Complexity

- Time: O(m · n) — up to m = max(piles) speeds, each costing an O(n) sum over the piles.
- Space: O(1) — only a running total is kept.
