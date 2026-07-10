Recursion is elegant here, but it ties up one stack frame per level of depth — on a very deep, unbalanced tree that risks blowing the call stack. The fix is to do the same swapping with an explicit queue instead of the call stack, visiting nodes level by level.

Pull a node off the queue, swap its two children, then push whichever children exist back onto the queue so they get the same treatment. There's no ordering requirement between levels, so a plain FIFO queue (breadth-first) works just as well as a stack would (depth-first) — either drains every node exactly once.

```cpp
#include <queue>
#include <utility>

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return nullptr;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            std::swap(node->left, node->right);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return root;
    }
};
```

## Why it works

Every node that ever enters the queue gets its children swapped exactly once, and a node's children are only enqueued after they exist (i.e., before the parent's swap reassigns them), so no node is skipped or processed twice. Once the queue drains, every node in the tree has been visited and flipped, so the whole structure is mirrored.

## Complexity

- Time: O(n) — every node is enqueued and dequeued exactly once.
- Space: O(w) — the queue holds at most one tree level at a time; w is the widest level, which is O(n) in the worst case (a complete tree's bottom row).
