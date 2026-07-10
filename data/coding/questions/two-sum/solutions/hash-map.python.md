Trade memory for speed. Walk the array once, and for each number ask: "have I already seen the value that completes this pair?" A hash map answers that in O(1), collapsing the inner loop.

Store each value's index as you go, so when its complement appears later you can return both positions at once.

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
```

## Why it works

`seen` maps a value to the index where it appeared. For the current number `n`, its partner must be `target - n`; if that partner is already in `seen`, the pair is found. Because `n` is recorded only *after* the check, an element is never paired with itself. One pass suffices — the partner of any element is always one that came before it.

## Complexity

- Time: O(n) — one pass; each lookup and insert is O(1) on average.
- Space: O(n) — the map holds up to n entries.
