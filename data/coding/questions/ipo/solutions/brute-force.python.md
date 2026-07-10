Simulate the process literally. At each of the `k` rounds, scan every project that hasn't been used yet, keep only the ones whose `capital` the company can currently afford, and greedily take the affordable one with the largest `profit`. Add that profit to the money and mark the project used.

This mirrors the problem statement exactly — no cleverness, just "look at everything, pick the best affordable option, repeat" — so it's a solid first pass before optimizing the repeated scanning.

```python
def max_capital(k, w, profit, capital):
    n = len(profit)
    used = [False] * n
    money = w

    for _ in range(k):
        best = -1
        for i in range(n):
            if not used[i] and capital[i] <= money:
                if best == -1 or profit[i] > profit[best]:
                    best = i
        if best == -1:
            break
        money += profit[best]
        used[best] = True

    return money
```

## Why it works

Each round is a local greedy choice: among everything currently affordable, taking the largest profit can never hurt, because money only grows and every affordable project stays affordable (or more so) later. Doing this `k` times, re-scanning from scratch each round, reproduces the optimal simulation — it's just slow because affordability and "used" status are recomputed every round instead of tracked incrementally.

## Complexity

- Time: O(k * n) — each of the `k` rounds rescans all `n` projects.
- Space: O(n) — the `used` array.
