Any recursion can be unrolled into an explicit queue of the pairs it would have compared. Seed the queue with the root's left and right children, then repeatedly pop a pair and apply the same rule as before: both empty is fine, one empty or unequal values is a mismatch, otherwise enqueue the pair's children in mirrored order.

This avoids growing the call stack, which matters for very tall or unbalanced trees.

```python
from collections import deque

def is_symmetric(root):
    if not root:
        return True
    queue = deque([(root.left, root.right)])
    while queue:
        a, b = queue.popleft()
        if a is None and b is None:
            continue
        if a is None or b is None or a.val != b.val:
            return False
        queue.append((a.left, b.right))
        queue.append((a.right, b.left))
    return True
```

## Why it works

Each queued pair represents two positions that must be reflections of one another. Aligned empties are skipped; a lone empty or a value mismatch fails immediately. A matching pair enqueues its children crossed — left with right, right with left — which is exactly the mirroring rule applied one level deeper. The queue drains only if no mismatch was ever found, which is precisely the condition for symmetry.

## Complexity

- Time: O(n) — each node is enqueued and processed once as part of exactly one pair.
- Space: O(n) — the queue can hold up to a full level of pairs in the worst case.
