Given the `root` of a binary tree, return its **level-order traversal**: a list of levels, where each level is the list of node values read from left to right, and the levels themselves run from the root downward.

The result is a list of lists — the first inner list holds the root's value, the next holds its children left to right, and so on. Return an empty list when the tree is empty.

## Examples

```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]
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
- -1000 <= Node.val <= 1000

## Follow-up

Can you produce the same result both with an explicit queue (breadth-first) and with a single recursive pass that carries the current depth?
