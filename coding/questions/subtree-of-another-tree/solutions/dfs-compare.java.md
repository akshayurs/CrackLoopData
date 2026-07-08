A subtree match can start at any node of `root`, so the direct approach is to try them all. Visit every node and ask a simple question: "if I treat this node as the top, is the tree hanging off it identical to `subRoot`?" If any node answers yes, we are done.

The identity check is its own small recursion: two trees are the same when their roots hold equal values and their left and right children are pairwise identical. Pairing this per-node comparison with a full traversal covers every possible starting point.

```java
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) {
            return false;
        }
        if (same(root, subRoot)) {
            return true;
        }
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean same(TreeNode a, TreeNode b) {
        if (a == null || b == null) {
            return a == b;
        }
        return a.val == b.val && same(a.left, b.left) && same(a.right, b.right);
    }
}
```

## Why it works

`same` returns `true` only when both trees run out of nodes at exactly the same places with matching values along the way — that is the definition of structural and value equality. The outer recursion tries `subRoot` against `root`, then against every descendant, so if a matching subtree exists anywhere it will be the current node in one of those calls. If no node matches, the traversal exhausts the tree and returns `false`.

## Complexity

- Time: O(m·n) — for each of the m nodes in `root`, `same` may compare up to n nodes of `subRoot`.
- Space: O(m) — the recursion stack can be as deep as the height of `root`, up to m for a skewed tree.
