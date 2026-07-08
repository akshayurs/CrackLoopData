There is a defining property of a BST: an **in-order traversal** (left, node, right) visits the values in strictly increasing order. So walk the tree in-order and check that each value exceeds the one before it. Here we do it iteratively with an explicit stack, which sidesteps recursion depth and keeps only the previous value around.

You never need the full sequence — just the last value seen. Comparing each node against it turns the check into one linear pass.

```cpp
#include <stack>

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        std::stack<TreeNode*> st;
        TreeNode* node = root;
        bool hasPrev = false;
        long long prev = 0;
        while (node != nullptr || !st.empty()) {
            while (node != nullptr) {
                st.push(node);
                node = node->left;
            }
            node = st.top();
            st.pop();
            if (hasPrev && node->val <= prev) return false;
            hasPrev = true;
            prev = node->val;
            node = node->right;
        }
        return true;
    }
};
```

## Why it works

Pushing left children then popping reproduces the in-order order without recursion. Each popped node is the in-order successor of the previous one, so asserting `node->val > prev` enforces strictly increasing values across the whole tree. Any equal or smaller value fails immediately.

## Complexity

- Time: O(n) — each node is pushed and popped once.
- Space: O(h) — the stack holds at most one root-to-leaf path, up to the tree's height h.
