Sort the array first so equal values sit next to each other and every subset comes out in ascending order. There are `2^n` possible subsets, so walk every integer mask from `0` to `2^n - 1`, treat each bit as "include this index," and build the subset that mask describes.

Duplicate values in `nums` mean different masks can build the exact same subset. Serialize each subset to a string key and stash it in a `Map` to collapse those repeats, then sort what's left — comparing element by element, the way array/tuple comparison works in most languages — so the final order is deterministic.

```javascript
function subsetsWithDup(nums) {
  const sorted = [...nums].sort((a, b) => a - b);
  const n = sorted.length;
  const byKey = new Map();
  for (let mask = 0; mask < (1 << n); mask++) {
    const subset = [];
    for (let i = 0; i < n; i++) {
      if (mask & (1 << i)) subset.push(sorted[i]);
    }
    byKey.set(subset.join(','), subset);
  }
  return [...byKey.values()].sort((a, b) => {
    for (let i = 0; i < Math.min(a.length, b.length); i++) {
      if (a[i] !== b[i]) return a[i] - b[i];
    }
    return a.length - b.length;
  });
}
```

## Why it works

Every mask from `0` to `2^n - 1` corresponds to exactly one way of including/excluding each index, so the loop enumerates every possible subset at least once. Because the array is pre-sorted, two masks that pick the same multiset of values always build the same subset, so the string key collapses them in the map. The final comparator walks both subsets element by element and falls back to length when one is a prefix of the other — the same rule tuple comparison uses — so a shorter subset always sorts before a longer one that extends it, fixing a single canonical order.

## Complexity

- Time: O(n · 2^n) — 2^n masks, each costing O(n) to build and key.
- Space: O(n · 2^n) — up to 2^n subsets stored before deduping.
