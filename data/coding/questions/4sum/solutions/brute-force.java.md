The honest baseline: examine every group of four distinct indices and keep those whose values sum to `target`. Four nested loops enumerate all combinations directly.

Sorting first means each combination `i < j < k < l` is already non-decreasing, so a `LinkedHashSet` of value-lists both deduplicates and preserves the lexicographic insertion order. The sum is accumulated as a `long` to avoid 32-bit overflow.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        Set<List<Integer>> found = new LinkedHashSet<>();
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    for (int l = k + 1; l < n; l++)
                        if ((long) nums[i] + nums[j] + nums[k] + nums[l] == target)
                            found.add(Arrays.asList(nums[i], nums[j], nums[k], nums[l]));
        return new ArrayList<>(found);
    }
}
```

## Why it works

The loops walk strictly increasing indices, so each unordered quadruplet of positions is visited once. Because the array is sorted and indices increase, quadruplets are discovered in lexicographic order; the `LinkedHashSet` drops duplicate value-groups while keeping that order. Casting to `long` before adding prevents overflow when four billion-scale values combine.

## Complexity

- Time: O(n^4) — every quadruplet of indices is inspected.
- Space: O(m) — the set holds the m distinct matching quadruplets.
