The recursive version is elegant but pays for a stack frame per node. The iterative fix is a classic trick: attach a dummy node in front of `head` so the real head can be deleted the same way as any other node, then walk the list with a `prev`/`curr` pair, splicing out matches in place.

Because `prev` always points at the last node kept so far, deleting `curr` is just a pointer rewrite — no recursion, constant extra memory.

```java
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        ListNode curr = head;
        while (curr != null) {
            if (curr.val == val) {
                prev.next = curr.next;
            } else {
                prev = curr;
            }
            curr = curr.next;
        }
        return dummy.next;
    }
}
```

## Why it works

The dummy node removes the special case of deleting the head — `prev` is never `null`, so `prev.next = curr.next` always works, including when the first node itself must go. `prev` only advances when the current node is kept, so it always trails the most recent surviving node, and `curr` advances every iteration regardless, guaranteeing termination after one full pass.

## Complexity

- Time: O(n) — a single pass over the list.
- Space: O(1) — only a fixed number of pointers, no recursion stack.
