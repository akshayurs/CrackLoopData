The cleanest first attempt mirrors the definition word for word: strip out everything that is not a letter or digit, lowercase what remains, and check whether that reduced string equals its own reverse.

It costs an extra copy of the string, but it is short, obviously correct, and a great baseline to state before optimizing away the extra memory.

```javascript
function isPalindrome(s) {
  const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  const reversed = cleaned.split("").reverse().join("");
  return cleaned === reversed;
}
```

## Why it works

Lowercasing first, then deleting every character outside `a-z0-9`, yields exactly the "cleaned form" the problem describes. A string is a palindrome precisely when it matches its reverse, so comparing `cleaned` to `reversed` is a direct test of the definition. Punctuation and spaces are removed before the comparison, so they cannot affect the result.

## Complexity

- Time: O(n) — the replace, the reverse, and the comparison each scan the string once.
- Space: O(n) — the cleaned string and its reversed copy both scale with the input.
