The trick is to turn "equal counts" into "same running total." Replace every `0` with `-1`, then a subarray is balanced exactly when its values sum to `0`. Keep a running sum as you sweep left to right: if the sum ever repeats a value you saw at an earlier index, everything between those two positions cancels out to zero — a balanced stretch.

So record the *first* index at which each running sum appears. When that sum shows up again at index `i`, the balanced subarray runs from just after the first occurrence to `i`, and its length is the gap between the indices. Seeding the map with sum `0` at index `-1` lets a balanced prefix starting at position `0` count correctly.

```javascript
function findMaxLength(nums) {
  const firstIndex = new Map([[0, -1]]);
  let running = 0;
  let best = 0;
  for (let i = 0; i < nums.length; i++) {
    running += nums[i] === 1 ? 1 : -1;
    if (firstIndex.has(running)) {
      best = Math.max(best, i - firstIndex.get(running));
    } else {
      firstIndex.set(running, i);
    }
  }
  return best;
}
```

## Why it works

With `0` counted as `-1` and `1` as `+1`, the running sum after index `i` equals `(ones - zeros)` over the prefix. Two prefixes with the *same* running sum enclose a segment whose ones and zeros are equal. By storing only the earliest index for each sum, the distance to any later matching index is the longest balanced subarray ending there, and taking the max over all `i` gives the global answer.

## Complexity

- Time: O(n) — one pass, O(1) average map operations.
- Space: O(n) — the map stores up to n distinct running sums.
