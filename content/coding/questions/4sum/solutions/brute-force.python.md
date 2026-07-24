The honest baseline: examine every group of four distinct indices and keep those whose values sum to `target`. Four nested loops enumerate all combinations directly.

Sorting first means each combination `i < j < k < l` is already non-decreasing, so a `set` of tuples cleanly removes duplicate value-groups; sorting the set at the end gives the canonical lexicographic order.

```python
def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    found = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        found.add((nums[i], nums[j], nums[k], nums[l]))
    return [list(t) for t in sorted(found)]
```

## Why it works

The four loops walk strictly increasing indices, so every unordered quadruplet of positions is tried exactly once. Because the array is sorted, the values in each tuple are non-decreasing, and identical value-groups collapse to one entry in the `set`. Sorting the survivors yields the required order.

## Complexity

- Time: O(n^4) — every quadruplet of indices is inspected.
- Space: O(m) — the set holds the m distinct matching quadruplets (plus O(1) for the sort in place).
