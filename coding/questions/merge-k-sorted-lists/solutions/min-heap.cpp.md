Each of the k lists is already sorted, so the smallest value not yet placed in the answer is always sitting at the front of one of them. Keep the current front node of every list in a min-heap, keyed by value; the heap top is always the global minimum. Pop it, attach it to the result, and if the list it came from has more nodes, push its new front back in.

`std::priority_queue` is a max-heap by default, so a comparator that flips the usual order (`a->val > b->val`) turns it into a min-heap over the raw node pointers.

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp)> heap(cmp);
        for (ListNode* node : lists) {
            if (node != nullptr) heap.push(node);
        }

        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (!heap.empty()) {
            ListNode* node = heap.top();
            heap.pop();
            tail->next = node;
            tail = tail->next;
            if (node->next != nullptr) heap.push(node->next);
        }
        return dummy.next;
    }
};
```

## Why it works

At any point the heap holds at most one candidate node per still-active list — its unconsumed front — because each list is sorted, so that front is that list's smallest remaining value. The true global minimum across all lists must therefore be one of those fronts, which is exactly what the heap top gives you. Popping it and pushing its successor keeps the invariant true for the next round, and splicing the popped node directly onto `tail` reuses the original nodes instead of copying values.

## Complexity

- Time: O(N log k) — N total nodes, each causing one push and one pop on a heap of size at most k.
- Space: O(k) — the heap never holds more than one node per list.
