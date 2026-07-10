Given the roots of two binary trees `p` and `q`, decide whether they are **identical**. Two trees count as identical when they have exactly the same shape and every pair of nodes in the same position holds the same value.

Trees are supplied in level-order array form, where `null` marks a missing child and trailing nulls are dropped. Return `true` if the trees match and `false` otherwise.

## Examples

```text
Input:  p = [1, 2, 3], q = [1, 2, 3]
Output: true
```

```text
Input:  p = [1, 2], q = [1, null, 2]
Output: false        # 2 is a left child in p but a right child in q
```

```text
Input:  p = [1, 2, 1], q = [1, 1, 2]
Output: false        # same shape, but the child values differ
```

## Constraints

- The number of nodes in each tree is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

## Follow-up

Can you solve it both recursively and iteratively without recursion?
