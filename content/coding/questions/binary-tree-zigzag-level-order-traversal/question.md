Given the `root` of a binary tree, return its **zigzag level-order traversal**: a list of levels, where values are read left-to-right on the first level, then right-to-left on the next, alternating direction as you go down the tree.

Each inner list holds one level's values in the direction that level should be read. Return an empty list when the tree is empty.

## Examples

```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [20, 9], [15, 7]]
```

```text
Input:  root = [1]
Output: [[1]]
```

```text
Input:  root = []
Output: []
```

## Constraints

- 0 <= number of nodes <= 2000
- -100 <= Node.val <= 100

## Follow-up

Can you produce the reversed levels without calling a reverse function — by choosing where you insert each value as you build the level?
