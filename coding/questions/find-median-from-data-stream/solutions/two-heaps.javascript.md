Split the numbers into two halves around the median: a max-heap `lo` holding the smaller half, and a min-heap `hi` holding the larger half, kept the same size (or `lo` one larger). The median then always sits at the top of one or both heaps — no sorting needed.

JavaScript has no built-in heap, so a small binary heap array is implemented here with a comparator, used once as a max-heap and once as a min-heap. On every `addNum`, push into one heap and rebalance by moving the top of one to the other so the size invariant holds.

```javascript
class Heap {
  constructor(compare) {
    this.data = [];
    this.compare = compare;
  }
  size() { return this.data.length; }
  peek() { return this.data[0]; }
  push(val) {
    this.data.push(val);
    let i = this.data.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.compare(this.data[i], this.data[p]) >= 0) break;
      [this.data[i], this.data[p]] = [this.data[p], this.data[i]];
      i = p;
    }
  }
  pop() {
    const top = this.data[0];
    const last = this.data.pop();
    if (this.data.length) {
      this.data[0] = last;
      let i = 0;
      while (true) {
        let smallest = i, l = 2 * i + 1, r = 2 * i + 2;
        if (l < this.data.length && this.compare(this.data[l], this.data[smallest]) < 0) smallest = l;
        if (r < this.data.length && this.compare(this.data[r], this.data[smallest]) < 0) smallest = r;
        if (smallest === i) break;
        [this.data[i], this.data[smallest]] = [this.data[smallest], this.data[i]];
        i = smallest;
      }
    }
    return top;
  }
}

class MedianFinder {
  constructor() {
    this.lo = new Heap((a, b) => b - a); // max-heap, smaller half
    this.hi = new Heap((a, b) => a - b); // min-heap, larger half
  }

  addNum(num) {
    this.lo.push(num);
    this.hi.push(this.lo.pop());
    if (this.hi.size() > this.lo.size()) {
      this.lo.push(this.hi.pop());
    }
  }

  findMedian() {
    if (this.lo.size() > this.hi.size()) return this.lo.peek();
    return (this.lo.peek() + this.hi.peek()) / 2;
  }
}
```

## Why it works

Every value first goes into `lo`, then its largest member is immediately promoted to `hi` — this guarantees every element of `lo` is `<=` every element of `hi`. Rebalancing keeps the sizes equal or `lo` exactly one larger, so the median is either `lo`'s top (odd total) or the average of both tops (even total).

## Complexity

- Time: O(log n) per `addNum` (heap push/pop); O(1) per `findMedian`.
- Space: O(n) — the two heaps together hold every number added.
