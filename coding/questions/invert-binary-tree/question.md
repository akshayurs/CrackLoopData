Given the `root` of a binary tree, invert it so that the whole tree is mirrored left-to-right, then return the new root.

Inverting means swapping the left and right child of **every** node in the tree. Trees are given and returned in level-order array form, where `null` marks a missing child and trailing nulls are dropped.

## Examples

```text
Input:  root = [4, 2, 7, 1, 3, 6, 9]
Output: [4, 7, 2, 9, 6, 3, 1]
```

```text
Input:  root = [2, 1, 3]
Output: [2, 3, 1]
```

```text
Input:  root = []
Output: []
```

## Constraints

- The number of nodes is in the range [0, 100].
- -100 <= Node.val <= 100

## Follow-up

Can you do it both recursively and iteratively?
