The simplest way to state "remove matching nodes" is recursively: fix the rest of the list first, then decide what to do with the current node. If the rest of the list is already clean, the current node just needs to point past itself when it matches, or keep pointing at the cleaned rest otherwise.

This mirrors how you would describe the problem in words, at the cost of one stack frame per node.

```java
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return null;
        }
        head.next = removeElements(head.next, val);
        return head.val == val ? head.next : head;
    }
}
```

## Why it works

The recursion bottoms out at `null`, which is already a valid (empty) cleaned list. Each call assumes `head.next` has already been fully cleaned by the recursive call, so it only has to judge the current node: skip it by returning `head.next`, or keep it by returning `head` itself. Every node is visited exactly once as the recursion unwinds.

## Complexity

- Time: O(n) — one recursive call per node.
- Space: O(n) — the call stack holds one frame per node.
