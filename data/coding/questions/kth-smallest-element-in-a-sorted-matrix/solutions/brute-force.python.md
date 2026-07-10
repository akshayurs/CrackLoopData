The simplest thing that works: forget the matrix structure entirely. Every value is a candidate, so collect them all into one flat list, sort it, and index into position `k`.

This throws away the sortedness of the rows and columns, but it's a correct baseline and easy to reason about — a good place to start before optimizing.

```python
def kth_smallest(matrix, k):
    flat = [value for row in matrix for value in row]
    flat.sort()
    return flat[k - 1]
```

## Why it works

Flattening gathers all n² values, and sorting puts them in ascending order including duplicates. The `k`th smallest in overall order is then simply the element at zero-based index `k - 1`.

## Complexity

- Time: O(n² log n) — sorting n² values dominates.
- Space: O(n²) — the flattened list holds every value.
