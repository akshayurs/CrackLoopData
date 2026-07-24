Push the target down the tree instead of accumulating a running total: at each node, subtract the node's value from the remaining sum before recursing into its children. When a leaf is reached, the path sums to `targetSum` exactly when the remaining amount equals the leaf's own value.

An empty tree can never satisfy the condition, so that check comes first. Otherwise the answer is true if this node closes out the sum as a leaf, or if either subtree can close it out with the reduced target.

```python
def has_path_sum(root, target_sum):
    if root is None:
        return False
    remaining = target_sum - root.val
    if root.left is None and root.right is None:
        return remaining == 0
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)
```

## Why it works

Every recursive call carries the amount still needed from that node downward, so by the time a leaf is reached `remaining` already accounts for every ancestor on the path. The leaf check is exact rather than `<= 0` because negative values are allowed, so overshooting or undershooting both simply fail. The `or` between the two subtree calls means any single successful root-to-leaf path is enough to return true.

## Complexity

- Time: O(n) — every node is visited at most once.
- Space: O(h) — the recursion stack is as deep as the tree height, up to O(n) for a skewed tree.
