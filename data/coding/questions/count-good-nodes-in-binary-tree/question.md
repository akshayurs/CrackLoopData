You are given the `root` of a binary tree. Call a node **good** if, walking down from the root to that node, none of its ancestors holds a value strictly greater than the node's own value (the root itself is always good, since it has no ancestors). Return the total number of good nodes in the tree.

In other words, a node is good exactly when its value is greater than or equal to the largest value seen so far on the path from the root down to it.

## Examples

```text
Input:  root = [3, 1, 4, 3, 1, 5]
Output: 4        # good nodes: 3 (root), 4, the left 3, and 5
```

```text
Input:  root = [3, 3, None, 4, 2]
Output: 3        # good nodes: 3 (root), 3, and 4; the 2 sees a larger 4 above it
```

```text
Input:  root = [1]
Output: 1        # a single node has no ancestors, so it is good
```

## Constraints

- The number of nodes is in the range [1, 10^5].
- -10^4 <= Node.val <= 10^4.

## Follow-up

Can you count the good nodes with a single traversal, without recomputing the maximum-so-far from scratch at every node?
