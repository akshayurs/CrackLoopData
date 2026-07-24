The most direct reading of the problem: there are `n - k + 1` window positions, so visit each one and take the max of its `k` elements with a built-in scan.

This does redundant work — adjacent windows overlap in `k - 1` elements that get re-examined — but it is the natural first pass and a useful correctness baseline.

```python
def max_sliding_window(nums, k):
    result = []
    for start in range(len(nums) - k + 1):
        result.append(max(nums[start:start + k]))
    return result
```

## Why it works

`start` ranges over every valid left edge, from `0` to `len(nums) - k`. For each, `nums[start:start + k]` is exactly the window, and `max` returns its largest element. Collecting them in order reproduces the required sequence.

## Complexity

- Time: O(n·k) — each of the ~n windows costs O(k) to scan.
- Space: O(1) — ignoring the output list, only the slice is held transiently.
