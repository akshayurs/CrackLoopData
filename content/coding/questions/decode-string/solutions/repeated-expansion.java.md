The most literal reading of the rule: keep expanding the innermost `k[...]` group until no brackets remain. An innermost group is a `]` whose matching `[` has no other `[` between them, so its contents are pure letters and can be repeated immediately.

Each pass scans for the first `]`, walks back to its `[`, reads the digits before that `[`, and splices in the repeated text. Repeat until the string is bracket-free. It is the honest baseline you would describe before reaching for a stack.

```java
class Solution {
    public String decodeString(String s) {
        while (s.indexOf(']') >= 0) {
            int close = s.indexOf(']');
            int open = s.lastIndexOf('[', close);
            String inner = s.substring(open + 1, close);
            int j = open;
            while (j > 0 && Character.isDigit(s.charAt(j - 1))) j--;
            int k = Integer.parseInt(s.substring(j, open));
            StringBuilder sb = new StringBuilder(s.substring(0, j));
            for (int r = 0; r < k; r++) sb.append(inner);
            s = sb.append(s.substring(close + 1)).toString();
        }
        return s;
    }
}
```

## Why it works

The first `]` in the string always closes an innermost group, and the nearest `[` to its left is its partner, so the text between them contains only letters. Reading the run of digits just before that `[` gives the repeat count `k`. Replacing the whole `k[inner]` span with `inner` repeated `k` times removes exactly one bracket pair while preserving every character outside it. Since each pass eliminates one pair, the loop terminates with a fully decoded string.

## Complexity

- Time: O(m · n) — one pass per bracket pair (m pairs), each rescanning a string up to the final length n.
- Space: O(n) — new strings built during expansion.
