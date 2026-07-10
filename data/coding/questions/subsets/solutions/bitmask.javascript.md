Every subset of an `n`-element array corresponds to one of the `2^n` binary strings of length `n` — bit `i` set means "include `nums[i]`". Loop a counter from `0` to `2^n - 1` and read off its bits to build each subset directly, with no recursion at all.

It's the most mechanical way to enumerate a power set, and a good baseline before reaching for backtracking.

```javascript
function subsets(nums) {
  const n = nums.length;
  const result = [];
  for (let mask = 0; mask < (1 << n); mask++) {
    const subset = [];
    for (let i = 0; i < n; i++) {
      if (mask & (1 << i)) subset.push(nums[i]);
    }
    result.push(subset);
  }
  result.sort((a, b) => {
    if (a.length !== b.length) return a.length - b.length;
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return a[i] - b[i];
    }
    return 0;
  });
  return result;
}
```

## Why it works

Each of the `2^n` values of `mask` is a unique bit pattern, and each bit pattern selects a unique combination of elements — so the loop visits every subset exactly once. Sorting by length then contents afterward just fixes a canonical order; it doesn't change which subsets are found.

## Complexity

- Time: O(n * 2^n) — 2^n masks, each scanned in O(n) to build its subset (plus a sort).
- Space: O(n * 2^n) — the output holds all subsets, each up to length n.
