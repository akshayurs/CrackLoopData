Instead of restarting for every start index, keep one window that slides across the string. Grow it on the right by adding characters; whenever it holds more than `k` distinct characters, shrink it from the left until it is valid again. Each character enters and leaves the window at most once.

A count map keyed by character tells you how many distinct characters the window currently has: its size. Track the widest valid window seen.

```python
def length_of_longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    counts = {}
    best = 0
    left = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while len(counts) > k:
            left_ch = s[left]
            counts[left_ch] -= 1
            if counts[left_ch] == 0:
                del counts[left_ch]
            left += 1
        best = max(best, right - left + 1)
    return best
```

## Why it works

`counts` always describes the current window `s[left..right]`, and `len(counts)` is its distinct-character count. After each right-side addition, the `while` loop restores the invariant "at most `k` distinct" by discarding characters from the left, deleting a key when its count hits zero. Because `left` and `right` each advance monotonically, every character is added and removed at most once, and every window measured is valid — so the maximum width is the answer.

## Complexity

- Time: O(n) — left and right pointers each traverse the string once.
- Space: O(k) — the map holds at most k + 1 distinct characters.
