A stack captures the "collide with the previous survivor" behaviour perfectly. Walk the string once; the stack always holds the result-so-far. For each character, if it equals the character on top of the stack, they annihilate — pop the top and drop the current one. Otherwise push the current character.

A `StringBuilder` doubles as the stack here: its last character is the top, so we either delete that last character or append the new one. This handles the cascade automatically without any restart.

```java
class Solution {
    public String removeDuplicates(String s) {
        StringBuilder stack = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            int len = stack.length();
            if (len > 0 && stack.charAt(len - 1) == ch) {
                stack.deleteCharAt(len - 1);
            } else {
                stack.append(ch);
            }
        }
        return stack.toString();
    }
}
```

## Why it works

The builder is an invariant: it is exactly the fully-reduced string of everything processed so far. When a new character matches the last one, that pair is adjacent in the reduced string and must cancel, so we delete it. When it does not match, it safely extends the reduced string. Because a deletion re-exposes the earlier character as the new last, chains like `"aaaa"` collapse in the same single pass. What remains is the unique pair-free result.

## Complexity

- Time: O(n) — each character is appended and deleted at most once.
- Space: O(n) — the builder in the worst case (no removals) holds the whole string.
