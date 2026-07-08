Instead of searching for a position, binary-search on the *answer value*. The smallest possible answer is the top-left corner and the largest is the bottom-right, so the answer lies in `[matrix[0][0], matrix[n-1][n-1]]`. For a candidate value `mid`, count how many matrix entries are `<= mid`; if that count is at least `k`, the answer is `<= mid`, otherwise it is strictly greater.

Counting is the elegant part: use a per-row column pointer that only ever moves left as rows advance, because columns are sorted. That "staircase" tallies all qualifying cells in O(n) without scanning every cell, and the loop converges to a value guaranteed to be present in the matrix.

```javascript
function kthSmallest(matrix, k) {
    const n = matrix.length;
    let lo = matrix[0][0], hi = matrix[n - 1][n - 1];
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        let count = 0, c = n - 1;
        for (let r = 0; r < n; r++) {
            while (c >= 0 && matrix[r][c] > mid) c--;
            count += c + 1;
        }
        if (count < k) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
```

## Why it works

`count(mid)` is non-decreasing in `mid`, so binary search finds the smallest value whose count reaches `k`. That value must itself be in the matrix: if it weren't, the count would be identical for `mid` and `mid - 1`, and the search would have moved lower. The column pointer `c` never resets upward across rows because columns are sorted, giving a linear count.

## Complexity

- Time: O(n log(hi − lo)) — each of log-range iterations counts in O(n).
- Space: O(1) — only a few scalars beyond the input.
