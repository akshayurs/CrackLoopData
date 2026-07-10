Reversing a level after the fact is an extra pass you don't actually need — you already know the direction *before* you start placing values into that level, so you can just put each value where it ultimately belongs.

Keep the same breadth-first structure, but instead of always pushing to the back of the level array, push to the back on a left-to-right level and unshift to the front on a right-to-left one. The queue that drives the traversal is unaffected — children are still discovered strictly left to right — only the side you're writing values into changes.

```javascript
function zigzagLevelOrder(root) {
  if (!root) return [];
  const result = [];
  const queue = [root];
  let leftToRight = true;
  while (queue.length) {
    const size = queue.length;
    const level = [];
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      if (leftToRight) level.push(node.val);
      else level.unshift(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    result.push(level);
    leftToRight = !leftToRight;
  }
  return result;
}
```

## Why it works

The traversal queue always discovers a level's nodes left to right, regardless of the output direction — only where each value lands in `level` changes. On a left-to-right level, pushing to the back reproduces that same order; on a right-to-left level, unshifting to the front means the first node discovered ends up last, which is exactly the mirrored order. No separate reversal step is needed because the direction is baked into the insertion itself.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once, and each value is inserted into its level exactly once.
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
