Explore every way of including or excluding each position: at index `i` you either take `candidates[i]` and move on, or skip it and move on. That generates every subset of the array. Whenever a subset's running sum hits the target, record it.

Because the array can hold duplicate values, different subsets of indices can produce the identical list of numbers — so the raw results need deduplication. Sorting the candidates first, then collecting each hit as a tuple in a set, cleans that up before the final sort into the required order.

```python
def combination_sum2(candidates, target):
    candidates.sort()
    n = len(candidates)
    seen = set()
    path = []

    def backtrack(i, remaining):
        if remaining == 0:
            seen.add(tuple(path))
            return
        if remaining < 0 or i == n:
            return
        path.append(candidates[i])
        backtrack(i + 1, remaining - candidates[i])
        path.pop()
        backtrack(i + 1, remaining)

    backtrack(0, target)
    return sorted(list(c) for c in seen)
```

## Why it works

Every combination is exactly one path through the include/exclude decision tree over indices, so no valid subset is missed. Sorting `candidates` up front means each recorded tuple already lists its numbers in ascending order; routing everything through a `set` collapses duplicate combinations that arose from different duplicate-valued indices, and the final `sorted(...)` puts the combinations themselves in ascending order.

## Complexity

- Time: O(2^n · n log n) — every index is included or excluded, and each of the up to 2^n paths costs O(n log n) to sort/hash into the result.
- Space: O(2^n · n) — the set can hold up to 2^n combinations of length up to n.
