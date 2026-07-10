Trade a little memory for a single pass. Walk the array once, keeping a set of everything seen so far. Before recording a value, check whether it is already in the set — if so, that value is a duplicate.

The set gives O(1) membership tests, so we never need the nested loop or a sort; the answer often comes long before the array ends.

```python
def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

## Why it works

`seen` holds exactly the values encountered before the current one. If `n` is already present, we have met it earlier in the same array, which is precisely the definition of a duplicate. Because we add `n` only after the check, a value is never mistaken for a copy of itself. If the loop finishes, no value was ever seen twice.

## Complexity

- Time: O(n) — one pass; each set lookup and insert is O(1) on average.
- Space: O(n) — the set may hold every distinct value.
