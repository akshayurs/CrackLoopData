The most literal reading of the problem: consider every pair of lines `(i, j)`, compute the water it holds, and keep the largest. Two nested loops enumerate all pairs.

This is the honest baseline you would state first in an interview — no insight required, just definition applied directly.

```java
class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int best = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int area = Math.min(heights[i], heights[j]) * (j - i);
                if (area > best) best = area;
            }
        }
        return best;
    }
}
```

## Why it works

Every container is defined by an unordered pair of indices, and the outer/inner loops visit each such pair exactly once. For each pair we apply the area rule directly — width times the shorter wall — and track the running maximum, so the final answer is the best over all possible containers.

## Complexity

- Time: O(n²) — about n²/2 pairs are evaluated.
- Space: O(1) — only the running maximum is stored.
