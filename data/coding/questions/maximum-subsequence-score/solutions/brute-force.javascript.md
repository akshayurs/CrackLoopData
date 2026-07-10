Sort the pairs by `nums2` descending. Once sorted this way, the smallest `nums2` value inside any prefix is always the last element of that prefix — so if the chosen `k` indices are made to come from a prefix, that last element is automatically the multiplier. For each prefix long enough to hold `k` items, re-sort just that prefix's `nums1` values and add up the `k` largest.

It is wasteful to re-sort the same numbers over and over as the prefix grows, but it is the natural first attempt: check every candidate pivot directly.

```javascript
function maxScore(nums1, nums2, k) {
  const n = nums1.length;
  const pairs = nums1.map((a, i) => [a, nums2[i]]).sort((p, q) => q[1] - p[1]);
  let best = 0;
  for (let i = k - 1; i < n; i++) {
    const topK = pairs
      .slice(0, i + 1)
      .map((p) => p[0])
      .sort((a, b) => b - a)
      .slice(0, k);
    const sum = topK.reduce((s, v) => s + v, 0);
    best = Math.max(best, sum * pairs[i][1]);
  }
  return best;
}
```

## Why it works

Any valid `k`-index choice has some element with the smallest `nums2`; call its value `m`. Restricting attention to indices whose `nums2 >= m` and picking the `k` largest `nums1` among them can only help the sum without lowering the multiplier below `m`. Sorting by `nums2` descending turns "indices with `nums2 >= pairs[i][1]`" into exactly the prefix `pairs[0..i]`, so scanning every possible pivot `i` and taking the best `k` `nums1` values from its prefix covers every optimal choice.

## Complexity

- Time: O(n² log n) — up to n prefixes, each re-sorted from scratch.
- Space: O(n) — the sorted pairs and a rebuilt prefix each iteration.
