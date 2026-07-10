Since the answer is a contiguous window of length `k`, the whole problem reduces to finding its left index `lo`, which ranges over `0 .. n - k`. Binary-search that range directly instead of shrinking one element at a time.

For a candidate start `mid`, compare the element just left of the window (`arr[mid]`) against the element just past it (`arr[mid + k]`). If `arr[mid]` is farther from `x` than `arr[mid + k]`, the window should slide right, so search the upper half; otherwise the left edge is at `mid` or earlier.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int lo = 0, hi = arr.length - k;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (x - arr[mid] > arr[mid + k] - x) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int i = lo; i < lo + k; i++) result.add(arr[i]);
        return result;
    }
}
```

## Why it works

`arr[mid]` and `arr[mid + k]` are the two elements that would leave or enter as the window starts at `mid` versus `mid + 1`. If dropping `arr[mid]` (the left edge) to gain `arr[mid + k]` reduces total distance, the answer lies further right, so `lo = mid + 1`. Otherwise `mid` is still a valid left edge and we keep it via `hi = mid`. The strict `>` breaks ties toward keeping the smaller-valued left element. The loop converges to the unique optimal start, and the collected slice is already ascending.

## Complexity

- Time: O(log(n - k) + k) — binary search for the start, then copying k elements.
- Space: O(1) — constant extra state, ignoring the output list.
