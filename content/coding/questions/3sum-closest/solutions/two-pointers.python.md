Sort the array first. Then fix the smallest element of the triple with an index `i` and let two pointers — `lo` just after `i` and `hi` at the end — sweep toward each other. Because the array is ordered, the sum tells you which way to move: too small means advance `lo` to grow it, too large means retreat `hi` to shrink it.

Sorting turns the third loop into a single linear sweep: for each `i` you scan the remaining window once instead of trying every pair, collapsing the cubic search to quadratic. Track the closest sum seen across all sweeps.

```python
def three_sum_closest(nums, target):
    nums.sort()
    n = len(nums)
    best = nums[0] + nums[1] + nums[2]
    for i in range(n - 2):
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if abs(s - target) < abs(best - target):
                best = s
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            else:
                return s
    return best
```

## Why it works

For a fixed `i`, moving `lo` right can only increase the sum and moving `hi` left can only decrease it, since the array is sorted. Comparing `s` to `target` therefore picks the one move that can bring the sum closer, and no promising pair is skipped. An exact hit (`s == target`) has distance 0, so it is immediately optimal and we return.

## Complexity

- Time: O(n²) — an O(n log n) sort plus, for each of n anchors, a linear two-pointer sweep.
- Space: O(1) — in-place sort aside, only a few indices.
