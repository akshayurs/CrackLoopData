The most literal reading of the problem: for every node, look back at the full path from the root and ask whether anything on it beats the node's value. Track the path explicitly as you recurse, and at each node recompute the maximum of everything seen so far by scanning the whole path list.

It works, but it throws away information — the maximum of the path up to the parent was already known one call earlier, yet this approach re-derives it from scratch at every node.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int countGoodNodes(TreeNode* root) {
        count = 0;
        std::vector<int> path;
        dfs(root, path);
        return count;
    }

private:
    int count = 0;

    void dfs(TreeNode* node, std::vector<int>& path) {
        if (node == nullptr) {
            return;
        }
        path.push_back(node->val);
        int maxVal = *std::max_element(path.begin(), path.end());
        if (node->val == maxVal) {
            count++;
        }
        dfs(node->left, path);
        dfs(node->right, path);
        path.pop_back();
    }
};
```

## Why it works

`path` always holds the values from the root down to the current node, inclusive, because entries are pushed before recursing and popped after both subtrees return. A node is good exactly when its own value equals the maximum of that path — no ancestor exceeds it. Scanning `path` at every node is correct but redundant, since most of that vector was already scanned one level up.

## Complexity

- Time: O(n * h) — each of the n nodes triggers an O(h) scan of its path, where h is the tree height (worst case O(n^2) on a skewed tree).
- Space: O(h) — the path vector and recursion stack both grow to the height of the tree.
