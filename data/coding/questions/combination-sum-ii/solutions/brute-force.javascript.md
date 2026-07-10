Explore every way of including or excluding each position: at index `i` you either take `candidates[i]` and recurse, or skip it and recurse. That walks every subset of the array, and any subset whose running sum lands exactly on the target gets recorded.

Duplicate values in the input mean different subsets of indices can produce the same list of numbers, so the raw hits need deduplication. Sorting the candidates first and stashing each hit as a serialized string in a `Set` handles that before the final sort puts everything in the required order.

```javascript
function combinationSum2(candidates, target) {
  const sorted = [...candidates].sort((a, b) => a - b);
  const n = sorted.length;
  const seen = new Set();
  const path = [];

  function backtrack(i, remaining) {
    if (remaining === 0) {
      seen.add(JSON.stringify(path));
      return;
    }
    if (remaining < 0 || i === n) return;
    path.push(sorted[i]);
    backtrack(i + 1, remaining - sorted[i]);
    path.pop();
    backtrack(i + 1, remaining);
  }

  backtrack(0, target);
  return Array.from(seen)
    .map((s) => JSON.parse(s))
    .sort((a, b) => {
      for (let k = 0; k < Math.min(a.length, b.length); k++) {
        if (a[k] !== b[k]) return a[k] - b[k];
      }
      return a.length - b.length;
    });
}
```

## Why it works

Every combination corresponds to exactly one path through the include/exclude decision tree over indices, so nothing valid is missed. Sorting the array up front means each recorded path already lists its numbers ascending; routing hits through a `Set` of serialized arrays collapses duplicate combinations, and the final comparator sorts the combinations lexicographically.

## Complexity

- Time: O(2^n · n log n) — every index is included or excluded, and each of the up to 2^n paths costs O(n log n) to serialize/sort into the result.
- Space: O(2^n · n) — the set can hold up to 2^n combinations of length up to n.
