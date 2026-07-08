Read the definition literally: a node is valid when *every* value in its left subtree is smaller and *every* value in its right subtree is larger. Verify those two rules directly at each node with helper walks, then recurse into the children to confirm they are valid BSTs too.

This is the most direct translation of the rules, but re-walking a subtree at every ancestor repeats work — the same nodes get visited once for each node above them.

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        if (!allLess(root.left, root.val)) return false;
        if (!allGreater(root.right, root.val)) return false;
        return isValidBST(root.left) && isValidBST(root.right);
    }

    private boolean allLess(TreeNode node, int limit) {
        if (node == null) return true;
        return node.val < limit && allLess(node.left, limit) && allLess(node.right, limit);
    }

    private boolean allGreater(TreeNode node, int limit) {
        if (node == null) return true;
        return node.val > limit && allGreater(node.left, limit) && allGreater(node.right, limit);
    }
}
```

## Why it works

`allLess` and `allGreater` confirm the two subtree rules for the current node, and the recursive call reapplies the same guarantee at every node. A single violating value short-circuits its helper to `false`, which propagates up and fails the whole check.

## Complexity

- Time: O(n^2) — each of n nodes may trigger a full walk of its subtree; worst case (a skewed tree) is quadratic.
- Space: O(n) — recursion depth in the worst case.
