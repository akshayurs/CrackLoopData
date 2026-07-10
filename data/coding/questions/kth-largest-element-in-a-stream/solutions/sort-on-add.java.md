The simplest thing that could work: keep every number the stream has ever seen in a list. Each time `add` is called, drop the new value in, sort the whole list in descending order, and read off the element at index `k - 1`.

It never gets the ordering wrong, but re-sorting the entire history on every single call is wasteful once the stream grows long.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class KthLargest {
    private final int k;
    private final List<Integer> nums;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.nums = new ArrayList<>();
        for (int n : nums) {
            this.nums.add(n);
        }
    }

    public int add(int val) {
        nums.add(val);
        nums.sort(Collections.reverseOrder());
        return nums.get(k - 1);
    }
}
```

## Why it works

Sorting the list in descending order puts the largest value at index 0, the second largest at index 1, and so on — so the k-th largest always sits at index `k - 1`. Because we re-sort after every insertion, the answer reflects the full stream seen so far.

## Complexity

- Time: O(n log n) per call to `add`, where n is the number of elements seen so far.
- Space: O(n) — the list stores every value ever added.
