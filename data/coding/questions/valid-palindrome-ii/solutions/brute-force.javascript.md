If at most one deletion is allowed, the simplest plan is to try every possibility. The string is already fine if it reads the same forwards and backwards; otherwise, remove one character at a time and re-check.

For each index, build the string without that character and test whether the result is a palindrome. If any single removal works — or the original was already a palindrome — the answer is `true`.

```javascript
function validPalindrome(s) {
  const isPal = (t) => t === t.split("").reverse().join("");

  if (isPal(s)) return true;
  for (let i = 0; i < s.length; i++) {
    if (isPal(s.slice(0, i) + s.slice(i + 1))) return true;
  }
  return false;
}
```

## Why it works

"At most one deletion" means the candidate palindromes are exactly the original string plus the `n` strings obtained by dropping one character. Testing all of them is exhaustive, so a `true` answer is never missed. Each palindrome check compares the string against its reverse.

## Complexity

- Time: O(n²) — up to n deletions, each followed by an O(n) palindrome check.
- Space: O(n) — each trimmed copy and its reverse take linear space.
