Given the `root` of a binary tree, return the length of its **diameter** — the number of edges on the longest path between any two nodes in the tree.

This path does not have to pass through the root, and the two endpoints can be any nodes. The length is counted in **edges**, so a path visiting `k` nodes has length `k - 1`.

## Examples

```text
Input:  root = [1, 2, 3, 4, 5]
Output: 3        # longest path 4 -> 2 -> 1 -> 3 (3 edges)
```

```text
Input:  root = [1, 2]
Output: 1        # longest path 2 -> 1 (1 edge)
```

```text
Input:  root = []
Output: 0        # empty tree has no edges
```

## Constraints

- The number of nodes is in the range [0, 10^4].
- -100 <= Node.val <= 100

## Follow-up

The obvious solution recomputes subtree heights for every node. Can you find the diameter in a single traversal that visits each node once?
