The most direct reading of the problem: examine every triple `(i, j, k)`, compute its sum, and remember the one whose distance to `target` is smallest. No sorting, no cleverness — just three nested loops.

It is the honest baseline you would state first in an interview before reaching for a faster structure.

```python
def three_sum_closest(nums, target):
    n = len(nums)
    best = nums[0] + nums[1] + nums[2]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(best - target):
                    best = s
    return best
```

## Why it works

Every unordered triple of distinct indices is generated exactly once by the strictly increasing loop bounds. We seed `best` with a real triple, then replace it whenever a new sum lands strictly closer to `target`. After all triples are seen, `best` holds the global closest sum.

## Complexity

- Time: O(n³) — every triple of the n elements is checked.
- Space: O(1) — only the running best and loop counters.
