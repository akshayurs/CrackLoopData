Because the array never changes, do the summing work once up front. Build a `prefix` array where `prefix[i]` holds the sum of the first `i` elements. Then the sum of any window `[left, right]` is just `prefix[right + 1] - prefix[left]` — one subtraction, no scanning.

The extra offset (a leading zero at `prefix[0]`) is what lets the formula handle `left = 0` without a special case.

```javascript
function rangeSum(nums, queries) {
  const prefix = new Array(nums.length + 1).fill(0);
  for (let i = 0; i < nums.length; i++) {
    prefix[i + 1] = prefix[i] + nums[i];
  }
  return queries.map(([left, right]) => prefix[right + 1] - prefix[left]);
}
```

## Why it works

`prefix[i]` equals `nums[0] + ... + nums[i-1]`. Subtracting the sum up to `left` from the sum up to `right + 1` cancels everything before `left` and keeps exactly `nums[left..right]`. The leading zero makes `prefix[left]` well defined even when `left` is 0. Preprocessing is a single pass; every query is then constant work.

## Complexity

- Time: O(n + q) — one pass to build the prefix array, then O(1) per query.
- Space: O(n) — the prefix array holds n + 1 sums.
