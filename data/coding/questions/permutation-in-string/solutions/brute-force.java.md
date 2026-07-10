A permutation of `s1` is any string with the exact same multiset of characters. So the most direct check is: slide a window of length `s1.length()` across `s2`, and for each window ask whether its characters are a rearrangement of `s1`'s. Sorting both strings turns "same multiset" into "equal after sorting".

Compare every window's sorted form against the sorted `s1`. If any window matches, a permutation is present.

```java
import java.util.Arrays;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        if (n > m) return false;
        char[] target = s1.toCharArray();
        Arrays.sort(target);
        for (int i = 0; i + n <= m; i++) {
            char[] window = s2.substring(i, i + n).toCharArray();
            Arrays.sort(window);
            if (Arrays.equals(window, target)) return true;
        }
        return false;
    }
}
```

## Why it works

Two strings are permutations of each other exactly when their sorted character sequences are identical. The loop considers every starting position where a length-`n` window fits, so if any substring of that length is a permutation of `s1`, it is found. The early `n > m` guard rules out the impossible case where `s1` is longer than `s2`.

## Complexity

- Time: O(m · n log n) — up to `m` windows, each sorted in O(n log n).
- Space: O(n) — the sorted window and target arrays.
