Restarting the scan from every index repeats work. Instead keep one window with two pointers: push the right edge to gather characters, and once the window covers `t`, pull the left edge inward as far as possible while it still covers `t`. Each pointer only ever moves forward, so the whole string is traversed a constant number of times.

Track coverage with a single `missing` counter — the number of still-needed characters. Let `need` counts go negative to represent surplus copies; a character is "still needed" only while its count is strictly positive. When `missing` hits zero the current window is valid and we try to shrink it.

```javascript
function minWindow(s, t) {
  if (t.length === 0 || t.length > s.length) return "";
  const need = new Map();
  for (const c of t) need.set(c, (need.get(c) || 0) + 1);
  let missing = t.length;
  let left = 0, bestLeft = 0, bestLen = Infinity;
  for (let right = 0; right < s.length; right++) {
    const ch = s[right];
    if ((need.get(ch) || 0) > 0) missing--;
    need.set(ch, (need.get(ch) || 0) - 1);
    while (missing === 0) {
      if (right - left + 1 < bestLen) { bestLeft = left; bestLen = right - left + 1; }
      const lc = s[left];
      need.set(lc, need.get(lc) + 1);
      if (need.get(lc) > 0) missing++;
      left++;
    }
  }
  return bestLen === Infinity ? "" : s.slice(bestLeft, bestLeft + bestLen);
}
```

## Why it works

Advancing `right` consumes a character; if it was one we still owed, `missing` drops. When `missing === 0` every required character is present, so we record the length and then release the leftmost character. Releasing raises its `need` count; only when it becomes positive again do we truly lose a required character, ending the shrink. Because both pointers march forward monotonically, every window boundary is examined once.

## Complexity

- Time: O(n + m) — each character enters and leaves the window at most once.
- Space: O(m) — the `need` map holds the distinct characters of `t`.
