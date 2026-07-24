The sum of `nums[i..j]` is a multiple of `k` exactly when the two prefix sums bounding it leave the **same remainder** modulo `k` — because their difference is then divisible by `k`. So instead of enumerating windows, track the running prefix sum's remainder and remember the earliest index at which each remainder first appeared.

When a remainder shows up again at least two positions later, the elements in between form a good subarray. Seeding the map with remainder `0` at index `-1` lets a prefix that is itself a multiple of `k` match cleanly, and keeping only the *first* occurrence of each remainder maximizes the gap so we never miss a length-2 window.

```javascript
function checkSubarraySum(nums, k) {
  const firstSeen = new Map([[0, -1]]);
  let running = 0;
  for (let i = 0; i < nums.length; i++) {
    running = (running + nums[i]) % k;
    if (firstSeen.has(running)) {
      if (i - firstSeen.get(running) >= 2) {
        return true;
      }
    } else {
      firstSeen.set(running, i);
    }
  }
  return false;
}
```

## Why it works

`firstSeen[r]` holds the earliest index where the prefix sum had remainder `r`. If the current prefix has that same remainder `r`, the block strictly after the stored index up to `i` sums to a multiple of `k`. We only accept it when the index gap is at least two, enforcing the length requirement. Storing only the first occurrence guarantees the widest possible gap, so any qualifying window is found.

## Complexity

- Time: O(n) — one pass, each remainder lookup and insert is O(1) on average.
- Space: O(min(n, k)) — at most one entry per distinct remainder.
