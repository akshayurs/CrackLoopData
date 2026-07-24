Read the definition literally: a node is valid when *every* value in its left subtree is smaller and *every* value in its right subtree is larger. So gather all the values on each side and check them against the node, then recurse into the children to verify they are valid BSTs too.

This is the most direct translation of the rules, but collecting an entire subtree's values at each node repeats a lot of work — the same nodes get scanned once for every ancestor above them.

```javascript
function isValidBST(root) {
  const collect = (node) =>
    node === null ? [] : [...collect(node.left), node.val, ...collect(node.right)];
  if (root === null) return true;
  if (collect(root.left).some((v) => v >= root.val)) return false;
  if (collect(root.right).some((v) => v <= root.val)) return false;
  return isValidBST(root.left) && isValidBST(root.right);
}
```

## Why it works

At each node we explicitly confirm the two subtree rules by inspecting every descendant value, then recurse so the same guarantee holds at every node. If any single node violates the ordering, one of the `some(...)` checks returns true and the whole result collapses to `false`.

## Complexity

- Time: O(n^2) — at each of n nodes we may scan its entire subtree; worst case (a skewed tree) is quadratic.
- Space: O(n) — the recursion depth plus the temporary arrays of subtree values.
