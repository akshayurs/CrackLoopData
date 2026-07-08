There is a defining property of a BST: an **in-order traversal** (left, node, right) visits the values in strictly increasing order. So walk the tree in-order and check that each value exceeds the one before it. Here we do it iteratively with an explicit stack, which sidesteps recursion depth and keeps only the previous value around.

You never need the full sequence — just the last value seen. Comparing each node against it turns the check into one linear pass.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean isValidBST(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode node = root;
        Integer prev = null;
        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            if (prev != null && node.val <= prev) return false;
            prev = node.val;
            node = node.right;
        }
        return true;
    }
}
```

## Why it works

Pushing left children then popping reproduces the in-order order without recursion. Each popped node is the in-order successor of the previous one, so asserting `node.val > prev` enforces strictly increasing values across the whole tree. Any equal or smaller value fails immediately.

## Complexity

- Time: O(n) — each node is pushed and popped once.
- Space: O(h) — the stack holds at most one root-to-leaf path, up to the tree's height h.
