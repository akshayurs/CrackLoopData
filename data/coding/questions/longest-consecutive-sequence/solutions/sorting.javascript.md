If the numbers were sorted, consecutive values would sit next to each other, so the longest run becomes a single left-to-right scan. Sort once, then walk the array tracking how long the current increasing-by-one streak is.

The only subtlety is duplicates: when the next value equals the current one it neither extends nor breaks the run, so we just skip past it.

```javascript
function longestConsecutive(nums) {
  if (nums.length === 0) return 0;
  const sorted = [...new Set(nums)].sort((a, b) => a - b);
  let best = 1, current = 1;
  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] === sorted[i - 1] + 1) {
      current += 1;
      best = Math.max(best, current);
    } else {
      current = 1;
    }
  }
  return best;
}
```

## Why it works

After deduping through a `Set` and sorting numerically, the values are unique and ascending. Each adjacent pair is either consecutive (`sorted[i] === sorted[i-1] + 1`), which grows the streak, or has a gap, which resets it to 1. Removing duplicates first eliminates the equal-neighbor case, so a plain adjacency test suffices, and `best` records the longest streak seen.

## Complexity

- Time: O(n log n) — dominated by the sort; the scan afterward is linear.
- Space: O(n) — the deduplicated sorted array.
