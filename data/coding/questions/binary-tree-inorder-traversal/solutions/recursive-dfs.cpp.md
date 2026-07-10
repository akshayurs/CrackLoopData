Inorder is defined recursively — left, node, right — so the cleanest solution just restates the definition: recurse into the left subtree, record the current value, then recurse into the right subtree.

An accumulator vector threaded through the calls collects values in the correct order, since each recursive call appends everything from its subtree before returning.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        visit(root, result);
        return result;
    }

private:
    void visit(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        visit(node->left, result);
        result.push_back(node->val);
        visit(node->right, result);
    }
};
```

## Why it works

`visit` fully drains the left subtree into `result` before touching the current node, then fully drains the right subtree after. Applying that rule at every level means each node's value lands strictly between everything in its left subtree and everything in its right subtree — exactly the inorder order, by induction on subtree size.

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(n) — O(h) for the recursion stack plus O(n) for the output vector; h can be O(n) for a skewed tree.
