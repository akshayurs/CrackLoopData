You're given a string `s` representing an arithmetic expression made of non-negative integers and the operators `+`, `-`, `*`, `/`, separated by optional spaces. Evaluate it and return the result as an integer.

Division between two integers truncates toward zero. You may assume the expression is always valid, and there is no parentheses support needed — just standard operator precedence (`*` and `/` bind tighter than `+` and `-`).

## Examples

```text
Input:  s = "3+2*2"
Output: 7        # 2*2 = 4, then 3+4 = 7
```

```text
Input:  s = " 3/2 "
Output: 1        # integer division truncates toward zero
```

```text
Input:  s = " 3+5 / 2 "
Output: 5        # 5/2 = 2 (truncated), then 3+2 = 5
```

## Constraints

- 1 <= s.length <= 3 * 10^5
- `s` consists of integers and the characters `'+'`, `'-'`, `'*'`, `'/'`, and `' '`.
- `s` is a valid expression.
- All intermediate results fit in a 32-bit signed integer.
- The answer is guaranteed to fit in a 32-bit signed integer.
