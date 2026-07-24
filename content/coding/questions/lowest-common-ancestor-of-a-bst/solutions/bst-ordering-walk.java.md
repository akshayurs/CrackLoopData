The BST invariant tells you which way to go without ever inspecting both subtrees. Start at the root: if both `p` and `q` are smaller than the current value, their ancestor must be somewhere in the left subtree, so step left. If both are larger, step right. The moment they no longer agree — one is on each side, or the current node's value equals one of them — you've found the split point, and it's the answer.

No recursion, no stored paths, no backtracking: the walk only ever moves downward, straight toward the answer.

```java
class Solution {
    public int lowestCommonAncestor(TreeNode root, int p, int q) {
        TreeNode node = root;
        while (node != null) {
            if (p < node.val && q < node.val) {
                node = node.left;
            } else if (p > node.val && q > node.val) {
                node = node.right;
            } else {
                return node.val;
            }
        }
        return -1;
    }
}
```

## Why it works

Because the tree is a BST, "both targets are less than the current node" means both live in the left subtree, and the search can safely discard the right side entirely — the true LCA can't be there. The same logic applies in reverse for the right subtree. The loop terminates the instant the targets stop being on the same side, which by definition is where their paths from the root diverge — the lowest common ancestor.

## Complexity

- Time: O(h) — one downward step per level, where h is the tree height (O(log n) if balanced, O(n) worst case).
- Space: O(1) — a single pointer, no recursion stack.
