Neighbouring windows overlap in all but one element. Instead of re-adding `k` numbers each time, keep a running sum: when the window slides one step right, add the element entering on the right and subtract the one leaving on the left.

Compare raw sums while sliding (they all share the same divisor `k`) and only divide once at the end — fewer floating-point operations and one clean pass.

```python
def max_average(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > best:
            best = window_sum
    return best / k
```

## Why it works

`window_sum` always holds the sum of the current `k`-length block. Each slide swaps exactly one element (`nums[i]` in, `nums[i - k]` out), so the update is O(1) and keeps the invariant. Since every window divides by the same `k`, the window with the largest sum also has the largest average, so we can defer the single division to the end.

## Complexity

- Time: O(n) — one pass; each slide is O(1).
- Space: O(1) — just the running sum and best.
