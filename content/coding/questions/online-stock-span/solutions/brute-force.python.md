Keep every price you have ever seen in a list. When a new price arrives, walk backwards from the newest entry, counting each day whose price is `<= today` until you hit a strictly larger price — that day ends the streak. The running count is the span.

This mirrors the definition literally: the span is exactly how far back the "less than or equal to today" run reaches, so scanning the history until the run breaks gives the answer directly.

```python
class StockSpanner:
    def __init__(self):
        self._prices = []

    def next(self, price):
        self._prices.append(price)
        span = 0
        i = len(self._prices) - 1
        while i >= 0 and self._prices[i] <= price:
            span += 1
            i -= 1
        return span
```

## Why it works

After appending, index `len - 1` is today. The loop moves leftward while each price is `<= price`, incrementing `span` once per qualifying day, and stops the moment a larger price appears (or the history runs out). That stopping point is precisely where the consecutive run ends, so `span` equals the number of days in the run including today.

## Complexity

- Time: O(n) per `next` — worst case (a non-increasing then equal streak) rescans the whole history; O(n²) over n calls.
- Space: O(n) — every price is stored.
