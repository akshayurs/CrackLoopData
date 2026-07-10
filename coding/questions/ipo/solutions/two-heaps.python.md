The brute force wastes time re-checking affordability from scratch every round. Instead, sort projects by `capital` once and pour them into a min-heap ordered by capital. Then, for each of the `k` rounds, pop every project out of that min-heap whose capital is now affordable and push its profit into a second, max-heap. The top of the max-heap is always the best project money can currently buy.

Once a round's candidates are moved into the max-heap, picking the winner is just popping the top — no rescanning, no re-checking "used" status, because a project only ever moves from the capital-heap to the profit-heap once.

```python
import heapq

def max_capital(k, w, profit, capital):
    n = len(profit)
    by_capital = sorted(range(n), key=lambda i: capital[i])
    affordable = []  # max-heap of profits (negated)
    pos = 0
    money = w

    for _ in range(k):
        while pos < n and capital[by_capital[pos]] <= money:
            heapq.heappush(affordable, -profit[by_capital[pos]])
            pos += 1
        if not affordable:
            break
        money += -heapq.heappop(affordable)

    return money
```

## Why it works

Sorting by capital lets each project be "unlocked" exactly once, in order, as `money` grows — no project is ever re-examined after it enters the profit max-heap. Within a round, taking the globally best-profit affordable project is safe: money is monotonically non-decreasing, so any project affordable now stays affordable later, meaning deferring a cheap high-profit pick can never help and greedily taking the max is optimal for that round.

## Complexity

- Time: O(n log n + k log n) — sorting once, then each of the n pushes and up to k pops costs O(log n).
- Space: O(n) — the capital ordering and the profit heap.
