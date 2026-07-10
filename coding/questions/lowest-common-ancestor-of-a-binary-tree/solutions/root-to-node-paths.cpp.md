The most literal reading of "common ancestor" is: find the full chain of ancestors from the root down to each target node, then see where those two chains stop agreeing. Everything before the split is shared.

Build each path with a DFS that pushes the current node, recurses into both children, and pops the node back off if neither side finds the target — that leaves the vector holding exactly the root-to-target chain when the search succeeds. Then walk the two vectors together and remember the last node where they still matched.

```cpp
#include <vector>

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::vector<TreeNode*> pathP, pathQ;
        findPath(root, p, pathP);
        findPath(root, q, pathQ);

        TreeNode* ancestor = nullptr;
        for (size_t i = 0; i < pathP.size() && i < pathQ.size(); i++) {
            if (pathP[i] != pathQ[i]) break;
            ancestor = pathP[i];
        }
        return ancestor;
    }

private:
    bool findPath(TreeNode* node, TreeNode* target, std::vector<TreeNode*>& path) {
        if (node == nullptr) return false;
        path.push_back(node);
        if (node == target) return true;
        if (findPath(node->left, target, path) || findPath(node->right, target, path)) {
            return true;
        }
        path.pop_back();
        return false;
    }
};
```

## Why it works

Every node on `pathP` is, by construction, an ancestor of `p` (the root itself, then each step down to `p`); the same holds for `pathQ`. Both paths start at the same root, so they agree for a while and then diverge at the point where `p` and `q` land in different subtrees. The last node before that divergence is an ancestor of both — and it's the deepest one, since anything further down the shared prefix would no longer be common to both paths.

## Complexity

- Time: O(n) — each `findPath` call visits every node once in the worst case, and the final walk is bounded by the shorter path.
- Space: O(n) — the two path vectors can each hold up to the tree's height, which is O(n) for a skewed tree.
