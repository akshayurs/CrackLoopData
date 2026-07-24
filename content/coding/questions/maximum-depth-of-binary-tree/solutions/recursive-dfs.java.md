The depth of a tree is defined in terms of its subtrees: the longest root-to-leaf path must dive through either the left child or the right child, then add one for the root itself. That self-referential shape is exactly what recursion expresses cleanly.

Ask each node for the deeper of its two subtrees and add one. A null node contributes depth `0`, which is the base case that unwinds the whole recursion.

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

## Why it works

Each call returns the maximum depth of the subtree rooted at that node. A missing child returns `0`, so a leaf returns `1 + max(0, 0) = 1`. Every internal node picks its deeper side and adds itself, so the value that bubbles up to the root is the length of the longest path in the whole tree.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) — the recursion stack holds one frame per level, up to the tree's height h (O(n) for a skewed tree, O(log n) when balanced).
