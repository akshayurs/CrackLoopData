Start with a plain breadth-first traversal: a queue holds one level's worth of nodes at a time, and you drain exactly that many before moving to the children. That alone produces the levels left-to-right, top to bottom.

Zigzag only changes the *order values are read in*, not which nodes belong to which level — so build each level normally, then flip it in place whenever the current level is meant to run right-to-left. A boolean flag toggled after every level tells you when to reverse.

```python
from collections import deque

def zigzag_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result
```

## Why it works

`len(queue)` is snapshotted before the inner loop, so exactly the nodes belonging to the current level are popped — their children get queued for the next round without being processed early. The level is collected in the natural left-to-right order every time; `left_to_right` only decides whether that list gets reversed before being appended to the answer, which is enough to alternate direction level by level.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once; reversing a level costs at most O(n) total across all levels.
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
