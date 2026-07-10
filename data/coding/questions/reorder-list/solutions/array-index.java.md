A singly linked list can only be walked forward, but the target pattern keeps needing the *last* remaining node — something you can't reach without either reversing part of the list or giving yourself random access. The easiest way to get random access is to record every node in a plain list first.

Once the nodes sit in an indexable list, run two indices toward each other from both ends, splicing `next` pointers to alternate front, back, front, back, until they meet in the middle.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public ListNode reorderList(ListNode head) {
        if (head == null) return head;
        List<ListNode> nodes = new ArrayList<>();
        for (ListNode node = head; node != null; node = node.next) nodes.add(node);
        int lo = 0, hi = nodes.size() - 1;
        while (lo < hi) {
            nodes.get(lo).next = nodes.get(hi);
            lo++;
            if (lo == hi) break;
            nodes.get(hi).next = nodes.get(lo);
            hi--;
        }
        nodes.get(lo).next = null;
        return head;
    }
}
```

## Why it works

The desired order `L0, Ln-1, L1, Ln-2, …` is just "take from the front, then from the back, repeat" — exactly what a converging pair of indices over a list produces. Writing `nodes.get(lo).next = nodes.get(hi)` then `nodes.get(hi).next = nodes.get(lo)` stitches each pair together before the indices step inward. The loop stops the instant the two indices meet or cross, and the last node visited has its `next` forced to `null` so the list doesn't loop back on itself.

## Complexity

- Time: O(n) — one pass to collect nodes, one pass to relink them.
- Space: O(n) — the list stores a reference to every node.
