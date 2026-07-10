Instead of restarting for every start index, keep a single window that slides across the string. Grow it on the right by adding characters; whenever it holds more than `k` distinct characters, shrink it from the left until it is valid again. Each character enters and leaves the window at most once.

A count map keyed by character reports the window's distinct-character count as its size. Track the widest valid window seen.

```javascript
function lengthOfLongestSubstringKDistinct(s, k) {
  if (k === 0) return 0;
  const counts = new Map();
  let best = 0;
  let left = 0;
  for (let right = 0; right < s.length; right++) {
    const ch = s[right];
    counts.set(ch, (counts.get(ch) || 0) + 1);
    while (counts.size > k) {
      const leftCh = s[left];
      counts.set(leftCh, counts.get(leftCh) - 1);
      if (counts.get(leftCh) === 0) counts.delete(leftCh);
      left++;
    }
    best = Math.max(best, right - left + 1);
  }
  return best;
}
```

## Why it works

`counts` always describes the current window `s[left..right]`, and its size is the distinct-character count. After each right-side addition, the `while` loop restores the "at most `k` distinct" invariant by dropping characters from the left, deleting a key when its count reaches zero. Since `left` and `right` only move forward, each character is added and removed at most once, and every measured window is valid — so the maximum width is the answer.

## Complexity

- Time: O(n) — left and right pointers each traverse the string once.
- Space: O(k) — the map holds at most k + 1 distinct characters.
