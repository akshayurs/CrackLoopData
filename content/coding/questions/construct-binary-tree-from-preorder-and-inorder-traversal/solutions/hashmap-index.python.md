The scan for the root's position in `inorder` is the only expensive part of the previous approach, and it is entirely avoidable: build a value-to-index map for `inorder` up front so every lookup becomes O(1).

The second refinement is to stop slicing `preorder` by index range. Since preorder visits root, then the whole left subtree, then the whole right subtree, a single shared pointer that always points at "the next unused preorder value" naturally advances in the right order as long as the left subtree is fully built before the right one starts — no bounds math needed on that side at all.

```python
def build_tree(preorder, inorder):
    index_of = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def build(in_lo, in_hi):
        nonlocal pre_idx
        if in_lo > in_hi:
            return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)
        mid = index_of[root_val]
        root.left = build(in_lo, mid - 1)
        root.right = build(mid + 1, in_hi)
        return root

    return build(0, len(inorder) - 1)
```

## Why it works

`index_of` gives the split point for any root value in constant time instead of a scan. The recursion still only needs the `inorder` range as bounds: `pre_idx` tracks progress through `preorder` on its own, and because `build` always finishes the entire left subtree (consuming exactly as many preorder values as it has nodes) before touching the right subtree, `pre_idx` is guaranteed to sit on the correct next root every time it's read.

## Complexity

- Time: O(n) — the map is built in one pass, and each of the n nodes does O(1) work.
- Space: O(n) — the index map plus O(n) recursion depth in the worst case.
