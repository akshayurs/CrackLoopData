The most literal reading of the rule: keep expanding the innermost `k[...]` group until no brackets remain. An innermost group is a `]` whose matching `[` has no other `[` between them, so its contents are pure letters and can be repeated immediately.

Each pass scans for the first `]`, walks back to its `[`, reads the digits before that `[`, and splices in the repeated text. Repeat until the string is bracket-free. It is the honest baseline you would describe before reaching for a stack.

```javascript
function decodeString(s) {
  while (s.includes(']')) {
    const close = s.indexOf(']');
    const open = s.lastIndexOf('[', close);
    const inner = s.slice(open + 1, close);
    let j = open;
    while (j > 0 && s[j - 1] >= '0' && s[j - 1] <= '9') j--;
    const k = parseInt(s.slice(j, open), 10);
    s = s.slice(0, j) + inner.repeat(k) + s.slice(close + 1);
  }
  return s;
}
```

## Why it works

The first `]` in the string always closes an innermost group, and the nearest `[` to its left is its partner, so the text between them contains only letters. Reading the run of digits just before that `[` gives the repeat count `k`. Replacing the whole `k[inner]` span with `inner` repeated `k` times removes exactly one bracket pair while preserving every character outside it. Since each pass eliminates one pair, the loop terminates with a fully decoded string.

## Complexity

- Time: O(m · n) — one pass per bracket pair (m pairs), each rescanning a string up to the final length n.
- Space: O(n) — new strings built during expansion.
