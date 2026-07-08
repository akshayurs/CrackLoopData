You are given a sorted array `nums` where every value appears exactly twice, except for one value that appears only once. Find and return that single, unpaired value.

Because the array is sorted, the two copies of each paired value sit next to each other.

## Examples

```text
Input:  nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
Output: 2
```

```text
Input:  nums = [3, 3, 7, 7, 10, 11, 11]
Output: 10
```

```text
Input:  nums = [5]
Output: 5
```

## Constraints

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- `nums` is sorted in non-decreasing order.
- Exactly one element appears once; every other element appears exactly twice.

## Follow-up

A linear scan is easy. Can you do it in O(log n) time and O(1) space by exploiting the sorted order?
