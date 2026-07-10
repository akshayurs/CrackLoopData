Inverting a tree is a naturally recursive act: a tree is mirrored when its two subtrees are each mirrored *and* then swapped. That gives a tiny recipe — invert the left subtree, invert the right subtree, hang them on the opposite sides, and hand back the node.

The base case is the empty tree, which is its own mirror, so we simply return `nullptr` and let the recursion unwind.

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return nullptr;
        TreeNode* left = invertTree(root->left);
        TreeNode* right = invertTree(root->right);
        root->left = right;
        root->right = left;
        return root;
    }
};
```

## Why it works

Each call fully mirrors the subtree rooted at `root`: the recursive calls return already-inverted left and right subtrees, and we reattach them on the opposite sides. Because every node is visited exactly once and its children are exchanged, the entire tree ends up mirrored. Leaves bottom out at the `nullptr` base case.

## Complexity

- Time: O(n) — every node is touched once.
- Space: O(h) — the recursion stack is as deep as the tree height, up to O(n) for a skewed tree.
