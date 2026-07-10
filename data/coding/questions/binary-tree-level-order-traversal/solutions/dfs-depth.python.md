Breadth-first is the obvious fit, but a plain depth-first walk works too if you tell each node which level it lives on. Carry a `depth` argument down the recursion; a node at depth `d` belongs in `levels[d]`. The first time recursion reaches a new depth, `levels` is one bucket short, so create the bucket, then append.

Visiting the left subtree before the right guarantees that within any level, values are appended left to right — even though the traversal itself dives deep rather than sweeping across.

```python
def level_order(root):
    levels = []

    def visit(node, depth):
        if node is None:
            return
        if depth == len(levels):
            levels.append([])
        levels[depth].append(node.val)
        visit(node.left, depth + 1)
        visit(node.right, depth + 1)

    visit(root, 0)
    return levels
```

## Why it works

`depth` uniquely identifies a node's level, so each value lands in the correct bucket regardless of visit order. The check `depth == len(levels)` fires exactly once per level — the first node reached at that depth — because depths are discovered in increasing order along any root-to-node path. Since the left child is always recursed before the right, the append order inside each bucket matches left-to-right position.

## Complexity

- Time: O(n) — every node is visited once.
- Space: O(n) — the output holds n values; the recursion stack adds O(h) for tree height h, up to O(n) when skewed.
