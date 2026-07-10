Sorting is wasteful — we don't need the full order, only the ability to ask "is `x` present?" in O(1). Drop every value into a `Set`, then walk the values and count a run only from its left end: a value `n` is a run start exactly when `n - 1` is not in the set. From each start, step forward while the next integer exists.

The trick that keeps this linear is starting only at run beginnings. Every value is visited by the outer loop once, and the inner walk touches each value at most once across the whole algorithm, so the total work is O(n) even though it looks nested.

```javascript
function longestConsecutive(nums) {
  const values = new Set(nums);
  let best = 0;
  for (const n of values) {
    if (values.has(n - 1)) continue;
    let length = 1;
    while (values.has(n + length)) length += 1;
    best = Math.max(best, length);
  }
  return best;
}
```

## Why it works

The `values.has(n - 1)` guard ensures the inner `while` only fires from the smallest element of each run. That run is then walked exactly once; interior elements are skipped by the guard, so no value is counted twice. Because each run is traversed a single time in total, the combined length of all inner walks is at most n.

## Complexity

- Time: O(n) — each value is inserted into the set once and visited by the inner walk at most once.
- Space: O(n) — the set of all distinct values.
