The brute force redoes work because the running sum from the root to any node gets recomputed from scratch for every candidate start along the way. Track the sum from the root to the current node instead, and the classic "subarray sum equals k" trick carries over directly: if `runningSum - targetSum` was already seen higher up the current root-to-node path, everything between that earlier point and here sums to `targetSum`.

Keep a map of how many times each prefix sum has occurred *on the current path*, adding the current node's contribution before recursing and removing it again on the way back up — the map must only reflect ancestors of the node being processed, not siblings elsewhere in the tree.

```cpp
#include <unordered_map>

class Solution {
public:
    int pathSum(TreeNode* root, long long targetSum) {
        std::unordered_map<long long, int> prefixCounts;
        prefixCounts[0] = 1;
        return dfs(root, 0, targetSum, prefixCounts);
    }

private:
    int dfs(TreeNode* node, long long runningSum, long long targetSum,
            std::unordered_map<long long, int>& prefixCounts) {
        if (node == nullptr) return 0;
        runningSum += node->val;
        int count = 0;
        auto it = prefixCounts.find(runningSum - targetSum);
        if (it != prefixCounts.end()) count = it->second;
        prefixCounts[runningSum]++;
        count += dfs(node->left, runningSum, targetSum, prefixCounts);
        count += dfs(node->right, runningSum, targetSum, prefixCounts);
        prefixCounts[runningSum]--;
        return count;
    }
};
```

## Why it works

`runningSum` is the sum of values from the root to the current node. A downward path from some ancestor `a` (exclusive) to the current node sums to `targetSum` exactly when `runningSum - sumToA == targetSum`, i.e. `sumToA == runningSum - targetSum`. `prefixCounts` holds exactly the root-to-ancestor sums still "open" on the current recursion stack, so looking up `runningSum - targetSum` counts every valid ancestor in O(1). Decrementing the count when backtracking out of a subtree keeps the map scoped to the current path, so paths through unrelated branches never interfere.

## Complexity

- Time: O(n) — each node is visited once, doing O(1) work per node.
- Space: O(n) — the map can hold up to n entries, plus O(h) recursion stack.
