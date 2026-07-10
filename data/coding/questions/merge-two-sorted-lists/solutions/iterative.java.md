Instead of recursing, walk both lists with two pointers and build the merged list by hand. A dummy sentinel node in front of the result avoids special-casing the first node — you always have a `tail` to attach onto.

At each step, compare the two current nodes, splice the smaller one onto `tail`, and advance that list's pointer. When one list runs out, the other is already sorted, so its remaining nodes are attached in one shot.

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        tail.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
```

## Why it works

`tail` always points at the last node placed in the result, so `tail.next = <smaller node>` extends the list in O(1). The loop only runs while both lists still have nodes, so the moment either is exhausted, the other holds a sorted suffix that can be linked directly — no need to walk it node by node. The dummy head removes the need to track a separate "head" variable during construction.

## Complexity

- Time: O(m + n) — each node from both lists is visited once.
- Space: O(1) — only pointers are used; nodes are relinked, not copied.
