Because every row's first element is larger than the previous row's last element, reading the matrix row by row produces one fully sorted array of `m·n` values. So you can run a single binary search over the *virtual* index range `0 .. m·n - 1`, converting a flat index back to a `(row, col)` pair on the fly with divide and modulo. No extra memory is needed — the matrix is never actually flattened.

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int rows = matrix.length, cols = matrix[0].length;
        int lo = 0, hi = rows * cols - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            int value = matrix[mid / cols][mid % cols];
            if (value == target) {
                return true;
            }
            if (value < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return false;
    }
}
```

## Why it works

Flat index `k` maps to `matrix[k / cols][k % cols]`, and thanks to the row-boundary guarantee this mapping enumerates the values in sorted order. A standard binary search on `[0, m·n - 1]` therefore behaves exactly as it would on a sorted 1D array, halving the search space each step until the target is found or the range empties.

## Complexity

- Time: O(log(m·n)) — one binary search over all cells.
- Space: O(1) — only index arithmetic, no flattening.
