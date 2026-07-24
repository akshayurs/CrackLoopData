Instead of collecting every path and checking it afterward, carry the answer to "how much is left to reach `targetSum`" down the recursion itself. Subtract the current node's value from the remaining amount before descending; a leaf only qualifies if that remaining amount has hit exactly zero. There is no need to ever revisit a value once it has been folded into `remaining`.

The path buffer is still shared and backtracked the same way as the brute-force version, but now a path is copied into the result only when it is actually valid — never for a discarded candidate.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, targetSum, path, result);
        return result;
    }

private:
    void dfs(TreeNode* node, int remaining, vector<int>& path, vector<vector<int>>& result) {
        if (node == nullptr) return;
        path.push_back(node->val);
        remaining -= node->val;
        if (node->left == nullptr && node->right == nullptr && remaining == 0) {
            result.push_back(path);
        } else {
            dfs(node->left, remaining, path, result);
            dfs(node->right, remaining, path, result);
        }
        path.pop_back();
    }
};
```

## Why it works

`remaining` always equals `targetSum` minus the sum of the values on the current root-to-node path, so checking `remaining == 0` at a leaf is exactly checking that the full path sums to `targetSum` — without ever re-summing it. Because `remaining` is passed by value, each recursive call gets its own copy, so returning from a call automatically restores the correct amount for the sibling branch. `path` is pushed before recursing and popped after, so it always mirrors the current DFS stack, and left-before-right recursion keeps the output in DFS order.

## Complexity

- Time: O(n) — each node is visited once and does O(1) work beyond copying a path into the result, and the total copying cost is bounded by the size of the output.
- Space: O(h) — the recursion stack and `path` buffer are as deep as the tree height, on top of the space needed for the result itself.
