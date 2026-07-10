Sorting every point is wasteful when `k` is small — you only need to know the `k` smallest distances, not the full order of `n` of them. A max-heap capped at size `k` does exactly that: push points in, and whenever the heap grows past `k`, remove the farthest one.

JavaScript has no built-in heap, so a small binary heap array is kept inline, ordered so the largest distance sits at the root.

```javascript
function kClosest(points, k) {
  const heap = []; // each entry: [dist, x, y], max-heap on dist
  const less = (a, b) => a[0] < b[0];

  const siftUp = (i) => {
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (!less(heap[p], heap[i])) break;
      [heap[p], heap[i]] = [heap[i], heap[p]];
      i = p;
    }
  };
  const siftDown = (i) => {
    for (;;) {
      let largest = i, l = 2 * i + 1, r = 2 * i + 2;
      if (l < heap.length && less(heap[largest], heap[l])) largest = l;
      if (r < heap.length && less(heap[largest], heap[r])) largest = r;
      if (largest === i) break;
      [heap[largest], heap[i]] = [heap[i], heap[largest]];
      i = largest;
    }
  };

  for (const [x, y] of points) {
    heap.push([x * x + y * y, x, y]);
    siftUp(heap.length - 1);
    if (heap.length > k) {
      heap[0] = heap[heap.length - 1];
      heap.pop();
      siftDown(0);
    }
  }

  return heap
    .map(([, x, y]) => [x, y])
    .sort((a, b) => {
      const d = (a[0] ** 2 + a[1] ** 2) - (b[0] ** 2 + b[1] ** 2);
      if (d !== 0) return d;
      if (a[0] !== b[0]) return a[0] - b[0];
      return a[1] - b[1];
    });
}
```

## Why it works

The heap always holds at most `k` points, with the farthest one at the root. Adding a new point and then evicting the root whenever the size exceeds `k` always removes the true farthest among the `k + 1` candidates, so a closer point is never mistakenly discarded. After every point is processed, the heap contains exactly the `k` nearest; the trailing sort just applies the required deterministic ordering.

## Complexity

- Time: O(n log k) — each push/sift costs O(log k), plus O(k log k) for the final sort.
- Space: O(k) — the heap never holds more than k points.
