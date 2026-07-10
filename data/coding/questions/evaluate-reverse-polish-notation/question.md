You are given an array of strings `tokens` representing an arithmetic expression in **Reverse Polish Notation** (RPN, also called postfix). Evaluate the expression and return its integer value.

Each token is either an integer or one of the operators `+`, `-`, `*`, `/`. In RPN an operator comes *after* its two operands, so `["3", "4", "+"]` means `3 + 4`. Division between two integers **truncates toward zero** (drop the fractional part), and the input is always a valid expression that evaluates to a value fitting in a 32-bit signed integer. No division by zero occurs.

## Examples

```text
Input:  tokens = ["2", "1", "+", "3", "*"]
Output: 9        # ((2 + 1) * 3) = 9
```

```text
Input:  tokens = ["4", "13", "5", "/", "+"]
Output: 6        # (4 + (13 / 5)) = 4 + 2 = 6
```

```text
Input:  tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
```

## Constraints

- 1 <= tokens.length <= 10^4
- Each token is either `+`, `-`, `*`, `/`, or an integer in the range [-200, 200].
- The expression is always valid; the answer and every intermediate result fit in a 32-bit signed integer.
- Division truncates toward zero (e.g. `6 / -132 == 0`, `-7 / 2 == -3`).

## Follow-up

Can you evaluate the expression in a single left-to-right pass?
