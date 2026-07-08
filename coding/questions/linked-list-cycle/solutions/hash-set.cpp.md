The most direct idea is to remember every node you have already visited. Walk the list and insert each node pointer into an `unordered_set` before moving on. If a pointer is already present, you have returned to a node you saw earlier — a cycle. If the walk reaches `nullptr`, the list has an end and therefore no cycle.

The set stores raw `ListNode*` pointers, so identity is the address of the node; two distinct nodes with equal values remain distinct entries.

```cpp
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> seen;
        while (head) {
            if (seen.count(head)) return true;
            seen.insert(head);
            head = head->next;
        }
        return false;
    }
};
```

## Why it works

Without a cycle, each node is inserted once and the loop ends at `nullptr`, returning `false`. With a cycle, `nullptr` is unreachable; since the node count is finite, some pointer is encountered twice and `seen.count` returns nonzero, giving `true`. Hashing pointer addresses makes identity exact regardless of stored values.

## Complexity

- Time: O(n) — each node is visited at most once.
- Space: O(n) — the set can hold every node pointer.
