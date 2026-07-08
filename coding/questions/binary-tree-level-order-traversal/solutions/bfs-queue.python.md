Level order is exactly what breadth-first search produces, so lean on a queue. The trick is grouping the output by level: before draining the queue, note how many nodes it currently holds — that count is precisely the size of the current level. Pop exactly that many, record their values, and enqueue their children to form the next level.

Because every child is pushed to the back while the current level is popped from the front, nodes always come out top-to-bottom and left-to-right.

```python
from collections import deque

def level_order(root):
    if root is None:
        return []
    levels = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels
```

## Why it works

Snapshotting `len(queue)` before the inner loop fixes how many nodes belong to the current level. The inner loop consumes exactly those nodes and appends their children behind the still-unprocessed nodes, so the queue's FIFO order guarantees each level is emitted fully before the next begins. Left children are enqueued before right children, preserving left-to-right order within every level.

## Complexity

- Time: O(n) — each node is enqueued and dequeued exactly once.
- Space: O(n) — the queue plus the output hold up to n values; a single level can be as wide as n/2.
