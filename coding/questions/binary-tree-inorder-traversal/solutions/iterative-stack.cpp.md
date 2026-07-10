Recursion works, but it hides the traversal state on the call stack, which is easy to overflow on a very deep tree and hard to pause or resume. Simulating the same left-node-right walk with an explicit stack gives full control over that state.

The trick is to keep pushing left children onto the stack until there are none left — that reaches the leftmost unvisited node. Popping the stack then visits it, and moving to its right child restarts the same "go left as far as possible" process from there.

```cpp
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> stk;
        TreeNode* node = root;
        while (node != nullptr || !stk.empty()) {
            while (node != nullptr) {
                stk.push(node);
                node = node->left;
            }
            node = stk.top();
            stk.pop();
            result.push_back(node->val);
            node = node->right;
        }
        return result;
    }
};
```

## Why it works

The inner loop dives to the leftmost node reachable from `node`, pushing every ancestor along the way so it can be revisited later. Popping gives the smallest unvisited node in the current subtree, which is correct because everything further left has already been recorded. Setting `node = node->right` then hands off to that subtree, and because it starts as `nullptr` when there is no right child, the outer loop simply pops the next pending ancestor instead.

## Complexity

- Time: O(n) — every node is pushed and popped exactly once.
- Space: O(n) — O(h) for the stack plus O(n) for the output vector; h can be O(n) for a skewed tree.
