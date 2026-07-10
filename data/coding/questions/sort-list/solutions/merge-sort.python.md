Merge sort fits a linked list better than an array does — splitting off the front half needs no copying, just cutting one `next` link, and merging two sorted lists is pure pointer splicing. Use a slow/fast pointer pair to find the midpoint, cut the list into two halves there, recursively sort each half, and merge the two sorted results.

A list with zero or one node is already sorted, so that is the base case the recursion bottoms out at.

```python
def sort_list(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)

    dummy = ListNode(0)
    tail = dummy
    while left and right:
        if left.val <= right.val:
            tail.next, left = left, left.next
        else:
            tail.next, right = right, right.next
        tail = tail.next
    tail.next = left if left else right

    return dummy.next
```

## Why it works

`fast` moves twice as fast as `slow` and starts one node ahead, so when `fast` runs out, `slow` sits just before the true midpoint — cutting after `slow` always splits the list into two halves of size ⌈n/2⌉ and ⌊n/2⌋, which guarantees the recursion terminates. Each half is sorted independently down to the single-node base case, then the merge step (identical to merging two sorted lists) recombines them while preserving order. Doing this at every level of the recursion sorts the whole list.

## Complexity

- Time: O(n log n) — log n levels of splitting, each doing O(n) total work to merge.
- Space: O(log n) — the recursion stack depth, not counting the input/output list itself.
