To drop the extra space, notice that a character's fate depends only on the `#`s that come *after* it. So scan both strings from the right. Keep a `skip` counter: every `#` you meet adds one deletion credit; every real letter either cancels a pending credit (it was backspaced) or is a surviving character you must compare.

Advance both strings to their next surviving character and check they match. When one runs out before the other, the strings differ. No rebuilt strings — just two indices walking backward.

```python
def backspace_compare(s, t):
    def next_valid(string, i):
        skip = 0
        while i >= 0:
            if string[i] == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                break
            i -= 1
        return i

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i, j = next_valid(s, i), next_valid(t, j)
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False
        i, j = i - 1, j - 1
    return True
```

## Why it works

Scanning right-to-left lets each `#` "consume" the nearest not-yet-deleted letter to its left, exactly matching editor behavior. `next_valid` lands on the next character that actually survives. If both pointers find survivors, they must be equal; if only one does, one final text is longer, so the answer is `false`. The loop ends when both are exhausted in lockstep.

## Complexity

- Time: O(m + n) — every character is visited at most once.
- Space: O(1) — only integer indices, no rebuilt strings.
