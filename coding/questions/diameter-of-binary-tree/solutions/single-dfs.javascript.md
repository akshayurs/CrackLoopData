The brute force wastes work because `height` gets called again for every node on top of the recursion that already walks the whole tree. But a single post-order pass can compute a subtree's height *and* update the answer at the same time — there is no need for two separate traversals.

Do one DFS that returns the height of each subtree as usual, but before returning, check whether `left height + right height` beats the best diameter seen so far and record it in a variable shared across calls.

```javascript
function diameterOfBinaryTree(root) {
  let best = 0;

  function height(node) {
    if (node === null) return 0;
    const left = height(node.left);
    const right = height(node.right);
    best = Math.max(best, left + right);
    return 1 + Math.max(left, right);
  }

  height(root);
  return best;
}
```

## Why it works

Every candidate diameter is "the path that turns at some node," worth `height(left) + height(right)` edges at that node. `height` already needs to visit every node once to compute subtree heights bottom-up, so folding the `best` update into that same call means each node contributes to the answer exactly when its height is computed — no revisiting, no separate diameter recursion.

## Complexity

- Time: O(n) — each node is visited exactly once.
- Space: O(h) — recursion stack depth equals the tree height h, up to O(n) for a skewed tree.
