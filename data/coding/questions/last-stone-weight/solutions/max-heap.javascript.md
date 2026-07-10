Re-sorting the whole array every round is overkill — all that's ever needed is the current two largest values, and a heap gives those in O(log n). JavaScript has no built-in heap, so a small max-heap (array-backed, parent at `(i-1)>>1`) is built inline.

Pop the two largest stones each round, smash them, and push the remainder back in if the stones weren't equal. Stop once at most one stone remains.

```javascript
function lastStoneWeight(stones) {
  const heap = [...stones];
  const siftUp = (i) => {
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (heap[p] >= heap[i]) break;
      [heap[p], heap[i]] = [heap[i], heap[p]];
      i = p;
    }
  };
  const siftDown = (i) => {
    const n = heap.length;
    while (true) {
      let largest = i, l = 2 * i + 1, r = 2 * i + 2;
      if (l < n && heap[l] > heap[largest]) largest = l;
      if (r < n && heap[r] > heap[largest]) largest = r;
      if (largest === i) break;
      [heap[largest], heap[i]] = [heap[i], heap[largest]];
      i = largest;
    }
  };
  for (let i = 1; i < heap.length; i++) siftUp(i);
  const pop = () => {
    const top = heap[0];
    const last = heap.pop();
    if (heap.length) { heap[0] = last; siftDown(0); }
    return top;
  };
  const push = (v) => { heap.push(v); siftUp(heap.length - 1); };

  while (heap.length > 1) {
    const heaviest = pop();
    const second = pop();
    if (heaviest !== second) push(heaviest - second);
  }
  return heap.length ? heap[0] : 0;
}
```

## Why it works

`siftUp`/`siftDown` maintain the max-heap invariant so `heap[0]` is always the largest stone; `pop` removes it in O(log n) by swapping in the last element and sifting down. Two pops always yield the current heaviest pair, and pushing the (positive) remainder back — only when the stones differ — keeps the heap representing the true multiset of stones after each smash.

## Complexity

- Time: O(n log n) — heapifying is O(n); each of up to n rounds does O(1) pops/push at O(log n) each.
- Space: O(n) — the heap array.
