Fix a left endpoint and grow the subarray to the right, tracking how many distinct values it currently holds with a frequency map. The moment the distinct count reaches exactly `k`, that window is one good subarray; the instant it exceeds `k`, no further extension from this left endpoint can ever come back down, so stop early.

This mirrors the definition directly, which makes it easy to trust — at the cost of re-scanning overlapping windows.

```javascript
function subarraysWithKDistinct(nums, k) {
  const n = nums.length;
  let total = 0;
  for (let i = 0; i < n; i++) {
    const freq = new Map();
    for (let j = i; j < n; j++) {
      freq.set(nums[j], (freq.get(nums[j]) || 0) + 1);
      const distinct = freq.size;
      if (distinct === k) {
        total++;
      } else if (distinct > k) {
        break;
      }
    }
  }
  return total;
}
```

## Why it works

For a fixed left index `i`, extending the right index `j` can only add elements, so the number of distinct values is non-decreasing. Every window `[i, j]` is considered exactly once, and we count it iff its distinct total equals `k`. Once the total passes `k` we break, since it will never drop back to `k` for a larger `j`.

## Complexity

- Time: O(n²) — each of the n left endpoints scans up to n right endpoints.
- Space: O(n) — the frequency map holds at most the distinct values of one window.
