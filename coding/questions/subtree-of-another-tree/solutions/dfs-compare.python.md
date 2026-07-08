A subtree match can start at any node of `root`, so the direct approach is to try them all. Visit every node and ask a simple question: "if I treat this node as the top, is the tree hanging off it identical to `subRoot`?" If any node answers yes, we are done.

The identity check is its own small recursion: two trees are the same when their roots hold equal values and their left and right children are pairwise identical. Pairing this per-node comparison with a full traversal covers every possible starting point.

```python
def is_subtree(root, subRoot):
    def same(a, b):
        if a is None or b is None:
            return a is b
        return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

    if root is None:
        return False
    if same(root, subRoot):
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)
```

## Why it works

`same` returns `True` only when both trees run out of nodes at exactly the same places with matching values along the way — that is the definition of structural and value equality. The outer recursion tries `subRoot` against `root`, then against every descendant, so if a matching subtree exists anywhere it will be the current node in one of those calls. If no node matches, the traversal exhausts the tree and returns `False`.

## Complexity

- Time: O(m·n) — for each of the m nodes in `root`, `same` may compare up to n nodes of `subRoot`.
- Space: O(m) — the recursion stack can be as deep as the height of `root`, up to m for a skewed tree.
