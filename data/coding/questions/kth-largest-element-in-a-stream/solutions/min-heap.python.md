You never need the full sorted history — only the k largest values matter, and among those only the smallest one (the k-th largest overall). Keep a min-heap capped at size k: whenever it grows past k, pop the smallest, since anything smaller than the current k-th largest can never become the answer again.

After seeding the heap with the initial array (trimmed to its k largest), every `add` is a single push, and possibly one pop, followed by peeking at the heap's root.

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

## Why it works

A min-heap of size k always holds exactly the k largest values seen so far, with the smallest of that group sitting at the root. Pushing a new value and evicting the root when the heap overflows keeps that invariant intact, so the root is always the k-th largest element after every `add`.

## Complexity

- Time: O(log k) per call to `add` — one push and at most one pop on a heap of size k.
- Space: O(k) — the heap only ever holds the k largest values.
