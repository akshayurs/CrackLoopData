Forget for a moment that this is a search tree and treat it as any old binary tree. The lowest common ancestor is where the root-to-`p` path and the root-to-`q` path stop overlapping: both routes leave the root together, march down the same nodes for a while, then diverge. The last node they share is the LCA.

So collect the full path from the root to each target, then walk the two paths in lockstep and remember the deepest node that is still identical in both.

```python
def lowest_common_ancestor(root, p, q):
    def find_path(node, target, trail):
        if node is None:
            return False
        trail.append(node)
        if node.val == target:
            return True
        if find_path(node.left, target, trail) or find_path(node.right, target, trail):
            return True
        trail.pop()
        return False

    path_p, path_q = [], []
    find_path(root, p, path_p)
    find_path(root, q, path_q)
    ancestor = None
    for x, y in zip(path_p, path_q):
        if x is y:
            ancestor = x
        else:
            break
    return ancestor
```

## Why it works

`find_path` does a depth-first search, appending nodes as it descends and popping them on the way back up, so when it returns `True` the `trail` holds exactly the nodes from the root down to the target. Two such paths share a common prefix — the ancestors both nodes descend from — and the moment they differ marks the split point. The last matching node is therefore the deepest common ancestor.

## Complexity

- Time: O(n) — each path search may visit every node.
- Space: O(n) — the recursion stack and stored paths grow with the tree height, up to O(n) when skewed.
