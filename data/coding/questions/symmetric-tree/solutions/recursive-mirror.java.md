Symmetry is a statement about two subtrees at a time: the whole tree is symmetric exactly when the left and right children are **mirrors** of each other. Reframe the problem as "are these two trees mirror images?" and recurse — a helper that takes two nodes instead of one.

Two nodes mirror each other when both are absent, or both hold the same value and node `a`'s left mirrors node `b`'s right while `a`'s right mirrors `b`'s left (the sides are swapped on purpose).

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return root == null || isMirror(root.left, root.right);
    }

    private boolean isMirror(TreeNode a, TreeNode b) {
        if (a == null && b == null) return true;
        if (a == null || b == null || a.val != b.val) return false;
        return isMirror(a.left, b.right) && isMirror(a.right, b.left);
    }
}
```

## Why it works

`isMirror` compares two positions that should be reflections of one another. Both empty is a match; one empty or differing values is an immediate mismatch. Otherwise the values agree, and the reflection property is enforced by crossing the recursive calls — `a.left` against `b.right`, `a.right` against `b.left` — so the check propagates the swap down every level. The top-level call seeds this with the root's two children.

## Complexity

- Time: O(n) — every node is visited once as part of exactly one mirrored pair.
- Space: O(h) — the recursion stack is as deep as the tree height, up to O(n) for a skewed tree.
