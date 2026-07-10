Skip the hash map by hiding each copy right next to its original. For every node `A -> B -> C`, splice in a copy of each so the list becomes `A -> A' -> B -> B' -> C -> C'`. Now every original node's immediate neighbor *is* its own copy, so `original->random->next` is exactly the copy of whatever `original->random` pointed to — no lookup table required.

Once every copy's `random` pointer is set using that trick, a final pass un-weaves the two lists: it restores each original node's `next` to skip over the inserted copy, while stitching the copies together into their own standalone list.

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        Node* curr = head;
        while (curr != nullptr) {
            Node* copy = new Node(curr->val);
            copy->next = curr->next;
            curr->next = copy;
            curr = copy->next;
        }
        curr = head;
        while (curr != nullptr) {
            if (curr->random != nullptr) curr->next->random = curr->random->next;
            curr = curr->next->next;
        }
        Node dummy(0);
        Node* copyCurr = &dummy;
        curr = head;
        while (curr != nullptr) {
            copyCurr->next = curr->next;
            curr->next = curr->next->next;
            curr = curr->next;
            copyCurr = copyCurr->next;
        }
        return dummy.next;
    }
};
```

## Why it works

Interleaving guarantees `curr->next` is always `curr`'s own copy, so `curr->random->next` is always the copy of `curr->random` — that single expression replaces the hash map lookup entirely. The final pass then peels the two lists apart: `curr->next = curr->next->next` restores the original list's shape, and `copyCurr->next = curr->next` (read before that restoration) links the copies to each other in the same order.

## Complexity

- Time: O(n) — three linear passes over the list.
- Space: O(1) — beyond the output list, only a handful of pointers are used.
