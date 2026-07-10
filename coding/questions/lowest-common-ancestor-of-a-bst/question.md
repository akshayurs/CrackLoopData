You're given the root of a binary search tree (BST) and two integer values `p` and `q` that are guaranteed to already exist somewhere in the tree. Find their **lowest common ancestor (LCA)** — the deepest node that has both `p` and `q` in its subtree. A node counts as its own ancestor, so if one value sits along the path down to the other, the shallower value's node is the answer. Return the LCA's value.

Remember what makes it a *search* tree: every node's value is strictly greater than everything in its left subtree and strictly less than everything in its right subtree. That ordering is a shortcut you don't get in a generic binary tree.

## Examples

```text
Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
Output: 6        # 2 lives in the left subtree, 8 in the right — they only meet at the root
```

```text
Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
Output: 2        # 4 hangs below 2, and a node is its own ancestor
```

```text
Input:  root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 0, q = 5
Output: 2        # path to 0 is 6→2→0, path to 5 is 6→2→4→5 — they last agree at 2
```

## Constraints

- The tree has between 2 and 10^5 nodes.
- -10^9 <= Node.val <= 10^9
- All node values are unique.
- `p != q`, and both values exist in the BST.

## Follow-up

A solution that ignores the BST ordering has to search the whole tree. Can you use the ordering to reach the answer in O(h) time and O(1) extra space, where h is the tree height?
