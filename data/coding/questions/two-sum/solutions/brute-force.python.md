The most direct reading of the problem: try every pair `(i, j)` and check whether they sum to the target. No cleverness, no extra memory — just two nested loops.

It is the honest baseline you would state first in an interview, before optimizing.

```python
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

## Why it works

The outer loop fixes the first index; the inner loop scans every later index, so each unordered pair is examined exactly once. The moment a pair sums to `target`, we return its indices — and because the problem guarantees one solution, we never fall through to the empty return.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — only loop counters, no extra structure.
