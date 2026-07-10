The set version still nudges `left` forward one step at a time. We can jump instead. Remember the last index at which each character appeared; when a character repeats, teleport `left` directly to just past that previous occurrence.

This keeps a single left-to-right pass with no inner loop at all — every index is touched exactly once, and the window boundary never moves backward.

```javascript
function lengthOfLongestSubstring(s) {
  const last = new Map();
  let left = 0;
  let best = 0;
  for (let right = 0; right < s.length; right++) {
    const ch = s[right];
    if (last.has(ch) && last.get(ch) >= left) {
      left = last.get(ch) + 1;
    }
    last.set(ch, right);
    best = Math.max(best, right - left + 1);
  }
  return best;
}
```

## Why it works

`last[ch]` records the most recent index of each character. A duplicate only matters if its previous position lies inside the current window (`last[ch] >= left`); otherwise it is stale and ignored. When it does matter, moving `left` to `last[ch] + 1` drops exactly the offending character, restoring uniqueness in one move. Guarding with `>= left` prevents `left` from ever rewinding.

## Complexity

- Time: O(n) — one pass, each character processed with O(1) map work.
- Space: O(min(n, k)) — the map stores one entry per distinct character.
