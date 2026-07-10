The simplest way to bound the target is to walk the array from left to right and remember the first index where it appears and the most recent index where it appears. The first match fixes the left boundary; the last match seen by the end of the scan fixes the right boundary.

Because the array is sorted, all occurrences of the target sit in one contiguous block, but this approach does not rely on that — it works on any array and simply records the extremes.

```python
def search_range(nums, target):
    first = -1
    last = -1
    for i, n in enumerate(nums):
        if n == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
```

## Why it works

`first` is set only once, the moment the target is encountered, so it captures the earliest index. `last` is overwritten on every match, so after the loop it holds the latest index. If the target never appears, both stay `-1`, giving `[-1, -1]`.

## Complexity

- Time: O(n) — a single pass over the array.
- Space: O(1) — only two index variables.
