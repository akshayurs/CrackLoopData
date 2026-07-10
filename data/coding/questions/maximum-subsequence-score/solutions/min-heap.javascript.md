The brute-force re-sort is doing the same work repeatedly: as the prefix grows by one element, the set of "current top `k` values" barely changes. A min-heap of size `k` tracks exactly that set incrementally — push the new value, and if the heap now holds more than `k` values, evict the smallest. The heap's total is always the sum of the best `k` values seen so far.

Sorting by `nums2` descending first is unchanged: it guarantees that whichever element we are currently processing has the smallest `nums2` among everything considered, so it is the correct multiplier the moment the heap reaches size `k`. JavaScript has no built-in heap, so a tiny binary min-heap is inlined below.

```javascript
function maxScore(nums1, nums2, k) {
  const pairs = nums1.map((a, i) => [a, nums2[i]]).sort((p, q) => q[1] - p[1]);
  const heap = [];
  const push = (v) => {
    heap.push(v);
    let i = heap.length - 1;
    while (i > 0 && heap[(i - 1) >> 1] > heap[i]) {
      const p = (i - 1) >> 1;
      [heap[p], heap[i]] = [heap[i], heap[p]];
      i = p;
    }
  };
  const pop = () => {
    const top = heap[0];
    heap[0] = heap.pop();
    let i = 0;
    while (true) {
      let s = i, l = 2 * i + 1, r = 2 * i + 2;
      if (l < heap.length && heap[l] < heap[s]) s = l;
      if (r < heap.length && heap[r] < heap[s]) s = r;
      if (s === i) break;
      [heap[s], heap[i]] = [heap[i], heap[s]];
      i = s;
    }
    return top;
  };
  let total = 0, best = 0;
  for (const [a, b] of pairs) {
    push(a);
    total += a;
    if (heap.length > k) total -= pop();
    if (heap.length === k) best = Math.max(best, total * b);
  }
  return best;
}
```

## Why it works

At every step the heap holds the `k` largest `nums1` values among all pairs processed so far, and `total` is their sum — pushing then popping the minimum whenever the heap overflows keeps that invariant. Because the pairs are processed in descending `nums2` order, the current pair's `nums2` is the smallest multiplier available among everything seen, matching the pivot argument from the brute-force approach. Taking the max of `total * b` at every point where the heap is full evaluates every valid pivot exactly once.

## Complexity

- Time: O(n log n) — one sort plus one heap push/pop per element.
- Space: O(n) — the heap holds at most `k` elements; the sorted pairs take O(n).
