Design a structure that supports adding integers from an endless stream one at a time and reporting the median of every number seen so far, at any point in the stream.

Implement a class `MedianFinder` with two operations: `addNum(num)` inserts a new integer into the running data set, and `findMedian()` returns the median of all integers added so far. If an even count of numbers has been added, the median is the average of the two middle values.

## Examples

```text
Input:  addNum(1), addNum(2), findMedian(), addNum(3), findMedian()
Output: 1.5, 2.0
# After [1, 2] the median is (1 + 2) / 2 = 1.5
# After [1, 2, 3] the median is the middle value, 2.0
```

```text
Input:  addNum(6), findMedian(), addNum(10), findMedian(), addNum(2), findMedian()
Output: 6.0, 8.0, 6.0
# After [6] median is 6.0
# After [6, 10] median is (6 + 10) / 2 = 8.0
# After [6, 10, 2] sorted is [2, 6, 10], median is 6.0
```

```text
Input:  addNum(-1), addNum(-2), findMedian(), addNum(-3), findMedian()
Output: -1.5, -2.0
# After [-1, -2] median is (-1 + -2) / 2 = -1.5
# After [-1, -2, -3] sorted is [-3, -2, -1], median is -2.0
```

## Constraints

- -10^5 <= num <= 10^5
- `findMedian` is only called after at least one `addNum`.
- Up to 5 * 10^4 calls total to `addNum` and `findMedian` combined.

## Follow-up

Can you support `findMedian` in O(1) time and `addNum` in better than O(n) time, instead of re-sorting or scanning the whole data set on every call?
