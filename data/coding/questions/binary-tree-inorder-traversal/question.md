Given the `root` of a binary tree, return the values of its nodes visited in **inorder**: left subtree, then the node itself, then right subtree. The result is a flat list of values in that left-to-right order.

Trees are given in level-order array form, where `null` marks a missing child and trailing nulls are dropped.

## Examples

```text
Input:  root = [1, null, 2, 3]
Output: [1, 3, 2]
```

```text
Input:  root = [4, 2, 6, 1, 3, 5, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
```

```text
Input:  root = []
Output: []
```

## Constraints

- The number of nodes is in the range [0, 100].
- -100 <= Node.val <= 100

## Follow-up

The recursive solution is a one-liner, but can you produce the same order using an explicit stack instead of the call stack?
