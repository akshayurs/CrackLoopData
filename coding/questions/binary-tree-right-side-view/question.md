Given the `root` of a binary tree, imagine standing to its right and looking at it from the side. Return the values of the nodes you can see, ordered from the top of the tree to the bottom.

At each depth exactly one node is visible: whichever node sits furthest to the right at that level. Return an empty list when the tree is empty.

## Examples

```text
Input:  root = [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]
```

```text
Input:  root = [1, null, 3]
Output: [1, 3]
```

```text
Input:  root = []
Output: []
```

## Constraints

- 0 <= number of nodes <= 100
- -100 <= Node.val <= 100

## Follow-up

Can you solve it both with an explicit level-by-level scan and with a single depth-first pass that never builds a queue?
