Ignore the BST ordering for a moment and solve the general-tree version: find the root-to-node path for `p`, find the root-to-node path for `q`, then walk both paths together from the start. The last value where they still agree is the deepest shared ancestor.

Recording a path is plain DFS — append the current value, recurse into the children looking for the target, and back the value out again if neither side finds it.

```python
def find_path(node, target, path):
    if node is None:
        return False
    path.append(node.val)
    if node.val == target:
        return True
    if find_path(node.left, target, path) or find_path(node.right, target, path):
        return True
    path.pop()
    return False

def lowest_common_ancestor(root, p, q):
    path_p, path_q = [], []
    find_path(root, p, path_p)
    find_path(root, q, path_q)
    lca = path_p[0]
    for a, b in zip(path_p, path_q):
        if a != b:
            break
        lca = a
    return lca
```

## Why it works

Both paths start at the root, so their prefixes describe the same ancestors until the two nodes' branches actually diverge. The loop tracks the last value that still matched in both paths — that's precisely the deepest node both `p` and `q` descend from, including the case where one is an ancestor of the other.

## Complexity

- Time: O(n) — each `find_path` call may visit every node once.
- Space: O(n) — the recursion stack and the two stored paths can each grow to the tree's size.
