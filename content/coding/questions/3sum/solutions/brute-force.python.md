The honest baseline: examine every combination of three distinct indices and keep the ones that sum to zero. The only wrinkle is duplicates — the same three values can be picked through different index combinations, so we canonicalize each hit by sorting its three numbers and storing it in a set of tuples.

At the end we sort the collected triplets so the output is deterministic, matching the canonical order the problem asks for.

```python
def three_sum(nums):
    n = len(nums)
    found = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    found.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return sorted(list(t) for t in found)
```

## Why it works

Every unordered triple of indices is visited exactly once by the three nested loops. Sorting each zero-sum triple before inserting it into `found` collapses permutations of the same three values into a single key, so duplicates never survive. Sorting the final list gives the required canonical ordering.

## Complexity

- Time: O(n³) — every triple of indices is tested.
- Space: O(m) — the set holds the m unique triplets found.
