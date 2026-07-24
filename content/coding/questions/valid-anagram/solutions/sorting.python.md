Two strings are anagrams exactly when their letters, laid out in a canonical order, are identical. Sorting is the simplest way to reach that canonical form: put both strings in sorted order and see if they match.

It is the honest baseline you would reach for first in an interview — no counting, no bookkeeping, just compare the sorted characters. A quick length check up front rules out the obvious non-anagrams before doing any work.

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

## Why it works

If `t` is a rearrangement of `s`, then sorting both collapses every rearrangement to the same sequence of characters, so the sorted lists are equal. If they differ in any letter or in how many times a letter appears, the sorted forms diverge at some position and the comparison fails. The length guard is an early exit — strings of unequal length can never be anagrams.

## Complexity

- Time: O(n log n) — dominated by sorting both strings.
- Space: O(n) — `sorted` builds a new list of characters for each string.
