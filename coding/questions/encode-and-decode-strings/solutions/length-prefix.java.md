The escaping approach fights the data — it has to hunt for and disarm every character that looks like a separator. Flip the problem around: instead of marking where each string *ends*, announce up front how *long* it is. Encode every string as its length, a single `#`, then the raw characters: `4#neet`. Now the `#` is never ambiguous, because the decoder only ever reads it in one place — right after the digits of a length.

This is the "chunked transfer" trick. To decode, read digits until the `#`, parse that as a count `L`, then grab exactly the next `L` characters verbatim — no scanning of the payload, no escaping, and no confusion even if those `L` characters are all `#`. It also cleanly distinguishes an empty list (`""` → `[]`) from a list holding one empty string (`"0#"` → `[""]`).

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length()).append('#').append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (s.charAt(j) != '#') j++;
            int length = Integer.parseInt(s.substring(i, j));
            int start = j + 1;
            result.add(s.substring(start, start + length));
            i = start + length;
        }
        return result;
    }
}
```

## Why it works

Every chunk is self-describing: the length prefix tells the decoder exactly how many characters to consume, so the payload is copied by count rather than by searching for a boundary. Because the decoder never inspects the content characters, any character — including the `#` separator — passes through untouched. The pointer always lands on the start of the next length prefix, so the loop cleanly walks chunk by chunk to the end.

## Complexity

- Time: O(N) where N is the total number of characters — the length scan plus the substring copy touch each character a constant number of times.
- Space: O(N) — the encoded string and the decoded list are proportional to the input.
