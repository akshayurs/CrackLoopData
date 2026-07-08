Sort the array first. Once the numbers are ordered, fix the smallest member of the triplet with an index `i`, then hunt for the other two with a classic two-pointer sweep over the remaining suffix: a left pointer just after `i` and a right pointer at the end. If the running sum is too small move left rightward, if too large move right leftward, and when it hits zero record the triplet.

Sorting also makes de-duplication cheap: identical values sit next to each other, so we skip over repeats of `i`, and of both pointers after a match. Because we always emit `[nums[i], nums[left], nums[right]]` in increasing order and advance `i` upward, the triplets come out already in canonical order.

```javascript
function threeSum(nums) {
  nums.sort((a, b) => a - b);
  const n = nums.length;
  const result = [];
  for (let i = 0; i < n - 2; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1, right = n - 1;
    while (left < right) {
      const total = nums[i] + nums[left] + nums[right];
      if (total < 0) {
        left++;
      } else if (total > 0) {
        right--;
      } else {
        result.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;
        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      }
    }
  }
  return result;
}
```

## Why it works

With `nums[i]` fixed, we need two later numbers summing to `-nums[i]`. On a sorted suffix the two-pointer scan finds every such pair in one linear pass: increasing `left` only grows the sum and decreasing `right` only shrinks it, so no valid pair is ever skipped. Skipping equal neighbors for `i`, `left`, and `right` guarantees each distinct triplet is emitted once. Since `nums[i] <= nums[left] <= nums[right]` always holds and `i` scans upward, no post-sort of the output is needed.

## Complexity

- Time: O(n²) — the initial sort is O(n log n), then each of the n anchors drives an O(n) two-pointer pass.
- Space: O(1) — ignoring the output list and the in-place sort, only a few pointers are used.
