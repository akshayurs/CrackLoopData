Given an integer `n`, generate every distinct string of `n` pairs of parentheses that is **well-formed** — every opening bracket is matched by a later closing bracket, and no prefix ever has more closing than opening brackets.

Return the list of strings sorted in ascending (lexicographic) order.

## Examples

```text
Input:  n = 1
Output: ["()"]
```

```text
Input:  n = 2
Output: ["(())", "()()"]
```

```text
Input:  n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

## Constraints

- 1 <= n <= 8
- The output must contain only well-formed combinations, each of length 2n.
- Return the combinations sorted lexicographically.

## Follow-up

The number of valid combinations is the nth Catalan number. Can you generate only the valid strings instead of filtering all 2^(2n) sequences?
