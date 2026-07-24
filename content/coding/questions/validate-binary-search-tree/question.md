You're handed the `root` of a binary tree and asked to decide whether it forms a legal **binary search tree (BST)**.

A tree earns that label only when, at every single node:

- All values in that node's **left** subtree are strictly **smaller** than the node's own value.
- All values in that node's **right** subtree are strictly **larger** than the node's own value.
- Both children are themselves the roots of valid BSTs.

Notice the rule reaches past direct children — a node buried deep in a left subtree still has to stay below every value it's nested under, not just its immediate parent.

## Examples

```text
Input:  root = [4, 2, 6]
Output: true         # 2 < 4 < 6
```

```text
Input:  root = [5, 1, 4, null, null, 3, 6]
Output: false        # 3 sits inside 5's right subtree yet 3 < 5, violating the BST rule
```

```text
Input:  root = [3, 3, 3]
Output: false        # equal values are not strictly less/greater, so duplicates break a BST
```

## Constraints

- The number of nodes is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

## Follow-up

Comparing a node only against its two children isn't sufficient — every ancestor's constraint has to carry forward. Can you do that in a single top-down pass instead of re-scanning subtrees?
