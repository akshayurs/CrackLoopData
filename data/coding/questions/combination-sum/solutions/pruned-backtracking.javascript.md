Once the candidates are sorted, a wasted branch becomes easy to spot early: if the current candidate already exceeds what's left to reach the target, every candidate after it (all larger) will too, so the whole rest of the loop can be skipped instead of merely skipped-per-branch at the base case.

That one change — breaking out of the loop instead of recursing one level deeper only to fail — is what turns the same index-based backtracking into something that stops fanning out the moment a subtree is provably useless.

```javascript
function combinationSum(candidates, target) {
  const sorted = [...candidates].sort((a, b) => a - b);
  const result = [];
  const path = [];

  function backtrack(start, remaining) {
    if (remaining === 0) {
      result.push([...path]);
      return;
    }
    for (let i = start; i < sorted.length; i++) {
      if (sorted[i] > remaining) {
        break;
      }
      path.push(sorted[i]);
      backtrack(i, remaining - sorted[i]);
      path.pop();
    }
  }

  backtrack(0, target);
  return result;
}
```

## Why it works

Because `sorted` is ordered ascending, the moment `sorted[i] > remaining` is true, every candidate after it is also too large — `break` discards all of them in one step instead of recursing into each and failing individually. The `start` index still prevents duplicate orderings of the same multiset, and the base case still fires exactly when a path sums to `target`, so the set of results is identical to the unpruned version; only the amount of wasted work changes.

## Complexity

- Time: O(N^(T/M + 1)) — N is the candidate count, T the target, M the smallest candidate; that bounds the depth and branching of the pruned tree.
- Space: O(target) — the recursion depth and `path` are bounded by how many times the smallest candidate divides into `target`.
