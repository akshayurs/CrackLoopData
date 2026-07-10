The same idea in JavaScript: two nested loops over the array, returning the first pair that reaches the target. Straightforward, with no auxiliary storage.

```javascript
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
}
```

## Why it works

The outer loop fixes the first index; the inner loop scans every later index, so each unordered pair is tested exactly once. The first pair that sums to `target` is returned immediately, and the problem's one-solution guarantee means the final `return []` is never reached.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — no extra structure.
