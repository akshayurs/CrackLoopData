Ignore the rotation entirely and just look at every element. Since we only need to know whether `target` exists, a single walk over the array that compares each value against `target` answers the question directly.

This throws away the sorted structure, but it is the natural baseline and is worth stating before optimizing — it always works regardless of how many duplicates the array holds.

```javascript
function search(nums, target) {
  for (const n of nums) {
    if (n === target) {
      return true;
    }
  }
  return false;
}
```

## Why it works

Membership is a pure existence check. Scanning left to right examines every candidate exactly once, so if `target` is anywhere in `nums` the loop finds it and returns early; otherwise it exhausts the array and returns `false`. Rotation and duplicates are irrelevant to a linear pass.

## Complexity

- Time: O(n) — every element may be inspected once.
- Space: O(1) — no extra storage.
