The simplest thing that works: forget the matrix structure entirely. Every value is a candidate, so collect them all into one flat array, sort it numerically, and index into position `k`.

This throws away the sortedness of the rows and columns, but it's a correct baseline and easy to reason about — a good place to start before optimizing.

```javascript
function kthSmallest(matrix, k) {
    const flat = matrix.flat();
    flat.sort((a, b) => a - b);
    return flat[k - 1];
}
```

## Why it works

`flat()` gathers all n² values into one array, and the numeric comparator sorts them ascending including duplicates. The `k`th smallest in overall order is then the element at zero-based index `k - 1`.

## Complexity

- Time: O(n² log n) — sorting n² values dominates.
- Space: O(n²) — the flattened array holds every value.
