You can decide the question with no extra memory by racing two pointers at different speeds — Floyd's tortoise-and-hare. The slow pointer advances one node per step; the fast pointer advances two. If the list has an end, the fast pointer walks off it into `null`. If the list has a cycle, the fast pointer laps the slow pointer and the two references become equal.

The intuition is two runners on a track: on a straight road the faster one just finishes, but on a circular track the faster one inevitably catches the slower from behind.

```java
class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
```

## Why it works

If no cycle exists, `fast` or `fast.next` becomes `null` and the loop returns `false`. If a cycle exists, both pointers eventually run inside it and the fast pointer closes the gap to the slow pointer by one node each step; the gap shrinks to zero and `slow == fast` holds, returning `true`. Since the gap changes by exactly one per step, the pointers must meet rather than skip past each other.

## Complexity

- Time: O(n) — the pointers meet within a constant factor of one traversal.
- Space: O(1) — only two references.
