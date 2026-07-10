Instead of collecting every path and checking it afterward, carry the answer to "how much is left to reach `targetSum`" down the recursion itself. Subtract the current node's value from the remaining amount before descending; a leaf only qualifies if that remaining amount has hit exactly zero. There is no need to ever revisit a value once it has been folded into `remaining`.

The path buffer is still shared and backtracked the same way as the brute-force version, but now a path is copied into the result only when it is actually valid — never for a discarded candidate.

```python
def path_sum(root, target_sum):
    result = []
    path = []

    def dfs(node, remaining):
        if node is None:
            return
        path.append(node.val)
        remaining -= node.val
        if node.left is None and node.right is None and remaining == 0:
            result.append(list(path))
        else:
            dfs(node.left, remaining)
            dfs(node.right, remaining)
        path.pop()

    dfs(root, target_sum)
    return result
```

## Why it works

`remaining` always equals `target_sum` minus the sum of the values on the current root-to-node path, so checking `remaining == 0` at a leaf is exactly checking that the full path sums to `target_sum` — without ever re-summing it. Because `remaining` is passed by value into each recursive call, popping back up automatically restores the correct amount for the sibling branch. `path` is pushed before recursing and popped after, so it always mirrors the current DFS stack, and left-before-right recursion keeps the output in DFS order.

## Complexity

- Time: O(n) — each node is visited once and does O(1) work beyond copying a path into the result, and the total copying cost is bounded by the size of the output.
- Space: O(h) — the recursion stack and `path` buffer are as deep as the tree height, on top of the space needed for the result itself.
