Sort the pairs by `nums2` descending. Once sorted this way, the smallest `nums2` value inside any prefix is always the last element of that prefix — so if the chosen `k` indices are made to come from a prefix, that last element is automatically the multiplier. For each prefix long enough to hold `k` items, re-sort just that prefix's `nums1` values and add up the `k` largest.

It is wasteful to re-sort the same numbers over and over as the prefix grows, but it is the natural first attempt: check every candidate pivot directly.

```python
def max_score(nums1, nums2, k):
    n = len(nums1)
    pairs = sorted(zip(nums1, nums2), key=lambda p: -p[1])
    best = 0
    for i in range(k - 1, n):
        prefix = [pairs[j][0] for j in range(i + 1)]
        top_k = sorted(prefix, reverse=True)[:k]
        best = max(best, sum(top_k) * pairs[i][1])
    return best
```

## Why it works

Any valid `k`-index choice has some element with the smallest `nums2`; call its value `m`. Restricting attention to indices whose `nums2 >= m` and picking the `k` largest `nums1` among them can only help the sum without lowering the multiplier below `m`. Sorting by `nums2` descending turns "indices with `nums2 >= pairs[i][1]`" into exactly the prefix `pairs[0..i]`, so scanning every possible pivot `i` and taking the best `k` `nums1` values from its prefix covers every optimal choice.

## Complexity

- Time: O(n² log n) — up to n prefixes, each re-sorted from scratch.
- Space: O(n) — the sorted pairs and a rebuilt prefix each iteration.
