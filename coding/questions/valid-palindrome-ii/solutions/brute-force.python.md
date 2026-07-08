If at most one deletion is allowed, the simplest plan is to try every possibility. The string is already fine if it reads the same forwards and backwards; otherwise, remove one character at a time and re-check.

For each index, build the string without that character and test whether the result is a palindrome. If any single removal works — or the original was already a palindrome — the answer is `true`.

```python
def valid_palindrome(s):
    def is_pal(t):
        return t == t[::-1]

    if is_pal(s):
        return True
    for i in range(len(s)):
        if is_pal(s[:i] + s[i + 1:]):
            return True
    return False
```

## Why it works

"At most one deletion" means the candidate palindromes are exactly the original string plus the `n` strings obtained by dropping one character. Testing all of them is exhaustive, so a `true` answer is never missed. Each palindrome check compares the string against its reverse.

## Complexity

- Time: O(n²) — up to n deletions, each followed by an O(n) palindrome check.
- Space: O(n) — each trimmed copy and its reverse take linear space.
