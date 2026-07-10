The scan-based check is the bottleneck: it re-examines every earlier queen on every candidate. Instead, track three sets of "attacked" positions as bitmasks — occupied columns, and the two diagonal families — so testing and placing a queen becomes O(1) bit arithmetic instead of an O(n) scan.

Shifting the diagonal masks by one bit as you descend a row is what makes them line up correctly against the next row's columns; a `1` bit at position `k` in `diag1` or `diag2` means "column `k` is under diagonal attack in the current row."

```java
class Solution {
    private int full;

    public int countQueens(int n) {
        full = (1 << n) - 1;
        return backtrack(0, 0, 0);
    }

    private int backtrack(int cols, int diag1, int diag2) {
        if (cols == full) return 1;
        int total = 0;
        int available = full & ~(cols | diag1 | diag2);
        while (available != 0) {
            int pos = available & (-available);
            available -= pos;
            total += backtrack(cols | pos, (diag1 | pos) << 1, (diag2 | pos) >>> 1);
        }
        return total;
    }
}
```

## Why it works

`cols` has a `1` bit for every occupied column; `diag1`/`diag2` carry the two diagonal directions, shifted by one position per row so bit `k` always means "column `k` is unsafe in the row currently being filled." `available` is the set of columns free of all three constraints; `pos = available & -available` peels off its lowest set bit, so every free column is tried exactly once per row. Recursing with the updated masks and shifting the diagonals advances to the next row; `cols == full` signals all n rows are placed, contributing one to the count.

## Complexity

- Time: O(n!) — the same search tree as the brute-force version, but each placement/safety check is O(1) instead of O(n).
- Space: O(n) — recursion depth is bounded by n; the masks themselves are fixed-size integers.
