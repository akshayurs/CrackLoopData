Keep a window that grows on the right and shrinks on the left. Extend the right edge, adding each new value to a running sum. Whenever the sum reaches `target`, the window qualifies — so record its length and then shrink from the left as far as you can while it still qualifies, hunting for the shortest valid window ending here.

Every element enters the window once and leaves at most once, so the two pointers sweep the array in a single linear pass.

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int best = n + 1;
        int left = 0;
        long total = 0;
        for (int right = 0; right < n; right++) {
            total += nums[right];
            while (total >= target) {
                best = Math.min(best, right - left + 1);
                total -= nums[left];
                left++;
            }
        }
        return best <= n ? best : 0;
    }
}
```

## Why it works

For each right end the inner loop pulls `left` forward until the window sum drops below `target`, so the recorded length is the shortest window ending at `right`. Positive values make the sum monotonic as the window changes, so shrinking is always safe: once the sum falls short, no further shrink helps. The minimum over all right ends is the global answer.

## Complexity

- Time: O(n) — `left` and `right` each advance at most n times.
- Space: O(1) — only pointers and a running sum.
