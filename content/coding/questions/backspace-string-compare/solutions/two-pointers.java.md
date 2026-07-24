To drop the extra space, notice that a character's fate depends only on the `#`s that come *after* it. So scan both strings from the right. Keep a `skip` counter: every `#` you meet adds one deletion credit; every real letter either cancels a pending credit (it was backspaced) or is a surviving character you must compare.

Advance both strings to their next surviving character and check they match. When one runs out before the other, the strings differ. No rebuilt strings — just two indices walking backward.

```java
class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1, j = t.length() - 1;
        while (i >= 0 || j >= 0) {
            i = nextValid(s, i);
            j = nextValid(t, j);
            if (i >= 0 && j >= 0) {
                if (s.charAt(i) != t.charAt(j)) return false;
            } else if (i >= 0 || j >= 0) {
                return false;
            }
            i--;
            j--;
        }
        return true;
    }

    private int nextValid(String str, int i) {
        int skip = 0;
        while (i >= 0) {
            if (str.charAt(i) == '#') skip++;
            else if (skip > 0) skip--;
            else break;
            i--;
        }
        return i;
    }
}
```

## Why it works

Scanning right-to-left lets each `#` "consume" the nearest not-yet-deleted letter to its left, exactly matching editor behavior. `nextValid` lands on the next character that actually survives. If both pointers find survivors, they must be equal; if only one does, one final text is longer, so the answer is `false`. The loop ends when both are exhausted in lockstep.

## Complexity

- Time: O(m + n) — every character is visited at most once.
- Space: O(1) — only integer indices, no rebuilt strings.
