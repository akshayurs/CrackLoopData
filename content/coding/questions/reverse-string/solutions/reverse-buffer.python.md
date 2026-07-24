The most literal approach: read the input from the last character to the first and append each one to a fresh buffer. Whatever was at the end lands at the front of the new string, which is exactly reversal.

It is the honest baseline — no pointer bookkeeping, just walk backwards and collect. The cost is a second buffer the size of the input.

```python
def reverse_string(s):
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return "".join(result)
```

## Why it works

Iterating with index going from `len(s) - 1` down to `0` visits characters in reverse order, and appending preserves that order in `result`. Joining the collected characters yields the input read back-to-front.

## Complexity

- Time: O(n) — one pass over every character.
- Space: O(n) — a separate buffer holds all n characters.
