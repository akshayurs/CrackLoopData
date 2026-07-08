The reordering weaves nodes from the two ends toward the middle, but a singly linked list only lets you walk forward — you can't step backward to reach `Ln`. The simplest fix is to give up random access to the nodes by first dumping their pointers into a vector.

Once every node sits in an indexable vector, keep a `left` index at the front and a `right` index at the back. Alternately relink `nodes[left]` then `nodes[right]`, moving the indices inward until they meet.

```cpp
#include <vector>

class Solution {
public:
    ListNode* reorderList(ListNode* head) {
        if (head == nullptr) return head;
        std::vector<ListNode*> nodes;
        for (ListNode* cur = head; cur != nullptr; cur = cur->next) nodes.push_back(cur);
        int left = 0, right = static_cast<int>(nodes.size()) - 1;
        while (left < right) {
            nodes[left]->next = nodes[right];
            ++left;
            if (left == right) break;
            nodes[right]->next = nodes[left];
            --right;
        }
        nodes[left]->next = nullptr;
        return head;
    }
};
```

## Why it works

The target order `L0, Ln, L1, Ln-1, …` is exactly "front, back, next-front, next-back, …". Storing node pointers in a vector gives O(1) access to both ends, so the two-pointer sweep emits them in that order. The final node written gets its `next` set to `nullptr` to terminate the list and avoid a cycle.

## Complexity

- Time: O(n) — one pass to collect, one pass to rewire.
- Space: O(n) — the vector holds a pointer to every node.
