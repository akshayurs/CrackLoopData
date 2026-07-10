Level order is exactly what breadth-first search produces, so lean on a queue. The trick is grouping the output by level: before draining the queue, note how many nodes it currently holds — that count is precisely the size of the current level. Pop exactly that many, record their values, and push their children to form the next level.

Because every child is pushed to the back while the current level is popped from the front, nodes always come out top-to-bottom and left-to-right.

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        if (root == nullptr) return levels;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            vector<int> level;
            for (int i = q.size(); i > 0; i--) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            levels.push_back(level);
        }
        return levels;
    }
};
```

## Why it works

Capturing `q.size()` before the inner loop fixes how many nodes belong to the current level. The inner loop consumes exactly those nodes and pushes their children behind the still-unprocessed nodes, so the queue's FIFO order guarantees each level is emitted fully before the next begins. Left children are pushed before right children, preserving left-to-right order within every level.

## Complexity

- Time: O(n) — each node is pushed and popped exactly once.
- Space: O(n) — the queue plus the output hold up to n values; a single level can be as wide as n/2.
