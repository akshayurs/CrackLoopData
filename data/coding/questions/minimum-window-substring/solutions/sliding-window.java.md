Restarting the scan from every index repeats work. Instead keep one window with two pointers: push the right edge to gather characters, and once the window covers `t`, pull the left edge inward as far as possible while it still covers `t`. Each pointer only ever moves forward, so the whole string is traversed a constant number of times.

Track coverage with a single `missing` counter — the number of still-needed characters. Let `need` counts go negative to represent surplus copies; a character is "still needed" only while its count is strictly positive. When `missing` hits zero the current window is valid and we try to shrink it.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty() || t.length() > s.length()) return "";
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);
        int missing = t.length();
        int left = 0, bestLeft = 0, bestLen = Integer.MAX_VALUE;
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (need.getOrDefault(ch, 0) > 0) missing--;
            need.merge(ch, -1, Integer::sum);
            while (missing == 0) {
                if (right - left + 1 < bestLen) { bestLeft = left; bestLen = right - left + 1; }
                char lc = s.charAt(left);
                need.merge(lc, 1, Integer::sum);
                if (need.get(lc) > 0) missing++;
                left++;
            }
        }
        return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestLeft, bestLeft + bestLen);
    }
}
```

## Why it works

Advancing `right` consumes a character; if it was one we still owed, `missing` drops. When `missing == 0` every required character is present, so we record the length and then release the leftmost character. Releasing raises its `need` count; only when it becomes positive again do we truly lose a required character, ending the shrink. Because both pointers march forward monotonically, every window boundary is examined once.

## Complexity

- Time: O(n + m) — each character enters and leaves the window at most once.
- Space: O(m) — the `need` map holds the distinct characters of `t`.
