Instead of rescanning each window, keep a heap that hands back the current maximum instantly. Push every element as `[value, index]` into a max-heap; the top is always the largest value seen so far.

The catch is that the top might sit *outside* the current window. Solve it with lazy deletion: before reading a window's answer, pop any entries whose index has slid off the left edge. Each element is pushed and popped at most once.

```javascript
function maxSlidingWindow(nums, k) {
  const heap = [];
  const swap = (i, j) => { [heap[i], heap[j]] = [heap[j], heap[i]]; };
  const push = (item) => {
    heap.push(item);
    let i = heap.length - 1;
    while (i > 0 && heap[(i - 1) >> 1][0] < heap[i][0]) { swap(i, (i - 1) >> 1); i = (i - 1) >> 1; }
  };
  const pop = () => {
    const last = heap.pop();
    if (!heap.length) return;
    heap[0] = last;
    let i = 0;
    for (;;) {
      let big = i, l = 2 * i + 1, r = 2 * i + 2;
      if (l < heap.length && heap[l][0] > heap[big][0]) big = l;
      if (r < heap.length && heap[r][0] > heap[big][0]) big = r;
      if (big === i) break;
      swap(i, big); i = big;
    }
  };
  const result = [];
  for (let i = 0; i < nums.length; i++) {
    push([nums[i], i]);
    if (i >= k - 1) {
      while (heap[0][1] <= i - k) pop();
      result.push(heap[0][0]);
    }
  }
  return result;
}
```

## Why it works

The array-backed binary heap keeps the largest value at index 0. An entry is valid for the window ending at `i` only when its stored index exceeds `i - k`; stale tops are popped before the max is read. Because a stale entry is discarded once and never returns, `heap[0]` is always the largest in-window value.

## Complexity

- Time: O(n log n) — each element is pushed and popped at most once, each heap op is O(log n).
- Space: O(n) — the heap can hold up to n entries before stale ones are purged.
