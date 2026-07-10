The quadratic cost of the brute force comes from recounting the same value again and again. Tally every value's frequency in a single pass instead: a `HashMap` from value to running count means each element is touched once.

As soon as any count crosses `n / 2` we have the answer, so we can even return early without scanning the rest.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {
        int threshold = nums.length / 2;
        Map<Integer, Integer> counts = new HashMap<>();
        for (int x : nums) {
            int next = counts.getOrDefault(x, 0) + 1;
            counts.put(x, next);
            if (next > threshold) return x;
        }
        return -1;
    }
}
```

## Why it works

The map accumulates exact occurrence counts as we stream through the array. The majority element, by definition, is the only value whose tally can exceed `n / 2`, and it must reach that threshold on some iteration — at which point we return it immediately.

## Complexity

- Time: O(n) — one pass; each map read and write is O(1) on average.
- Space: O(n) — the map may hold up to n distinct keys.
