The sorted order hides a clean invariant. Before the single element, every pair starts at an even index: the first copy sits at position 0, 2, 4, … and its twin at the odd index just after. That pattern holds up to the lone element, then the single value shifts everything, so afterward pairs start on odd indices instead.

So binary-search on the even indices only. Snap `mid` down to an even index and compare it with its neighbor `mid + 1`. If they match, the pairing is still intact here, so the single element lies to the right; otherwise it is at `mid` or to the left. The search collapses to one position in logarithmic time.

```java
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid % 2 == 1) {
                mid -= 1;
            }
            if (nums[mid] == nums[mid + 1]) {
                lo = mid + 2;
            } else {
                hi = mid;
            }
        }
        return nums[lo];
    }
}
```

## Why it works

Forcing `mid` even lets us test a whole pair with one comparison. `nums[mid] == nums[mid + 1]` means every element in `[lo, mid + 1]` is correctly paired, so the anomaly is strictly to the right (`lo = mid + 2`). A mismatch means the single element is at `mid` or earlier (`hi = mid`). The window always keeps the answer and shrinks by half, so `lo` finally lands on it.

## Complexity

- Time: O(log n) — the search space halves each step.
- Space: O(1) — only two pointers.
