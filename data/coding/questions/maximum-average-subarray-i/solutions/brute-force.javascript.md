The most direct reading of the problem: there are `n - k + 1` windows of length `k`, so line them all up, add each one, and keep the biggest average you see.

Because every window is summed independently, the same neighbouring elements get added over and over — correct, but wasteful.

```javascript
function maxAverage(nums, k) {
  let best = -Infinity;
  for (let i = 0; i + k <= nums.length; i++) {
    let windowSum = 0;
    for (let j = i; j < i + k; j++) windowSum += nums[j];
    best = Math.max(best, windowSum / k);
  }
  return best;
}
```

## Why it works

The outer loop fixes each valid start `i` (while a full window of `k` still fits), and the inner loop adds the `k` elements beginning there. Each window's average is compared against `best`, so after the sweep `best` holds the maximum. Starting from `-Infinity` keeps all-negative inputs correct.

## Complexity

- Time: O(n·k) — ~n windows, each summed in O(k).
- Space: O(1) — a couple of scalars.
