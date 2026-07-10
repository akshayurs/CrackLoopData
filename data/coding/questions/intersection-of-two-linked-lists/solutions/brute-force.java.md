The same idea in Java: for every node of `listA`, walk the whole of `listB` looking for the identical object reference. `==` on objects checks identity, which is exactly what's needed here.

```java
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        for (ListNode nodeA = headA; nodeA != null; nodeA = nodeA.next) {
            for (ListNode nodeB = headB; nodeB != null; nodeB = nodeB.next) {
                if (nodeA == nodeB) {
                    return nodeA;
                }
            }
        }
        return null;
    }
}
```

## Why it works

The outer loop visits every node of `listA` exactly once; for each one, the inner loop checks every node of `listB` for reference equality via `==`. If the two lists ever share a node, that node will eventually be compared against itself and the check succeeds — and because sharing one node means sharing the entire tail, the first match found is the intersection point closest to both heads.

## Complexity

- Time: O(m * n) — every node of `listA` is compared against every node of `listB`.
- Space: O(1) — only the two loop pointers.
