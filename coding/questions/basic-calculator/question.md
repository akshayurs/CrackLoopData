You are given a string `s` representing a valid arithmetic expression made up of non-negative integers, the operators `+` and `-`, parentheses `(` and `)`, and spaces. Evaluate the expression and return its integer value.

The `-` sign may act as a unary minus (for example `-2` or `-(3+1)`), but `+` is never unary. There is no multiplication or division. You must implement the evaluation yourself — do not use a built-in expression parser such as `eval`.

## Examples

```text
Input:  s = "1 + 1"
Output: 2
```

```text
Input:  s = " 2-1 + 2 "
Output: 3
```

```text
Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Constraints

- 1 <= s.length <= 3 * 10^5
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` is a valid expression with balanced parentheses.
- Every intermediate and final value fits in a 32-bit signed integer.

## Follow-up

Can you evaluate the expression in a single left-to-right pass, without first converting it to postfix notation?
