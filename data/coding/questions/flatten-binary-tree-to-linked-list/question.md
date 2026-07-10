Given the `root` of a binary tree, rewire it **in place** into a linked list: flatten it so every node's `left` child is `null` and its `right` child points to the next node, following the tree's preorder sequence (root, then left subtree, then right subtree).

The transformation must reuse the existing `TreeNode` objects — no new nodes, and the final chain should read out in the same order a preorder traversal would visit the original tree.

## Examples

```text
Input:  root = [1, 2, 5, 3, 4, null, 6]
Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]
```

```text
Input:  root = []
Output: []
```

```text
Input:  root = [0]
Output: [0]
```

## Constraints

- The number of nodes is in the range [0, 2000].
- -100 <= Node.val <= 100

## Follow-up

Can you do it using only O(1) extra space, without an explicit stack or an auxiliary list of nodes?
