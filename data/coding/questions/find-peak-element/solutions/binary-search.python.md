You don't need to see the whole array to find a peak. Look at the middle element and compare it to its right neighbor. If the middle is smaller, the values are still rising to the right, so a peak must exist somewhere in the right half. If the middle is larger, then it is itself a valid candidate and a peak lies in the left half (including the middle). Either way you can discard half the array.

This is binary search on an *unsorted* array: the "which side is going uphill" test always points toward a slope that must eventually turn into a peak, so halving repeatedly converges on one.

```python
def find_peak_element(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## Why it works

The search keeps the invariant that some peak lies within `[lo, hi]`. When `nums[mid] > nums[mid + 1]`, the left side (including `mid`) is descending on its right edge, so a peak sits at or before `mid`; set `hi = mid`. Otherwise `nums[mid] < nums[mid + 1]` means the right side is ascending and must peak later; set `lo = mid + 1`. The range shrinks each step until `lo == hi`, which is a peak.

## Complexity

- Time: O(log n) — the search space halves every iteration.
- Space: O(1) — only two pointers are stored.
