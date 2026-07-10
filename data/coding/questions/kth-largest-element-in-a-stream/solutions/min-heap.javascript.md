You never need the full sorted history — only the k largest values matter, and among those only the smallest one (the k-th largest overall). Keep a min-heap capped at size k: whenever it grows past k, pop the smallest, since anything smaller than the current k-th largest can never become the answer again.

JavaScript has no built-in heap, so this implements a small binary min-heap array with sift-up/sift-down. After seeding it with the initial array (trimmed to its k largest), every `add` is a single push, and possibly one pop, followed by peeking at the heap's root.

```javascript
class KthLargest {
  constructor(k, nums) {
    this.k = k;
    this.heap = [];
    for (const n of nums) this._push(n);
    while (this.heap.length > k) this._pop();
  }

  add(val) {
    this._push(val);
    if (this.heap.length > this.k) this._pop();
    return this.heap[0];
  }

  _push(val) {
    const h = this.heap;
    h.push(val);
    let i = h.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (h[p] <= h[i]) break;
      [h[p], h[i]] = [h[i], h[p]];
      i = p;
    }
  }

  _pop() {
    const h = this.heap;
    const top = h[0];
    const last = h.pop();
    if (h.length > 0) {
      h[0] = last;
      let i = 0;
      while (true) {
        const l = 2 * i + 1, r = 2 * i + 2;
        let smallest = i;
        if (l < h.length && h[l] < h[smallest]) smallest = l;
        if (r < h.length && h[r] < h[smallest]) smallest = r;
        if (smallest === i) break;
        [h[smallest], h[i]] = [h[i], h[smallest]];
        i = smallest;
      }
    }
    return top;
  }
}
```

## Why it works

A min-heap of size k always holds exactly the k largest values seen so far, with the smallest of that group sitting at the root (index 0). Pushing a new value and evicting the root when the heap overflows keeps that invariant intact, so the root is always the k-th largest element after every `add`.

## Complexity

- Time: O(log k) per call to `add` — one push and at most one pop on a heap of size k.
- Space: O(k) — the heap only ever holds the k largest values.
