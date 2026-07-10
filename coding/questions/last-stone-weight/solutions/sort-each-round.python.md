The simplest reading of the rules: keep a plain list, and on every round sort it to find the two heaviest stones. Smash them, drop the destroyed one(s), push the leftover weight back in, and repeat.

It costs a full re-sort per round, but it mirrors the problem statement almost line for line — a good baseline before reaching for a heap.

```python
def last_stone_weight(stones):
    stones = list(stones)
    while len(stones) > 1:
        stones.sort()
        heaviest = stones.pop()
        second = stones.pop()
        if heaviest != second:
            stones.append(heaviest - second)
    return stones[0] if stones else 0
```

## Why it works

Sorting after every smash guarantees the last two elements are always the current two heaviest stones. Popping them off and, if they differ, pushing the remainder back keeps the invariant true for the next round. The loop stops once at most one stone remains, which is exactly the answer the problem asks for.

## Complexity

- Time: O(n² log n) — up to n rounds, each paying O(n log n) to re-sort.
- Space: O(n) — the working list of stones.
