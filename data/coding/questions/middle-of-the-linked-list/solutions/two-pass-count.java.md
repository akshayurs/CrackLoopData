The most direct reading of "find the middle" is: figure out how many nodes there are, then walk exactly that far. Make one pass just to count the nodes, then make a second pass to step forward `length / 2` times — that lands you on the middle (or the second middle, for an even-length list).

This is easy to reason about but pays for two full traversals instead of one.

```java
class Solution {
    public ListNode middleNode(ListNode head) {
        int length = 0;
        ListNode node = head;
        while (node != null) {
            length++;
            node = node.next;
        }

        int steps = length / 2;
        node = head;
        for (int i = 0; i < steps; i++) {
            node = node.next;
        }
        return node;
    }
}
```

## Why it works

`length / 2` is the 0-indexed position of the middle node under the "return the second middle" rule: for length 5 it's index 2 (the 3rd node), and for length 6 it's index 3 (the 4th node) — exactly the second of the two middles. Walking that many `next` hops from `head` reaches it directly.

## Complexity

- Time: O(n) — two full passes over the list.
- Space: O(1) — a length counter and a couple of pointers.
