Reduce 4Sum to a familiar shape: sort the array, fix the two outer values with a double loop, then let a two-pointer sweep close the remaining pair in linear time. Sorting is what makes both the pointer logic and duplicate-skipping possible.

For each fixed `(i, j)`, `lo` starts just after `j` and `hi` at the end. If the four-way sum is too small, advancing `lo` raises it; too large, dropping `hi` lowers it; on a hit we record the quadruplet and step both pointers past any repeats. Skipping duplicate values at `i`, `j`, `lo`, and `hi` keeps every quadruplet unique and the output already sorted.

```javascript
function fourSum(nums, target) {
  nums.sort((a, b) => a - b);
  const n = nums.length;
  const res = [];
  for (let i = 0; i < n - 3; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    for (let j = i + 1; j < n - 2; j++) {
      if (j > i + 1 && nums[j] === nums[j - 1]) continue;
      let lo = j + 1, hi = n - 1;
      while (lo < hi) {
        const total = nums[i] + nums[j] + nums[lo] + nums[hi];
        if (total === target) {
          res.push([nums[i], nums[j], nums[lo], nums[hi]]);
          lo++; hi--;
          while (lo < hi && nums[lo] === nums[lo - 1]) lo++;
          while (lo < hi && nums[hi] === nums[hi + 1]) hi--;
        } else if (total < target) {
          lo++;
        } else {
          hi--;
        }
      }
    }
  }
  return res;
}
```

## Why it works

On a sorted array the two-pointer sweep is exhaustive: moving `lo` only increases the sum and moving `hi` only decreases it, so no valid pair between them is skipped. The `continue` and inner `while` guards ensure each distinct value combination is emitted once. JavaScript numbers stay exact well past 4·10^9, so the sum is safe. Ascending outer values plus an inward pair scan give quadruplets in canonical order.

## Complexity

- Time: O(n^3) — two nested loops times a linear pointer sweep, after an O(n log n) sort.
- Space: O(1) — ignoring the output, only pointers and counters are used.
