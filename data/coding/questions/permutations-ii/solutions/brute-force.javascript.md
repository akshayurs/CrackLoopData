The same idea in JavaScript: generate every position-based arrangement of the array, exactly as if all values were distinct, then discard the ones that duplicate an arrangement already produced.

A recursive swap-free backtrack over indices builds all `n!` orderings. Each finished arrangement is stringified so a `Set` can dedupe by value, then the survivors are parsed back and sorted for a deterministic result.

```javascript
function permuteUnique(nums) {
  const used = new Array(nums.length).fill(false);
  const current = [];
  const raw = [];

  function backtrack() {
    if (current.length === nums.length) {
      raw.push([...current]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      current.push(nums[i]);
      backtrack();
      current.pop();
      used[i] = false;
    }
  }

  backtrack();

  const unique = [...new Set(raw.map((p) => JSON.stringify(p)))].map((s) => JSON.parse(s));
  return unique.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return a[i] - b[i];
    }
    return 0;
  });
}
```

## Why it works

The backtrack visits every unused index at each depth, so it produces all `n!` position-based orderings regardless of repeated values. Two orderings that look identical (same values, same positions) serialize to the same JSON string, so the `Set` merges them. The final comparator sorts lexicographically by element so the output is deterministic.

## Complexity

- Time: O(n! · n) — n! permutations, each O(n) to build, stringify, and compare during sort.
- Space: O(n! · n) — every raw permutation and its string key are held before deduplication.
