The trap in this problem is that checking `left < node < right` on immediate children is not enough — a value must respect every ancestor above it. Capture that by threading an allowed open interval `(low, high)` down the recursion: each node must fall strictly inside its interval, and moving left tightens the upper bound to the node's value while moving right tightens the lower bound.

This propagates the full set of ancestor constraints to every node in a single top-down pass, with no extra scanning.

```python
def is_valid_bst(root):
    def valid(node, low, high):
        if node is None:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, None, None)
```

## Why it works

When we descend left, the current node becomes the strict upper bound; when we descend right, it becomes the strict lower bound. So each node inherits the tightest lower and upper limits from all of its ancestors, exactly encoding the BST rule across the whole tree. `None` bounds represent an open (unbounded) side, so the root is unconstrained.

## Complexity

- Time: O(n) — each node is checked once.
- Space: O(h) — the recursion stack holds one frame per level, up to the tree's height h.
