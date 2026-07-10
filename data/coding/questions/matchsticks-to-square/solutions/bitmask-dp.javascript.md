Plain backtracking retries the same subset of "already-placed" sticks over and over from different branches, which is what makes it exponential in the number of sides tried. Since `n <= 15`, we can instead track progress purely by *which sticks have been used* — a bitmask — and memoize the best partial side length reachable from each mask.

For every mask, `dp[mask]` stores how far the *current* side has been filled using exactly the sticks in `mask` (a value between 0 and `side - 1`, with `side` itself wrapping back to 0 to mean "a side just completed"). Transitioning by adding one more unused stick either extends the current side or starts a fresh one, and the mask with all sticks used is a valid square exactly when its stored progress is 0.

```javascript
function canFormSquare(matchsticks) {
  const total = matchsticks.reduce((a, b) => a + b, 0);
  if (total % 4 !== 0) return false;
  const side = total / 4;
  if (Math.max(...matchsticks) > side) return false;

  const n = matchsticks.length;
  const dp = new Array(1 << n).fill(-1);
  dp[0] = 0;

  for (let mask = 0; mask < 1 << n; mask++) {
    if (dp[mask] === -1) continue;
    for (let i = 0; i < n; i++) {
      if (mask & (1 << i)) continue;
      if (dp[mask] + matchsticks[i] <= side) {
        const nextMask = mask | (1 << i);
        dp[nextMask] = Math.max(dp[nextMask], (dp[mask] + matchsticks[i]) % side);
      }
    }
  }

  return dp[(1 << n) - 1] === 0;
}
```

## Why it works

`dp[mask]` is the length already committed to the side currently being built, using precisely the sticks marked in `mask`; when that running length hits `side` exactly, taking it modulo `side` resets it to 0, meaning a full side just closed and the next stick starts a new one. Because every reachable mask is visited once and only transitions that don't overshoot `side` are recorded, `dp[fullMask] === 0` means all sticks were used and the last side also closed cleanly — four complete sides, a square.

## Complexity

- Time: O(n · 2^n) — each of the 2^n masks considers up to n transitions.
- Space: O(2^n) — one DP entry per subset of sticks.
