The most direct reading of the problem: there are `n - k + 1` window positions, so visit each one and take the max of its `k` elements with an inner scan.

This repeats work — neighbouring windows share `k - 1` elements that get re-examined — but it is the natural first pass and a clean correctness baseline.

```javascript
function maxSlidingWindow(nums, k) {
  const result = [];
  for (let start = 0; start + k <= nums.length; start++) {
    let best = nums[start];
    for (let j = start + 1; j < start + k; j++) {
      if (nums[j] > best) best = nums[j];
    }
    result.push(best);
  }
  return result;
}
```

## Why it works

`start` walks every valid left edge, from `0` up to `nums.length - k`. The inner loop scans that window's `k` elements and keeps the largest in `best`. Pushing each `best` in order yields the answer sequence.

## Complexity

- Time: O(n·k) — each of the ~n windows costs O(k) to scan.
- Space: O(1) — only a running max beyond the output list.
