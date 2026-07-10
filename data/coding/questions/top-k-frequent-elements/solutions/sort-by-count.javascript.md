Start with the obvious plan: count how many times each value appears, then rank the distinct values by that count. A `Map` builds the counts in one pass, and sorting the keys by their frequency puts the most common ones at the front.

Once sorted, the answer is just the first `k` values. The counting is linear, but the sort of the distinct values is what dominates the running time.

```javascript
function topKFrequent(nums, k) {
  const counts = new Map();
  for (const n of nums) {
    counts.set(n, (counts.get(n) || 0) + 1);
  }
  const ordered = [...counts.keys()].sort((a, b) => counts.get(b) - counts.get(a));
  return ordered.slice(0, k).sort((a, b) => a - b);
}
```

## Why it works

`counts` maps each value to its number of occurrences. Sorting the keys by `counts.get(value)` in descending order lines them up from most to least frequent, so slicing off the first `k` gives exactly the `k` most common values. Because the answer is guaranteed unique, there is no tie to break at the boundary. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n log n) — counting is O(n); sorting the up-to-n distinct values costs O(n log n); the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the map and the key array each hold up to n entries.
