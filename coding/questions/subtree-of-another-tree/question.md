Given the roots of two binary trees, `root` and `subRoot`, return `true` if there is a node in `root` whose subtree is **structurally identical** to `subRoot` and carries the same node values, and `false` otherwise.

A subtree of a tree consists of some node in that tree together with **all** of its descendants. The whole tree also counts as a subtree of itself.

## Examples

```text
Input:  root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
Output: true        # the subtree rooted at node 4 matches subRoot exactly
```

```text
Input:  root = [3, 4, 5, 1, 2, null, null, null, null, 0], subRoot = [4, 1, 2]
Output: false       # node 2 has an extra child (0), so no subtree matches
```

```text
Input:  root = [1, 1], subRoot = [1]
Output: true        # the leaf node 1 matches the single-node subRoot
```

## Constraints

- The number of nodes in `root` is in the range [1, 2000].
- The number of nodes in `subRoot` is in the range [1, 1000].
- -10^4 <= Node.val <= 10^4

## Follow-up

Can you avoid the worst-case O(m·n) comparison and solve it closer to O(m + n)?
