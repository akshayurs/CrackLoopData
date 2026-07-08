Two strings are anagrams exactly when their letters, laid out in a canonical order, are identical. Sorting is the simplest way to reach that canonical form: sort the characters of both strings and check that the results match.

It is the honest baseline you would reach for first in an interview — no counting, no bookkeeping, just compare the sorted characters. A quick length check up front rules out the obvious non-anagrams before doing any work.

```java
import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        char[] a = s.toCharArray();
        char[] b = t.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }
}
```

## Why it works

If `t` is a rearrangement of `s`, then sorting both collapses every rearrangement to the same sequence of characters, so the sorted arrays are equal. If they differ in any letter or in how many times a letter appears, the sorted forms diverge at some position and `Arrays.equals` returns false. The length guard is an early exit — strings of unequal length can never be anagrams.

## Complexity

- Time: O(n log n) — dominated by sorting both character arrays.
- Space: O(n) — `toCharArray` allocates a copy of each string.
