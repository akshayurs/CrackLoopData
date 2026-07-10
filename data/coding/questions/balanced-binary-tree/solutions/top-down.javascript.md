The definition maps directly to a check: at every node, measure the height of the left subtree and the height of the right subtree, and confirm they differ by no more than one. If that holds at the current node *and* recursively at both children, the tree is balanced.

Computing a subtree's height is itself a small recursion — one plus the taller child. This approach keeps height and balance as two separate walks, which is the most literal translation of the problem.

```javascript
function isBalanced(root) {
  function height(node) {
    if (node === null) return 0;
    return 1 + Math.max(height(node.left), height(node.right));
  }
  if (root === null) return true;
  if (Math.abs(height(root.left) - height(root.right)) > 1) return false;
  return isBalanced(root.left) && isBalanced(root.right);
}
```

## Why it works

`height` returns the longest root-to-leaf distance in a subtree, so `Math.abs(height(left) - height(right))` is exactly the imbalance at the current node. Checking it here guarantees the local rule; recursing into both children extends the guarantee to every node. If any node fails, the `&&` short-circuits and `false` propagates up.

## Complexity

- Time: O(n^2) — for each of the n nodes we recompute a height, which itself scans the subtree; a skewed tree is the worst case.
- Space: O(n) — recursion stack depth equals the tree's height, up to n when skewed.
