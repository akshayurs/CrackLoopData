Instead of re-deciding the whole ladder assignment from scratch at every step, commit greedily and let a min-heap fix your mind if it turns out wrong. Every positive gap first "borrows" a ladder by going into a min-heap of size `ladders`. The moment the heap overflows, the smallest gap currently sitting in it is the least deserving of a free ladder, so it gets evicted and paid for with bricks instead — the biggest gaps naturally stay in the heap.

This turns the repeated re-sorting of the brute-force approach into a single push/pop per building.

```python
import heapq


def furthest_building(heights, bricks, ladders):
    ladder_climbs = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        heapq.heappush(ladder_climbs, diff)
        if len(ladder_climbs) > ladders:
            bricks -= heapq.heappop(ladder_climbs)
        if bricks < 0:
            return i
    return len(heights) - 1
```

## Why it works

The heap always holds the `ladders` largest gaps seen so far among the ones "in flight." Whenever a new gap arrives and the heap is full, the smallest of all gaps considered (old or new) is the correct one to demote to bricks, because keeping it in the ladder set instead of a larger gap could never be optimal. `bricks` is debited lazily as demotions happen, so the moment it goes negative, this exact prefix of the array is unreachable within budget.

## Complexity

- Time: O(n log l) — one heap push per building, one pop when it overflows the ladder capacity `l`.
- Space: O(l) — the heap never holds more than `ladders` elements.
