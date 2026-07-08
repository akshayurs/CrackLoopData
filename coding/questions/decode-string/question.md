You are given an encoded string `s` and must return its decoded form. The encoding rule is `k[encoded]`, meaning the substring `encoded` is repeated exactly `k` times. The bracketed groups may be nested, and `k` is always a positive integer.

The input is guaranteed to be well-formed: brackets are balanced, digits appear only as a repeat count directly before an opening bracket, and the original (decoded) string contains only letters. There are no stray digits or spaces to worry about.

## Examples

```text
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"
```

```text
Input:  s = "3[a2[c]]"
Output: "accaccacc"        # inner 2[c] -> "cc", then a+"cc" repeated 3 times
```

```text
Input:  s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints

- 1 <= s.length <= 30
- `s` consists of lowercase English letters, digits, and the characters `[` and `]`.
- Every repeat count `k` satisfies 1 <= k <= 300.
- The input is always valid, and the decoded string fits comfortably in memory.

## Follow-up

Can you decode the string in a single left-to-right pass, without repeatedly rescanning it?
