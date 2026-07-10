Because the array never changes, do the summing work once up front. Build a `prefix` array where `prefix[i]` holds the sum of the first `i` elements. Then the sum of any window `[left, right]` is just `prefix[right + 1] - prefix[left]` — one subtraction, no scanning.

The extra offset (a leading zero at `prefix[0]`) is what lets the formula handle `left = 0` without a special case.

```java
class Solution {
    public int[] rangeSum(int[] nums, int[][] queries) {
        int[] prefix = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        int[] answers = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            answers[q] = prefix[queries[q][1] + 1] - prefix[queries[q][0]];
        }
        return answers;
    }
}
```

## Why it works

`prefix[i]` equals `nums[0] + ... + nums[i-1]`. Subtracting the sum up to `left` from the sum up to `right + 1` cancels everything before `left` and keeps exactly `nums[left..right]`. The leading zero makes `prefix[left]` well defined even when `left` is 0. Preprocessing is a single pass; every query is then constant work.

## Complexity

- Time: O(n + q) — one pass to build the prefix array, then O(1) per query.
- Space: O(n) — the prefix array holds n + 1 sums.
