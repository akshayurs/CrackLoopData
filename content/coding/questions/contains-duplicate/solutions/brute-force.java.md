The most literal reading of the problem: compare every element against every element that comes after it, and if two match, a duplicate exists. No extra memory, just two nested loops.

It is the honest baseline you would state first in an interview before reaching for anything faster.

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Why it works

The outer loop fixes one element; the inner loop scans every later position, so each unordered pair is examined exactly once. The instant two equal values are found we return `true`; if no pair ever matches, the array is all-distinct and we fall through to `false`.

## Complexity

- Time: O(n²) — about n²/2 pairs are compared.
- Space: O(1) — only loop counters, no extra structure.
