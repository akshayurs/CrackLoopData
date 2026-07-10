Read the definition literally: a node is valid when *every* value in its left subtree is smaller and *every* value in its right subtree is larger. So gather all the values on each side and check them against the node, then recurse into the children to verify they are valid BSTs too.

This is the most direct translation of the rules, but collecting an entire subtree's values at each node repeats a lot of work — the same nodes get scanned once for every ancestor above them.

```python
def is_valid_bst(root):
    def all_values(node):
        if node is None:
            return []
        return all_values(node.left) + [node.val] + all_values(node.right)

    if root is None:
        return True
    if any(v >= root.val for v in all_values(root.left)):
        return False
    if any(v <= root.val for v in all_values(root.right)):
        return False
    return is_valid_bst(root.left) and is_valid_bst(root.right)
```

## Why it works

At each node we explicitly confirm the two subtree rules by inspecting every descendant value, then recurse so the same guarantee holds at every node. If any single node violates the ordering, one of the `any(...)` checks trips and the whole result collapses to `False`.

## Complexity

- Time: O(n^2) — at each of n nodes we may scan its entire subtree; worst case (a skewed tree) is quadratic.
- Space: O(n) — the recursion depth plus the temporary lists of subtree values.
