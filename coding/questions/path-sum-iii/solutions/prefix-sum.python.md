The brute force redoes work because the running sum from the root to any node gets recomputed from scratch for every candidate start along the way. Track the sum from the root to the current node instead, and the classic "subarray sum equals k" trick carries over directly: if `running_sum - target_sum` was already seen higher up the current root-to-node path, everything between that earlier point and here sums to `target_sum`.

Keep a hash map of how many times each prefix sum has occurred *on the current path*, adding the current node's contribution before recursing and removing it again on the way back up — the map must only reflect ancestors of the node being processed, not siblings elsewhere in the tree.

```python
def path_sum(root, target_sum):
    prefix_counts = {0: 1}

    def dfs(node, running_sum):
        if node is None:
            return 0
        running_sum += node.val
        count = prefix_counts.get(running_sum - target_sum, 0)
        prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1
        count += dfs(node.left, running_sum) + dfs(node.right, running_sum)
        prefix_counts[running_sum] -= 1
        return count

    return dfs(root, 0)
```

## Why it works

`running_sum` is the sum of values from the root to the current node. A downward path from some ancestor `a` (exclusive) to the current node sums to `target_sum` exactly when `running_sum - sum_to_a == target_sum`, i.e. `sum_to_a == running_sum - target_sum`. `prefix_counts` holds exactly the root-to-ancestor sums still "open" on the current recursion stack, so looking up `running_sum - target_sum` counts every valid ancestor in O(1). Decrementing the count when backtracking out of a subtree keeps the map scoped to the current path, so paths through unrelated branches never interfere.

## Complexity

- Time: O(n) — each node is visited once, doing O(1) work per node.
- Space: O(n) — the hash map can hold up to n entries, plus O(h) recursion stack.
