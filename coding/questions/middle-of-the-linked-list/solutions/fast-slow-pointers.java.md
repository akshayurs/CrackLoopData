You don't need to know the length up front if two pointers move at different speeds through the list at the same time. Send a `slow` pointer forward one node per step and a `fast` pointer forward two nodes per step; when `fast` runs off the end, `slow` has covered exactly half the distance and is sitting on the middle.

Starting `fast` at `head` (not `head.next`) is what makes the second-middle tie-break fall out naturally for even-length lists — no separate case needed.

```java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
```

## Why it works

Each loop iteration advances `slow` by one node and `fast` by two, so `fast` is always exactly twice as far from `head` as `slow`. The loop stops as soon as `fast` reaches the last node or falls past the end, which happens after `slow` has taken `length / 2` steps — landing it on the middle (the second one, when there are two).

## Complexity

- Time: O(n) — a single pass; `fast` reaches the end after roughly n/2 iterations.
- Space: O(1) — just the two pointers.
