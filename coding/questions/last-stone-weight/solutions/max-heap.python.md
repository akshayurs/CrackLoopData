Re-sorting the whole list every round is overkill — all that's ever needed is the current two largest values, and a heap gives those in O(log n) instead of O(n log n). Python's `heapq` is a min-heap, so push negated weights to simulate a max-heap.

Pop the two largest (most negative) values, smash them, and push the remainder back negated if any stone survives. Stop when at most one stone is left.

```python
import heapq

def last_stone_weight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        heaviest = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        if heaviest != second:
            heapq.heappush(heap, -(heaviest - second))
    return -heap[0] if heap else 0
```

## Why it works

Negating every weight turns "largest stone" into "smallest heap key", so `heappop` always returns the current heaviest, then second-heaviest, stone in O(log n). Pushing the (negated) remainder back, only when the stones differ, keeps the heap representing the true multiset of stones after each smash. The process mirrors the problem's rules exactly, just with a faster data structure.

## Complexity

- Time: O(n log n) — building the heap is O(n); each of up to n rounds does O(1) pops/push at O(log n) each.
- Space: O(n) — the heap holds the stones.
