The direct reading of the problem: try every starting index, then extend the window rightward until it first covers `t`, and remember the shortest cover seen. Once a start position produces a valid window we can stop extending it — growing further only makes that window longer.

Counting requirements with a frequency map lets us compare "how many of each character we have" against "how many we need," so duplicates in `t` are handled correctly.

```python
from collections import Counter

def min_window(s, t):
    if not t or len(t) > len(s):
        return ""
    need = Counter(t)
    best = ""
    for i in range(len(s)):
        window = Counter()
        for j in range(i, len(s)):
            window[s[j]] += 1
            if all(window[c] >= need[c] for c in need):
                if best == "" or j - i + 1 < len(best):
                    best = s[i:j + 1]
                break
    return best
```

## Why it works

`need` records how many copies of each character the window must contain. For a fixed start `i`, we widen the end `j` and stop the instant every requirement is met — that is the shortest valid window beginning at `i`. Comparing lengths across all starts yields the global minimum, and scanning starts left-to-right keeps the earliest window on ties.

## Complexity

- Time: O(n^2) — every start extends across the rest of the string; the coverage check touches only the distinct characters of `t`.
- Space: O(m) — the two frequency maps, where m = len(t).
