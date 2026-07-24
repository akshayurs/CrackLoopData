Inorder is defined recursively — left, node, right — so the cleanest solution just restates the definition: recurse into the left subtree, record the current value, then recurse into the right subtree.

An accumulator array threaded through the calls collects values in the correct order, since each recursive call appends everything from its subtree before returning.

```javascript
function inorderTraversal(root) {
  const result = [];

  function visit(node) {
    if (node === null) return;
    visit(node.left);
    result.push(node.val);
    visit(node.right);
  }

  visit(root);
  return result;
}
```

## Why it works

`visit` fully drains the left subtree into `result` before touching the current node, then fully drains the right subtree after. Applying that rule at every level means each node's value lands strictly between everything in its left subtree and everything in its right subtree — exactly the inorder order, by induction on subtree size.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(n) — O(h) for the recursion stack plus O(n) for the output array; h can be O(n) for a skewed tree.
