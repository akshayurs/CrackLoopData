Split the problem into two clean passes joined by a lookup table. In the first pass, walk the original list and create a brand-new node for every original node — same value, pointers left blank for now — while recording `old node -> new node` in a `HashMap`. By the time this pass finishes, every original node already has a twin waiting in the map.

In the second pass, walk the original list again and wire up the copies: a copy's `next` is the map's entry for the original's `next`, and its `random` is the map's entry for the original's `random`. Looking up `null` in the map naturally yields `null`, so nodes with no `random` pointer resolve correctly with no special-casing.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        Map<Node, Node> oldToNew = new HashMap<>();
        Node curr = head;
        while (curr != null) {
            oldToNew.put(curr, new Node(curr.val));
            curr = curr.next;
        }
        curr = head;
        while (curr != null) {
            oldToNew.get(curr).next = oldToNew.get(curr.next);
            oldToNew.get(curr).random = oldToNew.get(curr.random);
            curr = curr.next;
        }
        return oldToNew.get(head);
    }
}
```

## Why it works

The map guarantees every original node's copy already exists before any pointer needs to reference it, because all copies are created up front in the first pass. The second pass therefore only rewires pointers — it never has to fabricate a node mid-stitch, and it never accidentally points a copy back into the original list, since every pointer assignment goes through `oldToNew`.

## Complexity

- Time: O(n) — two linear passes over the list.
- Space: O(n) — the map holds one entry per node.
