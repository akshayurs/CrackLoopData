The most literal reading of the rule: keep expanding the innermost `k[...]` group until no brackets remain. An innermost group is a `]` whose matching `[` has no other `[` between them, so its contents are pure letters and can be repeated immediately.

Each pass scans for the first `]`, walks back to its `[`, reads the digits before that `[`, and splices in the repeated text. Repeat until the string is bracket-free. It is the honest baseline you would describe before reaching for a stack.

```python
def decode_string(s):
    while ']' in s:
        close = s.index(']')
        open_ = s.rindex('[', 0, close)
        inner = s[open_ + 1:close]
        j = open_
        while j > 0 and s[j - 1].isdigit():
            j -= 1
        k = int(s[j:open_])
        s = s[:j] + inner * k + s[close + 1:]
    return s
```

## Why it works

The first `]` in the string always closes an innermost group, and the nearest `[` to its left is its partner, so the text between them contains only letters. Reading the run of digits just before that `[` gives the repeat count `k`. Replacing the whole `k[inner]` span with `inner * k` removes exactly one bracket pair while preserving every character outside it. Since each pass eliminates one pair, the loop terminates with a fully decoded string.

## Complexity

- Time: O(m · n) — one pass per bracket pair (m pairs), each rescanning a string up to the final length n.
- Space: O(n) — new strings built during expansion.
