Given a non-negative integer `x`, return the integer square root of `x` — that is, the largest integer `r` such that `r * r <= x`. In other words, compute the square root and round it **down** to the nearest whole number.

You must not use any built-in exponent or square-root function (`pow`, `sqrt`, `**`, etc.).

## Examples

```text
Input:  x = 8
Output: 2        # sqrt(8) ≈ 2.828, floored to 2
```

```text
Input:  x = 16
Output: 4        # 4 * 4 == 16 exactly
```

```text
Input:  x = 0
Output: 0
```

## Constraints

- 0 <= x <= 2^31 - 1

## Follow-up

The linear scan is O(√x). Can you do it in O(log x) time?
