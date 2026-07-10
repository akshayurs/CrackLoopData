Rather than generating every arrangement and cleaning up afterward, avoid building duplicates at all. Sort the array so equal values are adjacent, then only let a repeated value start a new branch once the previous copy of that value has already been placed in the current path.

The pruning rule: at a given depth, skip index `i` if `nums[i] === nums[i - 1]` and the earlier copy is not currently in use. That fixes the relative order equal values can be placed in, which is exactly what removes duplicate permutations at the source.

```javascript
function permuteUnique(nums) {
  const sorted = [...nums].sort((a, b) => a - b);
  const used = new Array(sorted.length).fill(false);
  const current = [];
  const result = [];

  function backtrack() {
    if (current.length === sorted.length) {
      result.push([...current]);
      return;
    }
    for (let i = 0; i < sorted.length; i++) {
      if (used[i]) continue;
      if (i > 0 && sorted[i] === sorted[i - 1] && !used[i - 1]) continue;
      used[i] = true;
      current.push(sorted[i]);
      backtrack();
      current.pop();
      used[i] = false;
    }
  }

  backtrack();
  return result;
}
```

## Why it works

Sorting groups equal values together. If two equal values are both available at the same depth, placing the later one before the earlier one has been used would reach a permutation already reachable by placing the earlier one first — so that branch is redundant and can be cut without losing any distinct result. Because the array is sorted and indices are tried in increasing order, the recursion also emits results already in lexicographic order.

## Complexity

- Time: O(n! · n) worst case (all distinct values) — pruning only removes branches that would duplicate output; each surviving branch still costs O(n) to materialize.
- Space: O(n) for the recursion stack, `used`, and `current`, plus O(n! · n) for the collected output.
