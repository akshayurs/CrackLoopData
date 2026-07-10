Reduce 4Sum to a familiar shape: sort the array, fix the two outer values with a double loop, then let a two-pointer sweep close the remaining pair in linear time. Sorting is what makes both the pointer logic and duplicate-skipping possible.

For each fixed `(i, j)`, `lo` starts just after `j` and `hi` at the end. If the four-way sum is too small, advancing `lo` raises it; too large, dropping `hi` lowers it; on a hit we record the quadruplet and step both pointers past any repeats. Skipping duplicate values at `i`, `j`, `lo`, and `hi` keeps every quadruplet unique and the output already sorted.

```python
def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            lo, hi = j + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[j] + nums[lo] + nums[hi]
                if total == target:
                    res.append([nums[i], nums[j], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif total < target:
                    lo += 1
                else:
                    hi -= 1
    return res
```

## Why it works

On a sorted array the two-pointer sweep is exhaustive: because moving `lo` only increases the sum and moving `hi` only decreases it, no valid pair between them is ever skipped. The four `continue`/`while` guards ensure each distinct value combination is emitted once. Since outer values increase and the inner pair is scanned from both ends inward, quadruplets come out in ascending order, matching the required canonical form.

## Complexity

- Time: O(n^3) — two nested loops times a linear pointer sweep, after an O(n log n) sort.
- Space: O(1) — ignoring the output, only pointers and counters are used.
