A thief has found a new target: a neighborhood laid out as a binary tree instead of a street. Every node is a house holding some amount of cash, and the only path between two houses is the edge connecting them. The one rule the security system enforces is that no two **directly connected** houses (a node and its parent) can be robbed on the same night, or the alarm trips. Given the root of this binary tree, return the maximum total amount of cash the thief can collect.

## Examples

```text
Input:  root = [3, 2, 3, null, 3, null, 1]
Output: 7        # rob nodes 3 + 3 + 1 (the root's two grandchildren and the deep leaf)
```

```text
Input:  root = [3, 4, 5, 1, 3, null, 1]
Output: 9        # skip the root, rob nodes 4 + 5 (both direct children)
```

```text
Input:  root = [4, 1, null, 2, null, 3]
Output: 7        # rob nodes 4 + 3, a non-adjacent pair down the single chain
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `0 <= Node.val <= 10^4`.

## Follow-up

Can you avoid recomputing the same subtree's answer more than once, without using a hash map keyed on node references?
