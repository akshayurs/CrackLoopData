The most literal reading of "common ancestor" is: find the full chain of ancestors from the root down to each target node, then see where those two chains stop agreeing. Everything before the split is shared.

Build each path with a DFS that appends the current node, recurses into both children, and pops the node back off if neither side finds the target — that leaves `path` holding exactly the root-to-target chain when the search succeeds. Then walk the two paths together and remember the last node where they still matched.

```python
def lowest_common_ancestor(root, p, q):
    def find_path(node, target, path):
        if node is None:
            return False
        path.append(node)
        if node is target:
            return True
        if find_path(node.left, target, path) or find_path(node.right, target, path):
            return True
        path.pop()
        return False

    path_p, path_q = [], []
    find_path(root, p, path_p)
    find_path(root, q, path_q)

    ancestor = None
    for a, b in zip(path_p, path_q):
        if a is not b:
            break
        ancestor = a
    return ancestor
```

## Why it works

Every node on `path_p` is, by construction, an ancestor of `p` (the root itself, then each step down to `p`); the same holds for `path_q`. Both paths start at the same root, so they agree for a while and then diverge at the point where `p` and `q` land in different subtrees. The last node before that divergence is an ancestor of both — and it's the deepest one, since anything further down the shared prefix would no longer be common to both paths.

## Complexity

- Time: O(n) — each `find_path` call visits every node once in the worst case, and the final walk is bounded by the shorter path.
- Space: O(n) — the two path lists can each hold up to the tree's height, which is O(n) for a skewed tree.
