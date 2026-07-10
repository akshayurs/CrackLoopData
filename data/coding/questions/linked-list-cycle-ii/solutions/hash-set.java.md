The most direct way to find a repeated node is to remember every node you've already visited. Walk the list one node at a time, and the instant you land on a node you've seen before, that node is where the cycle begins — nothing later in the chain could have looped back earlier than that.

If you fall off the end (`next` becomes `null`) without ever revisiting a node, the list has no cycle.

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> seen = new HashSet<>();
        ListNode node = head;
        while (node != null) {
            if (seen.contains(node)) {
                return node;
            }
            seen.add(node);
            node = node.next;
        }
        return null;
    }
}
```

## Why it works

Each node is added to `seen` the first time it's reached. Because a singly linked list only ever has one `next` pointer per node, the first node found already in `seen` must be the one where some later node's pointer loops back to it — by definition, the start of the cycle. A list with no cycle simply terminates at `null` before any repeat occurs.

## Complexity

- Time: O(n) — each node is visited once.
- Space: O(n) — the set can hold every node.
