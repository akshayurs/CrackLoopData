An anagram is defined purely by letter frequencies, so build a 26-slot count for `p` once and compare it against the count of every length-`|p|` window in `s`. Equal counts mean the window is an anagram of `p`.

This version recounts each window from scratch. It is the clearest baseline before applying the sliding-window optimization.

```java
import java.util.*;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int m = p.length();
        List<Integer> result = new ArrayList<>();
        if (m > s.length()) return result;
        int[] target = count(p, 0, m);
        for (int i = 0; i + m <= s.length(); i++) {
            if (Arrays.equals(count(s, i, i + m), target)) result.add(i);
        }
        return result;
    }

    private int[] count(String s, int lo, int hi) {
        int[] c = new int[26];
        for (int i = lo; i < hi; i++) c[s.charAt(i) - 'a']++;
        return c;
    }
}
```

## Why it works

`count` tallies how many of each of the 26 lowercase letters a slice contains. A substring is an anagram of `p` exactly when its tally equals `target`. Checking every window of width `m` finds all matches, and the left-to-right scan produces indices in ascending order.

## Complexity

- Time: O(n * m) — for each of the ~n start positions we build and compare a count over m characters.
- Space: O(1) — each count array holds 26 fixed slots.
