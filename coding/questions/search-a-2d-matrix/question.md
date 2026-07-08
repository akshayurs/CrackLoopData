You are given an `m x n` integer matrix and a `target` value. The matrix has two useful properties: each row is sorted in non-decreasing order from left to right, and the first value of every row is greater than the last value of the row above it. In effect, if you read the matrix row by row it forms one fully sorted sequence.

Return `true` if `target` appears somewhere in the matrix, and `false` otherwise.

## Examples

```text
Input:  matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
Output: true
```

```text
Input:  matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
Output: false
```

```text
Input:  matrix = [[1]], target = 1
Output: true
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4
- Each row is sorted ascending, and every row's first element exceeds the previous row's last element.

## Follow-up

The layout guarantees the whole matrix is one sorted list. Can you find `target` in O(log(m·n)) time?
