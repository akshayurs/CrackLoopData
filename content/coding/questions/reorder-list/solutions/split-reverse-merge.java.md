The array trick works but spends O(n) extra memory just to get backward access. Notice instead that the target pattern is really "zip the first half with the *reversed* second half." If you physically reverse the back half of the list, both halves can then be walked forward and merged one node at a time — no auxiliary storage needed.

Three classic pointer techniques chain together: a slow/fast pointer pair finds the midpoint in one pass, an in-place reversal flips the second half, and a final interleaving pass alternates nodes from the two halves.

```java
class Solution {
    public ListNode reorderList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode second = slow.next;
        slow.next = null;
        ListNode prev = null;
        while (second != null) {
            ListNode next = second.next;
            second.next = prev;
            prev = second;
            second = next;
        }
        second = prev;

        ListNode first = head;
        while (second != null) {
            ListNode firstNext = first.next;
            ListNode secondNext = second.next;
            first.next = second;
            second.next = firstNext;
            first = firstNext;
            second = secondNext;
        }

        return head;
    }
}
```

## Why it works

The slow/fast walk lands `slow` on the midpoint (biased toward the first half for odd lengths), splitting the list into a front half starting at `head` and a back half starting at `slow.next`. Reversing the back half turns `Ln-1, Ln-2, …` into forward order, matching exactly what the interleave needs next. The final loop alternates one node from each half, always saving both `next` pointers before overwriting them; it stops once the (shorter or equal) reversed half is exhausted, leaving the front half's tail correctly pointing at `null`.

## Complexity

- Time: O(n) — the midpoint search, reversal, and merge are each a single pass.
- Space: O(1) — only a fixed number of pointers are used.
