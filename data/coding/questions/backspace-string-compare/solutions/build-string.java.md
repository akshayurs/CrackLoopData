The most literal reading: actually type each string out. Walk left to right pushing letters onto a `StringBuilder` used as a stack, and whenever a `#` appears, drop the last letter (if any). Whatever remains is the final text.

Do this for both strings and compare the results directly. It is the honest baseline you would describe first before worrying about extra space.

```java
class Solution {
    public boolean backspaceCompare(String s, String t) {
        return build(s).equals(build(t));
    }

    private String build(String str) {
        StringBuilder sb = new StringBuilder();
        for (char ch : str.toCharArray()) {
            if (ch == '#') {
                if (sb.length() > 0) sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}
```

## Why it works

The builder mirrors the editor exactly: typing a letter appends it, and a backspace removes the most recent letter — which is always the last character. Guarding the delete with a length check handles a backspace on empty text as a no-op. Two strings are equal after editing iff their reconstructed contents match character for character.

## Complexity

- Time: O(m + n) — each character of both strings is processed once.
- Space: O(m + n) — the two rebuilt strings are stored explicitly.
