The first element of `preorder` is always the current subtree's root, and that same value's position inside `inorder` tells you exactly how many nodes fall in the left subtree versus the right. Once you know that split, the rest of `preorder` and `inorder` can be divided into a left range and a right range and the whole thing repeats recursively.

The straightforward way to find the split point is to scan `inorder` for the root value each time a subtree is built. It works, but that scan makes every recursive call more expensive the deeper the tree gets.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build(preorder, inorder, 0, (int)preorder.size() - 1, 0, (int)inorder.size() - 1);
    }

private:
    TreeNode* build(vector<int>& preorder, vector<int>& inorder, int preLo, int preHi, int inLo, int inHi) {
        if (preLo > preHi) return nullptr;
        int rootVal = preorder[preLo];
        TreeNode* root = new TreeNode(rootVal);
        int rootIdx = inLo;
        while (inorder[rootIdx] != rootVal) rootIdx++;
        int leftSize = rootIdx - inLo;
        root->left = build(preorder, inorder, preLo + 1, preLo + leftSize, inLo, rootIdx - 1);
        root->right = build(preorder, inorder, preLo + leftSize + 1, preHi, rootIdx + 1, inHi);
        return root;
    }
};
```

## Why it works

`preorder[preLo]` is always the root of the subtree currently being built, because preorder visits a node before either of its children. Locating that value in `inorder` splits the remaining range into everything left of it (the left subtree, size `leftSize`) and everything right of it (the right subtree). The matching `preorder` range is divided the same way: the next `leftSize` elements after the root build the left subtree, and everything after that builds the right subtree. Passing index bounds instead of copying vectors keeps the recursion itself cheap; only the repeated linear scan is expensive.

## Complexity

- Time: O(n²) — each of the n recursive calls scans up to O(n) elements of `inorder` to find the root.
- Space: O(n) — recursion depth is O(n) in the worst case (a skewed tree); no other auxiliary storage.
