The regrouping is really just a stable partition of the nodes by position. Collecting every node into a vector first turns "split by odd/even position" into simple index arithmetic, and relinking the two runs back-to-back is one pass over the combined order.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head) return nullptr;
        vector<ListNode*> nodes;
        for (ListNode* node = head; node; node = node->next) nodes.push_back(node);
        vector<ListNode*> ordered;
        for (size_t i = 0; i < nodes.size(); i += 2) ordered.push_back(nodes[i]);
        for (size_t i = 1; i < nodes.size(); i += 2) ordered.push_back(nodes[i]);
        for (size_t i = 0; i + 1 < ordered.size(); i++) {
            ordered[i]->next = ordered[i + 1];
        }
        ordered.back()->next = nullptr;
        return ordered[0];
    }
};
```

## Why it works

The first loop over `nodes` (stepping by two, starting at index 0) collects every odd-position node in order; the second collects every even-position node. Appending the second run after the first gives exactly the required order, and relinking consecutive entries turns that order into an actual list, with the last node's `next` cleared.

## Complexity

- Time: O(n) — one pass to collect nodes, one to relink them.
- Space: O(n) — `nodes` and `ordered` each hold a pointer per node.
