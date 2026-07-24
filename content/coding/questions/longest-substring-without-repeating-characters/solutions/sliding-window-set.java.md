Instead of restarting the scan at every index, maintain one window `[left, right]` that always holds distinct characters. Extend `right` to take in the next character; if that character is already inside the window, shrink from the left until the duplicate is gone.

Each character enters the window once and leaves at most once, so the two pointers together sweep the string in linear time rather than re-examining old ground.

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            while (seen.contains(ch)) {
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(ch);
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

## Why it works

The set is the invariant: it holds exactly the characters of the current window, all distinct. When a new character collides, evicting characters from the left is the only way to restore uniqueness while keeping the window contiguous. After the `while` loop the window is valid again, and its width is a candidate answer.

## Complexity

- Time: O(n) — `left` and `right` each advance at most n times, so O(2n) total.
- Space: O(min(n, k)) — the set never exceeds the number of distinct characters.
