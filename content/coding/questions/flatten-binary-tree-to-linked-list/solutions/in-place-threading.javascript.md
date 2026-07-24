The extra array in the first approach only exists to remember "what comes after this node's left subtree finishes." That information is already sitting in the tree: it's the node's own `right` child, before we overwrite it. So instead of collecting nodes, graft the original right subtree onto the end of the left subtree, then slide the left subtree over to become the right subtree — no left ever appears again.

Walking down the current node's `right` chain, do this at every node that still has a left child: find the rightmost (last-in-preorder) node of that left subtree, hang the current node's original right subtree off of it, then move the left subtree into the right slot and clear left. Advancing to `node.right` after each step naturally continues into the just-grafted subtree, so a single pass threads the whole tree.

```javascript
function flatten(root) {
  let node = root;
  while (node !== null) {
    if (node.left !== null) {
      let rightmost = node.left;
      while (rightmost.right !== null) {
        rightmost = rightmost.right;
      }
      rightmost.right = node.right;
      node.right = node.left;
      node.left = null;
    }
    node = node.right;
  }
}
```

## Why it works

For any node, its subtree's preorder sequence is [node, preorder(left), preorder(right)]. Grafting the original right subtree onto the rightmost node of the left subtree places it immediately after the left subtree's last node — exactly where preorder puts it. Moving the left subtree into `right` and clearing `left` then makes the node's own local structure already match the target linked list, and advancing `node = node.right` walks straight into that grafted chain, repeating the fix-up further down without ever needing to backtrack.

## Complexity

- Time: O(n) — each edge is followed by the "find rightmost" search at most once in total across the whole run, since a node is never revisited through an already-threaded right pointer.
- Space: O(1) — only pointer variables are used; no recursion stack, no auxiliary array.
