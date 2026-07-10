The values live in `[1, n]` and the indices live in `[0, n-1]` — a value `v` maps naturally to slot `v - 1`. That lets the array double as its own presence tracker, so we can drop the extra set entirely.

Walk the array and, for each value seen, flip the sign of the number sitting at its target slot to mark "this value occurred". A second pass then reports every slot that is still positive: those slots were never marked, so their `index + 1` never appeared.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int x : nums) {
            int idx = Math.abs(x) - 1;
            if (nums[idx] > 0) nums[idx] = -nums[idx];
        }
        List<Integer> missing = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) missing.add(i + 1);
        }
        return missing;
    }
}
```

## Why it works

Using `Math.abs(x)` means earlier sign flips never corrupt the value we still need to read. Marking slot `v - 1` negative is a permanent "value `v` is present" stamp. After the pass, a positive entry at index `i` proves no value ever mapped to it, so `i + 1` is one of the disappeared numbers.

## Complexity

- Time: O(n) — two linear passes.
- Space: O(1) — the marks are stored in the input array itself; only the output list is allocated.
