The same idea in JavaScript: two nested loops over the array, XORing every pair and keeping the best result. Straightforward, with no auxiliary storage.

```javascript
function maxXor(nums) {
  let best = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      best = Math.max(best, nums[i] ^ nums[j]);
    }
  }
  return best;
}
```

## Why it works

The outer loop fixes the first element; the inner loop pairs it with every later element, so every unordered pair is XORed exactly once. Keeping a running maximum over all of them yields the overall answer once the loops finish.

## Complexity

- Time: O(n²) — every pair is XORed once.
- Space: O(1) — only a running maximum.
