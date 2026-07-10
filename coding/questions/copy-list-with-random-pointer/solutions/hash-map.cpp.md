Split the problem into two clean passes joined by a lookup table. In the first pass, walk the original list and create a brand-new node for every original node — same value, pointers left blank for now — while recording `old node -> new node` in an `unordered_map`. By the time this pass finishes, every original node already has a twin waiting in the map.

In the second pass, walk the original list again and wire up the copies: a copy's `next` is the map's entry for the original's `next`, and its `random` is the map's entry for the original's `random`. A `nullptr` original pointer maps back to `nullptr`, so nodes with no `random` pointer resolve correctly with no special-casing.

```cpp
#include <unordered_map>
using namespace std;

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        unordered_map<Node*, Node*> oldToNew;
        oldToNew[nullptr] = nullptr;
        Node* curr = head;
        while (curr != nullptr) {
            oldToNew[curr] = new Node(curr->val);
            curr = curr->next;
        }
        curr = head;
        while (curr != nullptr) {
            oldToNew[curr]->next = oldToNew[curr->next];
            oldToNew[curr]->random = oldToNew[curr->random];
            curr = curr->next;
        }
        return oldToNew[head];
    }
};
```

## Why it works

The map guarantees every original node's copy already exists before any pointer needs to reference it, because all copies are created up front in the first pass. Seeding `oldToNew[nullptr] = nullptr` lets the second pass look up `next`/`random` without branching on whether they are null. The pass then only rewires pointers — it never fabricates a node mid-stitch, and every pointer assignment goes through `oldToNew`, so no copy ever points back into the original list.

## Complexity

- Time: O(n) — two linear passes over the list.
- Space: O(n) — the map holds one entry per node.
