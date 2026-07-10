Design a class that tracks the k-th largest element in a growing stream of numbers. The constructor receives an integer `k` and an initial array `nums`. It exposes one method, `add(val)`, which inserts `val` into the stream and returns the k-th largest element among everything inserted so far.

You may assume `k` is always at least 1 and never larger than the current number of elements in the stream when `add` is called.

## Examples

```text
Input:
KthLargest(3, [4, 5, 8, 2])
add(3)
add(5)
add(10)
add(9)
add(4)
Output: [4, 5, 5, 8, 8]
```

```text
Input:
KthLargest(1, [])
add(-3)
add(-2)
add(-4)
add(0)
add(4)
Output: [-3, -2, -2, 0, 4]
```

```text
Input:
KthLargest(2, [0])
add(-1)
add(1)
add(-2)
add(3)
Output: [-1, 0, 1, 1]
```

## Constraints

- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the array when you search for the k-th element.
