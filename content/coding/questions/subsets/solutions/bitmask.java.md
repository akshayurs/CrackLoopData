Every subset of an `n`-element array corresponds to one of the `2^n` binary strings of length `n` — bit `i` set means "include `nums[i]`". Loop a counter from `0` to `2^n - 1` and read off its bits to build each subset directly, with no recursion at all.

It's the most mechanical way to enumerate a power set, and a good baseline before reaching for backtracking.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for (int mask = 0; mask < (1 << n); mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) subset.add(nums[i]);
            }
            result.add(subset);
        }
        result.sort((a, b) -> {
            if (a.size() != b.size()) return a.size() - b.size();
            for (int i = 0; i < a.size(); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return 0;
        });
        return result;
    }
}
```

## Why it works

Each of the `2^n` values of `mask` is a unique bit pattern, and each bit pattern selects a unique combination of elements — so the loop visits every subset exactly once. Sorting by length then contents afterward just fixes a canonical order; it doesn't change which subsets are found.

## Complexity

- Time: O(n * 2^n) — 2^n masks, each scanned in O(n) to build its subset (plus a sort).
- Space: O(n * 2^n) — the output holds all subsets, each up to length n.
