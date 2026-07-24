Instead of building paths and comparing them afterward, let each recursive call answer a narrower question directly: "does the subtree rooted here contain `p`, `q`, or both — and if both, is this the split point?" A node reports itself back up as soon as it *is* one of the targets, or once both targets have surfaced from its two children.

The recursion bottoms out on `null` or on hitting `p`/`q` directly. Higher up, if both the left and right subtree calls return something non-null, the targets live in different subtrees and the current node is where they meet — the LCA. If only one side is non-null, the answer (whatever it is) simply bubbles up unchanged.

```javascript
function lowestCommonAncestor(root, p, q) {
  if (root === null || root === p || root === q) return root;

  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);

  if (left && right) return root;
  return left ? left : right;
}
```

## Why it works

A call returns non-null exactly when its subtree contains `p`, `q`, or their LCA. If both children return non-null, `p` and `q` are split across the two subtrees, so the current node — the point where they meet — is the LCA, and it's reported upward from there on. If only one side returns non-null, both targets (or their already-found LCA) live entirely in that subtree, so that result is simply passed along untouched. Because the base case fires the instant a target is reached, a node that is itself `p` or `q` is correctly treated as its own ancestor.

## Complexity

- Time: O(n) — a single traversal visits every node at most once.
- Space: O(h) — the recursion stack is as deep as the tree's height, O(log n) balanced or O(n) skewed.
