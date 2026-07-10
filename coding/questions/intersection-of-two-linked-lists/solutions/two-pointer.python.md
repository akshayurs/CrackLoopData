The reason the brute force is slow is that it never accounts for the two lists possibly being different lengths — that mismatch is what forces it to keep re-scanning. Fix the length difference instead of comparing every pair.

Walk two pointers forward one step at a time, one starting at `head_a` and the other at `head_b`. Whenever a pointer runs off the end of its own list, redirect it to the *other* list's head instead of stopping. After at most one such switch each, both pointers will have traveled `len(A) + len(B)` steps in total by the time they reach the intersection — so they arrive there in lockstep, whether or not the lists share a node.

```python
def get_intersection_node(head_a, head_b):
    pointer_a = head_a
    pointer_b = head_b

    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next if pointer_a else head_b
        pointer_b = pointer_b.next if pointer_b else head_a

    return pointer_a
```

## Why it works

Let the unique prefix of `listA` have length `a` and the unique prefix of `listB` have length `b`, with a shared tail after that. `pointer_a` travels `a + shared + b` nodes by the time it finishes its second pass through the combined path, and `pointer_b` travels `b + shared + a` — the same total distance. Because both pointers cover an equal number of steps before reaching the shared tail, they land on the same node at the same time: the intersection, if one exists. If the lists never intersect, both pointers become `None` simultaneously after covering `a + b` steps each, and the loop ends with `pointer_a` equal to `None`.

## Complexity

- Time: O(m + n) — each pointer traverses at most one full pass of each list.
- Space: O(1) — two pointers, no auxiliary storage.
