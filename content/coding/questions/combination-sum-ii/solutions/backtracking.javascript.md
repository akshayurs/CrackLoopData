Sort the array first — that turns "skip duplicate values" into "skip repeated values sitting next to each other." Walk the candidates with a start index, and at each recursive level only try a value once: if the current index isn't the first one tried at this level and it matches the previous candidate, skip it, since starting a combination with that duplicate value again would just re-produce a combination already explored from the earlier occurrence.

Because the array is sorted, you can also cut a branch short the moment a candidate exceeds what's left to reach — everything after it is at least as large, so no later candidate at this level can help either. Together, the duplicate skip and the early cutoff avoid ever building a combination that will end up thrown away.

```javascript
function combinationSum2(candidates, target) {
  const sorted = [...candidates].sort((a, b) => a - b);
  const n = sorted.length;
  const result = [];
  const path = [];

  function backtrack(start, remaining) {
    if (remaining === 0) {
      result.push([...path]);
      return;
    }
    for (let i = start; i < n; i++) {
      if (i > start && sorted[i] === sorted[i - 1]) continue;
      if (sorted[i] > remaining) break;
      path.push(sorted[i]);
      backtrack(i + 1, remaining - sorted[i]);
      path.pop();
    }
  }

  backtrack(0, target);
  return result;
}
```

## Why it works

Fixing a `start` index and only moving forward ensures each array position is used at most once per combination. Skipping a value that equals its predecessor *at the same recursion level* prevents two different occurrences of the same duplicate value from spawning identical combinations, while still allowing that value to appear multiple times *within* one combination through the recursive call. Because the array is sorted, once a candidate exceeds the remaining target, every later candidate in the loop does too, so the loop can break instead of continuing to check. Sorting guarantees each `path` is built in ascending order, and scanning indices left to right means combinations are emitted in ascending lexicographic order already.

## Complexity

- Time: O(2^n · n) — worst case still explores an exponential number of valid combinations, each costing O(n) to copy into the result; the pruning removes wasted work but not the exponential ceiling.
- Space: O(n) — recursion depth and the `path` buffer are bounded by the array length, excluding the output.
