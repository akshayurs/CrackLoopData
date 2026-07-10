Push the target down the tree instead of accumulating a running total: at each node, subtract the node's value from the remaining sum before recursing into its children. When a leaf is reached, the path sums to `targetSum` exactly when the remaining amount equals the leaf's own value.

An empty tree can never satisfy the condition, so that check comes first. Otherwise the answer is true if this node closes out the sum as a leaf, or if either subtree can close it out with the reduced target.

```cpp
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) return false;
        int remaining = targetSum - root->val;
        if (root->left == nullptr && root->right == nullptr) {
            return remaining == 0;
        }
        return hasPathSum(root->left, remaining) || hasPathSum(root->right, remaining);
    }
};
```

## Why it works

Every recursive call carries the amount still needed from that node downward, so by the time a leaf is reached `remaining` already accounts for every ancestor on the path. The leaf check is exact rather than `<= 0` because negative values are allowed, so overshooting or undershooting both simply fail. The `||` between the two subtree calls means any single successful root-to-leaf path is enough to return true.

## Complexity

- Time: O(n) — every node is visited at most once.
- Space: O(h) — the recursion stack is as deep as the tree height, up to O(n) for a skewed tree.
