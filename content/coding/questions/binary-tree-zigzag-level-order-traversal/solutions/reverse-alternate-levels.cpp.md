Start with a plain breadth-first traversal: a queue holds one level's worth of nodes at a time, and you drain exactly that many before moving to the children. That alone produces the levels left-to-right, top to bottom.

Zigzag only changes the *order values are read in*, not which nodes belong to which level — so build each level normally, then flip it in place whenever the current level is meant to run right-to-left. A boolean flag toggled after every level tells you when to reverse.

```cpp
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            if (!leftToRight) reverse(level.begin(), level.end());
            result.push_back(level);
            leftToRight = !leftToRight;
        }
        return result;
    }
};
```

## Why it works

`size` is snapshotted before the inner loop, so exactly the nodes belonging to the current level are popped — their children get pushed for the next round without being processed early. The level is collected in the natural left-to-right order every time; `leftToRight` only decides whether that vector gets reversed before being pushed to the answer, which is enough to alternate direction level by level.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once; reversing a level costs at most O(n) total across all levels.
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
