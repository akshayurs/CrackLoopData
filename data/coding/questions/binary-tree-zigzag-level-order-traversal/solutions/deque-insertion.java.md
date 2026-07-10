Reversing a level after the fact is an extra pass you don't actually need — you already know the direction *before* you start placing values into that level, so you can just put each value where it ultimately belongs. Building the level as a `LinkedList` lets you add to either end in O(1).

Keep the same breadth-first structure, but instead of always appending to the tail, add to the tail on a left-to-right level and to the head on a right-to-left one. The queue that drives the traversal is unaffected — children are still discovered strictly left to right — only the container you're writing values into changes its insertion side.

```java
import java.util.*;

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        boolean leftToRight = true;
        while (!queue.isEmpty()) {
            int size = queue.size();
            LinkedList<Integer> level = new LinkedList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (leftToRight) level.addLast(node.val);
                else level.addFirst(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(level);
            leftToRight = !leftToRight;
        }
        return result;
    }
}
```

## Why it works

The traversal queue always discovers a level's nodes left to right, regardless of the output direction — only where each value lands in `level` changes. On a left-to-right level, `addLast` reproduces that same order; on a right-to-left level, `addFirst` means the first node discovered ends up last, which is exactly the mirrored order. No separate reversal step is needed because the direction is baked into the insertion itself.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once, and each value is inserted into its level in O(1).
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
