The most direct reading of the problem is to check every pair of positions and see if they hold the same value. Compare each element to every element after it; the first match you find is the duplicate.

This never modifies the array and uses no extra memory beyond a couple of loop counters, but it re-scans the tail of the array for every starting position.

```javascript
function findDuplicate(nums) {
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (nums[i] === nums[j]) {
        return nums[i];
      }
    }
  }
  return -1;
}
```

## Why it works

Exactly one value repeats, so somewhere among all pairs `(i, j)` with `i < j` there is a pair where `nums[i] === nums[j]`. Checking every pair is exhaustive, so the first equal pair found must involve the duplicated value. The loop terminates as soon as that pair is located.

## Complexity

- Time: O(n^2) — every pair of indices is compared in the worst case.
- Space: O(1) — only loop indices are kept.
