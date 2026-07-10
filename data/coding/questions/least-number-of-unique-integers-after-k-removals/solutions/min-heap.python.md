The brute-force scan is wasted work: once you know the counts, the removal order never changes — you always want to finish off the value with the smallest remaining count first. Push every value's count into a min-heap once, then keep popping the smallest count and spending removals on it as long as `k` covers it whole; the moment `k` can no longer clear the heap's minimum, stop — that value and everything left in the heap survives.

```python
import heapq
from collections import Counter

def least_number_of_unique_ints(arr, k):
    counts = Counter(arr)
    heap = list(counts.values())
    heapq.heapify(heap)

    unique = len(heap)
    while heap and k >= heap[0]:
        k -= heapq.heappop(heap)
        unique -= 1
    return unique
```

## Why it works

The heap always exposes the value that is cheapest to eliminate. If `k` is at least that count, removing it entirely is free (no leftover budget is wasted) and strictly reduces the unique count, so it's always safe to take. Once `k` is smaller than the heap's minimum, no remaining value can be fully cleared, so every value still in the heap must survive — the loop correctly stops there.

## Complexity

- Time: O(n log n) — building the counts is O(n); heapifying u values is O(u), and popping is O(log u) each, so O(n log n) overall.
- Space: O(n) — the count map and heap each hold up to n entries.
