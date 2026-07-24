You are given two integer arrays `preorder` and `inorder`, representing the preorder and inorder traversal of the same binary tree. Every value in the tree is unique. Rebuild the tree and return its root.

The output tree is shown as a level-order array — each level left to right, with `null` marking a missing child, and trailing `null`s dropped.

## Examples

```text
Input:  preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]
```

```text
Input:  preorder = [-1], inorder = [-1]
Output: [-1]
```

```text
Input:  preorder = [1, 2], inorder = [2, 1]
Output: [1, 2]        # 2 is the left child of 1
```

## Constraints

- 1 <= preorder.length == inorder.length <= 3000
- -3000 <= preorder[i], inorder[i] <= 3000
- All values in `preorder` are distinct, and all values in `inorder` are distinct.
- `inorder` is guaranteed to be the inorder traversal of the same tree that `preorder` is the preorder traversal of.
