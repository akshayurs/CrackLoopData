The most direct reading of the problem: there are `n - k + 1` windows of length `k`, so line them all up, add each one, and keep the biggest average you see.

Because every window is summed independently, the same neighbouring elements get added over and over — correct, but wasteful.

```python
def max_average(nums, k):
    best = None
    for i in range(len(nums) - k + 1):
        avg = sum(nums[i:i + k]) / k
        if best is None or avg > best:
            best = avg
    return best
```

## Why it works

`i` ranges over every valid starting index, and `nums[i:i + k]` is the window that begins there. Dividing the window's sum by `k` gives its average; tracking the running maximum across all windows yields the answer. The one-window guarantee (`k <= len(nums)`) means the loop always runs at least once.

## Complexity

- Time: O(n·k) — each of the ~n windows costs O(k) to sum.
- Space: O(1) — only the running best is stored (the slice is transient).
