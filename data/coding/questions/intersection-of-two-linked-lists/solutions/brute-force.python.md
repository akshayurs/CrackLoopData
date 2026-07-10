The most literal reading of "shared node": for every node in `listA`, scan the whole of `listB` and ask whether any node there is the *exact same object*. The first time you find a match, that's the intersection.

This never has to reason about lengths or offsets, but it pays for that simplicity by re-walking `listB` once per node of `listA`. Comparing with `is` (not `==`) matters — it checks identity, so two different nodes carrying the same `val` are correctly treated as unrelated.

```python
def get_intersection_node(head_a, head_b):
    node_a = head_a
    while node_a:
        node_b = head_b
        while node_b:
            if node_a is node_b:
                return node_a
            node_b = node_b.next
        node_a = node_a.next
    return None
```

## Why it works

The outer loop visits every node of `listA` exactly once; for each one, the inner loop checks every node of `listB` for identity equality. If the two lists ever share a node, that node will eventually be compared against itself and `is` will report a match — and because sharing one node means sharing the entire tail, the first match found is the intersection point closest to both heads.

## Complexity

- Time: O(m * n) — every node of `listA` is compared against every node of `listB`.
- Space: O(1) — only a couple of traversal pointers.
