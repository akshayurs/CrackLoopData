The most direct reading of the problem: if the array were sorted from largest to smallest, the k-th largest element would simply sit at index `k - 1`. So sort it, then read off that position.

It is the honest baseline you would state first in an interview, before optimizing away the full sort.

```java
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int kthLargest(int[] nums, int k) {
        Integer[] boxed = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed, Collections.reverseOrder());
        return boxed[k - 1];
    }
}
```

## Why it works

Sorting in descending order places the largest value at index 0, the second-largest at index 1, and so on — so the k-th largest lands exactly at index `k - 1`. Duplicates are kept as separate entries by the sort, which matches the problem's "not distinct" rule.

## Complexity

- Time: O(n log n) — dominated by the sort.
- Space: O(n) — boxing into `Integer[]` for the custom comparator.
