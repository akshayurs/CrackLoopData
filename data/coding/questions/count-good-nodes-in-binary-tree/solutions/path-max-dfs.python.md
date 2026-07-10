There is no need to store or rescan the whole path — the only fact that matters at any node is the single largest value seen on the way down. Carry that one number as an argument through the recursion instead of rebuilding it from a list every time.

At each node, compare its value against the running maximum to decide whether it is good, then pass the updated maximum (the larger of the two) down to both children.

```python
def count_good_nodes(root):
    def dfs(node, max_so_far):
        if node is None:
            return 0
        good = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)
        return good + dfs(node.left, new_max) + dfs(node.right, new_max)

    return dfs(root, root.val)
```

## Why it works

`max_so_far` is exactly the maximum ancestor value on the path from the root to `node`'s parent (or the root's own value at the top call). Comparing `node.val` against it answers "is this node good?" in O(1), and updating it once before recursing keeps every deeper call working with the correct running maximum — no rescanning is ever needed.

## Complexity

- Time: O(n) — each node is visited exactly once, doing O(1) work.
- Space: O(h) — recursion stack depth equals the tree height h, up to O(n) for a skewed tree.
