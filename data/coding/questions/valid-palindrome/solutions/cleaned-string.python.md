The cleanest first attempt mirrors the definition word for word: strip out everything that is not a letter or digit, lowercase what remains, and check whether that reduced sequence equals its own reverse.

It costs an extra copy of the string, but it is short, obviously correct, and a great baseline to state before optimizing away the extra memory.

```python
def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

## Why it works

The comprehension keeps only alphanumeric characters and folds their case, producing exactly the "cleaned form" the problem describes. A sequence is a palindrome precisely when it matches its reverse, so comparing `cleaned` to `cleaned[::-1]` is a direct test of the definition. Punctuation and spaces never enter the list, so they cannot affect the result.

## Complexity

- Time: O(n) — one pass to build the list, one comparison over its length.
- Space: O(n) — the cleaned list and its reversed copy both scale with the input.
