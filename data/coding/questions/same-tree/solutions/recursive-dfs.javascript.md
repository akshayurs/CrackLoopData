Sameness is defined recursively, so the solution is too: two trees are identical when their roots carry the same value *and* their left subtrees match *and* their right subtrees match. That single rule, applied top-down, covers the whole tree.

The base cases close it off. Two empty trees are trivially identical, while one empty and one non-empty tree can never be — so a mismatch in "is this node present?" is an immediate `false`.

```javascript
function isSameTree(p, q) {
  if (p === null && q === null) return true;
  if (p === null || q === null || p.val !== q.val) return false;
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```

## Why it works

Every node position is compared exactly once. If both sides are absent the branch agrees; if only one is absent, or the values differ, we short-circuit to `false`. Otherwise the values match and the answer defers to the two subtrees, which are checked the same way. Because a difference anywhere propagates up through the `&&`, the trees are declared identical only when every corresponding position agrees.

## Complexity

- Time: O(n) — each pair of aligned nodes is visited once, where n is the size of the smaller tree.
- Space: O(h) — the recursion stack is as deep as the tree height, up to O(n) for a skewed tree.
