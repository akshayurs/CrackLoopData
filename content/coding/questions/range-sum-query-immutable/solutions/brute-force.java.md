The literal reading of the problem: for each query, walk from `left` to `right` and add up the elements. No preprocessing, no extra memory beyond the answer array.

This is the honest baseline. It is fine when there are only a handful of queries, but it re-scans the array from scratch every time, so heavy querying makes it slow.

```java
class Solution {
    public int[] rangeSum(int[] nums, int[][] queries) {
        int[] answers = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int total = 0;
            for (int i = queries[q][0]; i <= queries[q][1]; i++) {
                total += nums[i];
            }
            answers[q] = total;
        }
        return answers;
    }
}
```

## Why it works

Each query independently sums the contiguous slice `nums[left..right]`. The inner loop uses `i <= right` so the last element is included. Nothing is cached between queries, so correctness is obvious — we add exactly the elements the query asks for.

## Complexity

- Time: O(q · n) — each of the `q` queries may scan up to `n` elements.
- Space: O(1) — ignoring the output array, only a running total is kept.
