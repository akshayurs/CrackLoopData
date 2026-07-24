Neighbouring windows overlap in all but one element. Instead of re-adding `k` numbers each time, keep a running sum: when the window slides one step right, add the element entering on the right and subtract the one leaving on the left.

Compare raw sums while sliding (they all share the same divisor `k`) and only divide once at the end. A `long` accumulator avoids overflow, and deferring the division keeps the loop integer-only.

```java
class Solution {
    public double maxAverage(int[] nums, int k) {
        long windowSum = 0;
        for (int i = 0; i < k; i++) windowSum += nums[i];
        long best = windowSum;
        for (int i = k; i < nums.length; i++) {
            windowSum += nums[i] - nums[i - k];
            best = Math.max(best, windowSum);
        }
        return (double) best / k;
    }
}
```

## Why it works

After the priming loop, `windowSum` is the sum of the first `k` elements. Each iteration slides the window one step by adding `nums[i]` and removing `nums[i - k]`, an O(1) update that preserves the invariant. Every window shares the divisor `k`, so the largest sum is the largest average; the single cast-and-divide at the end produces the result.

## Complexity

- Time: O(n) — one pass, O(1) per slide.
- Space: O(1) — a running sum and best.
