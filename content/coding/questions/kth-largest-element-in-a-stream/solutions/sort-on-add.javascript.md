The simplest thing that could work: keep every number the stream has ever seen in an array. Each time `add` is called, drop the new value in, sort the whole array in descending order, and read off the element at index `k - 1`.

It never gets the ordering wrong, but re-sorting the entire history on every single call is wasteful once the stream grows long.

```javascript
class KthLargest {
  constructor(k, nums) {
    this.k = k;
    this.nums = [...nums];
  }

  add(val) {
    this.nums.push(val);
    this.nums.sort((a, b) => b - a);
    return this.nums[this.k - 1];
  }
}
```

## Why it works

Sorting the array in descending order puts the largest value at index 0, the second largest at index 1, and so on — so the k-th largest always sits at index `k - 1`. Because we re-sort after every insertion, the answer reflects the full stream seen so far.

## Complexity

- Time: O(n log n) per call to `add`, where n is the number of elements seen so far.
- Space: O(n) — the array stores every value ever added.
