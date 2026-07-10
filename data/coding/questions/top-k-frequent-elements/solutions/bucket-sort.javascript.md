The key observation: a value can appear at most `n` times, so frequency is a small integer in the range `1..n`. That means you can bucket values by their exact count instead of comparing counts against each other — no sorting needed.

Build an array of buckets indexed by frequency, drop each value into the bucket matching its count, then walk the buckets from the highest frequency downward, collecting values until you have `k`. Every step is linear, so the whole thing runs in O(n).

```javascript
function topKFrequent(nums, k) {
  const counts = new Map();
  for (const n of nums) counts.set(n, (counts.get(n) || 0) + 1);

  const buckets = Array.from({ length: nums.length + 1 }, () => []);
  for (const [value, count] of counts) buckets[count].push(value);

  const result = [];
  for (let freq = buckets.length - 1; freq > 0 && result.length < k; freq--) {
    for (const value of buckets[freq]) {
      result.push(value);
      if (result.length === k) break;
    }
  }
  return result.sort((a, b) => a - b);
}
```

## Why it works

`buckets[f]` holds every value that occurs exactly `f` times, and `f` can never exceed `nums.length`, so the array is big enough. Scanning from the highest index down visits values in strictly decreasing frequency, so the first `k` collected are the `k` most frequent. Indexing by count replaces comparison-based sorting entirely. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n + k log k) — counting, filling buckets, and scanning are each linear in n; the final ascending sort of the k results costs O(k log k).
- Space: O(n) — the map and the bucket array together hold O(n) entries.
