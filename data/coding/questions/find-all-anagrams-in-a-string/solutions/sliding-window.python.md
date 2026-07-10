Consecutive windows overlap almost entirely: moving one step to the right drops a single character on the left and adds one on the right. So instead of rebuilding the count every time, keep a running frequency array for the current window and patch it in O(1) per move. Track how many of the 26 letters currently match the target's count exactly; when all 26 match, the window is an anagram.

Maintaining a single `matches` counter avoids re-scanning all 26 buckets on every step, so each slide is truly constant work.

```python
def find_anagrams(s, p):
    m, n = len(p), len(s)
    if m > n:
        return []
    need = [0] * 26
    win = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1
    matches = sum(1 for i in range(26) if need[i] == 0)
    result = []
    for i in range(n):
        r = ord(s[i]) - 97
        win[r] += 1
        if win[r] == need[r]:
            matches += 1
        elif win[r] == need[r] + 1:
            matches -= 1
        if i >= m:
            l = ord(s[i - m]) - 97
            win[l] -= 1
            if win[l] == need[l]:
                matches += 1
            elif win[l] == need[l] - 1:
                matches -= 1
        if matches == 26:
            result.append(i - m + 1)
    return result
```

## Why it works

`matches` counts how many of the 26 letters have `win[c] == need[c]`. Adding the incoming character and removing the outgoing one each shift at most one bucket, so we only adjust `matches` when that bucket crosses into or out of equality. Once the window has reached full width (`i >= m - 1`) and all 26 buckets agree, its letters are exactly those of `p`, so `i - m + 1` is a valid start. The scan runs left to right, producing ascending indices.

## Complexity

- Time: O(n) — one pass; every character enters and leaves the window once with O(1) bookkeeping.
- Space: O(1) — two fixed arrays of 26 counts.
