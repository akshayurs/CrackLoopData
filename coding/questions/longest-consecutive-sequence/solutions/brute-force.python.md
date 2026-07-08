The most literal reading: for every value in the array, pretend it is the start of a run and keep asking "is the next integer here too?" Each lookup scans the whole array, and we grow the run one step at a time until the next value is missing.

No extra data structures, no sorting — just repeated linear searches. It is the honest baseline you would state before reaching for something faster.

```python
def longest_consecutive(nums):
    best = 0
    for start in nums:
        if start - 1 in nums:
            continue
        length = 1
        while start + length in nums:
            length += 1
        best = max(best, length)
    return best
```

## Why it works

A value only begins a run if `start - 1` is absent, so we skip interior values and only count each run from its true left end. From a start we walk `start + 1`, `start + 2`, … using membership checks against the list, extending `length` until the chain breaks. The largest length seen wins. The `in` test on a list is itself a linear scan, which is what makes this slow.

## Complexity

- Time: O(n³) — for each of n values we may walk a run of length up to n, and every membership check scans the n-element list.
- Space: O(1) — only counters, no auxiliary structure.
