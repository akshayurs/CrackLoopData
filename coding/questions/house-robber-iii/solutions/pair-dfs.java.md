The waste in the naive version comes from asking "what if I rob this house?" and "what if I skip it?" as two separate top-down questions, which forces re-deriving each child's answer twice. Flip it around: make every recursive call return **both** answers for its own subtree at once — the best total if the subtree's root is robbed, and the best total if it is not. A parent can then combine its children's answers with no re-computation.

Each call does a single post-order pass: gather the `{with, without}` pair from the left and right children, then compute `withRoot = root.val + withoutLeft + withoutRight` (robbing the root forbids robbing either child) and `withoutRoot = max(withLeft, withoutLeft) + max(withRight, withoutRight)` (skipping the root frees each child to be robbed or not, whichever is better).

```java
class Solution {
    public int rob(TreeNode root) {
        int[] result = dfs(root);
        return Math.max(result[0], result[1]);
    }

    private int[] dfs(TreeNode node) {
        if (node == null) return new int[]{0, 0}; // {withNode, withoutNode}

        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        int withNode = node.val + left[1] + right[1];
        int withoutNode = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{withNode, withoutNode};
    }
}
```

## Why it works

Every node's pair of answers depends only on its two children's pairs, computed exactly once each, so no subtree is ever solved twice. Robbing the root is only valid if neither child is also robbed, hence `left[1]`/`right[1]`; skipping the root places no constraint on the children, so each child independently picks whichever of its two answers is larger. The final result is the better of robbing or skipping the overall root.

## Complexity

- Time: O(n) — one post-order visit per node.
- Space: O(h) — recursion stack proportional to the tree's height (worst case O(n) for a skewed tree).
