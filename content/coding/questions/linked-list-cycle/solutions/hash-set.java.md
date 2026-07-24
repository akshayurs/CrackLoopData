The most direct idea is to remember every node you have already visited. Walk the list and add each node to a `HashSet` before advancing. `HashSet.add` returns `false` when the element is already present, so a failed add is exactly the moment you have looped back to a node seen before — a cycle. Falling off the end into `null` means the list is acyclic.

The set stores `ListNode` references, so membership is decided by object identity rather than value; nodes carrying equal values are still treated as distinct.

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> seen = new HashSet<>();
        ListNode node = head;
        while (node != null) {
            if (!seen.add(node)) return true;
            node = node.next;
        }
        return false;
    }
}
```

## Why it works

An acyclic list is exhausted after each node is added once, so the loop ends at `null` and returns `false`. If a cycle exists, `null` is never reached; with finitely many nodes, some node is offered to the set twice, `add` returns `false`, and the method returns `true`. `HashSet` uses reference identity for these objects, so equal values never collide.

## Complexity

- Time: O(n) — each node is processed at most once.
- Space: O(n) — the set may hold every node.
