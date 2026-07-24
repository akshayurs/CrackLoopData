The rotation only rearranges where the sorted order wraps around; it does not hide any element. So the most direct approach ignores the structure entirely and simply looks at every position, returning the first index whose value equals the target.

This throws away the `O(log n)` opportunity, but it is a useful baseline: it always works, needs no reasoning about pivots, and is easy to get right.

```java
class Solution {
    public int search(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
```

## Why it works

Every element is inspected exactly once. Because the values are distinct, the first match is the only match, so returning its index is correct. If the loop finishes without a hit, the target is absent and we return `-1`.

## Complexity

- Time: O(n) — one pass over the array in the worst case.
- Space: O(1) — no extra storage.
