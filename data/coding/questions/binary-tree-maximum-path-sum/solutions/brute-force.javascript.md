A path either passes straight down through a node using at most one child, or it bends at a single "peak" node and uses both children. So try every node as that peak: its contribution is its own value plus the best downward run into its left subtree (if positive) plus the best downward run into its right subtree (if positive).

Computing "best downward run from a node" is itself a small recursion, and doing it fresh for every candidate peak is what makes this approach slow — the same subtrees get walked over and over.

```javascript
function maxPathSum(root) {
  const nodes = [];

  function collect(node) {
    if (!node) return;
    nodes.push(node);
    collect(node.left);
    collect(node.right);
  }

  function bestDownward(node) {
    if (!node) return 0;
    return node.val + Math.max(0, bestDownward(node.left), bestDownward(node.right));
  }

  collect(root);
  let best = -Infinity;
  for (const node of nodes) {
    const left = Math.max(0, bestDownward(node.left));
    const right = Math.max(0, bestDownward(node.right));
    best = Math.max(best, node.val + left + right);
  }
  return best;
}
```

## Why it works

Every path in the tree has a unique highest node — its peak. Trying each node as that peak and adding the best non-negative downward contribution from each child covers every possible path exactly once, so the true maximum is guaranteed to appear as one of the candidates.

## Complexity

- Time: O(n^2) — n candidate peaks, each paying up to O(n) to recompute its downward sums.
- Space: O(n) — the node list plus recursion stacks, up to O(n) for a skewed tree.
