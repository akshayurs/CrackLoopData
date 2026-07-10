Forget for a moment that this is a search tree and treat it as any old binary tree. The lowest common ancestor is where the root-to-`p` path and the root-to-`q` path stop overlapping: both routes leave the root together, march down the same nodes for a while, then diverge. The last node they share is the LCA.

So collect the full path from the root to each target, then walk the two paths in lockstep and remember the deepest node that is still identical in both.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, int p, int q) {
        vector<TreeNode*> pathP, pathQ;
        findPath(root, p, pathP);
        findPath(root, q, pathQ);
        TreeNode* ancestor = nullptr;
        int n = min(pathP.size(), pathQ.size());
        for (int i = 0; i < n; i++) {
            if (pathP[i] == pathQ[i]) ancestor = pathP[i];
            else break;
        }
        return ancestor;
    }

private:
    bool findPath(TreeNode* node, int target, vector<TreeNode*>& trail) {
        if (node == nullptr) return false;
        trail.push_back(node);
        if (node->val == target) return true;
        if (findPath(node->left, target, trail) || findPath(node->right, target, trail)) return true;
        trail.pop_back();
        return false;
    }
};
```

## Why it works

`findPath` does a depth-first search, pushing nodes as it descends and popping them on the way back up, so when it returns `true` the `trail` holds exactly the nodes from the root down to the target. Two such paths share a common prefix — the ancestors both nodes descend from — and the moment they differ marks the split point. The last matching node is therefore the deepest common ancestor.

## Complexity

- Time: O(n) — each path search may visit every node.
- Space: O(n) — the recursion stack and stored paths grow with the tree height, up to O(n) when skewed.
