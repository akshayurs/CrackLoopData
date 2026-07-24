When many queries share the same `t`, the linear scan re-reads all of `t` every time — wasteful. Instead, preprocess `t` once into a map from each character to the sorted list of positions where it occurs. Then a query only touches positions relevant to `s`.

For each character of `s`, we need the earliest occurrence in `t` that comes *after* the position we matched last. Since each character's positions are sorted, a binary search (upper bound of the previous index) finds it in logarithmic time. If any character has no such later position, `s` cannot be embedded.

```python
from bisect import bisect_right

def is_subsequence(s, t):
    positions = {}
    for i, c in enumerate(t):
        positions.setdefault(c, []).append(i)
    prev = -1
    for c in s:
        idxs = positions.get(c)
        if idxs is None:
            return False
        j = bisect_right(idxs, prev)
        if j == len(idxs):
            return False
        prev = idxs[j]
    return True
```

## Why it works

`positions[c]` lists, in increasing order, every index of `c` in `t`. Maintaining `prev` (the index we last consumed), the next character must land at some index strictly greater than `prev`; `bisect_right(idxs, prev)` returns exactly the first such slot. Advancing to the smallest valid index is the greedy choice — the same reasoning as the two-pointer scan — so it never rejects an embeddable string. Missing character or exhausted positions means no valid match remains.

## Complexity

- Time: O(n + m·log n) — building the index over `t` (length n), then each of the m = len(s) characters does one binary search.
- Space: O(n) — every position of `t` is stored once.
