The scan for the root's position in `inorder` is the only expensive part of the previous approach, and it is entirely avoidable: build a value-to-index map for `inorder` up front so every lookup becomes O(1).

The second refinement is to stop tracking `preorder` by index range. Since preorder visits root, then the whole left subtree, then the whole right subtree, a single shared pointer that always points at "the next unused preorder value" naturally advances in the right order as long as the left subtree is fully built before the right one starts — no bounds math needed on that side at all.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> indexOf;
        for (int i = 0; i < (int)inorder.size(); i++) {
            indexOf[inorder[i]] = i;
        }
        preIdx = 0;
        return build(preorder, indexOf, 0, (int)inorder.size() - 1);
    }

private:
    int preIdx;

    TreeNode* build(vector<int>& preorder, unordered_map<int, int>& indexOf, int inLo, int inHi) {
        if (inLo > inHi) return nullptr;
        int rootVal = preorder[preIdx++];
        TreeNode* root = new TreeNode(rootVal);
        int mid = indexOf[rootVal];
        root->left = build(preorder, indexOf, inLo, mid - 1);
        root->right = build(preorder, indexOf, mid + 1, inHi);
        return root;
    }
};
```

## Why it works

`indexOf` gives the split point for any root value in constant time instead of a scan. The recursion still only needs the `inorder` range as bounds: `preIdx` tracks progress through `preorder` on its own, and because `build` always finishes the entire left subtree (consuming exactly as many preorder values as it has nodes) before touching the right subtree, `preIdx` is guaranteed to sit on the correct next root every time it's read.

## Complexity

- Time: O(n) — the map is built in one pass, and each of the n nodes does O(1) work.
- Space: O(n) — the index map plus O(n) recursion depth in the worst case.
