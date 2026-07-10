The honest baseline: examine every combination of three distinct indices and keep the ones that sum to zero. The same three values can be reached through different index combinations, so we canonicalize each hit by sorting its three numbers into a list and adding it to a set.

At the end we sort the collected triplets so the output is deterministic, matching the canonical order the problem asks for.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Set<List<Integer>> found = new LinkedHashSet<>();
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        int[] t = {nums[i], nums[j], nums[k]};
                        Arrays.sort(t);
                        found.add(Arrays.asList(t[0], t[1], t[2]));
                    }
        List<List<Integer>> result = new ArrayList<>(found);
        result.sort((a, b) -> a.get(0) != b.get(0) ? a.get(0) - b.get(0)
                : a.get(1) != b.get(1) ? a.get(1) - b.get(1) : a.get(2) - b.get(2));
        return result;
    }
}
```

## Why it works

Every unordered triple of indices is visited exactly once by the three nested loops. Sorting each zero-sum triple before adding it to the set collapses permutations of the same three values into one element, so duplicates never survive. The final comparator sorts triplets lexicographically for the required canonical ordering.

## Complexity

- Time: O(n³) — every triple of indices is tested.
- Space: O(m) — the set holds the m unique triplets found.
