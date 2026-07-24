If the numbers were sorted, consecutive values would sit next to each other, so the longest run becomes a single left-to-right scan. Sort once, then walk the array tracking how long the current increasing-by-one streak is.

The only subtlety is duplicates: when the next value equals the current one it neither extends nor breaks the run, so we skip past it without changing the streak.

```java
import java.util.Arrays;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        int best = 1, current = 1;
        for (int i = 1; i < sorted.length; i++) {
            if (sorted[i] == sorted[i - 1]) continue;
            if (sorted[i] == sorted[i - 1] + 1) {
                current++;
                best = Math.max(best, current);
            } else {
                current = 1;
            }
        }
        return best;
    }
}
```

## Why it works

Once sorted, values are ascending. Equal neighbors are skipped so a duplicate never disturbs the streak; a true consecutive pair (`sorted[i] == sorted[i-1] + 1`) grows `current`, and any gap resets it to 1. `best` tracks the longest streak observed across the scan.

## Complexity

- Time: O(n log n) — dominated by `Arrays.sort`; the scan afterward is linear.
- Space: O(n) — the cloned array (O(1) extra if the input may be sorted in place).
