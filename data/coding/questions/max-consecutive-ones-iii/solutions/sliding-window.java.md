Reframe the problem: instead of asking which zeros to flip, ask for the longest window that contains at most `k` zeros — those zeros are exactly the ones you would flip. Slide a window across the array with two pointers, expanding the right edge over every element and counting the zeros inside.

Whenever the window holds more than `k` zeros it has become illegal, so pull the left edge forward until it is legal again. The window never shrinks below the best length seen, so its width at any moment is a candidate answer.

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int zeros = 0;
        int best = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

## Why it works

The window `[left, right]` always maintains the invariant `zeros <= k` after the inner loop, so it is a subarray flippable into all ones. Because `left` only ever moves forward, each index is added once and removed at most once — linear total work. The largest width achieved under the invariant is the answer.

## Complexity

- Time: O(n) — each pointer advances at most n times.
- Space: O(1) — three integer counters.
