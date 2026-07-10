Instead of re-deciding the whole ladder assignment from scratch at every step, commit greedily and let a min-heap correct course if needed. Every positive gap first "borrows" a ladder by going into a min-heap of size `ladders`. The moment the heap overflows, the smallest gap currently sitting in it is the least deserving of a free ladder, so it gets evicted and paid for with bricks instead — the biggest gaps naturally stay in the heap.

JavaScript has no built-in heap, so a small binary heap (array-backed, with sift-up/sift-down) does the job.

```javascript
function furthestBuilding(heights, bricks, ladders) {
  const heap = [];
  const push = (val) => {
    heap.push(val);
    let i = heap.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (heap[p] <= heap[i]) break;
      [heap[p], heap[i]] = [heap[i], heap[p]];
      i = p;
    }
  };
  const pop = () => {
    const top = heap[0];
    const last = heap.pop();
    if (heap.length) {
      heap[0] = last;
      let i = 0;
      while (true) {
        let smallest = i;
        const l = 2 * i + 1, r = 2 * i + 2;
        if (l < heap.length && heap[l] < heap[smallest]) smallest = l;
        if (r < heap.length && heap[r] < heap[smallest]) smallest = r;
        if (smallest === i) break;
        [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
        i = smallest;
      }
    }
    return top;
  };

  for (let i = 0; i < heights.length - 1; i++) {
    const diff = heights[i + 1] - heights[i];
    if (diff <= 0) continue;
    push(diff);
    if (heap.length > ladders) bricks -= pop();
    if (bricks < 0) return i;
  }
  return heights.length - 1;
}
```

## Why it works

The heap always holds the `ladders` largest gaps seen so far among the ones "in flight." Whenever a new gap arrives and the heap is full, the smallest of all gaps considered is the correct one to demote to bricks, since keeping it over a larger gap could never be optimal. `bricks` is debited lazily as demotions happen, so the moment it goes negative, this exact prefix is unreachable within budget.

## Complexity

- Time: O(n log l) — one heap push per building, one pop when it overflows the ladder capacity `l`.
- Space: O(l) — the heap never holds more than `ladders` elements.
