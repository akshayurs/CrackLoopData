The order the final list must follow is exactly preorder — visit a node, then its left subtree, then its right subtree. So the most direct plan is to first run an ordinary preorder traversal and stash every node in a plain array, then wire that array together afterward.

Once the array exists in the right order, rewiring is trivial: point each node's `right` at the next entry and clear its `left`, then close off the final node.

```javascript
function flatten(root) {
  if (root === null) return;
  const nodes = [];

  const preorder = (node) => {
    if (node === null) return;
    nodes.push(node);
    preorder(node.left);
    preorder(node.right);
  };

  preorder(root);
  for (let i = 0; i < nodes.length - 1; i++) {
    nodes[i].left = null;
    nodes[i].right = nodes[i + 1];
  }
  const last = nodes[nodes.length - 1];
  last.left = null;
  last.right = null;
}
```

## Why it works

The traversal visits nodes in the same root-left-right order the flattened list must have, so `nodes` already holds the target sequence before any pointer is touched. The rewiring pass then just links consecutive entries and nulls out every `left` pointer, which is exactly the shape a "linked list through right pointers" requires.

## Complexity

- Time: O(n) — one traversal to collect nodes, one pass to relink them.
- Space: O(n) — the `nodes` array holds every node, on top of an O(h) recursion stack.
