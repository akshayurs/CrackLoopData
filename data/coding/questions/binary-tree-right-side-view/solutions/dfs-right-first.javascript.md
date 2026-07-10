A queue is not required if the traversal visits nodes in the right order: walk the right child before the left child, and the first time a given depth is reached, that node must be the rightmost one at that depth — anything visited later at the same depth is further left and should be ignored.

This turns the problem into a single depth-first pass carrying the current depth, with the result array itself doubling as the "have I seen this depth yet?" check.

```javascript
function rightSideView(root) {
  const result = [];

  function dfs(node, depth) {
    if (node === null) return;
    if (depth === result.length) {
      result.push(node.val);
    }
    dfs(node.right, depth + 1);
    dfs(node.left, depth + 1);
  }

  dfs(root, 0);
  return result;
}
```

## Why it works

Recursing into the right subtree before the left guarantees that, for any given depth, the first node the traversal reaches is the rightmost one. `depth === result.length` is true exactly once per depth — at that first visit — so later, more-left nodes at the same depth see `depth < result.length` and add nothing.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) — the recursion stack depth is the tree's height, plus O(n) for the output array.
