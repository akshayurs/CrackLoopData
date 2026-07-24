Neighbouring windows overlap in all but one element. Instead of re-adding `k` numbers each time, keep a running sum: when the window slides one step right, add the element entering on the right and subtract the one leaving on the left.

Compare raw sums while sliding (they all share the same divisor `k`) and only divide once at the end — fewer floating-point operations and one clean pass.

```javascript
function maxAverage(nums, k) {
  let windowSum = 0;
  for (let i = 0; i < k; i++) windowSum += nums[i];
  let best = windowSum;
  for (let i = k; i < nums.length; i++) {
    windowSum += nums[i] - nums[i - k];
    best = Math.max(best, windowSum);
  }
  return best / k;
}
```

## Why it works

The first loop builds the sum of the initial window. Each later step advances the window by one: `nums[i]` joins and `nums[i - k]` drops off, so `windowSum` stays the sum of the current block in O(1). All windows share the divisor `k`, so the maximum sum gives the maximum average, and we divide just once.

## Complexity

- Time: O(n) — a single linear pass.
- Space: O(1) — two scalars.
