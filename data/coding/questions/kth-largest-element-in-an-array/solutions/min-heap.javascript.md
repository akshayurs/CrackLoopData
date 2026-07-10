We only need one value, not a fully ordered array, so sorting everything is wasteful. Instead, keep a min-heap that never holds more than `k` elements — the smallest of "the k largest seen so far" always sits at the root. JavaScript has no built-in heap, so a small binary heap array does the job.

Push every number in, and whenever the heap grows past size `k`, pop the smallest. After scanning the whole array, exactly the k largest values remain in the heap, and the root is the smallest of them — which is precisely the k-th largest overall.

```javascript
function kthLargest(nums, k) {
  const heap = [];

  const siftUp = (i) => {
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (heap[parent] <= heap[i]) break;
      [heap[parent], heap[i]] = [heap[i], heap[parent]];
      i = parent;
    }
  };
  const siftDown = (i) => {
    const n = heap.length;
    while (true) {
      let smallest = i;
      const l = 2 * i + 1, r = 2 * i + 2;
      if (l < n && heap[l] < heap[smallest]) smallest = l;
      if (r < n && heap[r] < heap[smallest]) smallest = r;
      if (smallest === i) break;
      [heap[smallest], heap[i]] = [heap[i], heap[smallest]];
      i = smallest;
    }
  };

  for (const n of nums) {
    heap.push(n);
    siftUp(heap.length - 1);
    if (heap.length > k) {
      heap[0] = heap[heap.length - 1];
      heap.pop();
      siftDown(0);
    }
  }
  return heap[0];
}
```

## Why it works

At every point the heap holds at most `k` elements, and it is trimmed by discarding the current minimum whenever it overflows. Anything that survives being the smallest of the "top k so far" must be among the true top k, so once every element has been offered, the heap contains exactly the k largest values, with the smallest of those — the answer — sitting at the root.

## Complexity

- Time: O(n log k) — each of the n pushes/pops costs O(log k) since the heap never exceeds size k.
- Space: O(k) — the heap holds at most k elements.
