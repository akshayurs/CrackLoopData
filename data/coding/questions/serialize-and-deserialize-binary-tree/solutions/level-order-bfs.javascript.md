Instead of recursing, sweep the tree breadth-first with a queue. Every time a real node comes off the queue, record its value and push both children onto the queue — pushing `null` for a missing child rather than skipping it, so the string also encodes exactly where the gaps are.

Deserializing mirrors the same sweep: read tokens off the split string in the order they were written, attach each one as the left or right child of the next node waiting in a queue, and only enqueue the children that weren't `'#'`. Because both sides visit nodes level by level, left-to-right, the queues stay in lockstep the whole way through.

```javascript
class Codec {
  serialize(root) {
    if (root === null) return '#';
    const vals = [];
    const queue = [root];
    while (queue.length) {
      const node = queue.shift();
      if (node === null) {
        vals.push('#');
        continue;
      }
      vals.push(String(node.val));
      queue.push(node.left);
      queue.push(node.right);
    }
    return vals.join(',');
  }

  deserialize(data) {
    if (data === '#') return null;
    const vals = data.split(',');
    const root = new TreeNode(Number(vals[0]));
    const queue = [root];
    let i = 1;
    while (queue.length) {
      const node = queue.shift();
      if (vals[i] !== '#') {
        node.left = new TreeNode(Number(vals[i]));
        queue.push(node.left);
      }
      i++;
      if (vals[i] !== '#') {
        node.right = new TreeNode(Number(vals[i]));
        queue.push(node.right);
      }
      i++;
    }
    return root;
  }
}
```

## Why it works

Both serialize and deserialize process nodes in identical breadth-first order, so the i-th "slot" written always corresponds to the i-th child position read back. Skipping the enqueue for `'#'` slots keeps the two queues synchronized without ever confusing a real node with a placeholder.

## Complexity

- Time: O(n) — every node and null placeholder is visited exactly once on each side.
- Space: O(n) — the queue holds up to one level's worth of nodes, and the token array holds one entry per slot.
