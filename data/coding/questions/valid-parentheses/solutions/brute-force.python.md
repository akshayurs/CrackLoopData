A valid string always contains at least one *innermost* pair — two adjacent matching brackets like `()`, `[]`, or `{}` with nothing between them. Removing such a pair leaves a string that is valid exactly when the original was. So repeatedly strip out every adjacent matched pair; if the string collapses to empty, it was balanced.

This is the naive approach: it keeps rescanning and shrinking the string until no more pairs can be removed. Anything left over is an unmatched or mis-ordered bracket.

```python
def is_valid(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""
```

## Why it works

Erasing an innermost pair never breaks the balance of the surrounding brackets — the neighbours that were separated by it become adjacent and can match on the next round. Each pass removes at least one pair until none remain. A truly balanced string reduces all the way to empty; any leftover character is a bracket that could never find its partner.

## Complexity

- Time: O(n^2) — each `replace` scan is O(n) and up to O(n) passes may be needed.
- Space: O(n) — a new string is built on every removal pass.
