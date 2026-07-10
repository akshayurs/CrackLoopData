The array trick works but spends O(n) extra memory just to get backward access. Notice instead that the target pattern is really "zip the first half with the *reversed* second half." If you physically reverse the back half of the list, both halves can then be walked forward and merged one node at a time — no auxiliary storage needed.

Three classic pointer techniques chain together: a slow/fast pointer pair finds the midpoint in one pass, an in-place reversal flips the second half, and a final interleaving pass alternates nodes from the two halves.

```python
def reorder_list(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    prev = None
    while second is not None:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev

    first = head
    while second is not None:
        first_next = first.next
        second_next = second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next

    return head
```

## Why it works

The slow/fast walk lands `slow` on the midpoint (biased toward the first half for odd lengths), splitting the list into a front half starting at `head` and a back half starting at `slow.next`. Reversing the back half turns `Ln-1, Ln-2, …` into forward order, matching exactly what the interleave needs next. The final loop alternates one node from each half, always saving both `next` pointers before overwriting them; it stops once the (shorter or equal) reversed half is exhausted, leaving the front half's tail correctly pointing at `None`.

## Complexity

- Time: O(n) — the midpoint search, reversal, and merge are each a single pass.
- Space: O(1) — only a fixed number of pointers are used.
