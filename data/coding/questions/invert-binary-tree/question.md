Given the `root` of a binary tree, flip it into its mirror image: at every node, its left and right children swap places, and this swap happens all the way down to the leaves. Return the root of the transformed tree.

Nodes keep their values — only the left/right wiring changes, so the tree ends up as a horizontal reflection of the original. Trees are given and returned in level-order array form, where `null` marks a missing child and trailing nulls are dropped.

## Examples

```text
Input:  root = [4, 2, 7, 1, 3, 6, 9]
Output: [4, 7, 2, 9, 6, 3, 1]
```

```text
Input:  root = [2, 1, 3]
Output: [2, 3, 1]
```

```text
Input:  root = []
Output: []
```

## Constraints

- The number of nodes is in the range [0, 100].
- -100 <= Node.val <= 100

## Follow-up

Can you invert the tree without recursion, using only O(w) extra space where w is the widest level of the tree?
