Sorting every distinct value is wasteful when `k` is small — you only care about the top few. JavaScript has no built-in heap, but the same idea works with a lightweight one: count the values, then keep the `k` most frequent by repeatedly extracting the current maximum from a simple binary heap.

Here we build a max-heap keyed on count and pop it `k` times. Each pop is O(log d) where `d` is the number of distinct values, giving O(n + k log d) overall — better than a full sort whenever `k` is small.

```javascript
function topKFrequent(nums, k) {
  const counts = new Map();
  for (const n of nums) counts.set(n, (counts.get(n) || 0) + 1);

  const heap = [...counts.entries()]; // [value, count]
  const size = heap.length;
  const swap = (i, j) => { [heap[i], heap[j]] = [heap[j], heap[i]]; };
  const siftDown = (i, n) => {
    for (let l; (l = 2 * i + 1) < n; i = l) {
      if (l + 1 < n && heap[l + 1][1] > heap[l][1]) l++;
      if (heap[i][1] >= heap[l][1]) break;
      swap(i, l);
    }
  };
  for (let i = (size >> 1) - 1; i >= 0; i--) siftDown(i, size);

  const result = [];
  for (let end = size - 1; result.length < k; end--) {
    result.push(heap[0][0]);
    swap(0, end);
    siftDown(0, end);
  }
  return result.sort((a, b) => a - b);
}
```

## Why it works

`heapify` arranges the distinct `[value, count]` pairs so the largest count is at the root. Swapping the root to the end and sifting down over the shrinking prefix extracts values in descending frequency, exactly like the selection phase of heapsort. Doing this `k` times yields the `k` most frequent values. A final ascending sort of those `k` values gives a deterministic output order.

## Complexity

- Time: O(n + k log d) — counting is O(n); building the heap is O(d) and each of the `k` extractions costs O(log d) for `d` distinct values; the final sort of the k results costs O(k log k), which does not change the dominant term.
- Space: O(n) — the map and heap hold up to n entries.
