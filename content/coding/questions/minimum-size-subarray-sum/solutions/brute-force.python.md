Start from every index and extend a window rightward, accumulating the sum until it reaches `target`. The moment a start position produces a qualifying window, record its length and move on — no shorter window can begin at that same start.

Because all values are positive, the running sum only grows as the window widens, so you can break out of the inner scan as soon as `target` is met.

```python
def min_subarray_len(target, nums):
    n = len(nums)
    best = n + 1
    for start in range(n):
        total = 0
        for end in range(start, n):
            total += nums[end]
            if total >= target:
                best = min(best, end - start + 1)
                break
    return best if best <= n else 0
```

## Why it works

Every possible starting index is tried, and for each one the window grows until it first hits `target`. Since positive values guarantee a monotonically increasing sum, the first qualifying window from a given start is also the shortest from that start. Taking the minimum over all starts yields the global answer; `best` staying above `n` means nothing ever reached `target`.

## Complexity

- Time: O(n²) — each start scans up to the end of the array.
- Space: O(1) — only a few counters are kept.
