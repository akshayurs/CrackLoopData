The simplest possible design: keep every number seen so far in one sorted list. On each `addNum`, find the insertion point with binary search and shift elements to keep the list sorted. `findMedian` then just reads the middle (or average of the two middles) directly.

This mirrors what you'd write in an interview before optimizing — correct, but every insert costs a linear shift, and the order has to be rebuilt by hand rather than maintained incrementally.

```java
import java.util.ArrayList;
import java.util.Collections;

class MedianFinder {
    private ArrayList<Integer> nums;

    public MedianFinder() {
        nums = new ArrayList<>();
    }

    public void addNum(int num) {
        int lo = Collections.binarySearch(nums, num);
        if (lo < 0) lo = -(lo + 1);
        nums.add(lo, num);
    }

    public double findMedian() {
        int n = nums.size();
        int mid = n / 2;
        if (n % 2 == 1) return nums.get(mid);
        return (nums.get(mid - 1) + nums.get(mid)) / 2.0;
    }
}
```

## Why it works

`binarySearch` returns the index of `num` if present, or `-(insertionPoint) - 1` otherwise; decoding that gives the correct spot to insert while keeping `nums` sorted. With a sorted list, the median is just the middle element (odd count) or the average of the two elements straddling the middle (even count).

## Complexity

- Time: O(n) per `addNum` (binary search is O(log n) but `ArrayList.add` shifts O(n) elements); O(1) per `findMedian`.
- Space: O(n) — one list holding every number added.
