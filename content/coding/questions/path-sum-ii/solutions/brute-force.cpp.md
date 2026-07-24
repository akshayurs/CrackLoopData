The most direct reading: find *every* root-to-leaf path first, ignoring the target entirely, then go back and keep only the ones that happen to add up to `targetSum`. Recording a path is a depth-first walk that pushes the current value, recurses, and pops it back off before returning to the parent — backtracking so one buffer serves every branch.

Once every path is collected, filtering is a second, separate pass: sum each stored path and compare it to `targetSum`. It works, but it does strictly more work than necessary since most collected paths are usually discarded.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> allPaths;
        vector<int> path;
        collect(root, path, allPaths);

        vector<vector<int>> result;
        for (auto& p : allPaths) {
            int total = 0;
            for (int v : p) total += v;
            if (total == targetSum) result.push_back(p);
        }
        return result;
    }

private:
    void collect(TreeNode* node, vector<int>& path, vector<vector<int>>& allPaths) {
        if (node == nullptr) return;
        path.push_back(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            allPaths.push_back(path);
        } else {
            collect(node->left, path, allPaths);
            collect(node->right, path, allPaths);
        }
        path.pop_back();
    }
};
```

## Why it works

`collect` performs a standard DFS, growing `path` on the way down and shrinking it on the way back up, so by the time a leaf is reached `path` holds exactly the values from the root to that leaf. Copying it into `allPaths` at each leaf preserves left-to-right, root-to-leaf order across the whole tree. The final loop then re-derives each path's sum independently and keeps only the matches.

## Complexity

- Time: O(n^2) — the DFS visits every node once, but each of the up to O(n) leaf paths can be O(n) long, and both copying and summing a path cost O(path length).
- Space: O(n^2) — `allPaths` retains every root-to-leaf path, not just the matching ones, before filtering.
