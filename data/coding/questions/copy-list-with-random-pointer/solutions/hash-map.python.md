Split the problem into two clean passes joined by a lookup table. In the first pass, walk the original list and create a brand-new node for every original node — same value, pointers left blank for now — while recording `old node -> new node` in a hash map. By the time this pass finishes, every original node already has a twin waiting in the map.

In the second pass, walk the original list again and wire up the copies: a copy's `next` is the map's entry for the original's `next`, and its `random` is the map's entry for the original's `random`. Looking up `None` in the map naturally yields `None` back, so nodes with no `random` pointer resolve correctly with no special-casing.

```python
def copy_random_list(head):
    if head is None:
        return None
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next
    return old_to_new[head]
```

## Why it works

The map guarantees every original node's copy already exists before any pointer needs to reference it, because all copies are created up front in the first pass. The second pass therefore only rewires pointers — it never has to fabricate a node mid-stitch, and it never accidentally points a copy back into the original list, since every pointer assignment goes through `old_to_new`.

## Complexity

- Time: O(n) — two linear passes over the list.
- Space: O(n) — the hash map holds one entry per node.
