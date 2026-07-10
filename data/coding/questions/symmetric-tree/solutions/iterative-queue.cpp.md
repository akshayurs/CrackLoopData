Any recursion can be unrolled into an explicit queue of the pairs it would have compared. Seed the queue with the root's left and right children, then repeatedly pop a pair and apply the same rule as before: both empty is fine, one empty or unequal values is a mismatch, otherwise enqueue the pair's children in mirrored order.

This avoids growing the call stack, which matters for very tall or unbalanced trees.

```cpp
#include <queue>
#include <utility>

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) return true;
        std::queue<std::pair<TreeNode*, TreeNode*>> q;
        q.push({root->left, root->right});
        while (!q.empty()) {
            auto [a, b] = q.front();
            q.pop();
            if (a == nullptr && b == nullptr) continue;
            if (a == nullptr || b == nullptr || a->val != b->val) return false;
            q.push({a->left, b->right});
            q.push({a->right, b->left});
        }
        return true;
    }
};
```

## Why it works

Each queued pair represents two positions that must be reflections of one another. Aligned empties are skipped; a lone empty or a value mismatch fails immediately. A matching pair enqueues its children crossed — left with right, right with left — which is exactly the mirroring rule applied one level deeper. The queue drains only if no mismatch was ever found, which is precisely the condition for symmetry.

## Complexity

- Time: O(n) — each node is enqueued and processed once as part of exactly one pair.
- Space: O(n) — the queue can hold up to a full level of pairs in the worst case.
