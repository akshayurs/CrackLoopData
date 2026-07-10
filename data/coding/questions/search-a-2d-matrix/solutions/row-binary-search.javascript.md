Each row is sorted, so instead of scanning a row left to right you can binary search it in O(log n). Loop over the rows, and for any row whose range could contain the target (its first value ≤ target ≤ its last value), binary search that row. This keeps the code simple while cutting the per-row cost from linear to logarithmic.

```javascript
function searchMatrix(matrix, target) {
  for (const row of matrix) {
    if (row.length === 0 || target < row[0] || target > row[row.length - 1]) {
      continue;
    }
    let lo = 0;
    let hi = row.length - 1;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      if (row[mid] === target) {
        return true;
      }
      if (row[mid] < target) {
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }
  }
  return false;
}
```

## Why it works

A row can only hold the target if the target lies within `[row[0], row[row.length - 1]]`; rows outside that band are skipped in O(1). Inside a candidate row, standard binary search converges on the target or proves its absence. Because rows are disjoint ranges, at most one row is ever actually searched.

## Complexity

- Time: O(m·log n) — up to m rows, each binary searched in O(log n).
- Space: O(1) — only index variables.
