Design a class that streams the daily price of a stock and, for each new price, reports its **span**. The span is the number of consecutive days ending today (today included) on which the price was less than or equal to today's price. Implement the `StockSpanner` class:

- `StockSpanner()` creates the streamer with no prices yet.
- `next(price)` records today's `price` and returns its span.

Prices arrive one at a time and are never given up front, so each `next` call must answer using only the history seen so far.

## Examples

```text
Input:
  ops  = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
  args = [[],             [100],  [80],   [60],   [70],   [60],   [75],   [85]]
Output: [null, 1, 1, 1, 2, 1, 4, 6]

# 100 -> 1  (only today)
# 80  -> 1  (80 < 100, streak breaks)
# 60  -> 1  (60 < 80)
# 70  -> 2  (70 >= 60, then 80 > 70 stops it: today + one day)
# 60  -> 1  (60 < 70)
# 75  -> 4  (75 >= 60, 60, 70; 80 > 75 stops it)
# 85  -> 6  (85 >= 75, 60, 70, 60, 80; 100 > 85 stops it)
```

```text
Input:
  ops  = ["StockSpanner", "next", "next", "next", "next"]
  args = [[],             [31],   [41],   [48],   [59]]
Output: [null, 1, 2, 3, 4]

# strictly rising prices: every prior day counts, so the span grows by one each time
```

## Constraints

- 1 <= price <= 10^5
- At most 10^4 calls are made to `next`.

## Follow-up

The brute force rescans history on every call. Can you make each `next` run in amortized O(1) time?
