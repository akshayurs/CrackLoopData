The direct reading of the problem: for each day, look at every later day in turn and stop at the first one that is warmer. The gap between the two positions is the wait, and if no warmer day is found the answer stays `0`.

This scans forward from every index, so a long run of cooling days makes each earlier day sweep across the whole tail — quadratic in the worst case, but simple and obviously correct.

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (temperatures[j] > temperatures[i]) {
                    answer[i] = j - i;
                    break;
                }
            }
        }
        return answer;
    }
}
```

## Why it works

For day `i` the inner loop visits days `i+1, i+2, ...` in order, so the first `j` with a strictly greater temperature is the nearest warmer day. Recording `j - i` gives the wait; breaking immediately guarantees it is the *closest* such day. Days with no warmer future keep their default `0`.

## Complexity

- Time: O(n²) — each day may scan the entire remaining array.
- Space: O(1) — ignoring the output, no extra structure.
