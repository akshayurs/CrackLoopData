Sort `nums` first so every duplicate value lands next to its twin. Then build subsets with standard backtracking: at each recursive call, record the current `path` as one valid subset, and try extending it with every index from `start` onward.

The dedup trick is a single rule at each level of the recursion: skip an index if it holds the same value as the index right before it *and* that earlier sibling was already considered at this level. That rule prunes the branch that would recreate a subset already produced by an earlier, equal-valued index — without ever building a subset just to throw it away.

```javascript
function subsetsWithDup(nums) {
  const sorted = [...nums].sort((a, b) => a - b);
  const result = [];
  const path = [];

  function backtrack(start) {
    result.push([...path]);
    for (let i = start; i < sorted.length; i++) {
      if (i > start && sorted[i] === sorted[i - 1]) continue;
      path.push(sorted[i]);
      backtrack(i + 1);
      path.pop();
    }
  }

  backtrack(0);
  return result;
}
```

## Why it works

Sorting groups equal values together, so at any recursion level the sibling calls try each *distinct* value exactly once — `i > start && sorted[i] === sorted[i - 1]` catches a second sibling with the same value and skips it, since its subtree would only reproduce subsets the first sibling's subtree already generated. Recording `path` on every entry (not just at the leaves) captures subsets of every length, including the empty one. Because indices are always visited in increasing sorted order, the subsets are emitted in ascending, lexicographic order with no extra sorting step needed.

## Complexity

- Time: O(n · 2^n) — up to 2^n subsets are emitted, each copied in O(n).
- Space: O(n · 2^n) — output storage; the recursion stack itself is only O(n).
