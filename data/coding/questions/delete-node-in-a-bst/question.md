You are given the `root` of a binary search tree and an integer `key`. Delete the node whose value equals `key` from the tree and return the root of the resulting BST — the BST property must still hold, and node uniqueness means there is at most one matching node.

Deletion has three cases. A node with no children is simply removed. A node with exactly one child is replaced by that child. A node with two children is trickier: replace its value with its **in-order successor** — the smallest value in its right subtree — and then delete that successor's original node from the right subtree (the successor itself can have at most one child, a right child, so removing it never recurses into the two-child case again). If `key` isn't present, return the tree unchanged. Trees are given and returned in level-order array form, where `null` marks a missing child and trailing nulls are dropped.

## Examples

```text
Input:  root = [5, 3, 6, 2, 4, null, 7], key = 3
Output: [5, 4, 6, 2, null, null, 7]
# node 3 has two children (2 and 4); its in-order successor is 4,
# so 3's value becomes 4 and the old leaf 4 is spliced out
```

```text
Input:  root = [5, 3, 6, 2, 4, null, 7], key = 2
Output: [5, 3, 6, null, 4, null, 7]
# node 2 is a leaf, so it is simply detached from its parent
```

```text
Input:  root = [5, 3, 6, 2, 4, null, 7], key = 0
Output: [5, 3, 6, 2, 4, null, 7]
# no node holds value 0, so the tree is returned untouched
```

## Constraints

- The number of nodes is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- All node values are unique.
- -10^5 <= key <= 10^5

## Follow-up

The optimal approach runs in O(h) time, where h is the tree's height. Why does replacing the deleted node's value with its in-order successor (rather than, say, its in-order predecessor) not matter for correctness — and when might you prefer one over the other?
