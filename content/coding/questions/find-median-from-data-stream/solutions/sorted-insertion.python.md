The simplest possible design: keep every number seen so far in one sorted list. On each `addNum`, find the insertion point and shift elements to keep the list sorted. `findMedian` then just reads the middle (or average of the two middles) directly.

This mirrors what you'd write in an interview before optimizing — correct, but every insert costs a linear shift, and the sort order has to be rebuilt on every call rather than maintained incrementally.

```python
import bisect

class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num):
        bisect.insort(self.nums, num)

    def findMedian(self):
        n = len(self.nums)
        mid = n // 2
        if n % 2 == 1:
            return float(self.nums[mid])
        return (self.nums[mid - 1] + self.nums[mid]) / 2.0
```

## Why it works

`bisect.insort` finds the correct position with binary search and shifts the tail of the list to make room, so `self.nums` is always sorted. With a sorted list, the median is just the middle element (odd count) or the average of the two elements straddling the middle (even count) — no extra scan needed.

## Complexity

- Time: O(n) per `addNum` (binary search is O(log n) but the shift is O(n)); O(1) per `findMedian`.
- Space: O(n) — one list holding every number added.
