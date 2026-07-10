Instead of searching over split points, search over the *answer* itself. Suppose we guess a cap `x` for the largest allowed piece. We can greedily walk the array, starting a new piece whenever adding the next number would exceed `x`, and count how many pieces that takes. If it takes at most `k` pieces, then `x` is achievable; if it needs more, `x` is too small.

The number of pieces needed is monotonic in `x` — a bigger cap never needs more pieces — so we binary search `x` over the range `[max(nums), sum(nums)]`. The lower bound must be at least the largest single element (no piece can be smaller than that), and the upper bound is one piece holding everything.

```javascript
function splitArray(nums, k) {
  const piecesNeeded = (cap) => {
    let count = 1, running = 0;
    for (const x of nums) {
      if (running + x > cap) {
        count += 1;
        running = x;
      } else {
        running += x;
      }
    }
    return count;
  };

  let lo = Math.max(...nums);
  let hi = nums.reduce((a, b) => a + b, 0);
  while (lo < hi) {
    const mid = Math.floor((lo + hi) / 2);
    if (piecesNeeded(mid) <= k) hi = mid;
    else lo = mid + 1;
  }
  return lo;
}
```

## Why it works

For a fixed cap, the greedy "extend until it would overflow, then cut" uses the fewest pieces possible, so it correctly decides feasibility. Feasibility is monotonic: any cap `>=` the true answer is feasible, any smaller cap is not. Binary search converges on the smallest feasible cap, which is exactly the minimized largest sum.

## Complexity

- Time: O(n · log(sum − max)) — each feasibility check is O(n), run for a logarithmic number of guesses.
- Space: O(1) — only a few counters.
