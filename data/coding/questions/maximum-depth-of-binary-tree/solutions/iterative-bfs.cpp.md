Recursion is elegant but leans on the call stack, which can overflow on a deeply skewed tree. Instead, walk the tree level by level with an explicit queue: the depth is simply the number of levels you process before the queue empties.

Start with the root as level one. Repeatedly drain the current level in full, enqueueing every child to form the next level, and bump a counter each round. When no children remain, the counter holds the maximum depth.

```cpp
#include <queue>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        std::queue<TreeNode*> q;
        q.push(root);
        int depth = 0;
        while (!q.empty()) {
            depth++;
            for (int i = q.size(); i > 0; i--) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return depth;
    }
};
```

## Why it works

Capturing `q.size()` before the inner loop fixes how many nodes belong to the current level, so each `while` iteration consumes exactly one level and adds one to `depth`. Children pushed during the loop wait until the next round. The outer loop runs once per level, so the final count equals the number of levels — the maximum depth.

## Complexity

- Time: O(n) — each node is enqueued and dequeued exactly once.
- Space: O(w) — the queue holds at most one level, whose width w can be up to n/2 for the bottom of a full tree.
