The longest path that bends at a given node runs down its left subtree, up through the node, and down its right subtree — so its edge count is exactly `height(left) + height(right)`. The overall diameter is the largest such value across every node in the tree.

The direct approach spells that out: for each node, measure the heights of its two subtrees and combine them, then recurse into the children to check whether a deeper node yields a longer bend. The catch is that computing a height is itself a full traversal, so heights get recomputed again and again.

```python
def diameter_of_binary_tree(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def diameter(node):
        if node is None:
            return 0
        through = height(node.left) + height(node.right)
        return max(through, diameter(node.left), diameter(node.right))

    return diameter(root)
```

## Why it works

For any node, the longest path bending at it uses the tallest branch on each side, giving `height(left) + height(right)` edges. Taking the maximum of that quantity over all nodes covers every possible longest path, because any path has a unique highest node where it turns. Recursing into both children guarantees every node is considered as the turning point.

## Complexity

- Time: O(n^2) — for each of the n nodes, `height` re-traverses its whole subtree; worst case (a skewed tree) is quadratic.
- Space: O(h) — recursion depth equals the tree height h, up to O(n) for a skewed tree.
