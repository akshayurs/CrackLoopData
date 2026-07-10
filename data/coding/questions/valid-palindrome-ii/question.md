You are given a string `s` made of lowercase English letters. Return `true` if `s` can be turned into a palindrome by deleting **at most one** character, and `false` otherwise.

Deleting zero characters is allowed, so any string that is already a palindrome qualifies.

## Examples

```text
Input:  s = "aba"
Output: true          # already a palindrome, delete nothing
```

```text
Input:  s = "abca"
Output: true          # delete 'c' (or 'b') to get "aba"
```

```text
Input:  s = "abec"
Output: false         # no single deletion makes it a palindrome
```

## Constraints

- 1 <= s.length <= 10^5
- `s` consists only of lowercase English letters.

## Follow-up

The brute-force scan is O(n²). Can you decide in a single O(n) pass?
