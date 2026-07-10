Recursion works, but it hides the traversal state on the call stack, which is easy to overflow on a very deep tree and hard to pause or resume. Simulating the same left-node-right walk with an explicit stack gives full control over that state.

The trick is to keep pushing left children onto the stack until there are none left — that reaches the leftmost unvisited node. Popping the stack then visits it, and moving to its right child restarts the same "go left as far as possible" process from there.

```java
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode node = root;
        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            result.add(node.val);
            node = node.right;
        }
        return result;
    }
}
```

## Why it works

The inner loop dives to the leftmost node reachable from `node`, pushing every ancestor along the way so it can be revisited later. Popping gives the smallest unvisited node in the current subtree, which is correct because everything further left has already been recorded. Setting `node = node.right` then hands off to that subtree, and because it starts as `null` when there is no right child, the outer loop simply pops the next pending ancestor instead.

## Complexity

- Time: O(n) — every node is pushed and popped exactly once.
- Space: O(n) — O(h) for the stack plus O(n) for the output list; h can be O(n) for a skewed tree.
