The most literal approach: read the input from the last character to the first and append each one to a fresh buffer. Whatever was at the end lands at the front of the new string, which is exactly reversal.

It is the honest baseline — no pointer bookkeeping, just walk backwards and collect. The cost is a `StringBuilder` the size of the input.

```java
class Solution {
    public String reverseString(String s) {
        StringBuilder result = new StringBuilder(s.length());
        for (int i = s.length() - 1; i >= 0; i--) {
            result.append(s.charAt(i));
        }
        return result.toString();
    }
}
```

## Why it works

Iterating with the index going from `s.length() - 1` down to `0` visits characters in reverse order, and appending preserves that order in `result`. Converting the builder to a string yields the input read back-to-front.

## Complexity

- Time: O(n) — one pass over every character.
- Space: O(n) — a separate buffer holds all n characters.
