The brute force redoes work: every time it scans past a day, it re-derives a fact that was already known — how far *that* day's own streak reached. Instead of rescanning prices, keep a stack of `[price, span]` pairs for days that could still start a future streak.

A day only matters going forward if some later day might stop at it — that is, if it is not dominated by an earlier, larger price. So whenever the new price is `>=` the top of the stack, pop it and absorb its span into the running total (skipping straight over everything it already covered), then push `[price, span]` once the stack top holds a strictly larger price (or the stack is empty).

```java
import java.util.ArrayDeque;
import java.util.Deque;

class StockSpanner {
    private final Deque<int[]> stack = new ArrayDeque<>(); // [price, span], prices strictly decreasing bottom to top

    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            span += stack.pop()[1];
        }
        stack.push(new int[]{price, span});
        return span;
    }
}
```

## Why it works

Each entry on the stack represents a block of consecutive days that are all `<= ` the price above them, collapsed into one `[price, span]` pair. When today's price beats the top pair, every day inside that block is automatically `<= ` today too, so its whole span is folded in with one pop instead of one comparison per day. The stack always stays strictly decreasing in price from bottom to top, so the loop stops the instant it meets a price too large to absorb — exactly where the historical scan would have stopped. Each price is pushed once and popped at most once, so the total work across all calls is linear.

## Complexity

- Time: O(1) amortized per `next`, O(n) total over n calls — each price is pushed and popped at most once.
- Space: O(n) — the stack holds at most one entry per day.
