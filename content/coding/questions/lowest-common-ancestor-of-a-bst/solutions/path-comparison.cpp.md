Ignore the BST ordering for a moment and solve the general-tree version: find the root-to-node path for `p`, find the root-to-node path for `q`, then walk both paths together from the start. The last value where they still agree is the deepest shared ancestor.

Recording a path is plain DFS — push the current value, recurse into the children looking for the target, and pop it back out if neither side finds it.

```cpp
#include <vector>

using namespace std;

class Solution {
    bool findPath(TreeNode* node, int target, vector<int>& path) {
        if (node == nullptr) return false;
        path.push_back(node->val);
        if (node->val == target) return true;
        if (findPath(node->left, target, path) || findPath(node->right, target, path)) return true;
        path.pop_back();
        return false;
    }

public:
    int lowestCommonAncestor(TreeNode* root, int p, int q) {
        vector<int> pathP, pathQ;
        findPath(root, p, pathP);
        findPath(root, q, pathQ);
        int lca = pathP[0];
        for (size_t i = 0; i < pathP.size() && i < pathQ.size(); i++) {
            if (pathP[i] != pathQ[i]) break;
            lca = pathP[i];
        }
        return lca;
    }
};
```

## Why it works

Both paths start at the root, so their prefixes describe the same ancestors until the two nodes' branches actually diverge. The loop tracks the last value that still matched in both paths — that's precisely the deepest node both `p` and `q` descend from, including the case where one is an ancestor of the other.

## Complexity

- Time: O(n) — each path search may visit every node once.
- Space: O(n) — the recursion stack and the two stored paths can each grow to the tree's size.
