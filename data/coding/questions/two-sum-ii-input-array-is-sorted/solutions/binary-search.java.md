Since the array is sorted, we can do better than scanning every partner. Fix the first element `numbers[i]`, then **binary search** the remaining suffix for its complement `target - numbers[i]`. Each search costs O(log n) instead of O(n).

This keeps memory constant while cutting the total work to O(n log n) — a clean midpoint between brute force and the two-pointer sweep.

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        for (int i = 0; i < n; i++) {
            int need = target - numbers[i];
            int lo = i + 1, hi = n - 1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (numbers[mid] == need) {
                    return new int[]{i + 1, mid + 1};
                }
                if (numbers[mid] < need) {
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
        }
        return new int[]{};
    }
}
```

## Why it works

For each `i`, the partner (if it exists) is a single value `target - numbers[i]`. Because the suffix to the right of `i` is sorted, binary search locates that value in logarithmic time. Searching only to the right guarantees `index1 < index2` and prevents reusing the same element.

## Complexity

- Time: O(n log n) — n elements, each triggering an O(log n) search.
- Space: O(1) — only index variables.
