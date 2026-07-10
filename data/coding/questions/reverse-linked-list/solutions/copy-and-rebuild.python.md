The most literal reading of "reversed" is: read off every value, then lay them back down in the opposite order. Walk the list once to copy each `val` into a plain array, then walk that array back to front, wiring up a brand-new chain of nodes as you go.

This sidesteps any pointer-rewiring puzzle entirely — the trade-off is that it throws away the original nodes and pays for a second array plus a full set of new nodes.

```python
def reverse_list(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next

    dummy = ListNode()
    tail = dummy
    for v in reversed(values):
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next
```

## Why it works

The first loop records the sequence of values in their original order. Iterating that array with `reversed()` visits them tail-first, so appending a fresh node for each one, in that order, reconstructs the exact mirror image of the input. The `dummy` node just avoids special-casing the very first append.

## Complexity

- Time: O(n) — one pass to read the values, one pass to rebuild.
- Space: O(n) — the values array plus n freshly allocated nodes.
