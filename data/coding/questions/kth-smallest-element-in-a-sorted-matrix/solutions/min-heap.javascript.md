Each row is already sorted, so the matrix is really `n` sorted lists to merge. This is the classic k-way merge: a min-heap holds the current front of each row, and popping the smallest `k` times reaches the answer without touching most of the matrix.

JavaScript has no built-in heap, so a compact binary min-heap over `[value, row, col]` tuples does the job. Seed it with the first cell of each row; each time you pop a cell, push the cell to its right.

```javascript
function kthSmallest(matrix, k) {
    const n = matrix.length;
    const heap = [];
    const up = (i) => { while (i > 0) { const p = (i - 1) >> 1; if (heap[p][0] <= heap[i][0]) break; [heap[p], heap[i]] = [heap[i], heap[p]]; i = p; } };
    const down = (i) => { for (;;) { let s = i, l = 2 * i + 1, r = 2 * i + 2; if (l < heap.length && heap[l][0] < heap[s][0]) s = l; if (r < heap.length && heap[r][0] < heap[s][0]) s = r; if (s === i) break; [heap[s], heap[i]] = [heap[i], heap[s]]; i = s; } };
    for (let r = 0; r < n; r++) { heap.push([matrix[r][0], r, 0]); up(heap.length - 1); }
    let value = 0;
    for (let i = 0; i < k; i++) {
        const [v, r, c] = heap[0];
        value = v;
        const last = heap.pop();
        if (heap.length) { heap[0] = last; down(0); }
        if (c + 1 < n) { heap.push([matrix[r][c + 1], r, c + 1]); up(heap.length - 1); }
    }
    return value;
}
```

## Why it works

The heap invariant keeps its root as the smallest value among all row fronts, so popping repeatedly yields values in global ascending order. Pushing the next cell of a popped row keeps every row represented, so after `k` pops the last value removed is exactly the `k`th smallest — equal values are distinct heap entries, so duplicates count correctly.

## Complexity

- Time: O(k log n) — k pops, each a log-n heap operation; the heap never exceeds n entries.
- Space: O(n) — one entry per row.
