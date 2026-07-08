You are given an `n x n` matrix where every row is sorted in ascending order from left to right, and every column is sorted in ascending order from top to bottom. Return the `k`th smallest element in the matrix when all of its values are considered in sorted order.

Note that this is the `k`th smallest element in the **overall sorted order**, counting duplicates — not the `k`th *distinct* value.

## Examples

```text
Input:  matrix = [[1, 5, 9],
                  [10, 11, 13],
                  [12, 13, 15]], k = 8
Output: 13        # sorted values: 1,5,9,10,11,12,13,13,15 → 8th is 13
```

```text
Input:  matrix = [[-5]], k = 1
Output: -5
```

```text
Input:  matrix = [[1, 2],
                  [1, 3]], k = 2
Output: 1         # sorted values: 1,1,2,3 → 2nd is 1
```

## Constraints

- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- Every row and every column is sorted in ascending order.
- 1 <= k <= n^2

## Follow-up

The brute-force sort ignores the matrix's structure. Can you do better than O(n² log n), ideally without materializing all n² values?
