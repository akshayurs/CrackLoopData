The safest way to reverse groups of k nodes without getting tangled in pointer edge cases is to sidestep pointer surgery entirely: read every node's value into a list, do the reversing there where indexing is trivial, then walk the original list once more and overwrite each node's value from the rebuilt order.

Split the values into chunks of size k, reverse only the chunks that are exactly k long, and copy a shorter trailing chunk through unchanged — then write everything back into the existing nodes.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        List<Integer> vals = new ArrayList<>();
        for (ListNode node = head; node != null; node = node.next) {
            vals.add(node.val);
        }

        int fullGroups = (vals.size() / k) * k;
        List<Integer> rewritten = new ArrayList<>();
        for (int start = 0; start < fullGroups; start += k) {
            for (int i = start + k - 1; i >= start; i--) {
                rewritten.add(vals.get(i));
            }
        }
        for (int i = fullGroups; i < vals.size(); i++) {
            rewritten.add(vals.get(i));
        }

        ListNode node = head;
        for (int v : rewritten) {
            node.val = v;
            node = node.next;
        }
        return head;
    }
}
```

## Why it works

`fullGroups` rounds the node count down to the nearest multiple of `k`, so every window of `k` values taken before that point is safe to reverse in place; whatever sits past `fullGroups` is the too-short tail, appended unchanged. Concatenating the reversed windows with that untouched tail reproduces the exact node order the problem asks for, and writing those values back into the existing nodes — rather than allocating new ones — keeps `head` a valid reference to return.

## Complexity

- Time: O(n) — one pass to read values, one to rebuild the order, one to write them back.
- Space: O(n) — `vals` and `rewritten` each hold every node's value.
