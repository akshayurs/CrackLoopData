Feasibility is monotonic: if you can make `m` bouquets by day `d`, you can also make them on any later day, because flowers never un-bloom. That turns the problem into finding the smallest `d` for which the check passes — a classic binary search on the answer.

Search the day range `[min(bloomDay), max(bloomDay)]`. For a midpoint day, run the same linear feasibility check; if it succeeds, the answer is at most that day, so shrink the upper bound, otherwise raise the lower bound. Guard the impossible case with `m * k > n` first.

```python
def min_days(bloom_day, m, k):
    n = len(bloom_day)
    if m * k > n:
        return -1

    def can(day):
        bouquets = run = 0
        for b in bloom_day:
            if b <= day:
                run += 1
                if run == k:
                    bouquets += 1
                    run = 0
            else:
                run = 0
        return bouquets >= m

    lo, hi = min(bloom_day), max(bloom_day)
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## Why it works

`can(day)` counts bouquets by cutting one per full run of `k` adjacent bloomed flowers. Because feasibility flips from false to true exactly once as the day increases, the loop converges the window `[lo, hi]` onto that boundary — the first day the check passes. Since `m * k <= n`, the maximum bloom day is always feasible, so `lo` ends on a real answer.

## Complexity

- Time: O(n log(maxDay)) — O(log(maxDay)) binary-search steps, each an O(n) scan.
- Space: O(1) — only counters.
