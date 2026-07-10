No copy is needed at all: the odd and even nodes are already interleaved in the list, so you can grow two chains — one for odd positions, one for even — by having each chain reach two nodes ahead and grab every other node as it passes. Once the even chain runs out, splice its head onto the tail of the odd chain.

```java
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;
        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }
        odd.next = evenHead;
        return head;
    }
}
```

## Why it works

At every step `odd.next` is pointed at the node two ahead (skipping the even node in between), and the same is done for `even`, so the two chains advance in lockstep while consuming the original list exactly once. The loop stops as soon as `even` (or `even.next`) is `null`, meaning every node has been assigned to one chain. Attaching `evenHead` to the end of the odd chain concatenates the two runs in the required order.

## Complexity

- Time: O(n) — each node's `next` pointer is rewritten once.
- Space: O(1) — only a few references are used; no extra list or nodes.
