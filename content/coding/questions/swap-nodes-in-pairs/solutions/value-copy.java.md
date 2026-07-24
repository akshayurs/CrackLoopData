The first instinct is to sidestep pointers entirely: read every node's value into a list, swap adjacent entries in that list, then walk the list a second time and write the swapped values back into the existing nodes.

It produces the right output sequence, but it quietly breaks the rule that only pointers may change — the nodes themselves keep their original identity while their `val` fields get overwritten. It's a useful warm-up because it separates "get the order right" from "rewire the structure correctly," which the optimal approach has to solve at the same time.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public ListNode swapPairs(ListNode head) {
        List<Integer> values = new ArrayList<>();
        for (ListNode node = head; node != null; node = node.next) {
            values.add(node.val);
        }

        for (int i = 0; i + 1 < values.size(); i += 2) {
            int tmp = values.get(i);
            values.set(i, values.get(i + 1));
            values.set(i + 1, tmp);
        }

        ListNode node = head;
        for (int v : values) {
            node.val = v;
            node = node.next;
        }

        return head;
    }
}
```

## Why it works

The first pass captures the list's values in order. Swapping each even-indexed entry with its neighbor reproduces the pairwise-swapped sequence without touching any pointers. The second pass streams those values back into the original nodes in order, so the list's length and node count are untouched — only what each node holds changes.

## Complexity

- Time: O(n) — two linear passes over the list.
- Space: O(n) — the values list holds every node's value.
