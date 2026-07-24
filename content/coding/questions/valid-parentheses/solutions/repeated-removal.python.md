The most literal reading of "balanced": keep deleting any adjacent matched pair — `()`, `[]`, or `{}` — from the string. If the string collapses down to empty, every bracket found a partner right next to it eventually; if something is left over, it never matched.

This is wasteful (each deletion rescans the string) but it mirrors how you'd explain the rule out loud before reaching for a stack.

```python
def is_valid(s):
    pairs = ["()", "[]", "{}"]
    changed = True
    while changed:
        changed = False
        for pair in pairs:
            if pair in s:
                s = s.replace(pair, "", 1)
                changed = True
    return s == ""
```

## Why it works

Any balanced string can be fully reduced to empty by repeatedly deleting an innermost matched pair — that pair is exactly an adjacent `()`, `[]`, or `{}` somewhere in the string. Each successful deletion shrinks `s`, so the loop terminates; if no adjacent pair remains but `s` is non-empty, the brackets could never have been balanced.

## Complexity

- Time: O(n²) — up to n/2 deletions, each an O(n) scan-and-replace.
- Space: O(n) — `replace` builds a new string each call.
