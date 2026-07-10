Keep every price you have ever seen in an array. When a new price arrives, walk backwards from the newest entry, counting each day whose price is `<= today` until you hit a strictly larger price — that day ends the streak. The running count is the span.

This mirrors the definition literally: the span is exactly how far back the "less than or equal to today" run reaches, so scanning the history until the run breaks gives the answer directly.

```javascript
class StockSpanner {
    constructor() {
        this.prices = [];
    }

    next(price) {
        this.prices.push(price);
        let span = 0;
        let i = this.prices.length - 1;
        while (i >= 0 && this.prices[i] <= price) {
            span++;
            i--;
        }
        return span;
    }
}
```

## Why it works

After pushing, the last index is today. The loop moves leftward while each price is `<= price`, incrementing `span` once per qualifying day, and stops the moment a larger price appears (or the array is exhausted). That stopping point is exactly where the consecutive run ends, so `span` equals the number of days in the run including today.

## Complexity

- Time: O(n) per `next` — worst case rescans the whole history; O(n²) over n calls.
- Space: O(n) — every price is stored.
