Recursion is elegant, but on a graph with a long dependency chain it costs one stack frame per hop and can blow the stack. Trading recursion for an explicit queue avoids that: clone the starting node, then flood outward level by level, cloning each newly discovered neighbor exactly once and wiring it up as it's found.

A node's clone is created the moment it's first seen — either as the start node or as someone else's neighbor — so by the time it's dequeued, only its own neighbor list still needs to be linked.

```python
from collections import deque

def clone_graph(node):
    if node is None:
        return None

    clones = {node.val: Node(node.val)}
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        for neighbor in cur.neighbors:
            if neighbor.val not in clones:
                clones[neighbor.val] = Node(neighbor.val)
                queue.append(neighbor)
            clones[cur.val].neighbors.append(clones[neighbor.val])
    return clones[node.val]
```

## Why it works

`clones` guarantees a single clone per original value, created the first time that value is encountered — either up front for the start node, or while scanning a neighbor list. Only unseen neighbors are enqueued for later expansion, so each node is dequeued and processed exactly once. Every time an edge `cur -> neighbor` is scanned, the corresponding clone edge is added, so the finished graph mirrors every connection in the original.

## Complexity

- Time: O(V + E) — each node is dequeued once and each edge is scanned once.
- Space: O(V) — the `clones` map and the queue each hold at most one entry per node.
