The simplest correct approach: compute every point's squared distance to the origin, sort the whole list by that distance, and take the first `k`. Squared distance avoids a needless square root and preserves ordering.

Ties are broken by `x` then `y` so the output is deterministic regardless of the input order.

```python
def k_closest(points, k):
    ordered = sorted(points, key=lambda p: (p[0] ** 2 + p[1] ** 2, p[0], p[1]))
    return ordered[:k]
```

## Why it works

Squared distance is a monotonic function of true distance, so sorting by it produces the same order as sorting by actual distance without a costly `sqrt` call. Once every point is ordered nearest-to-farthest (with the x/y tiebreak baked into the sort key), the first `k` entries are exactly the `k` closest points.

## Complexity

- Time: O(n log n) — one full sort of all points.
- Space: O(n) — `sorted` builds a new list.
