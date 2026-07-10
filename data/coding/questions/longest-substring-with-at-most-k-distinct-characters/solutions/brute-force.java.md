Start from the definition directly: try every starting index, extend the substring one character at a time, and track how many distinct characters the current window holds. Once the window would exceed `k` distinct characters, abandon that start and move on.

This inspects every substring, making it quadratic, but it is the most literal encoding of the problem and a good baseline.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (k == 0) return 0;
        int best = 0;
        int n = s.length();
        for (int start = 0; start < n; start++) {
            Map<Character, Integer> counts = new HashMap<>();
            for (int end = start; end < n; end++) {
                char c = s.charAt(end);
                counts.merge(c, 1, Integer::sum);
                if (counts.size() > k) break;
                best = Math.max(best, end - start + 1);
            }
        }
        return best;
    }
}
```

## Why it works

Fixing `start` and growing `end` enumerates every substring beginning at `start`. The `counts` map tracks distinct characters in the window; once it passes `k`, all longer windows from that start are invalid, so the early `break` is safe. The running maximum over valid windows is the answer.

## Complexity

- Time: O(n^2) — up to n starts, each scanning up to n characters.
- Space: O(k) — the map holds at most k + 1 distinct characters.
