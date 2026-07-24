Grow a window from the right and only shrink it when it becomes invalid. A window is valid when the letters you'd have to overwrite — `window - maxCount`, where `maxCount` is the frequency of the most common letter inside — is at most `k`. Keep the letter counts in a fixed 26-slot array so each step is constant work.

The trick that makes it a single pass: `maxCount` never needs to be lowered. If a previous window achieved a higher `maxCount`, no shorter window can beat the answer it already produced, so we let the window slide forward one step at a time rather than shrinking it. The window's width at the end is the longest valid substring seen.

```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] counts = new int[26];
        int left = 0;
        int maxCount = 0;
        int best = 0;
        for (int right = 0; right < s.length(); right++) {
            int idx = s.charAt(right) - 'A';
            counts[idx]++;
            maxCount = Math.max(maxCount, counts[idx]);
            if (right - left + 1 - maxCount > k) {
                counts[s.charAt(left) - 'A']--;
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

## Why it works

`(right - left + 1) - maxCount` counts the letters in the window that are not the majority letter — exactly the replacements needed to unify it. When that exceeds `k`, the window is one too wide, so we advance `left` by one, keeping the width monotonic. Because `maxCount` only ever rises, the window can only expand past widths that were already valid, so `best` correctly tracks the maximum achievable length in one sweep.

## Complexity

- Time: O(n) — each index enters and leaves the window at most once.
- Space: O(1) — a fixed array of 26 counters.
