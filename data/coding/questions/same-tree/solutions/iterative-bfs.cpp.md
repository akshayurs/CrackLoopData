The recursion just walks both trees in lockstep, comparing aligned nodes — and any recursion can be rewritten with an explicit queue. Push the two roots as a pair, then repeatedly pop a pair and apply the same three checks: both empty (fine, skip), exactly one empty or values unequal (mismatch), otherwise enqueue the two pairs of children to compare later.

This trades the call stack for a queue you control, which sidesteps recursion-depth limits on very tall trees.

```cpp
#include <queue>
#include <utility>
using namespace std;

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<pair<TreeNode*, TreeNode*>> todo;
        todo.push({p, q});
        while (!todo.empty()) {
            auto [a, b] = todo.front();
            todo.pop();
            if (a == nullptr && b == nullptr) continue;
            if (a == nullptr || b == nullptr || a->val != b->val) return false;
            todo.push({a->left, b->left});
            todo.push({a->right, b->right});
        }
        return true;
    }
};
```

## Why it works

Each queued pair represents two positions that must agree. Aligned empties contribute nothing and are skipped; a lone empty or a value difference fails immediately. When a pair matches, its children are enqueued so the same comparison reaches every position. The queue empties only if no mismatch was ever found, which is exactly the condition for the trees to be identical.

## Complexity

- Time: O(n) — each aligned node pair is enqueued and processed once.
- Space: O(n) — the queue can hold a full level of pairs, up to O(n) in the worst case.
