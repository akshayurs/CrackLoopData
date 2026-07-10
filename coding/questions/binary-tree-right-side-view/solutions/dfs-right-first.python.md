A queue is not required if the traversal visits nodes in the right order: walk the right child before the left child, and the first time a given depth is reached, that node must be the rightmost one at that depth — anything visited later at the same depth is further left and should be ignored.

This turns the problem into a single depth-first pass carrying the current depth, with the result list itself doubling as the "have I seen this depth yet?" check.

```python
def right_side_view(root):
    result = []

    def dfs(node, depth):
        if node is None:
            return
        if depth == len(result):
            result.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result
```

## Why it works

Recursing into the right subtree before the left guarantees that, for any given depth, the first node the traversal reaches is the rightmost one. `depth == len(result)` is true exactly once per depth — at that first visit — so later, more-left nodes at the same depth see `depth < len(result)` and add nothing.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) — the recursion stack depth is the tree's height, plus O(n) for the output list.
