Start with a plain breadth-first traversal: a queue holds one level's worth of nodes at a time, and you drain exactly that many before moving to the children. That alone produces the levels left-to-right, top to bottom.

Zigzag only changes the *order values are read in*, not which nodes belong to which level — so build each level normally, then flip it in place whenever the current level is meant to run right-to-left. A boolean flag toggled after every level tells you when to reverse.

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
      level.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    if (!leftToRight) level.reverse();
    result.push(level);
    leftToRight = !leftToRight;
  }
  return result;
}
```

## Why it works

`size` is snapshotted before the inner loop, so exactly the nodes belonging to the current level are shifted off — their children get pushed for the next round without being processed early. The level is collected in the natural left-to-right order every time; `leftToRight` only decides whether that array gets reversed before being pushed to the answer, which is enough to alternate direction level by level.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once; reversing a level costs at most O(n) total across all levels.
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
