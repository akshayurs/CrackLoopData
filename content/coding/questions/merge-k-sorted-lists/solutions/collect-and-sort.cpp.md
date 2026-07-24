Forget that the individual lists are sorted at all — walk every list, dump every value into one flat vector, sort it, then rebuild a brand-new list from the sorted values. It ignores the structure you're handed, but it's the fastest thing to reason about correctly.

Because the original nodes are discarded during traversal (only their `val` is kept), the final list is built out of fresh nodes rather than the input's own nodes.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        std::vector<int> values;
        for (ListNode* node : lists) {
            while (node != nullptr) {
                values.push_back(node->val);
                node = node->next;
            }
        }
        std::sort(values.begin(), values.end());

        ListNode dummy(0);
        ListNode* tail = &dummy;
        for (int v : values) {
            tail->next = new ListNode(v);
            tail = tail->next;
        }
        return dummy.next;
    }
};
```

## Why it works

`values` ends up holding every node's value exactly once, regardless of which list it came from. Sorting that flat vector produces the required non-decreasing order directly. The final loop then lays down one fresh node per value in that order — since the vector is already sorted, no comparisons are needed while rebuilding.

## Complexity

- Time: O(N log N) — N is the total number of nodes; dominated by the sort.
- Space: O(N) — the values vector plus N freshly allocated result nodes.
