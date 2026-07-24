You are given the `root` of a binary search tree (BST) and two distinct values `p` and `q` that are both guaranteed to exist in the tree. Return the value of their **lowest common ancestor (LCA)**.

The lowest common ancestor of two nodes is the deepest node in the tree that has both of them as descendants. By convention a node counts as a descendant of itself, so if one target lies on the path down to the other, the higher of the two is the answer. The tree is given in level-order array form, where `null` marks a missing child.

## Examples

```text
Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
Output: 6        # 2 sits in the left subtree, 8 in the right — they split at the root
```

```text
Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
Output: 2        # 4 is a descendant of 2, and a node is its own ancestor
```

```text
Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 3, q = 5
Output: 4        # both branch off node 4
```

## Constraints

- The number of nodes is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All `Node.val` are unique.
- `p != q`, and both `p` and `q` exist in the BST.

## Follow-up

The generic-tree solution scans the whole tree. Can you use the BST ordering to reach the answer in O(h) time and O(1) extra space, where h is the tree height?
