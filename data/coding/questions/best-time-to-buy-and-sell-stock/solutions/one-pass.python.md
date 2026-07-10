The key insight: to sell on day `i` for maximum profit, you only care about the cheapest price seen on any earlier day. So sweep left to right, tracking the minimum price so far, and at each day ask "what if I sold today?" — the answer is `today - cheapest so far`.

Keep the best of those hypothetical sells. One pass, no inner loop, constant memory.

```python
def max_profit(prices):
    cheapest = float("inf")
    best = 0
    for price in prices:
        cheapest = min(cheapest, price)
        best = max(best, price - cheapest)
    return best
```

## Why it works

At every day, `cheapest` is the lowest buy price available up to and including that day, so `price - cheapest` is the best profit achievable if we sell right now. Taking the max over all days covers every valid buy-before-sell pair without enumerating them. If prices never rise, `price - cheapest` is never positive, so `best` stays at its initial `0`.

## Complexity

- Time: O(n) — a single scan.
- Space: O(1) — two scalars.
