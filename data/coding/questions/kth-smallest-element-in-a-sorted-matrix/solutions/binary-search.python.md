Instead of searching for a position, binary-search on the *answer value*. The smallest possible answer is the top-left corner and the largest is the bottom-right, so the answer lies in `[matrix[0][0], matrix[n-1][n-1]]`. For a candidate value `mid`, count how many matrix entries are `<= mid`; if that count is at least `k`, the answer is `<= mid`, otherwise it is strictly greater.

Counting is the elegant part: start at the bottom-left corner and walk. If the current cell is `<= mid`, the whole column above it also qualifies, so add that column's count and step right; otherwise step up. This "staircase" counts all qualifying cells in O(n) without scanning every cell. The loop converges to a value that is guaranteed present in the matrix.

```python
def kth_smallest(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n - 1][n - 1]
    while lo < hi:
        mid = (lo + hi) // 2
        count, c = 0, n - 1
        for r in range(n):
            while c >= 0 and matrix[r][c] > mid:
                c -= 1
            count += c + 1
        if count < k:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

## Why it works

`count(mid)` is non-decreasing in `mid`, so binary search finds the smallest value whose count reaches `k`. That value must itself be in the matrix: if it weren't, the count would be identical for `mid` and `mid - 1`, and the search would have moved lower. The per-row pointer `c` never resets upward across rows because columns are sorted, giving a linear count.

## Complexity

- Time: O(n log(hi − lo)) — each of log-range iterations counts in O(n).
- Space: O(1) — only a few scalars beyond the input.
