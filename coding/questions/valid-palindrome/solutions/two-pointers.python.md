To avoid building a second string, compare the ends of the original directly. Keep one pointer at the far left and one at the far right, skip anything that is not alphanumeric, and match the two characters they land on. Walk both inward until they meet.

This is the two-pointer template: a single scan from both sides, with case folding applied only at the moment of comparison, using no extra storage beyond two indices.

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

## Why it works

A palindrome must have matching characters at mirrored positions. The inner loops advance past punctuation and spaces so the pointers always rest on the characters that actually count. If any mirrored pair disagrees after lowercasing, the string cannot be a palindrome and we return early. If the pointers cross without a mismatch, every meaningful pair matched.

## Complexity

- Time: O(n) — each pointer moves inward at most n steps total.
- Space: O(1) — only two indices, regardless of input size.
