Sorting every distinct value is wasteful when `k` is small — you only care about the top few. Keep a min-heap of size `k` instead: push each `(count, value)` pair, and whenever the heap grows past `k`, pop the smallest. The heap always holds the `k` most frequent values seen so far, and the cheapest of them sits at the root ready to be evicted.

This trades the full O(n log n) sort for O(n log k), which is a real win when `k` is much smaller than the number of distinct values.

```python
import heapq
from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    heap = []
    for value, count in counts.items():
        heapq.heappush(heap, (count, value))
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(value for count, value in heap)
```

## Why it works

The min-heap is ordered by count, so its root is always the least frequent value currently retained. After processing every distinct value, any value less frequent than the top `k` has already been popped, leaving precisely the `k` most frequent in the heap. Since only `k + 1` items ever coexist, each heap operation costs O(log k). A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n log k) — counting is O(n); each of the up-to-n pushes/pops costs O(log k); the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the counter holds up to n entries; the heap holds k.
