The top-down version wastes work: it recomputes heights from scratch at every node. But a single post-order traversal already knows each subtree's height the moment it finishes visiting it — so fold the balance check into that same pass.

Have the recursion return the subtree's height *unless* it discovers an imbalance, in which case it returns a sentinel `-1` that means "already unbalanced." Once `-1` appears it propagates straight to the root, letting every ancestor bail out immediately.

```python
def is_balanced(root):
    def check(node):
        if node is None:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1
```

## Why it works

`check` computes a subtree's height in post-order, but before returning it verifies the local balance rule. A `-1` from either child — or a height gap greater than one here — collapses the current call to `-1` as well, so the sentinel races to the top without any further computation. If the root's call is anything other than `-1`, no node ever violated the rule.

## Complexity

- Time: O(n) — each node is visited exactly once; height flows up instead of being recomputed.
- Space: O(n) — recursion stack depth equals the tree's height, up to n when skewed.
