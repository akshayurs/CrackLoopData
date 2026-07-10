The most literal reading of "what you'd see from the side" is to process the tree level by level and remember only the last node visited at each depth — that is exactly the rightmost node, since a standard left-to-right traversal reaches it last.

A queue-based breadth-first walk naturally groups nodes by level: process the queue's current contents as one batch, and whichever node comes off last in that batch is the one visible from the right.

```python
from collections import deque

def right_side_view(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
```

## Why it works

`level_size` freezes how many nodes belong to the current level before any children get appended, so the loop drains exactly that level. Nodes are dequeued left to right (children were enqueued left-then-right), so the last one popped in the batch is the rightmost node at that depth — the only one recorded.

## Complexity

- Time: O(n) — every node is enqueued and dequeued exactly once.
- Space: O(n) — the queue can hold an entire level, which is O(n) for a wide tree.
