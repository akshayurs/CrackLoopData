The defining property of a BST is that an **in-order** traversal — left subtree, node, right subtree — visits the values in sorted ascending order. So the straightforward approach is to run a full in-order walk, push every value into a vector, and then read position `k - 1`.

This ignores the fact that we could stop early, but it is the clearest way to see why the answer is correct: once the values are laid out in sorted order, the k-th smallest is just the element at the (k-1)-th slot.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> values;
        inorder(root, values);
        return values[k - 1];
    }

private:
    void inorder(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        inorder(node->left, values);
        values.push_back(node->val);
        inorder(node->right, values);
    }
};
```

## Why it works

In-order traversal of a BST emits nodes in increasing value order, so `values` ends up fully sorted. Element `values[k - 1]` is therefore the k-th smallest by definition. The recursion visits each node exactly once.

## Complexity

- Time: O(n) — every node is visited once regardless of `k`.
- Space: O(n) — the vector stores all `n` values, plus O(h) recursion stack.
