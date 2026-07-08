Given the `root` of a binary tree, determine whether it is a valid **binary search tree (BST)**.

A binary tree is a valid BST when every node satisfies all three rules:

- Every value in a node's **left** subtree is strictly **less** than the node's value.
- Every value in a node's **right** subtree is strictly **greater** than the node's value.
- Both subtrees are themselves valid BSTs.

The constraint is on the whole subtree, not just the immediate children — a node deep on the left must still be smaller than every ancestor it sits under on the right.

## Examples

```text
Input:  root = [2, 1, 3]
Output: true         # 1 < 2 < 3
```

```text
Input:  root = [5, 1, 4, null, null, 3, 6]
Output: false        # 3 sits in 5's right subtree but 3 < 5
```

```text
Input:  root = [2, 2, 2]
Output: false         # duplicates break the strict ordering
```

## Constraints

- The number of nodes is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

## Follow-up

The immediate-children check (`left < node < right`) is not enough — can you enforce the ordering across the entire subtree in a single pass?
