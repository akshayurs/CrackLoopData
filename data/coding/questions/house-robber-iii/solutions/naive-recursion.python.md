The most direct reading of the rule: at every node you face a binary choice. Either rob this house — in which case you must skip both children and can only add whatever the grandchildren yield — or skip this house and take the best each child can offer on its own. Recurse on both options and keep the larger.

This is the honest first pass. It is correct, but the same subtree gets solved from multiple different ancestors (once as a "grandchild" call, once as a "child" call), so work is repeated all the way down.

```python
def rob(root):
    if root is None:
        return 0

    rob_this = root.val
    if root.left:
        rob_this += rob(root.left.left) + rob(root.left.right)
    if root.right:
        rob_this += rob(root.right.left) + rob(root.right.right)

    skip_this = rob(root.left) + rob(root.right)

    return max(rob_this, skip_this)
```

## Why it works

`rob_this` commits to taking the current house, so the next houses that are still fair game are the grandchildren — the direct children are forbidden. `skip_this` gives up the current house entirely and simply asks each child subtree for its own best answer, with no restriction on whether the child itself gets robbed. Since these two choices cover every possibility for the current node, their maximum is the answer for the subtree rooted here.

## Complexity

- Time: O(2^n) — each node can be reached through several different recursive paths (as a grandchild of multiple ancestors), so subtrees are re-solved repeatedly.
- Space: O(n) — recursion depth in the worst case (a skewed tree), plus the call stack fan-out.
