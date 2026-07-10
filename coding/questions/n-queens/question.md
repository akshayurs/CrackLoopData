The **n-queens puzzle** asks you to place `n` chess queens on an `n x n` board so that no two queens attack each other — meaning no two queens share a row, a column, or a diagonal.

Given the integer `n`, return **all distinct board layouts** that place `n` queens safely. Represent each layout as a list of `n` strings, one per row, where `'Q'` marks a queen and `'.'` marks an empty square. Return the layouts in the order your search naturally discovers them (row 0 first, trying columns left to right).

## Examples

```text
Input:  n = 4
Output: [
  [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."]
]
```

```text
Input:  n = 1
Output: [["Q"]]
```

```text
Input:  n = 2
Output: []        # no arrangement of 2 queens avoids every attack
```

## Constraints

- 1 <= n <= 9
- Each returned layout must be a valid `n x n` placement of `n` non-attacking queens.
- If no arrangement exists, return an empty list.
