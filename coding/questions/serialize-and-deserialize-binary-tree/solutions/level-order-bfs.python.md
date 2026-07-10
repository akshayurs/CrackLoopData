Instead of recursing, sweep the tree breadth-first with a queue. Every time a real node comes off the queue, record its value and push both children onto the queue — pushing `None` for a missing child rather than skipping it, so the string also encodes exactly where the gaps are.

Deserializing mirrors the same sweep: pop tokens off the front of the split string in the order they were written, attach each one as the left or right child of the next node waiting in a queue, and only enqueue the children that weren't `#`. Because both sides visit nodes level by level, left-to-right, the queues stay in lockstep the whole way through.

```python
from collections import deque

class Codec:
    def serialize(self, root):
        if root is None:
            return '#'
        vals = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                vals.append('#')
                continue
            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ','.join(vals)

    def deserialize(self, data):
        if data == '#':
            return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != '#':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != '#':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root
```

## Why it works

Both serialize and deserialize process nodes in identical breadth-first order, so the i-th "slot" written always corresponds to the i-th child position read back. Skipping the enqueue for `#` slots keeps the two queues synchronized without ever confusing a real node with a placeholder.

## Complexity

- Time: O(n) — every node and null placeholder is visited exactly once on each side.
- Space: O(n) — the queue holds up to one level's worth of nodes, and the token list holds one entry per slot.
