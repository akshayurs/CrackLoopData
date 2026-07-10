Break the problem into its two halves. First figure out what the degree even is by counting every value; the degree is simply the largest of those counts. Then the answer must be a window that contains all occurrences of *some* value whose count equals the degree.

So for each value that hits the degree, the tightest window covering it runs from its first appearance to its last. Locate those two positions directly and take the shortest such span.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) count.merge(n, 1, Integer::sum);
        int degree = 0;
        for (int c : count.values()) degree = Math.max(degree, c);
        int best = nums.length;
        for (Map.Entry<Integer, Integer> e : count.entrySet()) {
            if (e.getValue() == degree) {
                int value = e.getKey(), first = -1, last = -1;
                for (int i = 0; i < nums.length; i++) {
                    if (nums[i] == value) {
                        if (first == -1) first = i;
                        last = i;
                    }
                }
                best = Math.min(best, last - first + 1);
            }
        }
        return best;
    }
}
```

## Why it works

Any subarray matching the degree must contain every copy of at least one maximal-frequency value, so its length is at least `last - first + 1` for that value. Conversely, the slice from first to last occurrence *does* contain all copies of that value and therefore has the full degree. Minimising over all degree-achieving values gives the shortest valid window.

## Complexity

- Time: O(n²) — for each degree-achieving value we re-scan the array to find its first and last index.
- Space: O(n) — the count map holds up to n distinct values.
