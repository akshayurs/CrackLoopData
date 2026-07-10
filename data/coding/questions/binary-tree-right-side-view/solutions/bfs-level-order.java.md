The most literal reading of "what you'd see from the side" is to process the tree level by level and remember only the last node visited at each depth — that is exactly the rightmost node, since a standard left-to-right traversal reaches it last.

A queue-based breadth-first walk naturally groups nodes by level: process the queue's current contents as one batch, and whichever node comes off last in that batch is the one visible from the right.

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == levelSize - 1) {
                    result.add(node.val);
                }
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
        }
        return result;
    }
}
```

## Why it works

`levelSize` freezes how many nodes belong to the current level before any children get added, so the loop drains exactly that level. Nodes are polled left to right (children were added left-then-right), so the last one polled in the batch is the rightmost node at that depth — the only one recorded.

## Complexity

- Time: O(n) — every node is added and polled exactly once.
- Space: O(n) — the queue can hold an entire level, which is O(n) for a wide tree.
