The brute-force scan is wasted work: once you know the counts, the removal order never changes — you always want to finish off the value with the smallest remaining count first. Conceptually that's a min-heap pop repeated until the budget runs out; JavaScript has no built-in heap, but sorting the counts ascending once produces exactly the same pop order, so a sorted array does the job just as well.

```javascript
function leastNumberOfUniqueInts(arr, k) {
  const counts = new Map();
  for (const num of arr) counts.set(num, (counts.get(num) || 0) + 1);

  const freqs = [...counts.values()].sort((a, b) => a - b);
  let unique = freqs.length;
  for (const freq of freqs) {
    if (k < freq) break;
    k -= freq;
    unique--;
  }
  return unique;
}
```

## Why it works

Walking the sorted frequency list from smallest to largest visits values in the exact order a min-heap would pop them. If `k` is at least the current frequency, removing that value entirely is free and strictly shrinks the unique count, so it's always safe to take. The first frequency `k` cannot fully cover means no later (larger) frequency can be cleared either, so stopping there is correct.

## Complexity

- Time: O(n log n) — building the counts is O(n); sorting the u frequencies is O(u log u).
- Space: O(n) — the count map and frequency array each hold up to n entries.
