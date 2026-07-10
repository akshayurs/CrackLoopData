A singly linked list can only be walked forward, but the target pattern keeps needing the *last* remaining node — something you can't reach without either reversing part of the list or giving yourself random access. The easiest way to get random access is to record every node in a plain list first.

Once the nodes sit in an indexable array, run two indices toward each other from both ends, splicing `next` pointers to alternate front, back, front, back, until they meet in the middle.

```python
def reorder_list(head):
    if head is None:
        return head
    nodes = []
    node = head
    while node is not None:
        nodes.append(node)
        node = node.next
    lo, hi = 0, len(nodes) - 1
    while lo < hi:
        nodes[lo].next = nodes[hi]
        lo += 1
        if lo == hi:
            break
        nodes[hi].next = nodes[lo]
        hi -= 1
    nodes[lo].next = None
    return head
```

## Why it works

The desired order `L0, Ln-1, L1, Ln-2, …` is just "take from the front, then from the back, repeat" — exactly what a converging pair of indices over an array produces. Writing `nodes[lo].next = nodes[hi]` then `nodes[hi].next = nodes[lo]` stitches each pair together before the indices step inward. The loop stops the instant the two indices meet or cross, and the last node visited has its `next` forced to `None` so the list doesn't loop back on itself.

## Complexity

- Time: O(n) — one pass to collect nodes, one pass to relink them.
- Space: O(n) — the array stores a reference to every node.
