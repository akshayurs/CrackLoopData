The most literal reading of "reversed" is: read off every value, then lay them back down in the opposite order. Walk the list once to copy each `val` into a `vector`, then walk that vector back to front, wiring up a brand-new chain of nodes as you go.

This sidesteps any pointer-rewiring puzzle entirely — the trade-off is that it throws away the original nodes and pays for a second vector plus a full set of new nodes.

```cpp
#include <vector>

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        std::vector<int> values;
        for (ListNode* node = head; node != nullptr; node = node->next) {
            values.push_back(node->val);
        }

        ListNode dummy(0);
        ListNode* tail = &dummy;
        for (int i = (int)values.size() - 1; i >= 0; i--) {
            tail->next = new ListNode(values[i]);
            tail = tail->next;
        }
        return dummy.next;
    }
};
```

## Why it works

The first loop records the sequence of values in their original order. Walking the vector from its last index down to `0` visits them tail-first, so appending a fresh node for each one, in that order, reconstructs the exact mirror image of the input. The stack-allocated `dummy` just avoids special-casing the very first append.

## Complexity

- Time: O(n) — one pass to read the values, one pass to rebuild.
- Space: O(n) — the values vector plus n freshly allocated nodes.
