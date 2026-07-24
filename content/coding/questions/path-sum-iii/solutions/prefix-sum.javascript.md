The brute force redoes work because the running sum from the root to any node gets recomputed from scratch for every candidate start along the way. Track the sum from the root to the current node instead, and the classic "subarray sum equals k" trick carries over directly: if `runningSum - targetSum` was already seen higher up the current root-to-node path, everything between that earlier point and here sums to `targetSum`.

Keep a map of how many times each prefix sum has occurred *on the current path*, adding the current node's contribution before recursing and removing it again on the way back up — the map must only reflect ancestors of the node being processed, not siblings elsewhere in the tree.

```javascript
function pathSum(root, targetSum) {
  const prefixCounts = new Map([[0, 1]]);

  function dfs(node, runningSum) {
    if (node === null) return 0;
    runningSum += node.val;
    let count = prefixCounts.get(runningSum - targetSum) || 0;
    prefixCounts.set(runningSum, (prefixCounts.get(runningSum) || 0) + 1);
    count += dfs(node.left, runningSum) + dfs(node.right, runningSum);
    prefixCounts.set(runningSum, prefixCounts.get(runningSum) - 1);
    return count;
  }

  return dfs(root, 0);
}
```

## Why it works

`runningSum` is the sum of values from the root to the current node. A downward path from some ancestor `a` (exclusive) to the current node sums to `targetSum` exactly when `runningSum - sumToA === targetSum`, i.e. `sumToA === runningSum - targetSum`. `prefixCounts` holds exactly the root-to-ancestor sums still "open" on the current recursion stack, so looking up `runningSum - targetSum` counts every valid ancestor in O(1). Decrementing the count when backtracking out of a subtree keeps the map scoped to the current path, so paths through unrelated branches never interfere.

## Complexity

- Time: O(n) — each node is visited once, doing O(1) work per node.
- Space: O(n) — the map can hold up to n entries, plus O(h) recursion stack.
