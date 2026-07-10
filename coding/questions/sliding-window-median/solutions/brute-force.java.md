The most direct reading of the problem: for every window position, just look at the `k` numbers inside it. Copy that slice, sort it, and read off the middle (or the average of the two middles when `k` is even).

There's no cleverness here — it's a straightforward simulation of the definition. It's a good starting point because it's obviously correct and makes the two-heap optimization easy to justify afterward.

```java
import java.util.Arrays;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        double[] result = new double[n - k + 1];
        for (int i = 0; i + k <= n; i++) {
            int[] window = Arrays.copyOfRange(nums, i, i + k);
            Arrays.sort(window);
            int mid = k / 2;
            result[i] = (k % 2 == 1)
                ? window[mid]
                : ((long) window[mid - 1] + window[mid]) / 2.0;
        }
        return result;
    }
}
```

## Why it works

Sorting the `k` elements currently in the window puts the middle element(s) at fixed positions (`k / 2` for odd `k`, or the pair straddling the center for even `k`), which is exactly the definition of the median. Doing this fresh for every window is slow but never wrong.

## Complexity

- Time: O(n * k log k) — n - k + 1 windows, each requiring an O(k log k) sort.
- Space: O(k) — one window's worth of elements at a time.
