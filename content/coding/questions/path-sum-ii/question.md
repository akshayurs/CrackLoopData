Given the `root` of a binary tree and an integer `targetSum`, return every root-to-leaf path whose node values add up to `targetSum`. Each path is reported as the list of values from the root down to the leaf, and the paths themselves must come out in the order a left-to-right depth-first search would visit them. A leaf is a node with no children.

## Examples

```text
Input:  root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
```

```text
Input:  root = [1, 2, 3], targetSum = 5
Output: []
```

```text
Input:  root = [1, 2], targetSum = 3
Output: [[1, 2]]        # root-to-leaf path 1 -> 2 sums to 3
```

## Constraints

- 0 <= number of nodes <= 5000
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

## Follow-up

Can you do it with a single DFS pass that tracks the remaining sum as it descends, instead of building every root-to-leaf path first and filtering afterward?
