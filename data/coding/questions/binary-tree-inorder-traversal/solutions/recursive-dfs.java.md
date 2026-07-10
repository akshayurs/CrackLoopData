Inorder is defined recursively — left, node, right — so the cleanest solution just restates the definition: recurse into the left subtree, record the current value, then recurse into the right subtree.

An accumulator list threaded through the calls collects values in the correct order, since each recursive call appends everything from its subtree before returning.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        visit(root, result);
        return result;
    }

    private void visit(TreeNode node, List<Integer> result) {
        if (node == null) return;
        visit(node.left, result);
        result.add(node.val);
        visit(node.right, result);
    }
}
```

## Why it works

`visit` fully drains the left subtree into `result` before touching the current node, then fully drains the right subtree after. Applying that rule at every level means each node's value lands strictly between everything in its left subtree and everything in its right subtree — exactly the inorder order, by induction on subtree size.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(n) — O(h) for the recursion stack plus O(n) for the output list; h can be O(n) for a skewed tree.
