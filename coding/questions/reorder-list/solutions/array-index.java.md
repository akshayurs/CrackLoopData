The reordering weaves nodes from the two ends toward the middle, but a singly linked list only lets you walk forward — you can't step backward to reach `Ln`. The simplest fix is to give up random access to the nodes by first dumping them into a list.

Once every node sits in an indexable list, keep a `left` pointer at the front and a `right` pointer at the back. Alternately relink `nodes.get(left)` then `nodes.get(right)`, moving the pointers inward until they meet.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public ListNode reorderList(ListNode head) {
        if (head == null) return head;
        List<ListNode> nodes = new ArrayList<>();
        for (ListNode cur = head; cur != null; cur = cur.next) nodes.add(cur);
        int left = 0, right = nodes.size() - 1;
        while (left < right) {
            nodes.get(left).next = nodes.get(right);
            left++;
            if (left == right) break;
            nodes.get(right).next = nodes.get(left);
            right--;
        }
        nodes.get(left).next = null;
        return head;
    }
}
```

## Why it works

The target order `L0, Ln, L1, Ln-1, …` is exactly "front, back, next-front, next-back, …". Storing nodes in a list gives O(1) access to both ends, so the two-pointer sweep emits them in that order. The final node written gets its `next` set to `null` to terminate the list and avoid a cycle.

## Complexity

- Time: O(n) — one pass to collect, one pass to rewire.
- Space: O(n) — the list holds a reference to every node.
