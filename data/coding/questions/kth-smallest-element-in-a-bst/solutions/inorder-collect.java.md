The defining property of a BST is that an **in-order** traversal — left subtree, node, right subtree — visits the values in sorted ascending order. So the straightforward approach is to run a full in-order walk, add every value to a list, and then read position `k - 1`.

This ignores the fact that we could stop early, but it is the clearest way to see why the answer is correct: once the values are laid out in sorted order, the k-th smallest is just the element at the (k-1)-th slot.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> values = new ArrayList<>();
        inorder(root, values);
        return values.get(k - 1);
    }

    private void inorder(TreeNode node, List<Integer> values) {
        if (node == null) return;
        inorder(node.left, values);
        values.add(node.val);
        inorder(node.right, values);
    }
}
```

## Why it works

In-order traversal of a BST emits nodes in increasing value order, so `values` ends up fully sorted. Element `values.get(k - 1)` is therefore the k-th smallest by definition. The recursion visits each node exactly once.

## Complexity

- Time: O(n) — every node is visited once regardless of `k`.
- Space: O(n) — the list stores all `n` values, plus O(h) recursion stack.
