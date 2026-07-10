The order the final list must follow is exactly preorder — visit a node, then its left subtree, then its right subtree. So the most direct plan is to first run an ordinary preorder traversal and stash every node in a list, then wire that list together afterward.

Once the list exists in the right order, rewiring is trivial: point each node's `right` at the next entry and clear its `left`, then close off the final node.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;
        List<TreeNode> nodes = new ArrayList<>();
        preorder(root, nodes);
        for (int i = 0; i < nodes.size() - 1; i++) {
            nodes.get(i).left = null;
            nodes.get(i).right = nodes.get(i + 1);
        }
        TreeNode last = nodes.get(nodes.size() - 1);
        last.left = null;
        last.right = null;
    }

    private void preorder(TreeNode node, List<TreeNode> nodes) {
        if (node == null) return;
        nodes.add(node);
        preorder(node.left, nodes);
        preorder(node.right, nodes);
    }
}
```

## Why it works

The traversal visits nodes in the same root-left-right order the flattened list must have, so `nodes` already holds the target sequence before any pointer is touched. The rewiring pass then just links consecutive entries and nulls out every `left` pointer, which is exactly the shape a "linked list through right pointers" requires.

## Complexity

- Time: O(n) — one traversal to collect nodes, one pass to relink them.
- Space: O(n) — the list holds every node, on top of an O(h) recursion stack.
