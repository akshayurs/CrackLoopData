Sorting every distinct word costs O(n log n) even though only `k` of them are ever returned. A binary heap lets you pay for just the `k` extractions you need on top of a linear-time build.

JavaScript has no built-in heap, so build a tiny array-based min-heap keyed by `(-count, word)`: heapify the array bottom-up in linear time, then repeatedly take the root and sift down. Negating the count means "highest frequency" sorts as "smallest," while the word only matters as a tie-breaker.

```javascript
function topKFrequentWords(words, k) {
  const counts = new Map();
  for (const w of words) counts.set(w, (counts.get(w) || 0) + 1);
  const heap = [...counts.entries()].map(([word, count]) => [-count, word]);

  const less = (a, b) => a[0] < b[0] || (a[0] === b[0] && a[1] < b[1]);
  const siftDown = (i) => {
    let best = i;
    while (true) {
      const l = 2 * best + 1, r = 2 * best + 2;
      let smallest = best;
      if (l < heap.length && less(heap[l], heap[smallest])) smallest = l;
      if (r < heap.length && less(heap[r], heap[smallest])) smallest = r;
      if (smallest === best) break;
      [heap[best], heap[smallest]] = [heap[smallest], heap[best]];
      best = smallest;
    }
  };
  for (let i = Math.floor(heap.length / 2) - 1; i >= 0; i--) siftDown(i);

  const result = [];
  for (let i = 0; i < k; i++) {
    result.push(heap[0][1]);
    heap[0] = heap[heap.length - 1];
    heap.pop();
    siftDown(0);
  }
  return result;
}
```

## Why it works

The pair `[-count, word]` compares the same way a Python tuple would: negating the count turns "most frequent" into "smallest," and `word` only decides ties, giving ascending alphabetical order exactly where the problem wants it. Building the heap bottom-up (`siftDown` from the last parent to the root) costs O(n), and each removal of the root followed by `siftDown` costs O(log n).

## Complexity

- Time: O(n + k log n) — counting and heap construction is O(n); each of the k removals costs O(log n).
- Space: O(n) — the map and the heap array each hold up to n entries.
