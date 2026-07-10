The most direct reading of the problem: generate every arrangement as if all elements were distinct — the standard `n!` permutations, treating position, not value, as what makes two arrangements different. Then throw away the duplicates that come from repeated values.

`itertools.permutations` already does the "arrange everything" part. Putting the results in a set collapses the ones that happen to match, and sorting gives a deterministic order to check against.

```python
from itertools import permutations


def permute_unique(nums):
    seen = set(permutations(nums))
    return sorted(list(p) for p in seen)
```

## Why it works

`permutations(nums)` enumerates all `n!` orderings by position, so a repeated value like the two `1`s in `[1, 1, 2]` produces two identical tuples for the same visible arrangement. Storing them in a `set` deduplicates by value, since tuples compare element-wise. Sorting the surviving results only fixes the output order for comparison — it doesn't affect correctness.

## Complexity

- Time: O(n! · n) — n! permutations are generated, each costing O(n) to build and hash.
- Space: O(n! · n) — every raw permutation is held before deduplication.
