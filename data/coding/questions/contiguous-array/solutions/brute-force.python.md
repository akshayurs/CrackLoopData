The most direct reading of the problem: consider every subarray and keep the longest one that is balanced. Fix a start index, then extend the end one step at a time, tracking a running count of `0`s and `1`s so far.

Whenever the two counts match, the current window is balanced, so update the best length. Reusing the running counts as the window grows avoids recounting from scratch, but you still examine every start, so it stays quadratic.

```python
def find_max_length(nums):
    n = len(nums)
    best = 0
    for i in range(n):
        zeros = ones = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                best = max(best, j - i + 1)
    return best
```

## Why it works

The outer loop pins the start of the subarray; the inner loop stretches the end rightward, incrementing `zeros` or `ones` for each new element. Every contiguous subarray is covered exactly once by some `(i, j)` pair. A subarray is valid precisely when its `0` and `1` counts are equal, so each time that holds we record its length and keep the maximum.

## Complexity

- Time: O(n²) — every start pairs with every later end.
- Space: O(1) — just two counters and the running best.
