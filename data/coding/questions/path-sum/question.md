You are given the root of a binary tree and an integer `targetSum`. Determine whether the tree has a **root-to-leaf** path such that the values along the path add up exactly to `targetSum`.

A leaf is a node with no children. The path must start at the root and end at a leaf — it cannot stop partway down the tree. Trees are supplied in level-order array form, where `null` marks a missing child and trailing nulls are dropped.

## Examples

```text
Input:  root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
Output: true        # 5 -> 4 -> 11 -> 2 sums to 22
```

```text
Input:  root = [1, 2, 3], targetSum = 5
Output: false        # root-to-leaf sums are 3 and 4, neither is 5
```

```text
Input:  root = [], targetSum = 0
Output: false        # an empty tree has no root-to-leaf path
```

## Constraints

- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

## Follow-up

Can you solve it without recursion, using an explicit stack?
