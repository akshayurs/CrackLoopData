The most direct reading of the problem: there are `n - k + 1` window positions, so visit each one and take the max of its `k` elements with an inner scan.

This repeats work — neighbouring windows share `k - 1` elements — but it is the natural first pass and a clean correctness baseline.

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n - k + 1];
        for (int start = 0; start + k <= n; start++) {
            int best = nums[start];
            for (int j = start + 1; j < start + k; j++) {
                if (nums[j] > best) best = nums[j];
            }
            result[start] = best;
        }
        return result;
    }
}
```

## Why it works

`start` walks every valid left edge, from `0` up to `n - k`. The inner loop scans that window's `k` elements and keeps the largest in `best`. Writing each `best` in order fills the result array with the answer sequence.

## Complexity

- Time: O(n·k) — each of the ~n windows costs O(k) to scan.
- Space: O(1) — only a running max beyond the output array.
