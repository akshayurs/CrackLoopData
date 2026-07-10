The cleanest first attempt mirrors the definition word for word: strip out everything that is not a letter or digit, lowercase what remains, and check whether that reduced string equals its own reverse.

It costs an extra copy of the string, but it is short, obviously correct, and a great baseline to state before optimizing away the extra memory.

```java
class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        String cleaned = sb.toString();
        return cleaned.equals(sb.reverse().toString());
    }
}
```

## Why it works

The loop appends only alphanumeric characters, each folded to lowercase, building exactly the "cleaned form" the problem describes. A string is a palindrome precisely when it matches its reverse, so comparing `cleaned` to `sb.reverse()` is a direct test of the definition. Punctuation and spaces are skipped, so they cannot affect the result.

## Complexity

- Time: O(n) — one pass to build the cleaned text, one comparison over its length.
- Space: O(n) — the builder and its reversed copy both scale with the input.
