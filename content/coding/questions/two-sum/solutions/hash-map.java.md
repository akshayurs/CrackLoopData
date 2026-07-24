Trade memory for speed. Walk the array once, and for each number ask whether the value that completes the pair has already been seen. A `HashMap` answers that in O(1), removing the inner loop.

Record each value's index as you go, so the complement's later appearance yields both positions immediately.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

## Why it works

`seen` maps a value to the index where it appeared. For the current number, its partner must be `target - nums[i]`; if that partner is already a key, the pair is found. Inserting the current value only *after* the check prevents pairing an element with itself, and one pass suffices because a partner is always an earlier element.

## Complexity

- Time: O(n) — one pass; each `HashMap` lookup and insert is O(1) on average.
- Space: O(n) — the map holds up to n entries.
