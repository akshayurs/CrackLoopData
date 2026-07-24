Instead of recomputing downward sums from scratch for every node, fold the two questions into one traversal. A helper `down(node)` reports the best sum of a path that starts at `node` and goes straight down through one child — exactly the value a *parent* needs. While computing that, the helper also has both children's downward values in hand, so it can check whether `node` acting as a peak (using both children) beats the running global best.

Negative subtrees are simply worth skipping: clamp each child's contribution to zero before adding it in, so a lousy branch never drags the sum down.

```java
class Solution {
    private int best;

    public int maxPathSum(TreeNode root) {
        best = Integer.MIN_VALUE;
        down(root);
        return best;
    }

    private int down(TreeNode node) {
        if (node == null) return 0;
        int left = Math.max(down(node.left), 0);
        int right = Math.max(down(node.right), 0);
        best = Math.max(best, node.val + left + right);
        return node.val + Math.max(left, right);
    }
}
```

## Why it works

`down(node)` always returns the best sum obtainable by starting at `node` and continuing into at most one child, which is the only shape of contribution a parent can legally use. Before returning, it also evaluates `node` as a potential peak — using both children — and folds that candidate into `best`. Since every path has exactly one peak, and every node is visited exactly once as a candidate peak, the global maximum is captured in a single traversal.

## Complexity

- Time: O(n) — each node is visited once.
- Space: O(h) — the recursion stack depth equals the tree height, up to O(n) for a skewed tree.
