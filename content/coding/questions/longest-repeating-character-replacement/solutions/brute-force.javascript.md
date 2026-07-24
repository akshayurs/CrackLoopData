A substring can be turned into a single repeated letter when the number of letters that are *not* the most common one is at most `k` — those are exactly the positions you would overwrite. So fix a start index, extend the substring one letter at a time, and while extending keep a running count of each letter and the highest count seen. If `windowLength - maxCount <= k`, this window is achievable, so record its length.

Trying every start index and extending to the end checks all substrings without ever building them explicitly.

```javascript
function characterReplacement(s, k) {
  const n = s.length;
  let best = 0;
  for (let i = 0; i < n; i++) {
    const counts = new Array(26).fill(0);
    let maxCount = 0;
    for (let j = i; j < n; j++) {
      const idx = s.charCodeAt(j) - 65;
      counts[idx]++;
      maxCount = Math.max(maxCount, counts[idx]);
      const window = j - i + 1;
      if (window - maxCount <= k) {
        best = Math.max(best, window);
      }
    }
  }
  return best;
}
```

## Why it works

For a fixed window, `window - maxCount` is the count of the least-needed letters, which is the minimum number of replacements to make the whole window one letter. When that value is within `k`, the window is valid. The outer loop anchors every possible start; the inner loop grows the window and updates counts incrementally, so each candidate substring is evaluated in O(1) extra work.

## Complexity

- Time: O(n²) — n start positions, each extended up to n times; the 26-slot count update is constant.
- Space: O(1) — a fixed array of 26 counters.
