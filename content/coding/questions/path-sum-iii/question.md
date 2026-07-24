You are given the `root` of a binary tree and an integer `targetSum`. Count the number of downward paths whose node values add up to `targetSum`.

A path does not need to start at the root or end at a leaf, but it must travel strictly downward — from a node to one of its descendants, always moving parent to child.

## Examples

```text
Input:  root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], targetSum = 8
Output: 3        # 5 -> 3, 5 -> 2 -> 1, -3 -> 11
```

```text
Input:  root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
Output: 3        # 5 -> 4 -> 11 -> 2, 5 -> 8 -> 4 -> 5, 4 -> 11 -> 7
```

```text
Input:  root = [1], targetSum = 1
Output: 1        # the single-node path 1
```

## Constraints

- The number of nodes is in the range [0, 1000].
- -1000 <= Node.val <= 1000
- -10^9 <= targetSum <= 10^9

## Follow-up

The brute force checks every node as a possible path start, redoing work along shared root-to-node prefixes. Can you count all paths in a single traversal?
