The most literal reading of "what you'd see from the side" is to process the tree level by level and remember only the last node visited at each depth — that is exactly the rightmost node, since a standard left-to-right traversal reaches it last.

A queue-based breadth-first walk naturally groups nodes by level: process the queue's current contents as one batch, and whichever node comes off last in that batch is the one visible from the right.

```cpp
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) return result;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return result;
    }
};
```

## Why it works

`levelSize` freezes how many nodes belong to the current level before any children get pushed, so the loop drains exactly that level. Nodes are popped left to right (children were pushed left-then-right), so the last one popped in the batch is the rightmost node at that depth — the only one recorded.

## Complexity

- Time: O(n) — every node is pushed and popped exactly once.
- Space: O(n) — the queue can hold an entire level, which is O(n) for a wide tree.
