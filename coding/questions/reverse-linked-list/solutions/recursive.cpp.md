Think recursively: if you could already reverse everything *after* the first node, you'd just need to make the second node point back to the first. So recurse to the end, get the new head of the reversed tail, then flip the single link between the current node and its successor.

The base case is a list of zero or one node — it is its own reverse, so hand it straight back and let the recursion unwind, fixing one pointer per return.

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode* newHead = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return newHead;
    }
};
```

## Why it works

`reverseList(head->next)` returns the head of the already-reversed remainder while `head->next` still refers to the node that was directly after `head` — now the tail of that reversed portion. Setting `head->next->next = head` appends the current node after it, and `head->next = nullptr` prevents a cycle (the old head becomes the new tail). `newHead` is unchanged as the stack unwinds, so the deepest node is returned all the way up.

## Complexity

- Time: O(n) — one call per node.
- Space: O(n) — the recursion stack is as deep as the list length.
