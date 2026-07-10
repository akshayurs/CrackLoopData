A **path** in a binary tree is any sequence of nodes where each pair of adjacent nodes is connected by an edge, and no node appears more than once. A path does not need to pass through the root, and it does not need to go strictly downward — it can bend at most once, at a single "peak" node, using both children.

The **path sum** is the total of the node values along the path. Given the root of a binary tree, return the maximum path sum over all non-empty paths.

## Examples

```text
Input:  root = [1, 2, 3]
Output: 6        # path 2 -> 1 -> 3
```

```text
Input:  root = [-10, 9, 20, null, null, 15, 7]
Output: 42       # path 15 -> 20 -> 7, bending at 20
```

```text
Input:  root = [-3]
Output: -3       # a single node is a valid path
```

## Constraints

- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000

## Follow-up

Can you compute the answer in a single pass over the tree, without recomputing subtree sums?
