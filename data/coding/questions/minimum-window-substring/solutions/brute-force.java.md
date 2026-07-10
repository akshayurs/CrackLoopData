The direct reading of the problem: try every starting index, then extend the window rightward until it first covers `t`, and remember the shortest cover seen. Once a start position produces a valid window we can stop extending it — growing further only makes that window longer.

Counting requirements with a frequency map lets us compare "how many of each character we have" against "how many we need," so duplicates in `t` are handled correctly.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty() || t.length() > s.length()) return "";
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);
        String best = "";
        for (int i = 0; i < s.length(); i++) {
            Map<Character, Integer> window = new HashMap<>();
            for (int j = i; j < s.length(); j++) {
                window.merge(s.charAt(j), 1, Integer::sum);
                boolean ok = true;
                for (Map.Entry<Character, Integer> e : need.entrySet()) {
                    if (window.getOrDefault(e.getKey(), 0) < e.getValue()) { ok = false; break; }
                }
                if (ok) {
                    if (best.isEmpty() || j - i + 1 < best.length()) best = s.substring(i, j + 1);
                    break;
                }
            }
        }
        return best;
    }
}
```

## Why it works

`need` records how many copies of each character the window must contain. For a fixed start `i`, we widen the end `j` and stop the instant every requirement is met — that is the shortest valid window beginning at `i`. Comparing lengths across all starts yields the global minimum, and scanning starts left-to-right keeps the earliest window on ties.

## Complexity

- Time: O(n^2) — every start extends across the rest of the string; the coverage check touches only the distinct characters of `t`.
- Space: O(m) — the two frequency maps, where m = t.length().
