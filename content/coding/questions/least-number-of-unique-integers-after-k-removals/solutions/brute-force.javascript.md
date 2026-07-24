Count how often each value occurs, then spend the k removals one at a time: each round, scan the counts to find the value with the fewest remaining copies and remove one of it. A value disappears from the map once its count hits zero.

This mirrors the problem statement literally — repeatedly attack whichever value is cheapest to finish off — but re-scanning the whole count table on every single removal is wasteful.

```javascript
function leastNumberOfUniqueInts(arr, k) {
  const counts = new Map();
  for (const num of arr) counts.set(num, (counts.get(num) || 0) + 1);

  while (k > 0) {
    let smallestKey = null;
    let smallestVal = Infinity;
    for (const [key, val] of counts) {
      if (val < smallestVal) {
        smallestVal = val;
        smallestKey = key;
      }
    }
    counts.set(smallestKey, counts.get(smallestKey) - 1);
    if (counts.get(smallestKey) === 0) counts.delete(smallestKey);
    k--;
  }
  return counts.size;
}
```

## Why it works

Removing from the currently-smallest count is always at least as good as removing from a larger one: it is the fastest way to zero out a value and shrink the unique count. Doing this greedily, one removal at a time, is correct — it just costs a fresh scan of `counts` on every iteration instead of pre-sorting once.

## Complexity

- Time: O(n \* u) — n to build the counts, then up to n removals each scanning up to u unique keys; worst case O(n²).
- Space: O(n) — the count map holds up to n distinct keys.
