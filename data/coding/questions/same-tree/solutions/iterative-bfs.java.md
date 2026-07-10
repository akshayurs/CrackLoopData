The recursion just walks both trees in lockstep, comparing aligned nodes — and any recursion can be rewritten with an explicit queue. Push the two roots as a pair, then repeatedly poll a pair and apply the same three checks: both empty (fine, skip), exactly one empty or values unequal (mismatch), otherwise enqueue the two pairs of children to compare later.

This trades the call stack for a queue you control, which sidesteps recursion-depth limits on very tall trees.

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Deque<TreeNode[]> queue = new ArrayDeque<>();
        queue.add(new TreeNode[]{p, q});
        while (!queue.isEmpty()) {
            TreeNode[] pair = queue.poll();
            TreeNode a = pair[0], b = pair[1];
            if (a == null && b == null) continue;
            if (a == null || b == null || a.val != b.val) return false;
            queue.add(new TreeNode[]{a.left, b.left});
            queue.add(new TreeNode[]{a.right, b.right});
        }
        return true;
    }
}
```

## Why it works

Each queued pair represents two positions that must agree. Aligned empties contribute nothing and are skipped; a lone empty or a value difference fails immediately. When a pair matches, its children are enqueued so the same comparison reaches every position. The queue empties only if no mismatch was ever found, which is exactly the condition for the trees to be identical.

## Complexity

- Time: O(n) — each aligned node pair is enqueued and processed once.
- Space: O(n) — the queue can hold a full level of pairs, up to O(n) in the worst case.
