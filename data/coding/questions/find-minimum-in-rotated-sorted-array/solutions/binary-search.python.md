A rotated sorted array splits into two ascending runs, and the minimum is exactly the point where the second run begins — the single place where an element is smaller than the one before it. The trick is to find that break without scanning everything.

Compare the middle element to the rightmost one. If `nums[mid] > nums[right]`, the rotation point lies strictly to the right of `mid`, so the minimum is in `mid + 1 .. right`. Otherwise the right half (including `mid`) is properly sorted, so the minimum is at `mid` or to its left. Shrinking the window this way halves the search each step and converges on the minimum.

```python
def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
```

## Why it works

The loop keeps the minimum inside `[left, right]`. When `nums[mid] > nums[right]`, everything from `left` through `mid` is part of the higher first run, so the minimum must be after `mid`. When `nums[mid] <= nums[right]`, the segment `mid .. right` is non-decreasing, meaning `mid` could itself be the minimum and nothing to its right can beat it. Since the window shrinks every iteration and never discards the answer, `left == right` lands exactly on the minimum.

## Complexity

- Time: O(log n) — the search range halves each iteration.
- Space: O(1) — only two indices are tracked.
