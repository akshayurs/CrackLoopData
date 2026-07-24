The instinct is to join the strings with some separator like `#`. That breaks the moment a string *contains* `#`, so the fix is to escape it: before joining, protect every separator (and the escape character itself) with a backslash. On the way back, a backslash means "the next character is literal, not a separator."

This works, but notice the seam it leaves: because the pieces are joined *between* elements, an empty input list and a list holding one empty string both encode to `""`. The length-prefixed approach avoids that ambiguity entirely.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (int k = 0; k < strs.size(); k++) {
            if (k > 0) sb.append('#');
            for (char c : strs.get(k).toCharArray()) {
                if (c == '\\' || c == '#') sb.append('\\');
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        StringBuilder buf = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (c == '\\') { buf.append(s.charAt(i + 1)); i += 2; }
            else if (c == '#') { result.add(buf.toString()); buf.setLength(0); i += 1; }
            else { buf.append(c); i += 1; }
        }
        result.add(buf.toString());
        return result;
    }
}
```

## Why it works

Escaping guarantees that every unescaped `#` in the encoded string is a real boundary and never part of the data. During decoding, a backslash consumes the character after it verbatim, so an escaped `#` or `\` rejoins the current buffer instead of splitting it. Everything else accumulates until an unescaped `#` flushes the buffer as one recovered string; the trailing buffer after the loop is the final element.

## Complexity

- Time: O(N) where N is the total number of characters across all strings — each character is scanned a constant number of times.
- Space: O(N) — the encoded string and the rebuilt list are proportional to the input.
