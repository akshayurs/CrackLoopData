The window for a value is fully determined by where it first and last appears — so there is no need for a separate degree-finding scan followed by re-scans. Track everything as you walk the array once.

For each value remember the index of its first sighting and how many times it has shown up. The current running length for that value is `i - first + 1`. Keep the best answer tied to the highest count seen so far, breaking ties toward the shorter window. Whenever a value's count sets a new record it dictates the answer; when it merely ties the record, it competes on length.

```javascript
function findShortestSubArray(nums) {
  const first = new Map();
  const count = new Map();
  let degree = 0;
  let best = 0;
  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    if (!first.has(n)) first.set(n, i);
    count.set(n, (count.get(n) || 0) + 1);
    const length = i - first.get(n) + 1;
    if (count.get(n) > degree) {
      degree = count.get(n);
      best = length;
    } else if (count.get(n) === degree) {
      best = Math.min(best, length);
    }
  }
  return best;
}
```

## Why it works

At any prefix of the array, `degree` is the max frequency seen so far and `best` is the shortest window achieving it. A new maximum can only come from the value just extended, and its tightest window is exactly first-to-current, so overwriting `best` is correct. A tie means another value now matches the leader, and we keep whichever window is shorter. Since indices only grow, the final `degree` equals the array's true degree.

## Complexity

- Time: O(n) — a single pass with O(1) map operations per element.
- Space: O(n) — two maps keyed by the distinct values.
