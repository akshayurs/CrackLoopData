You can decide the question with no extra memory by racing two pointers at different speeds — Floyd's tortoise-and-hare. The slow pointer moves one node per step; the fast pointer moves two. If the list terminates, the fast pointer reaches `nullptr`. If the list contains a cycle, the fast pointer keeps looping and eventually points at the same node as the slow pointer.

Imagine two runners on a track: on a straight road the faster one finishes and leaves, but on a circular track the faster one always laps and meets the slower.

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};
```

## Why it works

With no cycle, `fast` or `fast->next` becomes `nullptr` and the loop returns `false`. With a cycle, both pointers enter the loop and the fast pointer narrows the gap to the slow pointer by one node per step; the gap reaches zero, making `slow == fast` true and returning `true`. Because the gap decreases by exactly one each step, the pointers are guaranteed to coincide.

## Complexity

- Time: O(n) — a constant number of passes over the list.
- Space: O(1) — two pointers only.
