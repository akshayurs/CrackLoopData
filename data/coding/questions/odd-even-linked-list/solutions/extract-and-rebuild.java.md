The regrouping is really just a stable partition of the nodes by position. Collecting every node into a list first turns "split by odd/even position" into simple index arithmetic, and relinking the two runs back-to-back is one pass over the combined order.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;
        List<ListNode> nodes = new ArrayList<>();
        for (ListNode node = head; node != null; node = node.next) {
            nodes.add(node);
        }
        List<ListNode> ordered = new ArrayList<>();
        for (int i = 0; i < nodes.size(); i += 2) ordered.add(nodes.get(i));
        for (int i = 1; i < nodes.size(); i += 2) ordered.add(nodes.get(i));
        for (int i = 0; i < ordered.size() - 1; i++) {
            ordered.get(i).next = ordered.get(i + 1);
        }
        ordered.get(ordered.size() - 1).next = null;
        return ordered.get(0);
    }
}
```

## Why it works

The first loop over `nodes` (stepping by two, starting at index 0) collects every odd-position node in order; the second collects every even-position node. Appending the second run after the first gives exactly the required order, and relinking consecutive entries turns that order into an actual list, with the last node's `next` cleared.

## Complexity

- Time: O(n) — one pass to collect nodes, one to relink them.
- Space: O(n) — `nodes` and `ordered` each hold a reference per node.
