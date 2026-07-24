The most direct reading of the problem: every subset of `{1, ..., n}` is a candidate, so walk through all `2^n` of them and keep the ones with exactly `k` elements. A bitmask from `0` to `2^n - 1` is a compact way to represent "which numbers are in this subset" — bit `i` set means `i + 1` is included.

Because masks aren't visited in an order that matches sorted combinations, the collected list needs an explicit sort at the end to make the output deterministic.

```javascript
function combine(n, k) {
  const result = [];
  for (let mask = 0; mask < (1 << n); mask++) {
    const combo = [];
    for (let i = 0; i < n; i++) {
      if (mask & (1 << i)) combo.push(i + 1);
    }
    if (combo.length === k) result.push(combo);
  }
  result.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return a[i] - b[i];
    }
    return 0;
  });
  return result;
}
```

## Why it works

Every subset of `{1, ..., n}` corresponds to exactly one `n`-bit mask, so iterating masks from `0` to `2^n - 1` enumerates every subset without duplicates or omissions. Filtering on the decoded length keeps only size-`k` subsets, and decoding a mask's bits from low to high builds each combination already in increasing order. The final sort compares combinations element by element to fix the order *between* them, since mask value does not correspond to lexicographic order of the decoded numbers.

## Complexity

- Time: O(2^n * n) — every mask is inspected and decoded in O(n), plus a sort over the O(C(n, k)) matches.
- Space: O(n) — auxiliary space to decode a mask, excluding the returned combinations.
