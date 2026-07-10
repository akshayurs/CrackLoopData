Sorting every point is wasteful when `k` is small — you only need to know the `k` smallest distances, not the full order of `n` of them. A max-heap capped at size `k` does exactly that: push points in, and whenever the heap grows past `k`, pop the farthest one out.

Python's `heapq` is a min-heap, so distances are negated to simulate a max-heap. After one pass, the heap holds precisely the `k` closest points; a final sort makes the output deterministic.

```python
import heapq

def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (-dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    result = [[x, y] for _, x, y in heap]
    return sorted(result, key=lambda p: (p[0] ** 2 + p[1] ** 2, p[0], p[1]))
```

## Why it works

The heap always holds at most `k` points, ordered so its root is the current farthest one among them. When a new point arrives, adding it and immediately popping if the size exceeds `k` evicts whichever of the `k + 1` candidates is farthest — which can only ever be the true farthest, never a closer point wrongly discarded, since the popped item is always the heap's max. After all `n` points are processed, the survivors are the `k` nearest; the final sort just imposes the required deterministic order.

## Complexity

- Time: O(n log k) — each of the n pushes/pops costs O(log k), plus O(k log k) for the final sort.
- Space: O(k) — the heap never holds more than k points.
