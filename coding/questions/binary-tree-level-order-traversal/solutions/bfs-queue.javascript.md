Level order is exactly what breadth-first search produces, so lean on a queue. Instead of tracking a running count, keep the current level in one array and collect its children into a fresh `next` array; once the level is scanned, `next` becomes the queue for the following level.

Because children are appended left before right and levels are swapped only after the current one is fully read, nodes come out top-to-bottom and left-to-right.

```javascript
function levelOrder(root) {
  if (root === null) return [];
  const levels = [];
  let queue = [root];
  while (queue.length > 0) {
    const level = [];
    const next = [];
    for (const node of queue) {
      level.push(node.val);
      if (node.left) next.push(node.left);
      if (node.right) next.push(node.right);
    }
    levels.push(level);
    queue = next;
  }
  return levels;
}
```

## Why it works

Each pass of the `while` loop handles exactly one level: it reads every node currently in `queue`, records their values in `level`, and gathers their children into `next`. Swapping `queue = next` advances to the level below only after the current one is complete, so levels never interleave. Enqueuing the left child before the right preserves left-to-right order within each level.

## Complexity

- Time: O(n) — each node is visited once.
- Space: O(n) — the queue plus the output hold up to n values; a single level can be as wide as n/2.
