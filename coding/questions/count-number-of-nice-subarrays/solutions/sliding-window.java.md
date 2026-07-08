Counting subarrays with *exactly* `k` odds directly is fiddly, but counting subarrays with *at most* `m` odds is a textbook sliding window: grow the right edge, and whenever the window holds more than `m` odds shrink from the left. Every valid right position contributes `right - left + 1` subarrays ending there.

The exact answer then falls out of a subtraction: `atMost(k) - atMost(k - 1)` removes the subarrays that have `k - 1` or fewer odds, leaving only those with precisely `k`.

```java
class Solution {
    public int countNiceSubarrays(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    private int atMost(int[] nums, int m) {
        if (m < 0) return 0;
        int left = 0, odds = 0, res = 0;
        for (int right = 0; right < nums.length; right++) {
            odds += nums[right] & 1;
            while (odds > m) {
                odds -= nums[left] & 1;
                left++;
            }
            res += right - left + 1;
        }
        return res;
    }
}
```

## Why it works

For a fixed `right`, once `left` is the smallest index keeping the window within `m` odds, every subarray starting at `left..right` is valid, giving `right - left + 1` of them. Summing over all right ends counts all subarrays with at most `m` odds. Since every subarray has some odd count, the set with exactly `k` odds equals those with at most `k` minus those with at most `k - 1`.

## Complexity

- Time: O(n) — `atMost` moves each pointer forward at most n times; two calls stay linear.
- Space: O(1) — only pointers and counters.
