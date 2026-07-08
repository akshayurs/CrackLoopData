Trade a little memory for a single pass. Walk the array once, keeping a set of everything seen so far. Before recording a value, check whether it is already in the set — if so, that value is a duplicate.

The set gives O(1) membership tests, so we never need the nested loop or a sort; the answer often comes long before the array ends. `HashSet.add` even returns `false` when the value was already present, so the check and insert can be a single call.

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int n : nums) {
            if (!seen.add(n)) {
                return true;
            }
        }
        return false;
    }
}
```

## Why it works

`seen` holds exactly the values encountered before the current one. `add` inserts `n` and returns `false` if it was already there — meaning we met it earlier in the array, which is exactly a duplicate. If every `add` succeeds, no value was ever seen twice.

## Complexity

- Time: O(n) — one pass; each set lookup and insert is O(1) on average.
- Space: O(n) — the set may hold every distinct value.
