The most literal reading of "reversed" is: read off every value, then lay them back down in the opposite order. Walk the list once to copy each `val` into an `ArrayList`, then walk that list back to front, wiring up a brand-new chain of nodes as you go.

This sidesteps any pointer-rewiring puzzle entirely — the trade-off is that it throws away the original nodes and pays for a second collection plus a full set of new nodes.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public ListNode reverseList(ListNode head) {
        List<Integer> values = new ArrayList<>();
        ListNode node = head;
        while (node != null) {
            values.add(node.val);
            node = node.next;
        }

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        for (int i = values.size() - 1; i >= 0; i--) {
            tail.next = new ListNode(values.get(i));
            tail = tail.next;
        }
        return dummy.next;
    }
}
```

## Why it works

The first loop records the sequence of values in their original order. Iterating the list from its last index down to `0` visits them tail-first, so appending a fresh node for each one, in that order, reconstructs the exact mirror image of the input. The `dummy` node just avoids special-casing the very first append.

## Complexity

- Time: O(n) — one pass to read the values, one pass to rebuild.
- Space: O(n) — the values list plus n freshly allocated nodes.
