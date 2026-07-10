The array trick works but throws away the constant extra memory a real "in place" solution should use. The pointer-only version processes the list one group at a time: first walk exactly `k` nodes ahead to confirm a full group exists — if it doesn't, stop and leave the remainder untouched — then reverse that stretch by re-pointing `next` references the same way you'd reverse an entire linked list, just bounded to stop at the node after the group instead of `None`.

A dummy node placed before `head` gives the very first group a "previous group's tail" to attach to, just like every later group has. After each group is flipped, that tail pointer is re-linked to the new front of the group before moving on.

```python
def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        group_next = kth.next
        prev, curr = group_next, group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        new_group_prev = group_prev.next
        group_prev.next = kth
        group_prev = new_group_prev
```

## Why it works

Walking `k` steps ahead from `group_prev` before touching any pointer both locates the group's tail and confirms a full group of `k` nodes exists — if the walk runs off the end, the remaining nodes are already in valid order and `dummy.next` is the answer as-is. The inner loop is the same three-pointer trick used to reverse a whole list, just bounded to stop at `group_next` instead of `None`, so it only ever rewires the `k` nodes in the current group. Re-pointing `group_prev` to `kth` — the group's new front — stitches the just-reversed segment onto whatever came before it, and advancing `group_prev` to the old front (now the group's new tail) sets up the next iteration.

## Complexity

- Time: O(n) — every node is visited a constant number of times across the lookahead and the reversal.
- Space: O(1) — a fixed handful of pointers, regardless of `n` or `k`.
