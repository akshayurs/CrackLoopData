The literal reading of the problem: consider every possible buy day paired with every later sell day, compute the profit, and keep the largest. No cleverness, just two nested loops.

It is the honest baseline you would state first in an interview, before optimizing away the inner loop.

```javascript
function maxProfit(prices) {
  let best = 0;
  for (let buy = 0; buy < prices.length; buy++) {
    for (let sell = buy + 1; sell < prices.length; sell++) {
      best = Math.max(best, prices[sell] - prices[buy]);
    }
  }
  return best;
}
```

## Why it works

The outer loop fixes the buy day; the inner loop tries every strictly later sell day, so every valid ordered pair is examined exactly once. `best` starts at `0`, which also handles the case where prices only fall — no pair beats zero, so we return `0`.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — only a running maximum.
