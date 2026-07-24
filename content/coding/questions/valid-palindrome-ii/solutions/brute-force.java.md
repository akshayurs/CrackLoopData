If at most one deletion is allowed, the simplest plan is to try every possibility. The string is already fine if it reads the same forwards and backwards; otherwise, remove one character at a time and re-check.

For each index, build the string without that character and test whether the result is a palindrome. If any single removal works — or the original was already a palindrome — the answer is `true`.

```java
class Solution {
    public boolean validPalindrome(String s) {
        if (isPal(s)) return true;
        for (int i = 0; i < s.length(); i++) {
            String t = s.substring(0, i) + s.substring(i + 1);
            if (isPal(t)) return true;
        }
        return false;
    }

    private boolean isPal(String t) {
        int i = 0, j = t.length() - 1;
        while (i < j) {
            if (t.charAt(i++) != t.charAt(j--)) return false;
        }
        return true;
    }
}
```

## Why it works

"At most one deletion" means the candidate palindromes are exactly the original string plus the `n` strings obtained by dropping one character. Testing all of them is exhaustive, so a `true` answer is never missed. Each check walks inward from both ends comparing characters.

## Complexity

- Time: O(n²) — up to n deletions, each followed by an O(n) palindrome check.
- Space: O(n) — each trimmed substring takes linear space.
