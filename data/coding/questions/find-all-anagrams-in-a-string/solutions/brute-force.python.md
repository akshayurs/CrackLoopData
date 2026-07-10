An anagram is defined purely by letter frequencies, so build a frequency signature for `p` once and compare it against the signature of every length-`|p|` window in `s`. If two strings have identical letter counts, one is an anagram of the other.

The direct version recomputes the window's counts from scratch at each position. It is easy to reason about and a natural first cut before optimizing.

```python
from collections import Counter

def find_anagrams(s, p):
    m = len(p)
    if m > len(s):
        return []
    target = Counter(p)
    result = []
    for i in range(len(s) - m + 1):
        if Counter(s[i:i + m]) == target:
            result.append(i)
    return result
```

## Why it works

`Counter(p)` captures exactly which letters `p` contains and how many of each. A substring is an anagram of `p` if and only if its `Counter` equals `target`. Sliding a window of width `m` across every valid start position and testing this equality finds all matches, and because we scan left to right the indices come out in ascending order.

## Complexity

- Time: O(n * m) — for each of the ~n start positions we build and compare a count over m characters.
- Space: O(1) — the counters hold at most 26 distinct lowercase letters.
