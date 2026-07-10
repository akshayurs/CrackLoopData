Start with a plain breadth-first traversal: a queue holds one level's worth of nodes at a time, and you drain exactly that many before moving to the children. That alone produces the levels left-to-right, top to bottom.

Zigzag only changes the *order values are read in*, not which nodes belong to which level — so build each level normally, then flip it in place whenever the current level is meant to run right-to-left. A boolean flag toggled after every level tells you when to reverse.

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
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            if (!leftToRight) Collections.reverse(level);
            result.add(level);
            leftToRight = !leftToRight;
        }
        return result;
    }
}
```

## Why it works

`size` is snapshotted before the inner loop, so exactly the nodes belonging to the current level are polled — their children get offered for the next round without being processed early. The level is collected in the natural left-to-right order every time; `leftToRight` only decides whether that list gets reversed before being added to the answer, which is enough to alternate direction level by level.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once; reversing a level costs at most O(n) total across all levels.
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
