The repeated membership scans are the waste. Dump every value into a set once, and each "is this value present?" question becomes an O(1) lookup instead of a full pass.

Build the set from `nums`, then sweep the range `1..n` and collect whatever the set does not contain.

```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> present = new HashSet<>();
        for (int x : nums) present.add(x);
        List<Integer> missing = new ArrayList<>();
        for (int value = 1; value <= nums.length; value++) {
            if (!present.contains(value)) missing.add(value);
        }
        return missing;
    }
}
```

## Why it works

`present` records exactly which values occur, collapsing duplicates automatically. Because the array holds `n` values all inside `[1, n]`, the missing numbers are precisely the members of that range absent from the set — one linear sweep over `1..n` finds them all.

## Complexity

- Time: O(n) — one pass to build the set, one pass over the range.
- Space: O(n) — the set stores up to n distinct values.
