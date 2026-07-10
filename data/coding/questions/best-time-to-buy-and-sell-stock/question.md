You are given an array `prices` where `prices[i]` is the price of a given stock on day `i`. You want to buy on one day and sell on a later day to maximize your profit.

Return the maximum profit you can achieve from a single buy-then-sell transaction. If no profit is possible, return `0`.

## Examples

```text
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5        # buy on day 1 (price 1), sell on day 4 (price 6) → 6 - 1 = 5
```

```text
Input:  prices = [7, 6, 4, 3, 1]
Output: 0        # prices only fall, so the best move is to not trade
```

```text
Input:  prices = [2, 4, 1]
Output: 2        # buy at 2, sell at 4 → 2
```

## Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
- You must buy before you sell (sell day strictly after buy day).

## Follow-up

Can you do it in a single pass with O(1) extra space?
