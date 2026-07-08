There is a defining property of a BST: an **in-order traversal** (left, node, right) visits the values in strictly increasing order. So instead of comparing whole subtrees, walk the tree in-order and check that each value is larger than the one before it. The moment a value fails to increase, the tree is not a BST.

You never need to store the full sequence — only the previously visited value. Carrying that single running comparison turns the check into one linear pass.

```python
def is_valid_bst(root):
    prev = [None]

    def inorder(node):
        if node is None:
            return True
        if not inorder(node.left):
            return False
        if prev[0] is not None and node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right)

    return inorder(root)
```

## Why it works

In-order traversal emits BST values sorted ascending. By keeping only `prev`, the last value seen, we assert `node.val > prev` at every step; equality or a drop means the sort order broke, so the tree cannot be a BST. Because every node is compared against its true in-order predecessor, the check is global, not just parent-to-child.

## Complexity

- Time: O(n) — each node is visited once.
- Space: O(h) — the recursion stack holds one frame per level, up to the tree's height h.
