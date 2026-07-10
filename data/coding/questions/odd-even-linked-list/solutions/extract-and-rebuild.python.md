The regrouping is really just a stable partition of the nodes by position. If you collect every node into a plain list first, splitting it into "odd-indexed" and "even-indexed" slices is trivial slicing, and relinking the two runs back-to-back is a single pass over the combined order.

This trades the elegance of in-place pointer surgery for something easy to reason about: build the target order explicitly, then wire `next` pointers to match it.

```python
def odd_even_list(head):
    if not head:
        return head
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    ordered = nodes[0::2] + nodes[1::2]
    for i in range(len(ordered) - 1):
        ordered[i].next = ordered[i + 1]
    ordered[-1].next = None
    return ordered[0]
```

## Why it works

`nodes[0::2]` picks up every node at an odd position (0-indexed 0, 2, 4, ...) in the order they appeared, and `nodes[1::2]` does the same for even positions — concatenating them produces exactly the required ordering. Relinking `ordered[i].next = ordered[i + 1]` for consecutive entries reproduces that order as an actual list, and setting the last node's `next` to `None` closes it off cleanly.

## Complexity

- Time: O(n) — one pass to collect nodes, one to relink them.
- Space: O(n) — the `nodes` and `ordered` lists hold a pointer per node.
