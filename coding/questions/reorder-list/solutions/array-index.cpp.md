A singly linked list can only be walked forward, but the target pattern keeps needing the *last* remaining node — something you can't reach without either reversing part of the list or giving yourself random access. The easiest way to get random access is to record every node pointer in a plain vector first.

Once the nodes sit in an indexable vector, run two indices toward each other from both ends, splicing `next` pointers to alternate front, back, front, back, until they meet in the middle.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* reorderList(ListNode* head) {
        if (head == nullptr) return head;
        vector<ListNode*> nodes;
        for (ListNode* node = head; node != nullptr; node = node->next) nodes.push_back(node);
        int lo = 0, hi = static_cast<int>(nodes.size()) - 1;
        while (lo < hi) {
            nodes[lo]->next = nodes[hi];
            ++lo;
            if (lo == hi) break;
            nodes[hi]->next = nodes[lo];
            --hi;
        }
        nodes[lo]->next = nullptr;
        return head;
    }
};
```

## Why it works

The desired order `L0, Ln-1, L1, Ln-2, …` is just "take from the front, then from the back, repeat" — exactly what a converging pair of indices over a vector produces. Writing `nodes[lo]->next = nodes[hi]` then `nodes[hi]->next = nodes[lo]` stitches each pair together before the indices step inward. The loop stops the instant the two indices meet or cross, and the last node visited has its `next` forced to `nullptr` so the list doesn't loop back on itself.

## Complexity

- Time: O(n) — one pass to collect nodes, one pass to relink them.
- Space: O(n) — the vector stores a pointer to every node.
