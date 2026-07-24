The order the final list must follow is exactly preorder — visit a node, then its left subtree, then its right subtree. So the most direct plan is to first run an ordinary preorder traversal and stash every node in a vector, then wire that vector together afterward.

Once the vector exists in the right order, rewiring is trivial: point each node's `right` at the next entry and clear its `left`, then close off the final node.

```cpp
#include <vector>

class Solution {
public:
    void flatten(TreeNode* root) {
        if (root == nullptr) return;
        std::vector<TreeNode*> nodes;
        preorder(root, nodes);
        for (size_t i = 0; i + 1 < nodes.size(); i++) {
            nodes[i]->left = nullptr;
            nodes[i]->right = nodes[i + 1];
        }
        nodes.back()->left = nullptr;
        nodes.back()->right = nullptr;
    }

private:
    void preorder(TreeNode* node, std::vector<TreeNode*>& nodes) {
        if (node == nullptr) return;
        nodes.push_back(node);
        preorder(node->left, nodes);
        preorder(node->right, nodes);
    }
};
```

## Why it works

The traversal visits nodes in the same root-left-right order the flattened list must have, so `nodes` already holds the target sequence before any pointer is touched. The rewiring pass then just links consecutive entries and nulls out every `left` pointer, which is exactly the shape a "linked list through right pointers" requires.

## Complexity

- Time: O(n) — one traversal to collect nodes, one pass to relink them.
- Space: O(n) — the vector holds every node, on top of an O(h) recursion stack.
