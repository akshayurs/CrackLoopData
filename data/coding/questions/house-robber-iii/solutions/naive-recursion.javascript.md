The same direct reading in JavaScript: at every node, either rob it and add whatever the grandchildren yield, or skip it and take the best each child can offer on its own. Recurse on both branches and keep the larger.

It is correct but wasteful — the same subtree gets re-solved once as a "grandchild" call from one ancestor and again as a "child" call from another, so work stacks up down the tree.

```javascript
function rob(root) {
  if (root === null) return 0;

  let robThis = root.val;
  if (root.left) {
    robThis += rob(root.left.left) + rob(root.left.right);
  }
  if (root.right) {
    robThis += rob(root.right.left) + rob(root.right.right);
  }

  const skipThis = rob(root.left) + rob(root.right);

  return Math.max(robThis, skipThis);
}
```

## Why it works

`robThis` commits to taking the current house, so the next fair-game houses are the grandchildren — the direct children are off-limits. `skipThis` gives up the current house and simply asks each child subtree for its own best answer, with no restriction on whether the child gets robbed. These two choices cover every possibility for the current node, so their maximum is the answer for the subtree rooted here.

## Complexity

- Time: O(2^n) — each node can be reached through several recursive paths (as a grandchild of multiple ancestors), so subtrees are re-solved repeatedly.
- Space: O(n) — recursion depth in the worst case (a skewed tree).
