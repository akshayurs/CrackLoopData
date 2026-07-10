The same trick in Java: two pointers advance one node at a time, and each one hops to the other list's head the moment it falls off its own list. Because that hop happens at most once per pointer, both pointers cover the same total distance — `lenA + lenB` — before they either meet at the intersection or both become `null` together.

```java
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pointerA = headA;
        ListNode pointerB = headB;

        while (pointerA != pointerB) {
            pointerA = (pointerA != null) ? pointerA.next : headB;
            pointerB = (pointerB != null) ? pointerB.next : headA;
        }

        return pointerA;
    }
}
```

## Why it works

Let the unique prefix of `listA` have length `a` and the unique prefix of `listB` have length `b`, with a shared tail after that. `pointerA` travels `a + shared + b` nodes by the time it finishes its second pass through the combined path, and `pointerB` travels `b + shared + a` — the same total distance. Covering an equal number of steps before reaching the shared tail means the two pointers land on the same node at the same time: the intersection, if one exists. If the lists never intersect, both pointers become `null` together after `a + b` steps each, and the loop exits with `pointerA` equal to `null`.

## Complexity

- Time: O(m + n) — each pointer traverses at most one full pass of each list.
- Space: O(1) — two pointers, no auxiliary storage.
