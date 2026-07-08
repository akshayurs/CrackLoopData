Given the `root` of a binary tree, decide whether it is **height-balanced**. A tree is height-balanced when, for *every* node, the heights of its left and right subtrees differ by at most one.

Return `true` if the whole tree satisfies this rule, and `false` otherwise. An empty tree is considered balanced.

## Examples

```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: true         # every node's subtrees differ in height by at most 1
```

```text
Input:  root = [1, 2, 2, 3, 3, null, null, 4, 4]
Output: false        # the left subtree is 2 levels deeper than the right at the root
```

```text
Input:  root = []
Output: true         # an empty tree is balanced by definition
```

## Constraints

- The number of nodes is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4

## Follow-up

Can you decide balance in a single pass over the tree, rather than recomputing subtree heights at every node?
