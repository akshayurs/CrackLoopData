Recursion works but risks a stack overflow on a deeply skewed tree, and it hides the traversal state inside the call stack. Make that state explicit: keep an ordinary stack of node/remaining pairs, where `remaining` is the sum still needed once every ancestor on the path from the root has been paid for.

Pop one pair at a time. If the popped node is a leaf, check whether its own value finishes off `remaining`; if it does, the whole tree qualifies. Otherwise push each existing child with a `remaining` reduced by the current node's value, and keep going until the stack empties.

```cpp
#include <stack>
#include <utility>

class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) return false;
        std::stack<std::pair<TreeNode*, int>> stk;
        stk.push({root, targetSum});
        while (!stk.empty()) {
            auto [node, remainingBefore] = stk.top();
            stk.pop();
            int remaining = remainingBefore - node->val;
            if (node->left == nullptr && node->right == nullptr) {
                if (remaining == 0) return true;
                continue;
            }
            if (node->left != nullptr) stk.push({node->left, remaining});
            if (node->right != nullptr) stk.push({node->right, remaining});
        }
        return false;
    }
};
```

## Why it works

The stack simulates the same depth-first order recursion would use, just with the "amount still owed" carried alongside each node instead of being an implicit function argument. A leaf is only ever pushed once, is popped once, and is checked exactly like the recursive base case. Because every root-to-leaf path is eventually popped and tested, the loop finds a match if and only if one exists; exhausting the stack without a match proves none does.

## Complexity

- Time: O(n) — every node is pushed and popped exactly once.
- Space: O(h) — the stack holds at most one path's worth of pending siblings, up to O(n) for a skewed tree.
