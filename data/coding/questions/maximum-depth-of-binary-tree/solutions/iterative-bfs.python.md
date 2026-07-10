Recursion is elegant but leans on the call stack, which can overflow on a deeply skewed tree. Instead, walk the tree level by level with an explicit queue: the depth is simply the number of levels you process before the queue empties.

Start with the root as level one. Repeatedly drain the current level in full, enqueueing every child to form the next level, and bump a counter each round. When no children remain, the counter holds the maximum depth.

```python
from collections import deque

def max_depth(root):
    if root is None:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth
```

## Why it works

Snapshotting `len(queue)` before the inner loop fixes how many nodes belong to the current level, so each iteration of the outer loop consumes exactly one level and adds one to `depth`. Children pushed during the loop are only processed on the next round. The outer loop runs once per level, so the final count equals the number of levels — the maximum depth.

## Complexity

- Time: O(n) — each node is enqueued and dequeued exactly once.
- Space: O(w) — the queue holds at most one level, whose width w can be up to n/2 for the bottom of a full tree.
