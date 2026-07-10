The most direct reading of the problem: every good subarray starts at some index `i` and extends to some later index `j`. So fix the start, grow the window one element at a time, and keep a running total — the instant that total becomes a multiple of `k` on a window of length two or more, we have our answer.

Growing the sum incrementally instead of re-adding a slice each time keeps the inner step O(1), so the whole thing is a clean pair of nested loops with no extra memory.

```python
def check_subarray_sum(nums, k):
    n = len(nums)
    for i in range(n):
        total = nums[i]
        for j in range(i + 1, n):
            total += nums[j]
            if total % k == 0:
                return True
    return False
```

## Why it works

The outer loop pins the start index `i`; the inner loop extends the end index `j` from `i + 1` onward, so every window it tests already has length at least two. `total` accumulates `nums[i..j]` as `j` advances, and `total % k == 0` is exactly the "multiple of `k`" test. If any window passes we return immediately; if all starts are exhausted no good subarray exists.

## Complexity

- Time: O(n²) — for each start we scan every later end, about n²/2 windows.
- Space: O(1) — only the running total and loop counters.
