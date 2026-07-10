Given the `root` of a binary tree, return its **maximum depth** — the number of nodes along the longest path from the root down to the farthest leaf.

An empty tree has depth `0`; a tree with only a root has depth `1`.

## Examples

```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: 3        # 3 -> 20 -> 15 (or 3 -> 20 -> 7)
```

```text
Input:  root = [1, null, 2]
Output: 2        # 1 -> 2
```

```text
Input:  root = []
Output: 0        # empty tree
```

## Constraints

- The number of nodes is in the range [0, 10^4].
- -100 <= Node.val <= 100

## Follow-up

Can you compute the depth without recursion, avoiding a call stack that grows with the tree's height?
