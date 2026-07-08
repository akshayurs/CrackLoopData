The simplest thing that works: forget the matrix structure entirely. Every value is a candidate, so copy them all into one flat array, sort it, and index into position `k`.

This throws away the sortedness of the rows and columns, but it's a correct baseline and easy to reason about — a good place to start before optimizing.

```java
import java.util.Arrays;

class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int[] flat = new int[n * n];
        int idx = 0;
        for (int[] row : matrix) {
            for (int value : row) {
                flat[idx++] = value;
            }
        }
        Arrays.sort(flat);
        return flat[k - 1];
    }
}
```

## Why it works

Copying gathers all n² values into one array, and `Arrays.sort` orders them ascending including duplicates. The `k`th smallest in overall order is then the element at zero-based index `k - 1`.

## Complexity

- Time: O(n² log n) — sorting n² values dominates.
- Space: O(n²) — the flattened array holds every value.
