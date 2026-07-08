Handle each query independently. For a value `x` from `nums1`, locate it in `nums2`, then walk rightward from that position looking for the first value larger than `x`. The first hit is the answer; running off the end means there is none, so record `-1`.

This mirrors the definition directly with two nested scans and no extra data structures.

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            int x = nums1[i];
            int start = 0;
            while (nums2[start] != x) start++;
            int greater = -1;
            for (int j = start + 1; j < nums2.length; j++) {
                if (nums2[j] > x) {
                    greater = nums2[j];
                    break;
                }
            }
            ans[i] = greater;
        }
        return ans;
    }
}
```

## Why it works

Because the values are distinct, the first scan lands on the exact position of `x` in `nums2`. Scanning strictly to the right and stopping at the first larger value yields the next greater element by definition; if the scan finishes without a hit, `-1` correctly signals that none exists.

## Complexity

- Time: O(n * m) — for each of the n elements in `nums1`, locating it and scanning right each cost up to m, the length of `nums2`.
- Space: O(1) — only the output array, no auxiliary storage.
