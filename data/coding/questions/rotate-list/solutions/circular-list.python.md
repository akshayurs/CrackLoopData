There's no need to copy a single value: the nodes you already have are exactly the nodes you need, just cut at a different point. First find the length and the tail while walking the list once. Since rotating by the full length is a no-op, reduce `k` modulo the length — if that leaves `0`, the list is already in its final shape.

Otherwise, join the tail back to the head so the list becomes a ring. Walking forward `length - k - 1` steps from the head lands you exactly one node before the spot where the list should be cut; breaking the ring there produces the rotated list with its new head and tail already in place.

```python
def rotate_right(head, k):
    if not head or not head.next:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return head

    tail.next = head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
```

## Why it works

Closing the ring with `tail.next = head` lets a single walk of `length - k - 1` steps from the head reach the node that should become the new tail — the node `k` positions before the old tail. Everything after it, wrapping around through the old head, is the segment that belongs in front after rotation. Cutting `new_tail.next` there detaches that segment as the new list, whose first node (`new_head`) was previously the old head's neighbor `k` steps from the end.

## Complexity

- Time: O(n) — one pass to measure the list, one to find the new tail.
- Space: O(1) — the existing nodes are reused and only re-linked.
