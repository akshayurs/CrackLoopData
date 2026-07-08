Recursion is elegant but leans on the call stack, which can overflow on a deeply skewed tree. Instead, walk the tree level by level with an explicit queue: the depth is simply the number of levels you process before the queue empties.

Start with the root as level one. Repeatedly drain the current level in full, enqueueing every child to form the next level, and bump a counter each round. When no children remain, the counter holds the maximum depth.

```javascript
function maxDepth(root) {
  if (root === null) {
    return 0;
  }
  let queue = [root];
  let depth = 0;
  while (queue.length > 0) {
    depth++;
    const next = [];
    for (const node of queue) {
      if (node.left) next.push(node.left);
      if (node.right) next.push(node.right);
    }
    queue = next;
  }
  return depth;
}
```

## Why it works

Each pass of the `while` loop handles exactly one level: it scans every node currently in `queue` and collects their children into `next`, which becomes the queue for the following level. The counter increments once per level, so when the queue finally empties, `depth` equals the number of levels — the maximum depth.

## Complexity

- Time: O(n) — each node is enqueued and visited exactly once.
- Space: O(w) — the queue holds at most one level, whose width w can be up to n/2 for the bottom of a full tree.
