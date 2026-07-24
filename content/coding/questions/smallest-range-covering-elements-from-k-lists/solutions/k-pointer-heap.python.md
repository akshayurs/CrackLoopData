Instead of sorting everything up front, walk all `k` lists in lockstep with one pointer each, always advancing whichever list currently holds the smallest pointed-to value. A min-heap gives that minimum in O(log k) instead of scanning all `k` pointers, and tracking the running maximum alongside it turns every heap pop into one candidate range.

At every step the heap's minimum and the tracked maximum define a range that already touches all `k` lists — one element per list is on the "table" at all times — so shrinking is really just advancing the smallest pointer and re-measuring.

```python
import heapq
from typing import List


def smallest_range(lists: List[List[int]]) -> List[int]:
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists)]
    heapq.heapify(heap)
    current_max = max(lst[0] for lst in lists)
    best = [heap[0][0], current_max]

    while True:
        value, list_i, elem_i = heapq.heappop(heap)
        if current_max - value < best[1] - best[0]:
            best = [value, current_max]

        if elem_i + 1 == len(lists[list_i]):
            return best

        next_value = lists[list_i][elem_i + 1]
        current_max = max(current_max, next_value)
        heapq.heappush(heap, (next_value, list_i, elem_i + 1))
```

## Why it works

The heap always holds exactly one element per list, so its minimum and the tracked maximum bound the tightest range currently touching every list. Popping the minimum and advancing that list's pointer is the only way to shrink the range further, since raising the low end past any other pointer would drop that list out of coverage. The moment a list runs out of elements, no smaller range can be completed, so the best range found so far is final.

## Complexity

- Time: O(N log k) — N is the total number of elements; each of the N heap operations costs O(log k).
- Space: O(k) — the heap holds exactly one entry per list.
