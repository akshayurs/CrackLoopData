The simplest fix is to stop thinking about pointers and treat this as ordinary array sorting in disguise. Walk the list once and copy every node's value into a vector, let `std::sort` do the hard part, then walk the list a second time and overwrite each node's `val` in order.

No node is ever created or destroyed and no `next` pointer changes — only the values move, which keeps the logic trivial at the cost of an extra vector.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        vector<int> values;
        for (ListNode* node = head; node != nullptr; node = node->next) {
            values.push_back(node->val);
        }
        sort(values.begin(), values.end());

        ListNode* node = head;
        for (int v : values) {
            node->val = v;
            node = node->next;
        }
        return head;
    }
};
```

## Why it works

The first pass records values in the same order the nodes appear in the list. Sorting that vector gives the values in ascending order, independent of the list's structure. The second pass revisits the nodes in the exact same order as the first pass, so the i-th node receives `values[i]` — after the loop every node's value matches its sorted rank, and since connectivity was never touched, the list is still intact, just sorted.

## Complexity

- Time: O(n log n) — two O(n) traversals plus an O(n log n) sort.
- Space: O(n) — the `values` vector holds every node's value.
