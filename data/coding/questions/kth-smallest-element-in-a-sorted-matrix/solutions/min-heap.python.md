Each row is already sorted, so the matrix is really `n` sorted lists to merge. This is the classic k-way merge: a min-heap holds the current front of each row, and popping the smallest `k` times reaches the answer without touching most of the matrix.

Seed the heap with the first cell of each row, tagged with its coordinates. Every time you pop a cell, push the next cell to its right, so the heap always exposes the smallest value not yet emitted.

```python
import heapq

def kth_smallest(matrix, k):
    n = len(matrix)
    heap = [(matrix[r][0], r, 0) for r in range(n)]
    heapq.heapify(heap)
    value = 0
    for _ in range(k):
        value, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return value
```

## Why it works

The heap invariant guarantees its root is the smallest value among all row fronts, so popping repeatedly yields values in global ascending order. Pushing the next cell in a popped row keeps every row represented, so after `k` pops the last value removed is exactly the `k`th smallest — duplicates handled naturally since equal values are separate heap entries.

## Complexity

- Time: O(k log n) — k pops, each a log-n heap operation; the heap never exceeds n entries.
- Space: O(n) — one entry per row.
