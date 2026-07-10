The BST invariant tells you exactly which side `key` lives on, so use it: compare `key` against the current node's value and descend left or right, never both. The moment you land on the matching node, apply the same three splice rules as before — no children or one child returns the surviving side directly, two children copy up the in-order successor's value and remove that successor from the right subtree.

Since every step of the search follows a single path down the tree instead of branching both ways, the whole operation costs one root-to-node walk rather than a full traversal.

```cpp
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) return nullptr;

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            if (root->left == nullptr) return root->right;
            if (root->right == nullptr) return root->left;
            TreeNode* successor = root->right;
            while (successor->left != nullptr) {
                successor = successor->left;
            }
            root->val = successor->val;
            root->right = deleteNode(root->right, successor->val);
        }

        return root;
    }
};
```

## Why it works

At each step, exactly one branch can possibly contain `key` because the BST orders every value relative to the current node — so following the comparison is guaranteed not to miss the target. Once found, the splice rules preserve the BST property: a leaf or single-child node is removed without disturbing order, and a two-child node's in-order successor is its smallest larger value, so promoting it keeps everything to the left still smaller and everything to the right still larger.

## Complexity

- Time: O(h) — one path down for the initial search, plus at most one more path down the right subtree to remove the successor; h is the tree height (O(log n) balanced, O(n) skewed).
- Space: O(h) — the recursion stack matches the path length.
