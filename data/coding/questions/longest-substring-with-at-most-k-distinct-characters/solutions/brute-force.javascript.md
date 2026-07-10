Start from the definition directly: try every possible starting index, extend the substring one character at a time, and track how many distinct characters it currently holds. As soon as a window would exceed `k` distinct characters, stop extending that start and move to the next one.

This inspects every substring, so it is quadratic, but it mirrors the problem statement exactly and makes a clean baseline.

```javascript
function lengthOfLongestSubstringKDistinct(s, k) {
  if (k === 0) return 0;
  let best = 0;
  const n = s.length;
  for (let start = 0; start < n; start++) {
    const counts = new Map();
    for (let end = start; end < n; end++) {
      counts.set(s[end], (counts.get(s[end]) || 0) + 1);
      if (counts.size > k) break;
      best = Math.max(best, end - start + 1);
    }
  }
  return best;
}
```

## Why it works

Fixing `start` and growing `end` enumerates every substring that begins at `start`. The `counts` map tracks distinct characters in the current window; once it exceeds `k`, all longer windows from the same start are invalid too, so breaking early is safe. The running maximum over valid windows gives the answer.

## Complexity

- Time: O(n^2) — up to n starts, each scanning up to n characters.
- Space: O(k) — the map holds at most k + 1 distinct characters.
