Breadth-first is the obvious fit, but a plain depth-first walk works too if you tell each node which level it lives on. Carry a `depth` argument down the recursion; a node at depth `d` belongs in `levels[d]`. The first time recursion reaches a new depth, the vector is one bucket short, so create the bucket, then append.

Visiting the left subtree before the right guarantees that within any level, values are appended left to right — even though the traversal itself dives deep rather than sweeping across.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        visit(root, 0, levels);
        return levels;
    }

private:
    void visit(TreeNode* node, int depth, vector<vector<int>>& levels) {
        if (node == nullptr) return;
        if (depth == (int)levels.size()) levels.push_back({});
        levels[depth].push_back(node->val);
        visit(node->left, depth + 1, levels);
        visit(node->right, depth + 1, levels);
    }
};
```

## Why it works

`depth` uniquely identifies a node's level, so each value lands in the correct bucket regardless of visit order. The check `depth == levels.size()` fires exactly once per level — the first node reached at that depth — because depths are discovered in increasing order along any root-to-node path. Since the left child is always recursed before the right, the append order inside each bucket matches left-to-right position.

## Complexity

- Time: O(n) — every node is visited once.
- Space: O(n) — the output holds n values; the recursion stack adds O(h) for tree height h, up to O(n) when skewed.
