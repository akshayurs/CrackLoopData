Flatten the problem: tag every value with which list it came from, then sort all of those (value, list) pairs together. Any range that covers all `k` lists now corresponds to a contiguous window of this sorted sequence that contains every list tag at least once — a classic "smallest window with all tags" sliding-window problem.

Slide the window's right edge forward, and whenever all `k` tags are present, shrink from the left as far as possible while keeping that property, checking each valid window against the best range seen so far.

```python
from typing import List


def smallest_range(lists: List[List[int]]) -> List[int]:
    merged = sorted(
        (value, i) for i, lst in enumerate(lists) for value in lst
    )
    k = len(lists)
    count = {}
    formed = 0
    left = 0
    best = [merged[0][0], merged[-1][0]]

    for right, (value, tag) in enumerate(merged):
        count[tag] = count.get(tag, 0) + 1
        if count[tag] == 1:
            formed += 1
        while formed == k:
            lo, hi = merged[left][0], merged[right][0]
            if hi - lo < best[1] - best[0]:
                best = [lo, hi]
            left_tag = merged[left][1]
            count[left_tag] -= 1
            if count[left_tag] == 0:
                formed -= 1
            left += 1

    return best
```

## Why it works

Sorting merges all `k` lists into one non-decreasing sequence while remembering each value's origin. A window `[left, right]` covers every list exactly when its multiset of tags contains all `k` list indices, so the classic shrink-while-valid sliding window finds the tightest such window. Because the sequence is sorted, the window's endpoints are always the true `lo`/`hi` of the range, and shrinking greedily never skips a better answer since any smaller valid window must sit inside a currently valid one.

## Complexity

- Time: O(N log N) — N is the total number of elements; dominated by the sort.
- Space: O(N) — the merged array and the tag-count map.
