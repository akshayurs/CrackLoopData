The trap in this problem is that checking `left < node < right` on immediate children is not enough — a value must respect every ancestor above it. Capture that by threading an allowed open interval `(low, high)` down the recursion: each node must fall strictly inside its interval, and moving left tightens the upper bound to the node's value while moving right tightens the lower bound.

Using `long long` bounds seeded with `LLONG_MIN`/`LLONG_MAX` sidesteps the edge case where a node holds `INT_MIN` or `INT_MAX`, so the strict comparisons stay correct.

```cpp
#include <climits>

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return valid(root, LLONG_MIN, LLONG_MAX);
    }

private:
    bool valid(TreeNode* node, long long low, long long high) {
        if (node == nullptr) return true;
        if (node->val <= low || node->val >= high) return false;
        return valid(node->left, low, node->val) && valid(node->right, node->val, high);
    }
};
```

## Why it works

When we descend left, the current node becomes the strict upper bound; when we descend right, it becomes the strict lower bound. So each node inherits the tightest lower and upper limits from all of its ancestors, exactly encoding the BST rule across the whole tree. The sentinel `long long` bounds are wide enough that any valid 32-bit node value passes at the root.

## Complexity

- Time: O(n) — each node is checked once.
- Space: O(h) — the recursion stack holds one frame per level, up to the tree's height h.
