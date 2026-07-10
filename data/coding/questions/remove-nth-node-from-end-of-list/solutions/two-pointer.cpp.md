Counting the length first means touching every node twice. You can get away with one full pass by opening up a gap of `n` nodes between two pointers: advance a `fast` pointer `n` steps ahead of a `slow` one, then move both forward together. When `fast` runs off the end, `slow` is sitting exactly one node before the target — because the gap between them was fixed at `n` the whole time.

A dummy node before `head` keeps the "node before the target" idea valid even when the target is the head itself, so there's no separate case to handle.

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode* fast = &dummy;
        ListNode* slow = &dummy;

        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }

        while (fast->next != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        slow->next = slow->next->next;
        return dummy.next;
    }
};
```

## Why it works

After the head start, `fast` is always exactly `n` nodes ahead of `slow`. When `fast` reaches the last node (`fast->next == nullptr`), `slow` must be `n` nodes behind the last node — i.e. one node before the node that is `n`th from the end. Relinking `slow->next` removes that node in a single traversal, and `dummy.next` is returned so removing the original head needs no special-casing.

## Complexity

- Time: O(L) — a single pass over the list.
- Space: O(1) — two pointers and a stack-allocated dummy node, independent of list length.
