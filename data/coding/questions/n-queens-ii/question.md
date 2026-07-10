You are given an integer `n`. Count how many distinct ways exist to place `n` queens on an `n x n` chessboard so that no two queens attack each other — meaning no two share a row, a column, or either diagonal.

Return only the total count of valid arrangements, not the arrangements themselves.

## Examples

```text
Input:  n = 4
Output: 2
```

```text
Input:  n = 1
Output: 1
```

```text
Input:  n = 2
Output: 0        # no arrangement of 2 queens on a 2x2 board avoids all attacks
```

## Constraints

- 1 <= n <= 9

## Follow-up

Can you check whether a placement is safe in O(1) instead of scanning every previously placed queen?
