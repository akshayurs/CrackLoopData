The order the final list must follow is exactly preorder — visit a node, then its left subtree, then its right subtree. So the most direct plan is to first run an ordinary preorder traversal and stash every node in a plain list, then wire that list together afterward.

Once the list exists in the right order, rewiring is trivial: point each node's `right` at the next entry and clear its `left`, then close off the final node.

```python
def flatten(root):
    if root is None:
        return
    nodes = []

    def preorder(node):
        if node is None:
            return
        nodes.append(node)
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    for i in range(len(nodes) - 1):
        nodes[i].left = None
        nodes[i].right = nodes[i + 1]
    nodes[-1].left = None
    nodes[-1].right = None
```

## Why it works

The traversal visits nodes in the same root-left-right order the flattened list must have, so `nodes` already holds the target sequence before any pointer is touched. The rewiring pass then just links consecutive entries and nulls out every `left` pointer, which is exactly the shape a "linked list through right pointers" requires.

## Complexity

- Time: O(n) — one traversal to collect nodes, one pass to relink them.
- Space: O(n) — the `nodes` list holds every node, on top of an O(h) recursion stack.
