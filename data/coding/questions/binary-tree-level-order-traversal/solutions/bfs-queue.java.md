Level order is exactly what breadth-first search produces, so lean on a queue. The trick is grouping the output by level: before draining the queue, note how many nodes it currently holds — that count is precisely the size of the current level. Poll exactly that many, record their values, and offer their children to form the next level.

Because every child is added to the back while the current level is polled from the front, nodes always come out top-to-bottom and left-to-right.

```java
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levels = new ArrayList<>();
        if (root == null) return levels;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            for (int i = queue.size(); i > 0; i--) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            levels.add(level);
        }
        return levels;
    }
}
```

## Why it works

Capturing `queue.size()` before the inner loop fixes how many nodes belong to the current level. The inner loop consumes exactly those nodes and offers their children behind the still-unprocessed nodes, so the queue's FIFO order guarantees each level is emitted fully before the next begins. Left children are offered before right children, preserving left-to-right order within every level.

## Complexity

- Time: O(n) — each node is offered and polled exactly once.
- Space: O(n) — the queue plus the output hold up to n values; a single level can be as wide as n/2.
