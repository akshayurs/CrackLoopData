Because every row's first element is larger than the previous row's last element, reading the matrix row by row produces one fully sorted array of `m·n` values. So you can run a single binary search over the *virtual* index range `0 .. m·n - 1`, converting a flat index back to a `(row, col)` pair on the fly with divide and modulo. No extra memory is needed — the matrix is never actually flattened.

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        if value < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
```

## Why it works

Flat index `k` maps to `matrix[k // cols][k % cols]`, and thanks to the row-boundary guarantee this mapping enumerates the values in sorted order. A standard binary search on `[0, m·n - 1]` therefore behaves exactly as it would on a sorted 1D array, halving the search space each step until the target is found or the range empties.

## Complexity

- Time: O(log(m·n)) — one binary search over all cells.
- Space: O(1) — only index arithmetic, no flattening.
