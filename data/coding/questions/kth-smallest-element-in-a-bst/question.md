Given the `root` of a binary search tree and an integer `k`, return the value of the `k`-th smallest element in the tree, counting from 1 (so `k = 1` asks for the smallest value overall).

Recall that in a BST every node's value is greater than all values in its left subtree and smaller than all values in its right subtree. Trees are given in level-order array form, where `null` marks a missing child and trailing nulls are dropped.

## Examples

```text
Input:  root = [3, 1, 4, null, 2], k = 1
Output: 1
```

```text
Input:  root = [3, 1, 4, null, 2], k = 2
Output: 2
```

```text
Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
Output: 3
```

## Constraints

- The number of nodes is in the range [1, 10^4].
- 0 <= Node.val <= 10^4
- 1 <= k <= number of nodes

## Follow-up

If the BST is modified often (insertions and deletions) and you must answer many k-th smallest queries, how would you speed things up? Consider augmenting each node with the size of its subtree.
