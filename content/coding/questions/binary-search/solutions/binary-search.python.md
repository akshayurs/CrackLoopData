Because the array is sorted, one comparison against the middle element rules out half of what remains. Keep a `lo`/`hi` window over the candidate range and probe its midpoint: if it matches, you are done; if the middle value is too small, the answer can only lie to its right, so discard everything up to and including `mid`; otherwise discard the right half.

Each step halves the search space, so the window shrinks logarithmically. Compute the midpoint as `lo + (hi - lo) // 2` to keep the intent clear (and to avoid overflow in fixed-width languages).

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## Why it works

The loop invariant is that if `target` exists, its index is always within `[lo, hi]`. Each comparison against `nums[mid]` correctly eliminates the half that cannot contain it, preserving the invariant. When `lo > hi` the window is empty, so `target` is absent and `-1` is returned.

## Complexity

- Time: O(log n) — the range halves every iteration.
- Space: O(1) — only two indices are tracked.
