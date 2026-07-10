Split the numbers into two halves around the median: a max-heap `lo` holding the smaller half, and a min-heap `hi` holding the larger half, kept the same size (or `lo` one larger). The median is then always sitting at the top of one or both heaps — no sorting needed.

On every `addNum`, push into one heap and then rebalance by moving the top of one heap to the other so the size invariant holds. `findMedian` reads the top(s) in O(1). Since Python's `heapq` is a min-heap, `lo` is simulated as a max-heap by storing negated values.

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negated values), holds the smaller half
        self.hi = []  # min-heap, holds the larger half

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0
```

## Why it works

Every value first goes into `lo`, then its largest member is immediately promoted to `hi` — this guarantees every element of `lo` is `<=` every element of `hi`. Rebalancing keeps `len(lo)` equal to `len(hi)` or exactly one more, so the median is either `lo`'s top (odd total) or the average of both tops (even total). Both heaps only ever move their extreme element, never resort.

## Complexity

- Time: O(log n) per `addNum` (heap push/pop); O(1) per `findMedian`.
- Space: O(n) — the two heaps together hold every number added.
