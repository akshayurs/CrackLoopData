Sort the array first so equal values sit next to each other and every subset naturally comes out in ascending order. There are `2^n` possible subsets, so walk every integer mask from `0` to `2^n - 1`, treat each bit as "include this index," and build the subset that mask describes.

Duplicate values in `nums` mean different masks can build the exact same subset (e.g. picking index 1's `2` versus index 2's `2`). Throw every subset into a set of tuples to collapse those repeats, then sort what's left so the final order is deterministic.

```python
def subsets_with_dup(nums):
    nums = sorted(nums)
    n = len(nums)
    seen = set()
    for mask in range(1 << n):
        subset = tuple(nums[i] for i in range(n) if mask & (1 << i))
        seen.add(subset)
    return sorted([list(s) for s in seen])
```

## Why it works

Every mask from `0` to `2^n - 1` corresponds to exactly one way of including/excluding each index, so the loop enumerates every possible subset at least once. Because `nums` is pre-sorted, two masks that pick the same multiset of values always produce the identical tuple, so the `set` merges them into one entry. Sorting the collected subsets at the end fixes a single canonical order.

## Complexity

- Time: O(n · 2^n) — 2^n masks, each costing O(n) to build and hash.
- Space: O(n · 2^n) — up to 2^n subsets stored before deduping.
