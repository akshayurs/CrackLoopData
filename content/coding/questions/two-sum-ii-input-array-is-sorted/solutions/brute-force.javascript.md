The same idea in JavaScript: two nested loops over the array, returning the first pair that reaches the target. It ignores the sorted order, but it is the straightforward starting point with no auxiliary storage.

Since positions are 1-indexed, each returned index is its loop counter plus one.

```javascript
function twoSum(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return [i + 1, j + 1];
      }
    }
  }
  return [];
}
```

## Why it works

The outer loop fixes the first element; the inner loop scans every later element, so each unordered pair is tested exactly once. The first pair that sums to `target` is returned immediately, and the one-solution guarantee means the final `return []` is never reached.

## Complexity

- Time: O(n²) — about n²/2 pairs are checked.
- Space: O(1) — no extra structure.
