**Binary search** finds a target — or the boundary between "no" and "yes" — in **O(log n)** by repeatedly halving a search space instead of scanning it. Each check on the midpoint throws away one half of the remaining candidates, so n items take only ~log₂(n) checks.

The classic form searches a sorted array for an exact value. The more powerful form — **binary search on the answer** — doesn't need a sorted array at all. It needs a **monotonic predicate**: some `can(x)` that is `false` for a while and then `true` (or vice versa) as `x` increases. Binary search then finds the exact crossover point.

A typical shape:

```
lo, hi = search space bounds
while lo <= hi:
    mid = lo + (hi - lo) / 2
    if condition(mid) is true (goal is in the left half, inclusive):
        hi = mid - 1        # or record mid as a candidate answer, then shrink
    else:
        lo = mid + 1
return lo (or hi, depending on what you are looking for)
```

The two ingredients to check before reaching for binary search:

- **A search space you can index into by position or value** — an array, or a numeric range like "minimum possible speed" or "maximum possible capacity".
- **Monotonicity** — moving in one direction along that space only ever makes the predicate go from false to true (or true to false), never flips back and forth. Without monotonicity, halving the space can throw away the answer.

Once you see both, the problem is "just" finding the boundary — the hard part is defining `condition(mid)` correctly.
