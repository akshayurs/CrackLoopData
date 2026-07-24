Given the root of a binary tree, decide whether it is a **mirror image of itself** — that is, the left subtree is the mirror of the right subtree at every level.

Trees are supplied in level-order array form, where `null` marks a missing child and trailing nulls are dropped. Return `true` if the tree is symmetric around its center and `false` otherwise.

## Examples

```text
Input:  root = [1, 2, 2, 3, 4, 4, 3]
Output: true
```

```text
Input:  root = [1, 2, 2, null, 3, null, 3]
Output: false        # the inner grandchildren (3 and 3) sit on mismatched sides
```

```text
Input:  root = [1]
Output: true          # a single node is trivially symmetric
```

## Constraints

- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100

## Follow-up

Can you solve it both recursively and iteratively without recursion?
