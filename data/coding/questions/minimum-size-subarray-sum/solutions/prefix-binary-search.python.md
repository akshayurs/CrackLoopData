Build prefix sums so that the sum of any window `[i, j)` is `prefix[j] - prefix[i]`. Because every value is positive, `prefix` is strictly increasing — which means for a fixed left end `i` you can *binary search* for the smallest right end whose prefix is at least `prefix[i] + target`.

Each left end contributes one logarithmic lookup instead of a linear scan, trading the quadratic inner loop for a sorted-array search.

```python
from bisect import bisect_left

def min_subarray_len(target, nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    best = n + 1
    for i in range(n):
        need = prefix[i] + target
        j = bisect_left(prefix, need, i + 1)
        if j <= n:
            best = min(best, j - i)
    return best if best <= n else 0
```

## Why it works

`prefix[j] - prefix[i] >= target` is equivalent to `prefix[j] >= prefix[i] + target`. Since `prefix` is monotonically increasing, `bisect_left` finds the first index `j` satisfying that bound; that `j` gives the shortest window starting at `i`. Minimizing `j - i` over all left ends produces the global shortest window.

## Complexity

- Time: O(n log n) — one binary search per starting index.
- Space: O(n) — the prefix-sum array.
