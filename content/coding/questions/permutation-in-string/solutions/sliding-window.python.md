Re-sorting every window throws away work: consecutive windows differ by only one character leaving and one entering. Track a running frequency count of a fixed-size window instead, and keep a `matches` counter of how many of the 26 letters currently have the exact count `s1` needs.

Slide the window one step at a time. When a character enters or leaves, update its count and adjust `matches` only for that letter. The moment all 26 letters match, the window is a permutation of `s1`.

```python
def check_inclusion(s1, s2):
    n, m = len(s1), len(s2)
    if n > m:
        return False
    need = [0] * 26
    win = [0] * 26
    for c in s1:
        need[ord(c) - 97] += 1
    matches = sum(1 for i in range(26) if need[i] == win[i])
    for i in range(m):
        r = ord(s2[i]) - 97
        win[r] += 1
        matches += 1 if win[r] == need[r] else (-1 if win[r] == need[r] + 1 else 0)
        if i >= n:
            l = ord(s2[i - n]) - 97
            win[l] -= 1
            matches += 1 if win[l] == need[l] else (-1 if win[l] == need[l] - 1 else 0)
        if matches == 26:
            return True
    return False
```

## Why it works

`matches` counts how many letters have `win[c] == need[c]`. Each character add/remove changes one letter's count by one, so `matches` can only shift by one, and we update it in O(1): +1 when the count just became equal, -1 when it just left equality. Once the window holds exactly `n` characters, `matches == 26` means every letter's frequency equals `s1`'s — i.e. the window is a permutation.

## Complexity

- Time: O(m) — each character enters and leaves the window once; alphabet work is constant.
- Space: O(1) — two fixed 26-slot arrays.
