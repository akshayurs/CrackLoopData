Both earlier approaches spend O(h) extra space remembering how to get back up to an ancestor. Morris traversal removes that cost entirely by temporarily rewiring the tree itself: before descending into a left subtree, drop a thread from its rightmost node back up to the current node, so there is always a way home without a stack.

Concretely, for each node, find the rightmost node of its left subtree (its inorder predecessor). If that predecessor's right pointer is still empty, link it to the current node and move left. If the link is already there, it means the left subtree has been fully processed — record the current value, remove the thread to restore the tree, and move right.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        TreeNode node = root;
        while (node != null) {
            if (node.left == null) {
                result.add(node.val);
                node = node.right;
            } else {
                TreeNode predecessor = node.left;
                while (predecessor.right != null && predecessor.right != node) {
                    predecessor = predecessor.right;
                }
                if (predecessor.right == null) {
                    predecessor.right = node;
                    node = node.left;
                } else {
                    predecessor.right = null;
                    result.add(node.val);
                    node = node.right;
                }
            }
        }
        return result;
    }
}
```

## Why it works

A thread from a subtree's rightmost node back to its parent is the exact pointer needed to return after finishing that subtree, so no explicit stack is required. The first visit to a node with a left child builds the thread and dives left; when control returns via the thread, the code recognizes it (`predecessor.right == node`), removes it to leave the tree unchanged, records the value in the correct left-node-right position, and continues right. Every node is threaded and unthreaded at most once, so the tree is restored to its original shape by the end.

## Complexity

- Time: O(n) — each edge is traversed at most twice (once to build a thread, once to remove it).
- Space: O(1) — no recursion stack or explicit stack; only the output list, which doesn't count as extra space.
