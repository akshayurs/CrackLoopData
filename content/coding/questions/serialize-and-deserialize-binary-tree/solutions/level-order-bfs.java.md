Instead of recursing, sweep the tree breadth-first with a queue. Every time a real node comes off the queue, record its value and offer both children onto the queue — offering `null` for a missing child rather than skipping it, so the string also encodes exactly where the gaps are.

Deserializing mirrors the same sweep: split the string back into tokens and read them in the order they were written, attaching each one as the left or right child of the next node waiting in a queue, and only enqueuing the children that weren't `"#"`. Because both sides visit nodes level by level, left-to-right, the queues stay in lockstep the whole way through.

```java
import java.util.*;

class Codec {
    public String serialize(TreeNode root) {
        if (root == null) return "#";
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null) {
                sb.append("#,");
                continue;
            }
            sb.append(node.val).append(",");
            queue.offer(node.left);
            queue.offer(node.right);
        }
        return sb.toString();
    }

    public TreeNode deserialize(String data) {
        if (data.equals("#")) return null;
        String[] vals = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(vals[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (!vals[i].equals("#")) {
                node.left = new TreeNode(Integer.parseInt(vals[i]));
                queue.offer(node.left);
            }
            i++;
            if (!vals[i].equals("#")) {
                node.right = new TreeNode(Integer.parseInt(vals[i]));
                queue.offer(node.right);
            }
            i++;
        }
        return root;
    }
}
```

## Why it works

Both serialize and deserialize process nodes in identical breadth-first order, so the i-th "slot" written always corresponds to the i-th child position read back. Skipping the enqueue for `"#"` slots keeps the two queues synchronized without ever confusing a real node with a placeholder.

## Complexity

- Time: O(n) — every node and null placeholder is visited exactly once on each side.
- Space: O(n) — the queue holds up to one level's worth of nodes, and the token array holds one entry per slot.
