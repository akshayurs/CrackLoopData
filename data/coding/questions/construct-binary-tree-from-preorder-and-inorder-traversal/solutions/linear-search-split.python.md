The first element of `preorder` is always the current subtree's root, and that same value's position inside `inorder` tells you exactly how many nodes fall in the left subtree versus the right. Once you know that split, the rest of `preorder` and `inorder` can be sliced into a left chunk and a right chunk and the whole thing repeats recursively.

The straightforward way to find the split point is to scan `inorder` for the root value each time a subtree is built. It works, but that scan makes every recursive call more expensive the deeper the tree gets.

```python
def build_tree(preorder, inorder):
    def build(pre_lo, pre_hi, in_lo, in_hi):
        if pre_lo > pre_hi:
            return None
        root_val = preorder[pre_lo]
        root = TreeNode(root_val)
        root_idx = in_lo
        while inorder[root_idx] != root_val:
            root_idx += 1
        left_size = root_idx - in_lo
        root.left = build(pre_lo + 1, pre_lo + left_size, in_lo, root_idx - 1)
        root.right = build(pre_lo + left_size + 1, pre_hi, root_idx + 1, in_hi)
        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

## Why it works

`preorder[pre_lo]` is always the root of the subtree currently being built, because preorder visits a node before either of its children. Locating that value in `inorder` splits the remaining range into everything left of it (the left subtree, size `left_size`) and everything right of it (the right subtree). The matching `preorder` range is sliced the same way: the next `left_size` elements after the root build the left subtree, and everything after that builds the right subtree. Passing index bounds instead of copying arrays keeps the recursion itself cheap; only the repeated linear scan is expensive.

## Complexity

- Time: O(n²) — each of the n recursive calls scans up to O(n) elements of `inorder` to find the root.
- Space: O(n) — recursion depth is O(n) in the worst case (a skewed tree); no other auxiliary storage.
