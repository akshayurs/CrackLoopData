You are given the root of a binary tree and two of its nodes, `p` and `q`. Find their **lowest common ancestor (LCA)** — the deepest node in the tree that has both `p` and `q` as descendants (a node is allowed to be a descendant of itself).

Trees are supplied in level-order array form, where `null` marks a missing child and trailing nulls are dropped. All node values are unique, and both `p` and `q` are guaranteed to exist in the tree.

## Examples

```text
Input:  root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
Output: 3        # 5 and 1 only meet back up at the root
```

```text
Input:  root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
Output: 5        # 4 is in 5's own subtree, so 5 is its own ancestor here
```

```text
Input:  root = [1, 2], p = 1, q = 2
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All `Node.val` are unique.
- `p != q` and both values exist in the tree.

## Follow-up

Can you find the ancestor with a single top-down traversal instead of building and comparing two root-to-node paths?
