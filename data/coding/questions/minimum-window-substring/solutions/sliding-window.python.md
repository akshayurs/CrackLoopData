Restarting the scan from every index repeats work. Instead keep one window with two pointers: push the right edge to gather characters, and once the window covers `t`, pull the left edge inward as far as possible while it still covers `t`. Each pointer only ever moves forward, so the whole string is traversed a constant number of times.

Track coverage with a single `missing` counter — the number of still-needed characters. Let `need[c]` go negative to represent surplus copies; a character is "still needed" only while its count is strictly positive. When `missing` hits zero the current window is valid and we try to shrink it.

```python
from collections import Counter

def min_window(s, t):
    if not t or len(t) > len(s):
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best_left, best_len = 0, float("inf")
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_left, best_len = left, right - left + 1
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best_len == float("inf") else s[best_left:best_left + best_len]
```

## Why it works

Advancing `right` consumes a character; if it was one we still owed, `missing` drops. When `missing == 0` every required character is present, so we record the length and then release the leftmost character. Releasing raises `need[s[left]]`; only when it becomes positive again do we truly lose a required character, ending the shrink. Because both pointers march forward monotonically, every window boundary is examined once.

## Complexity

- Time: O(n + m) — each character enters and leaves the window at most once.
- Space: O(m) — the `need` map holds the distinct characters of `t`.
