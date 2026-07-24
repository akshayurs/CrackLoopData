The simplest possible design: keep every number seen so far in one sorted vector. On each `addNum`, binary-search the insertion point with `lower_bound` and insert to keep the vector sorted. `findMedian` then just reads the middle (or average of the two middles) directly.

This mirrors what you'd write in an interview before optimizing — correct, but every insert costs a linear shift, and the order has to be maintained by hand rather than incrementally by a smarter structure.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class MedianFinder {
public:
    MedianFinder() {}

    void addNum(int num) {
        auto it = lower_bound(nums.begin(), nums.end(), num);
        nums.insert(it, num);
    }

    double findMedian() {
        int n = nums.size();
        int mid = n / 2;
        if (n % 2 == 1) return nums[mid];
        return (nums[mid - 1] + nums[mid]) / 2.0;
    }

private:
    vector<int> nums;
};
```

## Why it works

`lower_bound` finds the first position whose value is not less than `num`, and inserting there keeps `nums` sorted at all times. With a sorted vector, the median is just the middle element (odd count) or the average of the two elements straddling the middle (even count).

## Complexity

- Time: O(n) per `addNum` (binary search is O(log n) but `insert` shifts O(n) elements); O(1) per `findMedian`.
- Space: O(n) — one vector holding every number added.
