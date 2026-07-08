The most literal reading of the problem: for every candidate value in `1..n`, walk the array and ask "is this value here?". Whatever you never find is missing.

It is the baseline you would state first — no auxiliary structure, just a membership scan per candidate.

```python
def find_disappeared_numbers(nums):
    n = len(nums)
    missing = []
    for value in range(1, n + 1):
        found = False
        for x in nums:
            if x == value:
                found = True
                break
        if not found:
            missing.append(value)
    return missing
```

## Why it works

The answer set is defined directly against the range `[1, n]`, so we test each member of that range in turn. The inner loop is an honest linear search that stops at the first match; any value whose search fails never appears in `nums` and belongs in the result.

## Complexity

- Time: O(n²) — up to n candidates, each scanning up to n elements.
- Space: O(1) — ignoring the output list, only a flag and counters.
