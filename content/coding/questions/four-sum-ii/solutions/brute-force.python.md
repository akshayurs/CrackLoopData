Start from the definition: try every way to pick one element from each array and count the combinations that sum to zero. Four nested loops enumerate all `n⁴` tuples directly.

This is the reference implementation — obviously correct, but it grows far too fast to survive large inputs. It is the baseline the optimal solution improves on.

```python
def four_sum_count(a, b, c, d):
    count = 0
    for x in a:
        for y in b:
            for z in c:
                for w in d:
                    if x + y + z + w == 0:
                        count += 1
    return count
```

## Why it works

Each loop walks one array end to end, so the four loops together visit every possible tuple of indices exactly once. Whenever the four chosen values add to zero, the tuple is counted. Because indices are independent, reusing equal values across arrays is handled naturally.

## Complexity

- Time: O(n⁴) — one iteration per tuple across the four arrays.
- Space: O(1) — only a running counter is kept.
