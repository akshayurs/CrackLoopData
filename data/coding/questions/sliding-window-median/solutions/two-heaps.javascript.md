Re-sorting the whole window every step throws away almost all of the previous work. Instead, keep the window split across two heaps: a max-heap `small` holding the lower half and a min-heap `large` holding the upper half, kept balanced in size so the median always sits at one (or both) of their tops. JavaScript has no built-in heap, so a tiny binary heap backed by an array does the job.

The wrinkle is deletion — heaps don't support "remove this arbitrary value" efficiently. The trick is lazy deletion: when a number slides out of the window, record that it owes a removal in a `delayed` map, and only actually pop it once it would otherwise surface at the top. Sizes are still tracked exactly, so balancing and the median calculation stay correct even while stale values linger deeper in a heap.

```javascript
class Heap {
  constructor(cmp) { this.cmp = cmp; this.data = []; }
  size() { return this.data.length; }
  peek() { return this.data[0]; }
  push(val) {
    const d = this.data; d.push(val);
    for (let i = d.length - 1, p = (i - 1) >> 1; i > 0 && this.cmp(d[i], d[p]) < 0; i = p, p = (i - 1) >> 1) {
      [d[i], d[p]] = [d[p], d[i]];
    }
  }
  pop() {
    const d = this.data, top = d[0], last = d.pop();
    if (d.length) {
      d[0] = last;
      let i = 0;
      while (true) {
        const l = 2 * i + 1, r = 2 * i + 2;
        let s = i;
        if (l < d.length && this.cmp(d[l], d[s]) < 0) s = l;
        if (r < d.length && this.cmp(d[r], d[s]) < 0) s = r;
        if (s === i) break;
        [d[i], d[s]] = [d[s], d[i]]; i = s;
      }
    }
    return top;
  }
}

function medianSlidingWindow(nums, k) {
  const small = new Heap((a, b) => b - a); // max-heap
  const large = new Heap((a, b) => a - b); // min-heap
  const delayed = new Map();
  let smallSize = 0, largeSize = 0;

  const prune = (heap) => {
    while (heap.size() && delayed.get(heap.peek()) > 0) {
      const cnt = delayed.get(heap.peek()) - 1;
      cnt === 0 ? delayed.delete(heap.peek()) : delayed.set(heap.peek(), cnt);
      heap.pop();
    }
  };
  const balance = () => {
    if (smallSize > largeSize + 1) { large.push(small.pop()); smallSize--; largeSize++; prune(small); }
    else if (smallSize < largeSize) { small.push(large.pop()); largeSize--; smallSize++; prune(large); }
  };
  const insert = (num) => {
    if (!small.size() || num <= small.peek()) { small.push(num); smallSize++; }
    else { large.push(num); largeSize++; }
    balance();
  };
  const erase = (num) => {
    delayed.set(num, (delayed.get(num) || 0) + 1);
    if (num <= small.peek()) { smallSize--; if (num === small.peek()) prune(small); }
    else { largeSize--; if (num === large.peek()) prune(large); }
    balance();
  };

  const result = [];
  for (let i = 0; i < nums.length; i++) {
    insert(nums[i]);
    if (i >= k) erase(nums[i - k]);
    if (i >= k - 1) result.push(k % 2 ? small.peek() : (small.peek() + large.peek()) / 2);
  }
  return result;
}
```

## Why it works

`small` and `large` are kept the same size (or `small` one larger), so the median is always `small`'s top for odd `k`, or the average of both tops for even `k`. Lazy deletion keeps the heaps' logical sizes accurate — `smallSize`/`largeSize` reflect reality even before a stale entry is physically popped — so every balance and median read uses correct counts, and pruning only touches values that have actually become garbage.

## Complexity

- Time: O(n log k) — each insert, erase, and balance touches a heap of size O(k), and each element causes O(1) amortized heap operations overall.
- Space: O(k) — the two heaps together hold the current window (plus bounded stale entries awaiting cleanup).
