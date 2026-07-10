Reversing a level after the fact is an extra pass you don't actually need — you already know the direction *before* you start placing values into that level, so you can just put each value where it ultimately belongs. Building the level itself as a deque lets you append to either end in O(1).

Keep the same breadth-first structure, but instead of always pushing to the back, push to the back on a left-to-right level and to the front on a right-to-left one. The queue that drives the traversal is unaffected — children are still discovered strictly left to right — only the container you're writing values into changes its insertion side.

```python
from collections import deque

def zigzag_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result
```

## Why it works

The traversal queue always discovers a level's nodes left to right, regardless of the output direction — only where each value lands in `level` changes. On a left-to-right level, appending to the back reproduces that same order; on a right-to-left level, appending to the front means the first node discovered ends up last, which is exactly the mirrored order. No separate reversal step is needed because the direction is baked into the insertion itself.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once, and each value is inserted into its level exactly once.
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
