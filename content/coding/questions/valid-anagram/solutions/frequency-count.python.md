Anagrams are defined entirely by *how many* of each letter appear — order is irrelevant. So instead of sorting, tally the letters: add one for every character in `s` and subtract one for every character in `t`. If the two strings match, every count cancels back to zero.

This replaces the O(n log n) sort with a single linear pass over each string, using a small map keyed by character.

```python
from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
```

## Why it works

`Counter(s)` records how often each character occurs in `s`, and likewise for `t`. Two strings are anagrams precisely when these frequency tables are identical — same keys, same counts. Comparing the two counters checks exactly that. The length guard is a cheap early exit that also means a difference must show up as a mismatched count rather than a missing letter.

## Complexity

- Time: O(n) — one pass to build each counter, plus a comparison over the distinct keys.
- Space: O(k) — where k is the number of distinct characters (at most 26 for lowercase English letters).
