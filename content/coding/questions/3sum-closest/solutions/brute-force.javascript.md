The same idea in JavaScript: iterate over every triple `(i, j, k)`, compute its sum, and keep the one whose distance to `target` is smallest. Straightforward, with no auxiliary storage.

```javascript
function threeSumClosest(nums, target) {
  const n = nums.length;
  let best = nums[0] + nums[1] + nums[2];
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        const s = nums[i] + nums[j] + nums[k];
        if (Math.abs(s - target) < Math.abs(best - target)) {
          best = s;
        }
      }
    }
  }
  return best;
}
```

## Why it works

The strictly increasing loop bounds generate each unordered triple of distinct indices exactly once. `best` starts at a genuine triple sum and is overwritten only when a new sum is strictly closer to `target`, so after the scan it is the global closest.

## Complexity

- Time: O(n³) — every triple of the n elements is checked.
- Space: O(1) — only the running best and loop counters.
