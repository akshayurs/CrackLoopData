Reversing a level after the fact is an extra pass you don't actually need — you already know the direction *before* you start placing values into that level, so you can just put each value where it ultimately belongs. Building the level as a `deque<int>` lets you push to either end in O(1).

Keep the same breadth-first structure, but instead of always pushing to the back, push to the back on a left-to-right level and to the front on a right-to-left one. The queue that drives the traversal is unaffected — children are still discovered strictly left to right — only the container you're writing values into changes its insertion side.

```cpp
#include <vector>
#include <queue>
#include <deque>
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
            deque<int> level;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front(); q.pop();
                if (leftToRight) level.push_back(node->val);
                else level.push_front(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(vector<int>(level.begin(), level.end()));
            leftToRight = !leftToRight;
        }
        return result;
    }
};
```

## Why it works

The traversal queue always discovers a level's nodes left to right, regardless of the output direction — only where each value lands in `level` changes. On a left-to-right level, `push_back` reproduces that same order; on a right-to-left level, `push_front` means the first node discovered ends up last, which is exactly the mirrored order. No separate reversal step is needed because the direction is baked into the insertion itself.

## Complexity

- Time: O(n) — every node is enqueued and dequeued once, and each value is inserted into its level in O(1).
- Space: O(n) — the queue holds up to a full level of nodes, and the output stores every value.
