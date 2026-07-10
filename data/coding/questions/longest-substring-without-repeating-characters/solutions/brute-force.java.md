Start from the definition: try every substring and keep the longest one whose characters are all distinct. Fix a left endpoint, then extend the right endpoint one character at a time, tracking the characters seen so far in a set.

The moment a character repeats inside the current window, that starting point can grow no further, so we break and move the left endpoint forward.

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int best = 0;
        for (int i = 0; i < s.length(); i++) {
            Set<Character> seen = new HashSet<>();
            for (int j = i; j < s.length(); j++) {
                if (seen.contains(s.charAt(j))) break;
                seen.add(s.charAt(j));
                best = Math.max(best, j - i + 1);
            }
        }
        return best;
    }
}
```

## Why it works

For each start index `i`, the inner loop grows the window until it hits a duplicate, which is exactly the longest duplicate-free substring beginning at `i`. Taking the maximum over all starts covers every candidate, so the true answer is never missed.

## Complexity

- Time: O(n²) — n start positions, each scanning up to n characters before a repeat.
- Space: O(min(n, k)) — the set holds distinct characters, bounded by the alphabet size k.
