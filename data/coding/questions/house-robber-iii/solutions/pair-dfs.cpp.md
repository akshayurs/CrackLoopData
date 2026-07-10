The waste in the naive version comes from asking "what if I rob this house?" and "what if I skip it?" as two separate top-down questions, which forces re-deriving each child's answer twice. Flip it around: make every recursive call return **both** answers for its own subtree at once — the best total if the subtree's root is robbed, and the best total if it is not. A parent can then combine its children's answers with no re-computation.

Each call does a single post-order pass: gather the `{with, without}` pair from the left and right children, then compute `withRoot = root->val + withoutLeft + withoutRight` (robbing the root forbids robbing either child) and `withoutRoot = max(withLeft, withoutLeft) + max(withRight, withoutRight)` (skipping the root frees each child to be robbed or not, whichever is better).

```cpp
#include <utility>
#include <algorithm>

class Solution {
public:
    int rob(TreeNode* root) {
        auto [withRoot, withoutRoot] = dfs(root);
        return std::max(withRoot, withoutRoot);
    }

private:
    std::pair<int, int> dfs(TreeNode* node) {
        if (node == nullptr) return {0, 0}; // {withNode, withoutNode}

        auto [withLeft, withoutLeft] = dfs(node->left);
        auto [withRight, withoutRight] = dfs(node->right);

        int withNode = node->val + withoutLeft + withoutRight;
        int withoutNode = std::max(withLeft, withoutLeft) + std::max(withRight, withoutRight);
        return {withNode, withoutNode};
    }
};
```

## Why it works

Every node's pair of answers depends only on its two children's pairs, computed exactly once each, so no subtree is ever solved twice. Robbing the root is only valid if neither child is also robbed, hence `withoutLeft`/`withoutRight`; skipping the root places no constraint on the children, so each child independently picks whichever of its two answers is larger. The final result is the better of robbing or skipping the overall root.

## Complexity

- Time: O(n) — one post-order visit per node.
- Space: O(h) — recursion stack proportional to the tree's height (worst case O(n) for a skewed tree).
