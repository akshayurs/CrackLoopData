The trap in this problem is that checking `left < node < right` on immediate children is not enough — a value must respect every ancestor above it. Capture that by threading an allowed open interval `(low, high)` down the recursion: each node must fall strictly inside its interval, and moving left tightens the upper bound to the node's value while moving right tightens the lower bound.

Using `long` bounds seeded with `Long.MIN_VALUE`/`Long.MAX_VALUE` sidesteps the edge case where a node holds `Integer.MIN_VALUE` or `Integer.MAX_VALUE`, so the strict comparisons stay correct.

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return valid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean valid(TreeNode node, long low, long high) {
        if (node == null) return true;
        if (node.val <= low || node.val >= high) return false;
        return valid(node.left, low, node.val) && valid(node.right, node.val, high);
    }
}
```

## Why it works

When we descend left, the current node becomes the strict upper bound; when we descend right, it becomes the strict lower bound. So each node inherits the tightest lower and upper limits from all of its ancestors, exactly encoding the BST rule across the whole tree. The sentinel `long` bounds are wide enough that any valid 32-bit node value passes at the root.

## Complexity

- Time: O(n) — each node is checked once.
- Space: O(h) — the recursion stack holds one frame per level, up to the tree's height h.
