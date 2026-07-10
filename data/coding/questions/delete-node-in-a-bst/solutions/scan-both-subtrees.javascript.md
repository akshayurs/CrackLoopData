The tree is a BST, but nothing stops you from ignoring that fact while searching: recurse into *both* children looking for the value, the way you would in any binary tree. Only when a node's own value matches `key` do you actually perform the splice.

Once the target node is found, handle its children. Zero or one child is easy — return whichever child exists (or `null`). Two children means copying up the in-order successor's value (the leftmost node of the right subtree) and then recursively deleting that successor's value from the right subtree, which is itself a smaller instance of the same problem.

```javascript
function deleteNode(root, key) {
  if (root === null) return null;

  if (root.val === key) {
    if (root.left === null) return root.right;
    if (root.right === null) return root.left;
    let successor = root.right;
    while (successor.left !== null) {
      successor = successor.left;
    }
    root.val = successor.val;
    root.right = deleteNode(root.right, successor.val);
    return root;
  }

  root.left = deleteNode(root.left, key);
  root.right = deleteNode(root.right, key);
  return root;
}
```

## Why it works

Because values are unique, at most one branch can ever contain `key`, so recursing into both sides is wasteful but never incorrect — the branch that doesn't hold `key` just rebuilds itself unchanged. Once the matching node is found, the standard splice rules apply: a childless or single-child node is replaced outright, and a two-child node keeps its position by adopting its successor's value, then removing the now-duplicated successor node from the right subtree.

## Complexity

- Time: O(n) — every node can be visited, since the search never uses the BST ordering to prune a branch.
- Space: O(h) — the recursion stack depth is the tree height, up to O(n) for a skewed tree.
