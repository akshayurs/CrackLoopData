Each row is already sorted, so the matrix is really `n` sorted lists to merge. This is the classic k-way merge: a `PriorityQueue` holds the current front of each row, and polling the smallest `k` times reaches the answer without touching most of the matrix.

Seed the queue with the first cell of each row, stored as `[value, row, col]`. Every time you poll a cell, offer the cell to its right, so the queue always exposes the smallest value not yet emitted.

```java
import java.util.PriorityQueue;

class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int r = 0; r < n; r++) {
            heap.offer(new int[]{matrix[r][0], r, 0});
        }
        int value = 0;
        for (int i = 0; i < k; i++) {
            int[] cell = heap.poll();
            value = cell[0];
            int r = cell[1], c = cell[2];
            if (c + 1 < n) {
                heap.offer(new int[]{matrix[r][c + 1], r, c + 1});
            }
        }
        return value;
    }
}
```

## Why it works

The priority queue always returns the smallest value among the row fronts, so polling repeatedly produces values in global ascending order. Offering the next cell of a polled row keeps every row represented, so after `k` polls the last value removed is exactly the `k`th smallest — equal values are separate entries, so duplicates count correctly.

## Complexity

- Time: O(k log n) — k polls, each a log-n queue operation; the queue never exceeds n entries.
- Space: O(n) — one entry per row.
