The most literal reading of "what you'd see from the side" is to process the tree level by level and remember only the last node visited at each depth — that is exactly the rightmost node, since a standard left-to-right traversal reaches it last.

A queue-based breadth-first walk naturally groups nodes by level: process the queue's current contents as one batch, and whichever node comes off last in that batch is the one visible from the right.

```javascript
function rightSideView(root) {
  if (root === null) return [];
  const result = [];
  const queue = [root];
  while (queue.length) {
    const levelSize = queue.length;
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      if (i === levelSize - 1) {
        result.push(node.val);
      }
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }
  return result;
}
```

## Why it works

`levelSize` freezes how many nodes belong to the current level before any children get pushed, so the loop drains exactly that level. Nodes are shifted off left to right (children were pushed left-then-right), so the last one shifted in the batch is the rightmost node at that depth — the only one recorded.

## Complexity

- Time: O(n) — every node is pushed and shifted exactly once.
- Space: O(n) — the queue can hold an entire level, which is O(n) for a wide tree.
