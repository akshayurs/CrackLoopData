The simplest possible design: keep every number seen so far in one sorted array. On each `addNum`, binary-search the insertion point and splice the value in to keep the array sorted. `findMedian` then just reads the middle (or average of the two middles) directly.

This mirrors what you'd write in an interview before optimizing — correct, but every insert costs a linear splice, and the order has to be maintained by hand rather than incrementally by a smarter structure.

```javascript
class MedianFinder {
  constructor() {
    this.nums = [];
  }

  addNum(num) {
    let lo = 0, hi = this.nums.length;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (this.nums[mid] < num) lo = mid + 1;
      else hi = mid;
    }
    this.nums.splice(lo, 0, num);
  }

  findMedian() {
    const n = this.nums.length;
    const mid = Math.floor(n / 2);
    if (n % 2 === 1) return this.nums[mid];
    return (this.nums[mid - 1] + this.nums[mid]) / 2;
  }
}
```

## Why it works

The binary search locates the first index whose value is not less than `num`, and splicing there keeps `this.nums` sorted at all times. With a sorted array, the median is just the middle element (odd count) or the average of the two elements straddling the middle (even count).

## Complexity

- Time: O(n) per `addNum` (binary search is O(log n) but the splice shifts O(n) elements); O(1) per `findMedian`.
- Space: O(n) — one array holding every number added.
