If the array is sorted, any duplicate values become neighbours. So sort first, then make a single sweep comparing each element with the one immediately before it — a match means a repeat.

This drops the cost from quadratic to the sort's O(n log n), and it needs no auxiliary hash structure, which can be attractive when memory is tight.

```python
def contains_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```

## Why it works

Sorting groups equal values into contiguous runs. If any value repeats, at least two copies end up adjacent, so a single neighbour comparison across the sorted array is enough to catch it. If no adjacent pair is equal, every value is distinct.

## Complexity

- Time: O(n log n) — dominated by the sort; the sweep is O(n).
- Space: O(1) to O(n) — depends on the sort's implementation; the extra logic uses no additional memory.
